import pika
 
QUEUE_1 = 'queue1'
QUEUE_2 = 'queue2'
 
def service_a(max_iterations):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
 
    channel.queue_declare(queue=QUEUE_1)
    channel.queue_declare(queue=QUEUE_2)
 
    B = 6
    x = 2 * B
 
    for _ in range(max_iterations):
        channel.basic_publish(exchange='', routing_key=QUEUE_1, body=str(x))
        print(f"Service A produced: {x} -> Queue 1")
 
        method_frame, header_frame, body = channel.basic_get(QUEUE_2, auto_ack=True)
        while method_frame is None:
            method_frame, header_frame, body = channel.basic_get(QUEUE_2, auto_ack=True)
 
        x = int(body)
        print(f"Service A consumed: {x} -> Queue 2")
 
        x *= B
    connection.close()