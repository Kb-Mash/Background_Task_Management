from django.http import JsonResponse
from tasks.producer import send_task_to_queue

# Producing task
def send_email_notification(request):
    email = "user@example.com"
    message = "Hello, this is a test email"
    subject = "Test Email"
    
    # Send the task to the queue
    send_task_to_queue(email, message, subject)
    
    return JsonResponse({"status": "Task has been sent to queue"})

