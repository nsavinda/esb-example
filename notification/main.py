from confluent_kafka import Consumer, KafkaException, KafkaError
import time

# Configuration for Kafka Consumer
conf = {
    'bootstrap.servers': 'kafka:9092',  # Kafka broker(s)
    'group.id': 'my-consumer-group',        # Consumer group ID
    'auto.offset.reset': 'earliest'         # Start from the earliest message
}

# Function to create and return a Kafka Consumer
def create_consumer(config):
    return Consumer(config)

# Main function to handle the message consumption
def main():
    while True:
        try:
            consumer = create_consumer(conf)
            consumer.subscribe(['test'])

            while True:
                msg = consumer.poll(timeout=1.0)  # Timeout in seconds
                # print("A")

                if msg is None:
                    continue  # No message available yet

                print(msg)
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        # End of partition event
                        print(f"End of partition reached {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")
                    elif msg.error().code() == KafkaError._ALL_BROKERS_DOWN:
                        print("All brokers are down. Attempting to reconnect in 10 seconds...")
                        raise KafkaException(msg.error())
                    else:
                        raise KafkaException(msg.error())
                else:
                    # Proper message received
                    print(f"Received message: {msg.value().decode('utf-8')} from topic: {msg.topic()}")

        except KafkaException as e:
            print(f"Error: {e}")
            consumer.close()
            print("Waiting 10 seconds before reattempting...")
            time.sleep(10)
        except KeyboardInterrupt:
            break
        finally:
            try:
                consumer.close()
            except:
                pass  # Handle error if consumer is not defined or already closed

if __name__ == "__main__":
    main()
