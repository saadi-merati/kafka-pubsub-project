import json
from kafka import KafkaConsumer

print("INVENTORY Consumer (Group: inventory_group) waiting for orders...")

consumer = KafkaConsumer(
    'commandes_validees', # Subscribes ONLY to orders
    bootstrap_servers=['localhost:29092'],
    auto_offset_reset='earliest',
    group_id='inventory_group', # Consumer group for inventory management
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

for message in consumer:
    data = message.value
    # Business logic: simulate order processing / stock update
    print(f"[INVENTORY] Processing order {data['order_id']} (Amount: {data['amount']} EUR)")