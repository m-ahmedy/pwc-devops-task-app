# App README

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
