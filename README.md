# Docker Compose Get Started

**Name:** Muhammad Arman Prambudya  
**NIM:** 123103146

## Overview
This project demonstrates a multi-container application using Docker Compose with Flask and Redis.

## Technologies
- Docker
- Docker Compose
- Python Flask
- Redis

## Project Structure
- app/: Flask application
- compose.yaml: Main Compose configuration
- infra.yaml: Redis infrastructure configuration
- .env: Environment variables

## Run the Application
docker compose up -d

Open http://localhost:8000

## Inspect Services
docker compose ps
docker compose logs -f
docker compose exec web env
docker compose exec redis redis-cli GET hits

## Stop the Application
docker compose down

## GitHub Repository
https://github.com/muhammadprambudya-png/docker-compose-get-started-123103146
