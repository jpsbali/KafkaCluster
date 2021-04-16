1. Use the following commands for docker

    docker-compose up -d  

    docker exec -it kafka_kafka1_1 kafka-topics --zookeeper zookeeper:2181 --create --topic my-topic --partitions 3 --replication-factor 3
    
    docker exec -ti cc1294d34e1f  ./bin/zkCli.sh ls /brokers/ids
    
    docker-compose down
    
2. Use the following command to open up KadDrop
    
    http://localhost:9000/
    
3. Open a command prompt
    
    install python 3.8.X
    
    pip install kafka-python
    
4. Open another command prompt and start consumer
    
    python consumer.py
    
5. Open another command prompt and start producer
    
    python  producer.py
   
Reference - https://betterprogramming.pub/a-simple-apache-kafka-cluster-with-docker-kafdrop-and-python-cf45ab99e2b9
