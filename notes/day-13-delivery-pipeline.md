# Day 13 — Inventory Alert Delivery Pipeline

## Problem

A retailer, pharmacy or distributor may notice low stock too late when inventory information is kept mainly in spreadsheets. Changes may also be difficult to test and release safely.

## Solution

I built a small inventory API and created a delivery process that tests, containerises, scans and stores the application in Amazon ECR.

The delivery flow is:

```text
Source Code
    ↓
Git / GitHub
    ↓
GitHub Actions
    ↓
Automated Tests
    ↓
Docker Build
    ↓
Trivy Security Scan
    ↓
Git SHA Tag
    ↓
Amazon ECR
    ↓
Deployment
```

## API Validation

The `/items` endpoint validates inventory data before accepting it.

Example valid request:

```json
{
  "name": "gloves",
  "quantity": 4,
  "reorder_level": 10
}
```

I also tested an invalid request using `na1` instead of `name`. The API rejected it because the required `name` field was missing. This confirmed that input validation was working correctly.

## Docker Compose

Docker Compose provides a repeatable way to build and start the API.

```bash
docker compose up -d --build
```

The application can therefore be started without manually setting up the application each time.

## CI Pipeline

GitHub Actions automatically checks changes to the project.

The pipeline performs:

```text
Code
 ↓
Tests
 ↓
Docker Build
 ↓
Security Scan
 ↓
Pass / Fail
```

A failed check should be fixed before the change is merged.

## Trivy Security Scan

Trivy is used to scan the Docker image for known vulnerabilities.

```bash
docker run --rm \
-v /var/run/docker.sock:/var/run/docker.sock \
aquasec/trivy:latest \
image inventory-alert-api:0.1
```

HIGH and CRITICAL findings should be reviewed rather than ignored.

## Git SHA Tagging

The Git commit ID provides a traceable version of the application.

```bash
git rev-parse --short HEAD
```

The Docker image is tagged using this Git SHA before being pushed to ECR.

This creates a clear link between:

```text
Source Code → Git Commit → Docker Image
```

## Amazon ECR

Amazon ECR stores the Docker image that can later be used for deployment.

The image is pushed using its Git SHA tag so that the exact application version can be identified.

## Tag Immutability

ECR tag immutability helps prevent an existing image tag from being silently replaced with another image.

This improves image traceability and makes deployment and rollback safer.

## Branch Protection

The `main` branch should require a successful CI check before changes are merged, where the GitHub account and repository settings support this.

The expected flow is:

```text
Feature Branch → Pull Request → CI Passes → Merge to main
```

## Deployment Procedure

Before deployment:

1. Confirm the correct AWS account and region.
2. Confirm CI passed.
3. Confirm the required image exists in ECR.
4. Confirm the image security scan has been reviewed.
5. Deploy the approved Git SHA image.

## Health Check

After deployment, the application health endpoint should be checked:

```bash
curl -f http://localhost:8001/health
```

A successful response confirms that the API is reachable and healthy.

## Rollback

If a new version fails, the previous known-good Git SHA image should be redeployed.

For example:

```text
New version → Failure
                  ↓
Previous Git SHA → Redeploy
```

This is one reason why traceable image versions are important.

## Cleanup

Local containers can be stopped with:

```bash
docker compose down
```

Unused local resources should be removed when they are no longer needed. The ECR repository should be kept if it will be used in later challenge projects.

## Lessons Learned

Day 13 showed that DevOps is not only about writing application code. A reliable application also needs automated testing, repeatable builds, security scanning, version tracking, safe storage and a clear rollback process.

The main delivery process is:

```text
Code → Test → Build → Scan → Tag → Push → Verify → Deploy
```
