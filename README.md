# Django Project with RabbitMQ Background Task Management

## Overview
- This project is a simple Django application that integrates with RabbitMQ for background task management. It demonstrates how to offload tasks, such as sending emails, to a background worker to improve performance and user experience.

## Features:
- Background task management using RabbitMQ.
- Django-based web application.
- Task examples include sending welcome emails.
- Separation of task producers and workers.

## Setting Up RabbitMQ
- sudo apt-get install rabbitmq-server
- sudo service rabbitmq-server start
- RabbitMQ Management Interface: web browser and navigate to http://localhost:15672/. The default username and password are guest

## Installation
1. **Clone the repository:**
[Background-Task-Management](https://github.com/Kb-Mash/Background_Task_Management)
- cd into repository

2. **Create and activate a virtual environment**
- python3 -m venv venv
- source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install dependencies**
- pip install -r requirements.txt

4. **Apply migrations**
- python3 manage.py migrate

5. **Start the development server**
- python3 manage.py runserver

6. **Run the worker**
- python3 manage.py runworker

## Usage
- Set up RabbitMQ and Email configurations in Django settings
- Go to http://localhost:8000 to access the application.
- Register a new account and verify via email.
- Send background tasks via the app and check the email inbox.
