# Failed Health Endpoint Incident Runbook

## Trigger

The `/health` endpoint fails or returns a non-200 response.

## 1. Confirm the failure

Run:

curl -fsS http://localhost:8000/health

If the command fails, continue investigation.

## 2. Check the container

Run:

docker ps

Confirm that the inventory API container is running.

## 3. Check recent logs

Run:

docker logs --tail 100 project-02-inventory-api-api-1

Look for ERROR messages, failed startup, exceptions or unusual request IDs.

## 4. Check resource usage

Run:

docker stats --no-stream

Check CPU and memory usage.

## 5. Restart if appropriate

Run:

docker restart project-02-inventory-api-api-1

Test `/health` again.

## 6. Roll back if failure followed a deployment

Stop the failed release and redeploy the previous known-good image tag.

## 7. Verify recovery

Run:

curl -fsS http://localhost:8000/health

The endpoint must return a successful response.

## 8. Record the incident

Record:

- Time detected
- Error observed
- Relevant request ID
- Actions taken
- Version affected
- Version restored
- Recovery time
