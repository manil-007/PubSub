from src.main.publisher import Publisher
import redis


redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)


if __name__ == "__main__":
    topic = input("Enter the topic: ")
    if topic != "":
        publisher = Publisher(topic, redis_client)
        print("Type 'exit' to stop publishing.")
        while True:
            message = input("Enter message: ")
            if message.lower() == 'exit':
                break
            publisher.publish(message)
