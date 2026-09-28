# Rollback and Cleanup Plan

## Rollback criteria

Investigate and roll back when:

- API 5xx error rate exceeds 2% for five minutes;
- synthetic health checks fail twice consecutively;
- new reports are lost;
- duplicate protection fails;
- a significant security regression is introduced.

The 2% threshold is a lab example and must be adjusted
for real traffic volume and reliability objectives.

## Application rollback

1. Stop further deployment.
2. Identify the last known-good Git commit and Lambda version.
3. Review infrastructure compatibility.
4. Restore the known-good application version.
5. Run a fictional API test.
6. Confirm DynamoDB state.
7. Verify CloudWatch metrics and logs.
8. Verify notification behaviour.
9. Record the recovery.

## Infrastructure rollback

Do not blindly reverse infrastructure changes.

Generate and review a new Terraform plan showing the
intended recovery changes before applying it.

## Lab cleanup

1. Save required evidence.
2. Generate a Terraform destroy plan.
3. Review every resource marked for deletion.
4. Apply the reviewed destroy plan.
5. Verify Terraform state.
6. Check for remaining tagged AWS resources.

Never delete unrelated shared resources.
