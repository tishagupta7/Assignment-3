# Banking Kafka Streaming Project - Rebuilt

This project reconstructs the previous banking Kafka assignment using the same recovered datasets and Kafka configuration.

Topics:
- card-transactions
- upi-payments
- loan-applications

## Start
1. python -m venv .venv
2. .\.venv\Scripts\Activate.ps1
3. pip install -r requirements.txt
4. docker compose up -d
5. docker compose ps
6. python create_topics.py

## Run in separate VS Code terminals
1. python consumers/stream_monitor.py
2. python producers/card_producer.py
3. python producers/upi_producer.py
4. python producers/loan_kyc_producer.py
5. python consumers/fraud_consumer.py

## Dashboard stage
1. Copy .env.example to .env
2. Add MongoDB Atlas MONGO_URI
3. python consumers/mongodb_consumer.py
4. Configure Grafana to read the MongoDB collection
5. Create at least 3 charts
