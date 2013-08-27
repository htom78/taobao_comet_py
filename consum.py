import pika

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)

if __name__ == '__main__':
    
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',5672))
    channel = connection.channel()
    channel.queue_declare(queue='TRADE')
    channel.basic_consume(callback,queue="TRADE",no_ack=True)
    channel.start_consuming()
