from kafka.admin import KafkaAdminClient, NewTopic
from kafka.errors import TopicAlreadyExistsError

BOOTSTRAP = "localhost:9092"
TOPICS = {
    "card-transactions": 2,
    "upi-payments": 2,
    "loan-applications": 2,
}

admin = KafkaAdminClient(bootstrap_servers=BOOTSTRAP, client_id="banking-topic-admin")
try:
    new_topics = [NewTopic(name=t, num_partitions=p, replication_factor=3) for t,p in TOPICS.items()]
    try:
        admin.create_topics(new_topics=new_topics, validate_only=False)
    except TopicAlreadyExistsError:
        pass
    print("Kafka topics ready:")
    for topic, partitions in TOPICS.items():
        print(f"  {topic:<20} partitions={partitions} replication-factor=3")
finally:
    admin.close()
