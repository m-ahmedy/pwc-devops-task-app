# PwC DevOps Task App

## Overview

This application is part of the `pwc-devops-task` project. It is designed to demonstrate DevOps best practices and application deployment workflows.

## Features

- Modular architecture
- Easy configuration
- Container-ready setup

## Prerequisites

- [Docker](https://www.docker.com/) (optional, for containerization)
- [Python 3.x](https://www.python.org/) (if applicable)
- Other dependencies as specified in `requirements.txt` or relevant files

### GitHub Actions Setup

- Secrets:
    - ACR_PASSWORD: The password of docker login credentials to the ACR
    - DEPLOY_GH_TOKEN: The GitHub Personal Access Token (PAT) of the infra repo
- Variables:
    - ACR_LOGIN_SERVER: The login server of the ACR
    - ACR_USERNAME: The username of docker login credentials to the ACR
    - APP_NAME: The name of the app
    - INFRA_REPO: The repo containing infrastructure specifications

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/m-ahmedy/pwc-devops-task-app.git
    cd pwc-devops-task/app
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the application:
    ```bash
    python run.py
    ```

## Usage

- Access the application at `http://localhost:5000`.
- Refer to the documentation for API endpoints.

## API Endpoints

### Users

- `GET /users` — Retrieve a list of users.
- `GET /users/<id>` — Retrieve details for a specific user.

### Products

- `GET /products` — Retrieve a list of products.
- `GET /products/<id>` — Retrieve details for a specific product.

## Deployment

### CI/CD Setup

To enable CI/CD workflows, configure the following in your GitHub repository:

### Required Secrets

- **ACR_PASSWORD**: Docker login password for Azure Container Registry.
- **DEPLOY_GH_TOKEN**: GitHub Personal Access Token for infra repo access, must have contents write permission.

### Required Variables

- **ACR_LOGIN_SERVER**: Azure Container Registry login server.
- **ACR_USERNAME**: Docker login username for ACR.
- **APP_NAME**: Application name.
- **INFRA_REPO**: Infrastructure repository name.

### Environments

Create two environments in your repository settings:

#### 1. `dev`
- Used for development deployments.
- Add required secrets and variables to this environment.
- Enable branch protection rules (e.g., require pull request reviews before merging to `dev`).

#### 2. `prod`
- Used for production deployments.
- Add required secrets and variables to this environment.
- Enable stricter branch protection rules (e.g., require status checks, pull request reviews, and deployment approvals before merging to `main`).

> **Tip:** Configure environment protection rules in GitHub under **Settings > Environments** to control who can deploy to each environment.
