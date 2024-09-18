import pika
 
QUEUE_1 = 'queue1'
QUEUE_2 = 'queue2'
 
def service_b(max_iterations):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
 
    channel.queue_declare(queue=QUEUE_1)
    channel.queue_declare(queue=QUEUE_2)
 
    for _ in range(max_iterations):
        method_frame, header_frame, body = channel.basic_get(QUEUE_1, auto_ack=True)
        while method_frame is None:
            method_frame, header_frame, body = channel.basic_get(QUEUE_1, auto_ack=True)
 
        x = int(body)
        print(f"Service B consumed: {x} -> Queue 1")
        x = x ** 2
 
        channel.basic_publish(exchange='', routing_key=QUEUE_2, body=str(x))
        print(f"Service B produced: {x} -> Queue 2")
    connection.close()