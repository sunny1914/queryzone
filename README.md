# QueryZone - A Django Q&A Platform

QueryZone is a Quora-inspired platform built with Django where users can:

- Register/Login
- Post questions
- Answer others' questions
- Like others' answers

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/yourusername/queryzone.git
cd queryzone

2. Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies:
pip install -r requirements.txt

4. Run migrations and start the server: 
python manage.py migrate
python manage.py runserver


