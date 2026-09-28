output "api_url" {
  value = aws_apigatewayv2_stage.default.invoke_url
}

output "lambda_name" {
  value = aws_lambda_function.intake.function_name
}

output "dynamodb_table" {
  value = aws_dynamodb_table.reports.name
}

output "incident_topic_arn" {
  value = aws_sns_topic.high_severity.arn
}

output "log_group" {
  value = aws_cloudwatch_log_group.lambda.name
}
