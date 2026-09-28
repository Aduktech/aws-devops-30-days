# Day 27 — Serverless Incident Intake Deployment Evidence

## Release Details

- **Project:** Serverless Incident Intake
- **Deployment date:** 28 September 2026
- **AWS Region:** eu-west-2
- **Git commit:** [ADD COMMIT HASH]
- **Environment:** Lab

## Terraform Deployment

- **Terraform validation:** Passed
- **Terraform plan:** [15 to be created]
- **Terraform apply:** [Passed]
- **Infrastructure managed with Terraform:** API Gateway, Lambda, DynamoDB, SNS, CloudWatch and IAM resources.

No Terraform state, plan files, credentials, personal email addresses, AWS account numbers or full API URLs are included in this document.

## Verification Results

| Check | Result | Evidence |
|---|---|---|
| API test | [Passed] | POST `/incidents` tested |
| Duplicate handling | [Passed] | Duplicate report returns existing report ID |
| SNS notification | [Pending] | High-severity notification checked |
| CloudWatch alarm | [OK] | Lambda error alarm checked |
| Unit tests | Passed | Automated Lambda handler tests completed |

## Issues Encountered

During deployment, the AWS SSO deployment identity initially lacked several permissions required by Terraform to manage the infrastructure.

Issues included:

- Lambda read permissions required during Terraform refresh.
- API Gateway stage creation attempted resource tagging inherited from Terraform provider `default_tags`.
- SNS subscription configuration required a valid notification email value.
- AWS SSO sessions had to be refreshed after permission-set changes.

The deployment continued to use AWS IAM Identity Center/SSO credentials. Root credentials and AdministratorAccess were not used.

## Security and Cost Controls

- IAM permissions are scoped to the lab resources where practical.
- DynamoDB uses on-demand capacity.
- SNS is used only for incident notifications and operational alerts.
- CloudWatch log retention is limited.
- No NAT Gateway is required for this project.
- Terraform state, plan files, local variable files and generated deployment ZIP files are excluded from Git.
