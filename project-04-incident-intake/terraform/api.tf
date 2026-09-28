resource "aws_apigatewayv2_api" "http" {
  name          = "${var.project_name}-api"
  protocol_type = "HTTP"
}

resource "aws_apigatewayv2_integration" "lambda" {
  api_id                 = aws_apigatewayv2_api.http.id
  integration_type       = "AWS_PROXY"
  integration_uri        = aws_lambda_function.intake.invoke_arn
  payload_format_version = "2.0"
}

resource "aws_apigatewayv2_route" "incidents" {
  api_id    = aws_apigatewayv2_api.http.id
  route_key = "POST /incidents"
  target    = "integrations/${aws_apigatewayv2_integration.lambda.id}"
}

resource "aws_apigatewayv2_stage" "default" {
  provider    = aws.untagged
  api_id      = aws_apigatewayv2_api.http.id
  name        = "$default"
  auto_deploy = true

  lifecycle {
    create_before_destroy = true
  }

  default_route_settings {
    throttling_burst_limit = 5
    throttling_rate_limit  = 2

  }
}

resource "aws_lambda_permission" "gateway" {
  statement_id  = "AllowAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.intake.function_name
  principal     = "apigateway.amazonaws.com"

  source_arn = "${aws_apigatewayv2_api.http.execution_arn}/*/*"
}
