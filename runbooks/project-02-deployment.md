# Inventory API Deployment Runbook

## Pre-check
- Confirm CI passed
- Confirm correct AWS account
- Confirm image exists in ECR

## Deploy
Use the Docker image tagged with the approved Git SHA.

## Health Check
GET /health must return HTTP 200.

## Rollback
Redeploy the previous known-good Git SHA image.

## Cleanup
Stop unused containers and remove temporary resources.
