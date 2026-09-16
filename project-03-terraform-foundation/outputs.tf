output "vpc_id" {
  description = "ID of the foundation VPC"
  value       = aws_vpc.main.id
}

output "public_subnet_ids" {
  description = "IDs of the public subnets"
  value = [
    aws_subnet.public_1.id,
    aws_subnet.public_2.id
  ]
}

output "security_group_id" {
  description = "ID of the application security group"
  value       = aws_security_group.app.id
}

output "artifact_bucket_name" {
  description = "Name of the private artifact bucket"
  value       = aws_s3_bucket.artifacts.bucket
}
