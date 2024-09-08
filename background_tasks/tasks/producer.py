import pika
import json
from django.conf import settings

# Publish Task
def send_welcome_email_to_queue(email, username):
    # Get RabbitMQ connection settings
    rabbitmq_settings = settings.RABBITMQ

    # Establish a connection to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=rabbitmq_settings['HOST'],
        port=rabbitmq_settings['PORT'],
        credentials=pika.PlainCredentials(rabbitmq_settings['USER'], rabbitmq_settings['PASSWORD'])
    ))

    channel = connection.channel()

    # Declare a queue to send tasks to
    channel.queue_declare(queue='email_queue', durable=True)

    # Create a task object to send
    task = {
        'email': email,
        'username': username,
    }

    # Send the task to the queue
    channel.basic_publish(
        exchange='',
        routing_key='email_queue',
        body=json.dumps(task),
        properties=pika.BasicProperties(delivery_mode=2)  # Make message persistent
    )

    print(f"Task sent to queue: {task}")
    connection.close()

