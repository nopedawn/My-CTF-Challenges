#!/bin/bash

declare IMAGE_AND_CONTAINER_NAME="technofair11_finals_foren__hilf"

docker stop $IMAGE_AND_CONTAINER_NAME
docker rm $IMAGE_AND_CONTAINER_NAME
docker image rm $IMAGE_AND_CONTAINER_NAME
