# Personal Cloud & DevOps Operating Standard

## Purpose

This standard defines how I will design, change, deploy,
operate and remove infrastructure.

## 1. Identity and Access

- I will not use root access keys.
- I will prefer short-lived credentials and federated access.
- I will apply least privilege to users, workloads and CI/CD.
- I will not place credentials in source code.
- I will review IAM permissions before deployment.

## 2. Infrastructure

- Infrastructure should be defined as code where practical.
- Every cloud resource should have an identifiable owner,
  project and environment.
- Infrastructure changes should be reviewed before apply.
- Terraform state and variable files containing sensitive
  information must not be committed.
- Every temporary environment must have a cleanup path.

## 3. Source Control

- Meaningful changes should be committed to Git.
- Changes should be small enough to review.
- Secrets, credentials, state files, private keys, personal
  data and confidential company information must not enter
  public repositories.
- Pull requests should be used for significant changes.

## 4. CI/CD

- Automated tests should run before deployment.
- Infrastructure formatting and validation should run in CI.
- Security scanning should be part of the pipeline.
- Production-style applies require human approval.
- CI/CD should use short-lived credentials where supported.

## 5. Deployment

A deployment is complete only when the new version has been
verified as healthy.

Every deployment should have:

- a reviewed change;
- automated tests;
- a health or synthetic check;
- monitoring;
- a known-good rollback target;
- documented rollback criteria.

## 6. Observability

- Applications should produce structured logs.
- Logs should not expose secrets or unnecessary personal data.
- Important services should have useful metrics and alarms.
- Every actionable alarm must have an owner and response path.
- An alarm without a response procedure is incomplete.

## 7. Security

Security is part of design and delivery rather than a final
check.

I will:

- minimise permissions;
- scan dependencies, containers and infrastructure code;
- avoid unnecessary public exposure;
- encrypt stored data where appropriate;
- investigate security findings before accepting exceptions.

## 8. Cost

- I will understand the cost implications of architecture
  decisions before deployment.
- Temporary resources should be removed after use.
- I will check for forgotten resources after labs and tests.
- I will avoid unnecessary continuously billed resources.

## 9. Operations

When something fails:

1. Observe before changing.
2. Read the actual error.
3. Identify the affected component.
4. Check logs, metrics and state.
5. Make the smallest safe change.
6. Verify recovery.
7. Record what happened.
8. Improve the system to reduce recurrence.

## 10. Definition of Done

Work is not complete simply because deployment succeeded.

It is complete when it is:

- tested;
- reviewed;
- observable;
- secure enough for its purpose;
- recoverable;
- documented;
- and cleanly removable.
