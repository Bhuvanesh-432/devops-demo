# devops-demo

A small, beginner-friendly DevOps project: a Python Flask web app, containerized with Docker, tested with pytest, and automatically built (and optionally deployed) via GitHub Actions CI/CD.

This project is intentionally minimal — no Kubernetes, Terraform, or databases. The goal is to understand the core CI/CD loop end to end: **code → test → build → ship.**

## Tech stack

- Python 3.12
- Flask
- pytest
- Docker
- GitHub Actions
- Docker Hub (image registry)

## Project structure

```
devops-demo/
├── app.py                     # Flask application
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Container build instructions
├── .dockerignore               # Files excluded from the Docker image
├── tests/
│   └── test_app.py            # pytest test suite
└── .github/
    └── workflows/
        └── ci.yml              # CI pipeline: test -> build -> push
```

## Endpoints

| Route      | Method | Response                       |
|------------|--------|---------------------------------|
| `/`        | GET    | `Hello DevOps!` (plain text)    |
| `/health`  | GET    | `{"status": "healthy"}` (JSON)  |

## Running locally (without Docker)

```bash
pip install -r requirements.txt
python app.py
```
Visit `http://localhost:5000`.

## Running tests

```bash
pip install -r requirements.txt
pytest -v
```

## Running with Docker

```bash
docker build -t devops-demo .
docker run -p 5000:5000 devops-demo
```
Visit `http://localhost:5000`.

## CI/CD pipeline

On every push or pull request to `main`, GitHub Actions:

1. Checks out the code
2. Sets up Python 3.12
3. Installs dependencies
4. Runs the pytest suite
5. Builds the Docker image (only if tests pass)
6. On a direct push to `main`: logs in to Docker Hub and pushes the image, tagged both `latest` and with the commit SHA

Pipeline status is visible under the repository's **Actions** tab.

## Deploying to EC2 (optional*)

The built image can be pulled and run on any Docker host, including an AWS EC2 instance:

```bash
docker pull YOUR-DOCKERHUB-USERNAME/devops-demo:latest
docker run -d -p 5000:5000 --name devops-demo YOUR-DOCKERHUB-USERNAME/devops-demo:latest
```

## License

Personal / educational project — no license applied.
