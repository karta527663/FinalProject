import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(host='203.64.125.80'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

message = ' '.join(sys.argv[1:]) or "NPTU Cloud Computing"

channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(delivery_mode=2)
)

print(" [x] Sent %r" % message)
connection.close()
