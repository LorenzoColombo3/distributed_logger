from cassandra.cluster import Cluster
from cassandra import ConsistencyLevel
from cassandra.query import SimpleStatement
from datetime import datetime
import uuid
import time

cluster = Cluster(['10.0.1.4','10.0.1.5','10.0.1.6'])
session = cluster.connect('log_keyspace')

services = ['auth', 'billing', 'notifications']
levels = ['INFO', 'WARNING', 'ERROR']

NUM_INSERTS = 100000

consistency_levels = {
    "ONE": ConsistencyLevel.ONE,
    "QUORUM": ConsistencyLevel.QUORUM,
    "ALL": ConsistencyLevel.ALL
}

def run_test(consistency_label, consistency_level):
    print(f"\nTesting con ConsistencyLevel = {consistency_label}")

    insert_query = """
        INSERT INTO logs (id, service, level, message, timestamp)
        VALUES (?, ?, ?, ?, ?)
    """
    statement = session.prepare(insert_query)
    statement.consistency_level = consistency_level

    start_time = time.time()

    for i in range(NUM_INSERTS):
        log_id = uuid.uuid4()
        service = services[i % len(services)]
        level = levels[i % len(levels)]
        message = f"Log test {i} [{consistency_label}]"
        timestamp = datetime.utcnow()

        session.execute(statement, (log_id, service, level, message, timestamp))

    end_time = time.time()
    total_time = end_time - start_time
    avg_time = total_time / NUM_INSERTS

    print(f"  -> Totale: {total_time:.3f} sec")
    print(f"  -> Media per inserimento: {avg_time*1000:.2f} ms")

for label, level in consistency_levels.items():
    run_test(label, level)

cluster.shutdown()