# Llm Ops Platform

LLMOps — prompt versioning, evaluation, A/B testing

## Features

- Api
Deployment - Ab Testing
Deployment - Canary
Evaluation - Metrics
Evaluation - Pipeline
Monitoring - Logger
Prompts - Template Engine
Prompts - Version Control

## Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **Key Dependencies:** pydantic,fastapi,uvicorn,anthropic,openai,numpy
- **Containerization:** Docker + Docker Compose

## Getting Started

### Prerequisites

- Python 3.11+
- Docker & Docker Compose (optional)

### Installation

```bash
git clone https://github.com/MukundaKatta/llm-ops-platform.git
cd llm-ops-platform
pip install -r requirements.txt
```

### Running

```bash
uvicorn app.main:app --reload
```

### Docker

```bash
docker-compose up
```

## Project Structure

```
llm-ops-platform/
├── src/           # Source code
├── tests/         # Test suite
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## License

MIT
