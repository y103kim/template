from kafka import KafkaProducer
from json import dumps

producer = KafkaProducer(
    acks=0,
    compression_type='gzip',
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: dumps(x).encode('utf-8'))

for i in range(100):
    producer.send('test', {"data": "chunk %d" % i})
    producer.flush()
