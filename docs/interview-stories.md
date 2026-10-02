## STAR 1 — Recovering a Failed Kubernetes Deployment

### Situation

While building a containerised FastAPI application, I was
practising Kubernetes deployment and release recovery using
a local Kind cluster.

### Task

I needed to demonstrate that I could identify a failed
release and safely restore the application rather than
simply redeploying randomly.

### Action

I deliberately deployed a non-existent image version.

I checked Pod status, used kubectl describe and Kubernetes
events to identify the image pull failure, and reviewed the
Deployment rollout.

I then used Kubernetes rollout undo to restore the previous
known-good image and verified the Deployment became healthy.

### Result

The application returned to its previous working version.

The exercise changed how I think about deployment: a release
needs observable health checks and a known rollback target,
not simply a successful deployment command.

## STAR 2 — Reducing Cloud Permission Risk

### Situation

During my Terraform AWS labs, infrastructure operations
failed because my authenticated identity did not have some
required IAM permissions.

### Task

I needed to resolve the deployment problem without using
root credentials or simply granting AdministratorAccess.

### Action

I read the AWS AccessDenied responses and identified the
specific denied API actions.

I separated the permissions required by my Terraform
deployment identity from the permissions required by the
application workload.

I reviewed the execution policies and reduced them to the
AWS actions and resources required by the application.

I continued using short-lived IAM Identity Center
credentials rather than storing long-lived access keys.

### Result

I developed a clearer least-privilege model and learned to
treat AccessDenied as an authorization problem to diagnose,
rather than automatically increasing permissions.


## STAR 3 — Making AWS Infrastructure Repeatable

### Situation

Manually creating cloud infrastructure can cause
configuration drift and makes environments difficult to
reproduce.

### Task

I wanted to create a small AWS foundation that could be
reviewed, recreated and removed consistently.

### Action

I defined the environment in Terraform, including the VPC,
subnets, routing and secure S3 configuration.

I added consistent tags, remote Terraform state, formatting
and validation checks and a plan-before-apply workflow.

I also documented cleanup and used Terraform destroy plans
rather than relying on manual console deletion.

### Result

The infrastructure became reproducible and reviewable from
source control.

The project also gave me practical experience with state
management, IAM permissions, change review and infrastructure
cleanup.## STAR 3 — Making AWS Infrastructure Repeatable

### Situation

Manually creating cloud infrastructure can cause
configuration drift and makes environments difficult to
reproduce.

### Task

I wanted to create a small AWS foundation that could be
reviewed, recreated and removed consistently.

### Action

I defined the environment in Terraform, including the VPC,
subnets, routing and secure S3 configuration.

I added consistent tags, remote Terraform state, formatting
and validation checks and a plan-before-apply workflow.

I also documented cleanup and used Terraform destroy plans
rather than relying on manual console deletion.

### Result

The infrastructure became reproducible and reviewable from
source control.

The project also gave me practical experience with state
management, IAM permissions, change review and infrastructure
cleanup.
