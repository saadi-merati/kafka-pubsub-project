# Multi-Topic Publish/Subscribe System with Apache Kafka

## Project Description
This project implements a real-time data streaming pipeline simulating an e-commerce platform. It demonstrates the **Publish/Subscribe** pattern using **Apache Kafka** running on Docker. The system decouples data producers from consumers, allowing for scalable and organized data processing across multiple topics.

## Technology Stack
* **Tool:** Apache Kafka (v7.5.0) & Zookeeper
* **Containerization:** Docker & Docker Compose
* **Language:** Python 3 (kafka-python library)

## Why Apache Kafka?
I selected Apache Kafka for this Big Data project because:
1.  **Decoupling:** It separates the data generation (Producer) from processing (Consumers), allowing services to evolve independently.
2.  **Scalability:** The partitioning mechanism allows for high-throughput parallel processing.
3.  **Real-Time Processing:** It enables low-latency handling of continuous data streams (clicks, orders).

## Project Architecture
The system consists of three main components:

1.  **Producer (`producer.py`):** Simulates web traffic.
    * Sends `CLICK` events to the topic `clics_utilisateur`.
    * Sends `ORDER` events to the topic `commandes_validees`.
2.  **Analytics Consumer (`consumer_analytics.py`):**
    * Subscribes to **BOTH** topics.
    * Represents a Data Lake ingestion process (analyzing all traffic).
3.  **Inventory Consumer (`consumer_inventory.py`):**
    * Subscribes **ONLY** to `commandes_validees`.
    * Represents a critical business service (stock management) that must not be polluted by clickstream data.

## Installation & Setup

### 1. Prerequisites
* Docker Desktop installed and running.
* Python 3.x installed.
* Python library: `pip install kafka-python`

### 2. Run the Environment
Start the Kafka and Zookeeper containers using Docker Compose:
```bash
docker-compose up -d