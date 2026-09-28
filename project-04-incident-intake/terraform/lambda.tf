data "archive_file" "lambda" {
  type        = "zip"
  source_file = "${path.module}/../app/handler.py"
  output_path = "${path.module}/build/lambda.zip"
}

resource "aws_lambda_function" "intake" {
  function_name = var.project_name
  role          = aws_iam_role.lambda.arn

  runtime = "python3.12"
  handler = "handler.lambda_handler"

  filename         = data.archive_file.lambda.output_path
  source_code_hash = data.archive_file.lambda.output_base64sha256

  timeout     = 10
  memory_size = 128

  environment {
    variables = {
      TABLE_NAME = aws_dynamodb_table.reports.name
      TOPIC_ARN  = aws_sns_topic.high_severity.arn
    }
  }

  depends_on = [
    aws_iam_role_policy.lambda,
    aws_cloudwatch_log_group.lambda
  ]
}
