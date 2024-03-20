import os
import pika
from producer_interface import mqProducerInterface

class mqProducer(mqProducerInterface):
    def __init__(self, routing_key: str, exchange_name: str) -> None:
        # body of constructor
        #self.name = name
        self.routing_key = routing_key
        self.exchange_name = exchange_name
        self.setupRMQConnection()

    def setupRMQConnection(self) -> None:
        # Set-up Connection to RabbitMQ service
        conParams = pika.URLParameters(os.environ['AMQP_URL'])
        self.connection = pika.BlockingConnection(parameters=conParams)
        # Establish Channel
        self.channel = self.connection.channel()
        # Create the exchange if not already present
        self.exchange = self.channel.exchange_declare(exchange = self.exchange_name)

    def publishOrder(self, message: str) -> None:
        #publish order function
        self.channel.basic_publish(
            exchange=self.exchange_name,
            routing_key=self.routing_key,
            body="Message",
        )
        self.channel.close()
        self.connection.close()
