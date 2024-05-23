class Publisher:
    def __init__(self, topic, redis_db):
        self.topic = topic
        self.redis_db = redis_db

    def publish(self, message):
        self.redis_db.rpush(self.topic, message)
        print(f"Published message '{message}' to topic '{self.topic}'")
