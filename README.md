# Real-Time E-Commerce Analytics Pipeline

> A production-grade pipeline built with Kafka, PySpark, dbt, Airflow, and AWS

![Status](https://img.shields.io/badge/status-in%20progress-yellow)
![Month](https://img.shields.io/badge/month-1%20of%206-blue)
![Stack](https://img.shields.io/badge/stack-Kafka%20%7C%20PySpark%20%7C%20dbt%20%7C%20Airflow-orange)

---

## Architecture

```mermaid
flowchart LR
    A([🛒 Event Generator\nproducer.py]) -->|orders / clicks / users| B[(Apache Kafka\nlocalhost:9092)]
    B --> C[⚡ PySpark\nStreaming Job]
    C -->|cleaned + enriched| D[(PostgreSQL\nData Warehouse)]
    C -->|raw parquet| E[(S3 / LocalStack)]
    D --> F[🔁 dbt\nTransformations]
    F --> G[📊 Mart Models\nRevenue · Cohorts · Funnel]
    B -.->|monitor| H([Kafka Console\nlocalhost:8080])

    style A fill:#4361EE,color:#fff
    style B fill:#E1F5EE,color:#085041
    style C fill:#FAEEDA,color:#633806
    style D fill:#EEEDFE,color:#3C3489
    style E fill:#EEEDFE,color:#3C3489
    style F fill:#E6F1FB,color:#0C447C
    style G fill:#E6F1FB,color:#0C447C
    style H fill:#F1EFE8,color:#444441
```

---

## Project Structure

```
de-ecommerce-pipeline/
├── docker-compose.yml       # Local infrastructure (Kafka, Postgres, etc.)
├── requirements.txt         # Python dependencies
├── producer/
│   └── producer.py          # Publishes fake e-commerce events to Kafka
├── consumer/
│   └── consumer.py          # Consumes and validates events
├── spark/
│   └── transform.py         # PySpark transformation jobs
├── dbt/                     # dbt transformation models
├── airflow/
│   └── dags/                # Airflow pipeline DAGs
└── README.md
```

---

## Tech Stack

| Layer | Tool | Purpose |
|---|---|---|
| Ingestion | Apache Kafka | Event streaming |
| Processing | PySpark | Data transformation |
| Storage | PostgreSQL + S3 | Data warehouse + data lake |
| Transformation | dbt | SQL models + testing |
| Orchestration | Airflow | Pipeline scheduling |
| Cloud | AWS | Production deployment |
| IaC | Terraform | Infrastructure as code |

---

## Quick Start

### Prerequisites
- Docker Desktop running
- Python 3.10+

### Run locally
```bash
# Start infrastructure
docker compose up -d

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Run event producer
python producer/producer.py
```

---

## Roadmap

- [x] Month 1 — Kafka ingestion layer
- [ ] Month 2 — PySpark + Postgres + S3
- [ ] Month 3 — dbt transformation models
- [ ] Month 4 — Airflow orchestration
- [ ] Month 5 — AWS deployment
- [ ] Month 6 — Portfolio polish + job search

---

## Author

**Jeyrome Orosco**  
[LinkedIn](https://www.linkedin.com/in/jeyromeorosco/) · [GitHub](https://github.com/jeyromeorosco)