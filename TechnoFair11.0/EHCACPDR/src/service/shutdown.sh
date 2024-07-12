#!/bin/bash

declare IMAGE_AND_CONTAINER_NAME="final_foren__ehcacpdr"

# docker compose down

docker compose stop $IMAGE_AND_CONTAINER_NAME 
docker compose rm $IMAGE_AND_CONTAINER_NAME
docker image rm $IMAGE_AND_CONTAINER_NAME
