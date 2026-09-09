# Day 9 — Build and Containerise a Small Service

## What I Built

I created a small FastAPI inventory service using fictional stock information.

The service provides:

* `GET /health`
* `GET /items`
* `POST /items`

## Health Endpoint

The `/health` endpoint returns HTTP 200 and a short JSON response when the application is running correctly.

Health endpoints can be used by Docker, load balancers and orchestration systems to determine whether an application should receive traffic.

## Input Validation

The API validates incoming inventory data.

Item names must not be empty and stock quantities cannot be negative.

Invalid requests are rejected before they are added to the application's inventory data.

## Structured Logs

The application writes request information as JSON log entries.

The logs include fields such as the event name, request method, path and HTTP status code.

Structured logs are easier for monitoring systems to search and analyse than unstructured text.

## Docker Image

The Dockerfile uses a Python slim base image.

Dependencies are copied and installed before the application source code so Docker can reuse cached dependency layers when only the application code changes.

## Non-Root User

The image creates and uses an `appuser` account.

The application does not need root privileges, so it should not run as root.

This follows the least-privilege principle.

## Port

Uvicorn listens on port 8000 inside the container.

Docker maps host port 8000 to container port 8000.

## Fixed Startup Command

The image contains a fixed `CMD` that starts Uvicorn with the same application module, host and port each time the container starts.

This helps the service start consistently across different environments.

## Health Check

The Docker image includes a `HEALTHCHECK` that calls the `/health` endpoint.

Docker can therefore report whether the running container is healthy.

## Temporary Data

The current inventory is stored only in Python memory.

Items added at runtime disappear when the container is replaced.

Persistent data will require a database or other persistent storage.

## Main Lesson

A useful containerised service needs more than application code.

It should have clear startup behaviour, health checks, input validation, useful logs, limited privileges and predictable networking.
