# FastAPI-GPT-API

A seamless integration of FastAPI with OpenAI's GPT models to create a powerful, scalable, and efficient chatbot API. This repository provides a robust framework for building and deploying conversational AI applications using FastAPI, leveraging the capabilities of OpenAI's GPT models and MongoDB for caching previous questions.

## Features

- FastAPI for high-performance API development.
- OpenAI GPT models for advanced natural language processing.
- MongoDB for caching and performance optimization.
- Scalable, efficient, and customizable framework.
- Comprehensive documentation.

## Tech Stack

- **FastAPI**
- **OpenAI GPT**
- **MongoDB**
- **Docker**

## Prerequisites

- Python 3.7+
- Docker
- MongoDB instance (local or cloud-based)

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/fastapi-gpt-api.git
    cd fastapi-gpt-api
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Start MongoDB** (if not already running):
    ```bash
    docker run -d -p 27017:27017 --name mongodb mongo
    ```

## Configuration

1. **Set environment variables**:
    Create a `.env` file in the root directory with the following content, take the `.env.sample` for default:

## Usage

1. **Run the FastAPI server**:
    ```bash
    uvicorn app.main:app --reload
    ```

2. **Access the API**:
    Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the Swagger UI documentation.

## Contributing

Contributions are welcome! Fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License.
