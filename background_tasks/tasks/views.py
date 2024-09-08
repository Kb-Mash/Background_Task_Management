from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
import pika
import json
from .producer import  send_welcome_email_to_queue

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Basic validation
        if not username or not email or not password1 or not password2:
            return render(request, 'register.html', {'error': 'All fields are required'})

        if password1 != password2:
            return render(request, 'register.html', {'error': 'Passwords do not match'})

        try:
            # Create the user
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.save()

            # Send the welcome email task to the queue
            send_welcome_email_to_queue(user.email, user.username)

            # Render a success message
            return render(request, 'register.html', {'success_message': 'User registered and email task sent to queue'})

        except Exception as e:
            return render(request, 'register.html', {'error': str(e)})

    return render(request, 'register.html')

