# Day 10 — Docker Compose, Tests and Configuration

## Docker Compose

Docker Compose makes the local application environment easier to repeat.

Instead of remembering a long `docker run` command, the service configuration is stored in `docker-compose.yml`.

The Compose file defines the application build, port mapping, environment variables and health check.

## Configuration

Application configuration is separated from the Python source code.

The project includes `.env.example` with safe example values.

The real `.env` file is ignored by Git.

The application reads values such as `APP_ENV` and `LOG_LEVEL` from environment variables.

## Automated Tests

I created three automated tests.

The health test confirms that `/health` returns HTTP 200.

The valid-item test confirms that correct inventory data can be created.

The invalid-input test confirms that a negative quantity is rejected with HTTP 422.

## Test Failure

I deliberately changed the expected health status code from 200 to 201.

The test failed and pytest returned a non-zero exit code.

I changed the expected value back to 200 and all tests passed.

## Makefile

I created a Makefile so common actions can be run using short commands.

`make up` builds and starts the local service.

`make test` runs pytest inside the API container.

`make logs` follows application logs.

`make down` stops the local Compose environment.

## Data Services

Redis and PostgreSQL were not added because the current application does not use either service.

Infrastructure should be added when there is a real application requirement rather than only to make the stack appear more complex.

## Main Lesson

A local development environment becomes more reliable when configuration is separated from code, the startup process is described in Compose and automated tests can be run through one repeatable command.
