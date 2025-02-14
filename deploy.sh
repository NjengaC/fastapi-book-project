#!/bin/bash
set -e  # Exit immediately if any command fails

# Define the container name (adjust if needed)
CONTAINER_NAME="fastapi-app-container"

echo "Starting deployment..."

# Check if a container with the same name is running
if [ "$(docker ps -q -f name=${CONTAINER_NAME})" ]; then
    echo "Stopping running container: ${CONTAINER_NAME}..."
    docker stop ${CONTAINER_NAME}
fi

# Remove the container if it exists (stopped or not)
if [ "$(docker ps -aq -f name=${CONTAINER_NAME})" ]; then
    echo "Removing container: ${CONTAINER_NAME}..."
    docker rm ${CONTAINER_NAME}
fi

# Optionally, remove the old image if needed (uncomment if desired)
# echo "Removing old image..."
# docker rmi fastapi-app

echo "Starting a new container from the image 'fastapi-app'..."
docker run -d --name ${CONTAINER_NAME} -p 8000:8000 fastapi-app

echo "Deployment completed successfully."
