import time
from django.core.mail import send_mail
from django.conf import settings

def send_welcome_email(email, username):
    """
    Sends a welcome email to the newly registered user.
    """
    time.sleep(2)  # Simulate time taken to send the email
    
    # Use Django's send_mail function to send the email
    send_mail(
        subject='Welcome!',
        message=f'Hi {username}, welcome to our platform!',
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[email],
        fail_silently=False,
    )
    
    print(f"Email sent to {email}")

