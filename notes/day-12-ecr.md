# Day 12 — Amazon ECR and Image Traceability

## What I Learned

Amazon Elastic Container Registry (ECR) is an AWS service used to store container images.

A Docker image is a packaged version of an application. A container is a running instance of an image. A registry stores images so that deployment systems can retrieve them.

## Why Image Traceability Matters

A deployment should be traceable to the source-code version that produced it.

Using only the `latest` Docker tag can make it difficult to know exactly which code is running because the tag can point to different images over time.

A Git commit SHA provides a precise reference to the source-code commit.

The traceability chain is:

Git commit
↓
Docker image
↓
ECR image
↓
Deployment

## ECR Repository

I created a private ECR repository named:

`inventory-alert-api`

The repository was configured for image scanning on push.

## Image Tags

I pushed the image using:

* `0.1` — a human-friendly version tag.
* Git commit SHA — a traceable reference to the source-code version.

The Git SHA is more useful for identifying exactly which source commit produced an image.

## Authentication

Docker was authenticated to ECR using the AWS CLI `get-login-password` command.

The authentication password was passed through standard input rather than being written directly into the command.

I did not create or store a permanent AWS access key for Docker authentication.

## Security Scanning

ECR scanning was enabled on push.

The scan checks the image for known vulnerabilities.

A scan result should be treated as evidence about the image at that point in time, not as a permanent guarantee that the image is secure.

## Important Identifiers

A Docker image can have:

* A tag such as `0.1`
* A Git commit SHA identifying the source version
* An image digest beginning with `sha256:` identifying the image content

These identifiers serve different purposes.

## Main Lesson

The important lesson from Day 12 is that a deployable container should be traceable.

I should be able to identify:

1. Which Git commit produced the image.
2. Which ECR image tag was pushed.
3. Which image digest represents the image.
4. What security scan results were associated with the image.

This makes future deployments and incident investigation easier.
