class Subscriber:
    def __init__(self, topic, redis_db, celery_app):
        self.topic = topic
        self.redis_db = redis_db
        self.celery_app = celery_app

        @self.celery_app.task
        def consume(topic):
            print(f"Subscribed: the topic is {topic}")

        self.consume_task = consume

    def subscribe(self):
        self.consume_task.delay(self.topic)  # Start consuming messages asynchronously
        print(f"Subscribed to topic '{self.topic}'")

        # Keep the subscriber running to continuously listen for messages
        while True:
            message = self.redis_db.blpop(self.topic, timeout=None)
            print(f"Consumed message '{message[1].decode()}' from topic '{self.topic}'")
