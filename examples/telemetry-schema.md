# Telemetry Schema Examples

## Minimal Cloud Identity Event

| Field | Required | Description |
|---|---|---|
| `event_time_utc` | Yes | Event timestamp in UTC |
| `event_source` | Yes | Source system name |
| `user` | Yes | Actor user principal or service identity |
| `src_ip` | Yes | Source IP or host address |
| `operation` | Yes | Activity or audit operation |
| `target` | Yes | Target resource or role |
| `result` | Yes | Operation result |
| `correlation_id` | Yes | Correlation ID for event stitching |

## ECS-Aligned Field Mapping

| Project field | ECS-style field |
|---|---|
| `event_time_utc` | `@timestamp` |
| `event_source` | `event.provider` |
| `user` | `user.email` |
| `src_ip` | `source.ip` |
| `operation` | `event.action` |
| `target` | `cloud.resource.name` |
| `result` | `event.outcome` |
| `correlation_id` | `event.id` |

## OCSF-Aligned Field Mapping

| Project field | OCSF-style field |
|---|---|
| `event_time_utc` | `time` |
| `event_source` | `metadata.product.name` |
| `user` | `actor.user.email_addr` |
| `src_ip` | `src_endpoint.ip` |
| `operation` | `activity_name` |
| `target` | `resources.name` |
| `result` | `status` |
| `correlation_id` | `correlation_id` |
