# Microservice Cookiecutter Template

This repository contains a Cookiecutter template for generating microservice
projects using FastAPI, Docker, Alembic, and other tools.

## Getting Started

To create a new microservice project using this template, follow these steps:

1. **Install Cookiecutter:**

    ```bash 
    pip install cookiecutter
    ```

2. **Generate a new project:**

    - If you are using GitHub, you can use the following command:
    ```bash
    cookiecutter https://github.com/your-username/microservice-cookiecutter
    ```

    - If you are using a local copy of the template, you can use the following
      command (an absolute path is required):
    ```bash
    cookiecutter /path/to/microservice-cookiecutter-template.json
    ```
   
   - Note: It's better to be in an empty directory when running Cookiecutter
     because it will generate project files into the current directory.

3. **Follow the prompts to provide project details and configure your
   microservice.**

## Features

- FastAPI for building API endpoints
- Docker for containerization
- Alembic for database migrations
- Pytest for testing
- And more!

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with
any improvements or suggestions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE)
file for details.
