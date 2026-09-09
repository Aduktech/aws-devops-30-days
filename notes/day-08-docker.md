# Day 8 — Docker Concepts and First Container

## Why Docker Is Useful

Docker helps package an application and the environment it requires so that it can run more consistently across development, testing and deployment systems.

It reduces problems where an application works on one computer but fails on another because the runtime or dependencies are different.

## Docker Image

A Docker image is a reusable package used to create containers.

It can contain the operating-system base, runtime, dependencies, application files and startup configuration required by an application.

An image is not the same as a running application.

## Docker Container

A container is an instance created from a Docker image.

A container can be running or stopped.

Several containers can be created from the same image.

## Image Versus Container

An image is the reusable blueprint or package.

A container is a running or stopped instance created from that image.

Removing a container does not automatically remove the image that was used to create it.

## Dockerfile

A Dockerfile contains instructions Docker uses to build an image.

Instructions such as `FROM`, `WORKDIR`, `COPY`, `RUN`, `EXPOSE`, `ENV` and `CMD` can describe how an application image should be built and started.

## Layers

Docker images are built from layers.

Different Dockerfile instructions can create layers, and Docker can reuse unchanged layers during later builds. This can make builds faster.

## Ports

Applications inside containers can listen on network ports.

A port mapping such as `8000:8000` sends traffic from port 8000 on the host machine to port 8000 inside the container.

## Environment Variables

Environment variables provide configuration values to running applications.

For example, `APP_ENV=development` can tell an application which environment it is running in.

Environment variables should not automatically be treated as a secure secret-management system.

## Volumes

A Docker volume stores data separately from the container.

This is useful because containers can be deleted and recreated while important data may need to remain.

## Docker Compose

Docker Compose allows multiple container settings and services to be described in a YAML file.

It can define build instructions, ports, environment variables, volumes and networks.

## Commands Practised

`docker version` checks whether the Docker client and engine can communicate.

`docker run --rm hello-world` runs the Docker test image and removes the container after it exits.

`docker ps` lists running containers.

`docker ps -a` also lists stopped containers.

`docker image ls` lists locally stored images.

`docker inspect` displays detailed information about a Docker object.

`docker logs` displays container logs.

`docker stop` stops a running container.

`docker rm` removes a container.

`docker image rm` removes an image.

`docker system df` shows disk space used by Docker resources.

## Main Lesson

Docker separates the reusable application package from the running instance.

Image = reusable package.

Container = instance created from the image.
