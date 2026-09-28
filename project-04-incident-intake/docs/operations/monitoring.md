# Incident Intake Monitoring

## Lambda logs

Recent logs:

    aws logs tail "$LOG_GROUP" --since 30m

Recent structured events:

    aws logs filter-log-events \
      --log-group-name "$LOG_GROUP" \
      --limit 20

## Lambda error alarm

    aws cloudwatch describe-alarms \
      --alarm-name-prefix incident-intake

## Lambda metrics

Relevant operational signals:

- Invocations
- Errors
- Duration
- Throttles

## API signals

Monitor:

- HTTP 5xx responses
- HTTP 4xx responses
- request count
- latency

4xx validation failures should be analysed separately
from service-side 5xx failures.

## DynamoDB

For a known idempotency key use GetItem.

Do not use Scan as the normal production access pattern.

## SNS

Verify subscription state with:

    aws sns list-subscriptions-by-topic \
      --topic-arn "$TOPIC_ARN"

## Privacy

Logs should contain operational identifiers such as
request ID and report ID.

Do not log report summaries, personal information,
credentials or authorization tokens.
