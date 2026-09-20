# Inventory API Threat Model

| Asset | Threat | Control | Remaining Risk | Owner |
|---|---|---|---|---|
| API | Unauthorised access | Security groups and authentication where required | Misconfiguration could expose the API | DevOps |
| AWS credentials | Credentials leaked into Git or logs | IAM roles, temporary credentials and secret scanning | Developer may accidentally commit a secret | DevOps |
| Inventory data | Unauthorised reading or modification | Least-privilege IAM and application validation | Application-level vulnerability | Application Team |
| Docker image | Vulnerable dependency or OS package | Trivy image scanning in CI | New vulnerability may appear after build | DevOps |
| Terraform configuration | Insecure cloud configuration | Checkov, Terraform validation and plan review | Scanner may not detect every design issue | DevOps |
| Terraform state | State exposure or corruption | Private encrypted S3, versioning and lock file | Excessive IAM access to state bucket | DevOps |
| S3 artifacts | Public exposure | S3 Block Public Access and encryption | IAM or bucket policy misconfiguration | DevOps |
