from cassandra.cluster import Cluster
from datetime import datetime
import uuid
import random
import time

cluster = cluster = Cluster(['10.0.1.4','10.0.1.5', '10.0.1.6'])
session = cluster.connect('log_keyspace')

services = ['auth', 'billing', 'notifications']
levels = ['INFO', 'WARNING', 'ERROR']

i = 0
try:
    while True:
        service = random.choice(services)
        level = random.choice(levels)
        message = f"Log message {i}"
        timestamp = datetime.utcnow()
        log_id = uuid.uuid4()

        session.execute("""
            INSERT INTO logs (id, service, level, message, timestamp)
            VALUES (%s, %s, %s, %s, %s)
        """, (log_id, service, level, message, timestamp))

        print(f"[{timestamp}] {level} - {service}: {message}")

        time.sleep(random.uniform(2, 10))
        i += 1

except KeyboardInterrupt:
    print("\nInterrotto dall'utente. Chiusura del generatore di log.")