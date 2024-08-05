import pika
import json
from faker import Faker
from models import Contact

fake = Faker()

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


channel.queue_declare(queue='email_queue')


for _ in range(10):  
    contact = Contact(
        fullname=fake.name(),
        email=fake.email()
    )
    contact.save()
    
    
    channel.basic_publish(
        exchange='',
        routing_key='email_queue',
        body=str(contact.id)
    )
    print(f"Sent contact ID {contact.id} to queue")


connection.close()
