import pika
import json
import time
from django.core.management.base import BaseCommand
from tasks.tasks import send_welcome_email


class Command(BaseCommand):
    help = 'Starts the RabbitMQ worker to consume tasks'

    def handle(self, *args, **kwargs):
        from django.conf import settings
        rabbitmq_settings = settings.RABBITMQ

        # Establish RabbitMQ connection
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=rabbitmq_settings['HOST'],
            port=rabbitmq_settings['PORT'],
            credentials=pika.PlainCredentials(rabbitmq_settings['USER'], rabbitmq_settings['PASSWORD'])
        ))
        channel = connection.channel()

        # Declare the queue
        channel.queue_declare(queue='email_queue', durable=True)

        def callback(ch, method, properties, body):
            task = json.loads(body)
            print(f"Received task: {task}")

            # Process the task (send email)
            send_welcome_email(task['email'], task['username'])
            # Acknowledge the task is done
            ch.basic_ack(delivery_tag=method.delivery_tag)

        # Set up consumer
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue='email_queue', on_message_callback=callback)

        print(' [*] Waiting for tasks. To exit press CTRL+C')
        channel.start_consuming()

