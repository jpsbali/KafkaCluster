from kafka import KafkaConsumer

bootstrap_servers = ['localhost:9091', 'localhost:9092', 'localhost:9093']
topicName = 'my-topic'

consumer = KafkaConsumer(topicName, bootstrap_servers=bootstrap_servers, auto_offset_reset='earliest', enable_auto_commit=True, auto_commit_interval_ms=1000, group_id='my-group')

for message in consumer:
    print (message)