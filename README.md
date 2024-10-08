﻿# Flask App Production Recipes

* Flask API
* MongoDB
* Docker
* Gunicorn
* Nginx
* JWT Authentication

This project is a Flask-based web application configured with MongoDB for data storage, Docker for containerization, Gunicorn as the WSGI server, Nginx as the reverse proxy and load balancer, and JWT (JSON Web Tokens) for authentication.

## File Structure
- `app/`: Directory containing the Flask application code.
  - `__init__.py`: Initializes the Flask app and sets up configurations.
  - `models.py`: Contains MongoDB data models.
  - `routes.py`: Defines API endpoints.
  - `auth.py`: Handles authentication-related functionality.
  - `config.py`: Contains configuration settings for the app.
- `docker`: Directory containing docker files
  - `Dockerfile`: Instructions for building the Docker image.
  - `gunicorn_config.py`: Gunicorn configuration file.
  - `nginx.conf`: Nginx configuration file for reverse proxy.
- `docker-compose.yml`: Configuration for Docker Compose to set up services.
- `.env`: Environment variables file.
- `requirements.txt`: Python dependencies for the application.
- `README.md`: Project details.
- `manage.py`: App init file

## Features

- **MongoDB**: NoSQL database for storing user data.
- **Docker**: Containerization for consistent deployment.
- **Gunicorn**: WSGI server for serving the Flask application.
- **Nginx**: Reverse proxy and load balancer.
- **JWT Authentication**: Secure user authentication using JSON Web Tokens.

## Prerequisites

- Python >=3.10.7
- Docker
- Docker Compose

## Setup

### Clone the Repository

```bash
git clone https://github.com/dpralay07/python-flask-production-recipes.git
cd your-repository
```

### Configuration
1. Environment Variables : Update the .env file with your configuration values. This will help to run the application in development server.
2. Docker compose : The docker-compose.yml file is configured to build and run the Flask application along with MongoDB. It also sets up the Nginx reverse proxy. Update the environment variables with your configuration values to run the application in production server.
3. Nginx Configuration : The nginx.conf file is used to configure Nginx to proxy requests to the Flask application.

### Build and Run
Build the docker images
```bash
docker-compose build
```
Start the Containers
```bash
docker-compose up -d
```
This will start the MongoDB, Flask application, and Nginx services.

### Access the application
Access the Application
The Flask API will be available at `http://<your_ip_address>:80`

### Stopping the Application
To stop and remove the containers, run:
```bash
docker-compose down
```

## API Endpoints

    POST /register: Register a new user. Requires username and password in the request body.
    POST /login: Authenticate a user and receive a JWT token. Requires username and password in the request body.
    GET /protected: Access protected content. Requires a valid JWT token in the Authorization header.

## Testing
We can test the API endpoints using tools like Postman or cURL.
Example cURL Commands

Register a User:
```bash
curl -X POST http://<your_ip_address>:80/register -H "Content-Type: application/json" -d '{"username": "testuser", "password": "password123"}'
```
Login and Get Access Token:
```bash
curl -X POST http://<your_ip_address>:80/login -H "Content-Type: application/json" -d '{"username": "testuser", "password": "password123"}'
```
Access Protected Endpoint:
Replace your_jwt_token with the token received from login.
```bash
curl -X GET http://<your_ip_address>:80/protected -H "Authorization: Bearer your_jwt_token"
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request to improve this project.

## Contact
For any questions or feedback, please contact [pralaykumar.daz@gmail.com](mailto:pralaykumar.daz@gmail.com).
