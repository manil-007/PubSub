# PubSub System

This repository contains a simple Publisher-Subscriber (PubSub) system implemented using Python, Celery, and Redis.

## Setup Instructions

1. **Activate Virtual Environment**: Activate your virtual environment to isolate the project dependencies.

   ```bash
   source /path/to/your/venv/bin/activate
   ```

2. **Install Dependencies**: Install the required Python packages using pip.

   ```bash
   pip install -r requirements.txt

   ```

2. **Install Dependencies**: Install the required Python packages using pip.

   ```bash
   pip install -r requirements.txt

   ```

3. **Start Redis Server**: Start the Redis server to serve as the message broker for the PubSub system.

   ```bash
   redis-server

   ```


## Running the Publisher and Subscriber

1. **Run the Publisher**: In one terminal, run the publisher script to send messages to the PubSub system.

   ```bash
   python3 -m src.test.publisher
   
   ```
2. **Run the Subscriber**: In another terminal, run the subscriber script to receive messages from the PubSub system.

   ```bash
   python3 -m src.test.subscriber
   
   ```

3. **Checking Redis Database (Optional)**: You can use the redis-cli tool to interact with the Redis database and inspect the messages stored in the queues.

   ```bash
   redis-cli
   LRANGE <topic> 0 -1
   
   ```
