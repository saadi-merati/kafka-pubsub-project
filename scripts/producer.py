import time
import json
import random
from kafka import KafkaProducer

# Connect to port 29092 (exposed for the host machine)
producer = KafkaProducer(
    bootstrap_servers=['localhost:29092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

print("Producer started! Sending data...")

user_ids = ["User_1", "User_2", "User_3", "User_4", "User_5"]

try:
    while True:
        # 1. Click Simulation (Topic: clics_utilisateur)
        # Sends a click event in every iteration
        click_data = {
            "type": "CLICK",
            "user_id": random.choice(user_ids),
            "page": random.choice(["/home", "/product/A", "/cart"]),
            "timestamp": time.time()
        }
        producer.send('clics_utilisateur', value=click_data)
        print(f"--> Click sent: {click_data['user_id']} on {click_data['page']}")

        # 2. Order Simulation (Topic: commandes_validees)
        # Sends an order occasionally (approx. 1 out of 5 iterations)
        if random.randint(1, 5) == 5:
            order_data = {
                "type": "ORDER",
                "order_id": f"ORD-{random.randint(1000, 9999)}",
                "amount": round(random.uniform(20.0, 150.0), 2),
                "status": "VALIDATED"
            }
            producer.send('commandes_validees', value=order_data)
            print(f"*** ORDER VALIDATED: {order_data['order_id']} ({order_data['amount']} EUR) ***")

        time.sleep(2) # Wait 2 seconds between events

except KeyboardInterrupt:
    print("Producer stopped.")