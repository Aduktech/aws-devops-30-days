# Terraform Change Control

Infrastructure changes follow this process:

1. Create a feature branch.
2. Modify the Terraform configuration.
3. Run formatting, validation and security checks locally.
4. Push the branch and create a pull request.
5. CI runs Terraform checks and produces a plan.
6. A human reviews the Terraform plan.
7. The approved plan is applied.
8. Outputs and verification results are recorded as evidence.
9. The change is merged after successful verification.

Terraform changes must not be automatically applied from an unreviewed pull request.

## Emergency Changes

If an urgent infrastructure change is required, the reason, change, result and rollback action must still be documented.
