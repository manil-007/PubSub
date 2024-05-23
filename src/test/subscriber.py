from src.main.subscriber import Subscriber
import redis
from celery import Celery


# Initialize Celery with the correct Redis database
app = Celery('src.main.subscriber', broker='redis://localhost:6379/0')

# Initialize Redis connection to use database 1
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

if __name__ == "__main__":
    topic = input("Enter the topic to subscribe to: ")

    # Instantiate the Subscriber object with the specified topic
    subscriber = Subscriber(topic, redis_client, app)

    # Start consuming messages for the specified topic
    subscriber.subscribe()

    # Keep the script running to continuously listen for messages
    while True:
        pass
