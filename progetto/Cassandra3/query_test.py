from cassandra.cluster import Cluster
from cassandra.query import SimpleStatement
from cassandra import ConsistencyLevel
from uuid import UUID
import time

cluster = Cluster(['10.0.1.4', '10.0.1.5', '10.0.1.6'])
session = cluster.connect('log_keyspace')

existing_id = UUID("addcd3c3-87f5-406e-919a-6fd6a472b278")

def run_query_service(cl, description):
    print(f"\n[Test servizio] {description}")
    query = SimpleStatement(
        "SELECT * FROM logs WHERE service = 'auth' ALLOW FILTERING",
        consistency_level=cl
    )

    start = time.time()
    try:
        rows = session.execute(query)
        count = sum(1 for _ in rows)
        end = time.time()
        print(f"  Risultati trovati: {count}")
        print(f"  Tempo: {(end - start)*1000:.2f} ms")
    except Exception as e:
        end = time.time()
        print(f"  Errore: {e}")
        print(f"  Tempo (fallito): {(end - start)*1000:.2f} ms")
def run_query_pk(cl, description):
    print(f"\n[Test PK] {description}")
    query = SimpleStatement(
        "SELECT service FROM logs WHERE id = %s",
        consistency_level=cl
    )

    start = time.time()
    try:
        row = session.execute(query, (existing_id,))
        end = time.time()
        count = sum(1 for _ in row)
        print(f"  Risultati trovati: {count}")
        print(f"  Tempo: {(end - start)*1000:.2f} ms")
    except Exception as e:
        end = time.time()
        print(f"  Errore: {e}")
        print(f"  Tempo (fallito): {(end - start)*1000:.2f} ms")

print("== ESECUZIONE QUERIES CON 3 NODI ==")

consistency_levels = {
    "ONE": ConsistencyLevel.ONE,
    "QUORUM": ConsistencyLevel.QUORUM,
    "ALL": ConsistencyLevel.ALL
}

for name, cl in consistency_levels.items():
    run_query_service(cl, f"Query su 'service' con ALLOW FILTERING (CL = {name})")
    run_query_pk(cl, f"Query su chiave primaria 'id' (CL = {name})")        