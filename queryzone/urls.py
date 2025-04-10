from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.welcome, name='welcome'),
    path('post_question/', views.post_question, name='post_question'),
    path('view_questions/', views.view_questions, name='view_questions'),
    path('answer/<int:question_id>/', views.answer_question, name='answer_question'),
    path('like/<int:answer_id>/', views.like_answer, name='like_answer'),
    path('custom_login/', views.custom_login, name='custom_login'),
    path('custom_logout/', views.custom_logout, name='custom_logout')
]
