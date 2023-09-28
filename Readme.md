# Realtime Chat Django

This repository contains a real-time chat application built with Django Channels and Docker Compose.
It includes a Django server, a PostgreSQL database, and a Redis instance to enable real-time communication.

## Requirements

Make sure you have Docker and Docker Compose installed in your system:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/ericknavarro97/realtime-django-chat.git
   cd realtime-django-chat
   ```

2. Build and start the Docker containers with Django server, PostgreSQL database, and Redis:

   ```bash
   docker compose up --build
   ```

3. Access the Django application in your web browser at http://localhost:8000.

## Creating a Superuser (Optional)

To create a superuser in Django from Docker Compose, follow the next steps:

1. Open a terminal and run the following command to create a superuser:

   ```bash
    docker compose exec django python manage.py createsuperuser
   ```

## Congrats! 🥳 You can use it now! 🚀

With just a simple sign-up/login, you can dive into the world of seamless 
communication. Create a new chat and connect with people instantly to start chatting!

### TODO's and Improvements:

1. Improve cleaning cache.
2. Delete chats (Only admin users).
3. Add more message errors.
4. Set `.env` file for environment variables.