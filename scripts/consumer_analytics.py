import json
from kafka import KafkaConsumer

print("ANALYTICS Consumer (Group: analytics_group) waiting for messages...")

consumer = KafkaConsumer(
    'clics_utilisateur', 'commandes_validees', # Subscribes to BOTH topics
    bootstrap_servers=['localhost:29092'],
    auto_offset_reset='earliest', # Start reading from the beginning if no offset exists
    group_id='analytics_group',   # Consumer group for analytics
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    data = message.value
    # Prints every message received from any subscribed topic
    print(f"[ANALYTICS] Received from {message.topic}: {data}")