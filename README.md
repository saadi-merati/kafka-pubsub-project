# Big Data Introduction – Final Project  
## Multi-Topic Publish/Subscribe System with Apache Kafka

---

## Project Overview

This project implements a real-time data streaming system based on the **Publish/Subscribe pattern** using **Apache Kafka**.  
The goal is to demonstrate how Big Data streaming tools enable scalable, decoupled, and real-time data processing.

The system simulates an **e-commerce platform** where different types of events are produced continuously and consumed by multiple services according to their specific needs.  
Apache Kafka runs locally using **Docker and Docker Compose**, with containers launched and managed through **PowerShell**, ensuring an easy and reproducible setup.

---

## Chosen Tool: Apache Kafka

Apache Kafka is a distributed event streaming platform designed to handle large volumes of data with low latency.  
It is widely used in Big Data architectures for real-time ingestion, buffering, and distribution of data streams.

In this project, Kafka acts as the **central messaging layer** between producers and consumers.

---

## Why Apache Kafka?

Kafka was chosen for this project because it provides:

- **Decoupling**: Producers and consumers operate independently, allowing services to evolve separately.
- **Scalability**: Partitioned topics allow high throughput and parallel processing.
- **Real-Time Processing**: Handles continuous streams with minimal latency.
- **Industry Standard**: Widely used in Big Data pipelines for streaming analytics.

---

## Project Architecture

The system follows a **multi-topic Publish/Subscribe architecture**:

### Components

**Producer (producer.py)**  
- Generates **user click events** to the `clics_utilisateur` topic.  
- Generates **validated order events** to the `commandes_validees` topic.  
- Simulates real-time user activity in a loop.

**Analytics Consumer (consumer_analytics.py)**  
- Subscribes to both topics.  
- Prints all received messages, simulating a real-time analytics dashboard.  

**Inventory Consumer (consumer_inventory.py)**  
- Subscribes only to the `commandes_validees` topic.  
- Processes order events to simulate inventory management.  
- Demonstrates topic-specific processing.

### Flow of Data

```
producer.py
    │
    ├──> Kafka Topic: clics_utilisateur
    │         │
    │         ├──> consumer_analytics.py (monitors all clicks)
    │         
    └──> Kafka Topic: commandes_validees
              │
              ├──> consumer_analytics.py (monitors all orders)
              └──> consumer_inventory.py (processes orders only)
```

---

## Installation Steps

**Environment:** Windows 11, Docker Desktop, Python 3.11

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd kafka-cluster
```

### 2. Start Kafka and Zookeeper using Docker Compose

```bash
docker-compose up -d
```

### 3. Create Kafka topics

```bash
docker exec -it kafka kafka-topics --create --topic clics_utilisateur --bootstrap-server kafka:9092 --partitions 3 --replication-factor 1

docker exec -it kafka kafka-topics --create --topic commandes_validees --bootstrap-server kafka:9092 --partitions 3 --replication-factor 1
```

### 4. Install Python dependencies

```bash
pip install kafka-python
```

### 5. Run the producer to generate events

```bash
python producer.py
```

### 6. Run the analytics consumer

```bash
python consumer_analytics.py
```

### 7. Run the inventory consumer

```bash
python consumer_inventory.py
```

---

## Minimal Working Example

### Producer example

```python
click_data = {
    "type": "CLICK", 
    "user_id": "User_1", 
    "page": "/home", 
    "timestamp": time.time()
}
producer.send('clics_utilisateur', value=click_data)

order_data = {
    "type": "ORDER", 
    "order_id": "ORD-1001", 
    "amount": 50.25, 
    "status": "VALIDATED"
}
producer.send('commandes_validees', value=order_data)
```

### Analytics Consumer example

```python
for message in consumer:
    print(f"[ANALYTICS] Received from {message.topic}: {message.value}")
```

### Inventory Consumer example

```python
for message in consumer:
    print(f"[INVENTORY] Processing order {message.value['order_id']}")
```

---

## Screenshots & Explanations

### Screen 1 – Producer Output

- Shows real-time click and order events being sent to Kafka.
- Click events contain `user_id` and `page`; order events show `order_id` and `amount`.
- Demonstrates continuous data production.

### Screen 2 – Analytics Consumer Output

- Displays all messages from both topics.
- Illustrates how analytics services can monitor all activity on the platform.
- Useful for dashboards or real-time metrics.

### Screen 3 – Inventory Consumer Output

- Displays only `commandes_validees` messages.
- Shows inventory updates triggered by validated orders.
- Highlights topic-specific consumption and decoupled service architecture.

---

## How Kafka Fits into Big Data

- Kafka acts as a centralized messaging backbone, enabling real-time analytics.
- Integrates easily with other Big Data tools like Spark, Hive, or HDFS.
- Supports high-throughput, fault-tolerant, and scalable streaming architectures.

---

## Challenges & Solutions

### Persistent Zookeeper Nodes

- **Cause**: Kafka startup failed due to leftover ephemeral nodes.
- **Solution**: Remove Kafka data volume (`docker volume rm kafka-cluster_kafka-data`) and restart.

### Windows Path Issues

- **Cause**: Spaces in folder names caused script errors.
- **Solution**: Use quoted paths in PowerShell.

---

## My Setup Notes

- Learned Docker Kafka configuration for Windows with multiple listeners.
- Practiced multi-topic consumption with separate consumer groups.

---

## Folder Structure

```
kafka-pubsub-project/
│
├── docker-compose.yml
├── README.md
├── .gitignore
│
├── screenshots/
│   ├── analytics_output.png
│   ├── inventory_output.png
│   └── producer_output.png
│
└── scripts/
    ├── producer.py
    ├── consumer_analytics.py
    └── consumer_inventory.py
```

---

## Conclusion

This project demonstrates the power of Apache Kafka for building scalable, real-time streaming architectures in Big Data ecosystems. The decoupled architecture allows each service to operate independently while sharing a common data stream, making it ideal for modern distributed systems.
