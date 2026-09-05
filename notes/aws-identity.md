# AWS Identity and Access Notes

## Root User

The root user is the original and most powerful identity in an AWS account. It should be protected with MFA and should not be used for normal daily AWS work. Root access keys should not be created.

## IAM User

An IAM user is an identity created inside one AWS account. It can have permissions, console credentials and long-term access keys. Human users should use temporary credentials instead of long-term access keys where possible.

## IAM Identity Center User

An IAM Identity Center user is a workforce identity that can be given access to AWS accounts through permission sets. It can use single sign-on and temporary AWS credentials instead of permanent access keys.

## IAM Role

An IAM role is an AWS identity with permissions that can be assumed by a user, application or AWS service. A role normally provides temporary credentials instead of permanent access keys.

## IAM Policy

An IAM policy defines what actions are allowed or denied. Policies can control which AWS services, actions and resources an identity can access.

## Permission Set

A permission set is used by IAM Identity Center to define the permissions a user or group receives when accessing an AWS account.

## Least Privilege

Least privilege means giving an identity only the permissions it needs to perform its work. A lab user that only needs to view Regions and list S3 buckets should not receive administrator access.

## Region

An AWS Region is a separate geographic area where AWS operates infrastructure. Resources created in one Region do not automatically appear in every other Region.

My main lab Region is `eu-west-2`.

## Availability Zone

An Availability Zone is an isolated location inside an AWS Region. Using resources across multiple Availability Zones can improve availability because a problem in one location does not have to stop the whole application.

## Shared Responsibility

AWS is responsible for security of the cloud, including its physical infrastructure and underlying cloud platform.

The customer is responsible for security in the cloud, including data, IAM permissions, application configuration and many operating-system and network settings depending on the AWS service being used.

## AWS CLI Identity Check

Before making important changes through the AWS CLI, I should confirm the identity being used:

`aws sts get-caller-identity --profile devops-lab`

I should also check the configured Region:

`aws configure get region --profile devops-lab`

This reduces the risk of making changes in the wrong AWS account or Region.
