import pika


def test_rabbitmq_connection():
    try:
        connection_params = pika.ConnectionParameters('localhost')
        connection = pika.BlockingConnection(connection_params)
        channel = connection.channel()
        print("Connection to RabbitMQ successful")

        # Optionally, you can declare a test queue and send a message to verify further
        channel.queue_declare(queue='test_queue')
        channel.basic_publish(exchange='', routing_key='test_queue', body='Test message')
        print("Message sent to test_queue")

        connection.close()
        print("Connection closed successfully")

    except pika.exceptions.AMQPConnectionError as e:
        print(f"Failed to connect to RabbitMQ: {e}")


if __name__ == '__main__':
    test_rabbitmq_connection()
