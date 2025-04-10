from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm



def welcome(request):
    return render(request, 'queryzone/welcome.html')



@login_required
def post_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.user = request.user
            question.save()
            return redirect('view_questions')
    else:
        form = QuestionForm()
    return render(request, 'queryzone/post_question.html', {'form': form})

def view_questions(request):
    questions = Question.objects.all()
    return render(request, 'queryzone/view_questions.html', {'questions': questions})

@login_required
def answer_question(request, question_id):
    question = Question.objects.get(id=question_id)
    if question.user == request.user:
        return render(request, 'queryzone/not_allowed.html', {
            'message': "You cannot answer your own question."
        })
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            return redirect('view_questions')
    else:
        form = AnswerForm()
    return render(request, 'queryzone/answer_question.html', {'question': question, 'form': form})

@login_required
def like_answer(request, answer_id):
    answer = Answer.objects.get(id=answer_id)
    if answer.user == request.user:
        return render(request, 'queryzone/not_allowed.html', {
            'message': "You cannot like your own answer."
        })
    if request.user not in answer.likes.all():
        answer.likes.add(request.user)
    else:
        answer.likes.remove(request.user) 
    return redirect('view_questions')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print("user = ", user)
            login(request, user)
            return redirect('view_questions')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('view_questions')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def custom_logout(request):
    logout(request)
    return redirect('custom_login')
