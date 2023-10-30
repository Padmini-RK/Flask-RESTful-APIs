
A repo to demonstrate implementation of JWT Authentication, CURD operations and file upload for a health and fitness application using Flask REST APIs.

Team members:
1. Padmini Ramapura Keshavkumar
2. Akshay Patil

Download and Install

1. VSCode
2. Python
3. SQLite 
4. DB Brwoser

Create a virtual environment and activate it.

To do that:

1. Create a directory and navigate to that new directory
2. Then submit the command py -3 -m venv .venv
3. Activate the environment - `.venv\Scripts\activate` on windows

For requirement installation do the following 

`pip install` -r requirements.txt

Create the database by running

flask shell

In the interactive shell run the following
Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
App: main
Instance:
from models import User
db.create_all()


To run application use flask run
