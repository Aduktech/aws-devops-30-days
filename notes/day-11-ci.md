# Day 11 — Continuous Integration with GitHub Actions

## What CI Means

Continuous Integration automatically applies the same checks to code changes.

Instead of depending only on developers to remember every command, GitHub Actions runs the agreed validation workflow for pull requests and changes to the main branch.

## Pipeline Triggers

The Inventory API CI workflow runs when a pull request targets `main` and when code is pushed to `main`.

Feature branches are therefore checked through their pull requests before they are merged.

## Pipeline Checks

The workflow performs the following checks in order:

1. Check out the repository.
2. Configure Python 3.12.
3. Install application and CI dependencies.
4. Run Ruff lint checks.
5. Check Python formatting.
6. Run pytest.
7. Build the Docker image.
8. Scan the image with Trivy.

## Fail Fast

The pipeline stops when an earlier required check fails.

For example, if pytest fails, the Docker build and security scan should not continue.

This avoids wasting time on code that is already known to be incorrect.

## Deliberate Failure Test

I deliberately changed the health test to expect HTTP 201 instead of HTTP 200.

The test failed locally and the GitHub Actions workflow also failed.

The failing CI run provided evidence that broken code would not pass the pipeline.

I restored the correct HTTP 200 expectation, ran the tests locally and pushed another commit.

The GitHub Actions workflow ran again and the test stage passed.

## Docker Build

The pipeline builds `inventory-alert-api:ci`.

This proves that tested source code can also be packaged successfully using the project's Dockerfile.

## Security Scan

Trivy scans the built Docker image for HIGH and CRITICAL known vulnerabilities.

The pipeline is configured to fail when relevant fixable vulnerabilities are detected.

A failed security scan should be investigated rather than simply disabled to make the pipeline green.

## Main Lesson

CI creates a repeatable quality gate.

Code should move toward deployment only after formatting, tests, build checks and required security checks have passed.
