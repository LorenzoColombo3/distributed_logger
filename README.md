# distributed_logger

Sistema distribuito di logging basato su Apache Cassandra. Simula più servizi che generano log in tempo reale salvati in un cluster Cassandra. Include analisi di scalabilità, tolleranza ai guasti e performance con diversi numeri di nodi.

## Caratteristiche

- Simulazione di più microservizi che generano log.
- Salvataggio distribuito dei log in un cluster Cassandra.
- Analisi di:
  - Scalabilità al variare dei nodi.
  - Tolleranza ai guasti (fallimento di nodi).
  - Performance in scrittura e lettura.

## Tecnologie utilizzate

- Python 3.x
- Apache Cassandra
- Docker / Docker Compose (per la gestione del cluster)
- cqlsh (per la gestione manuale del DB)

