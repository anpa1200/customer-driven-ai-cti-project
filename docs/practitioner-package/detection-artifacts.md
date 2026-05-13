---
id: detection-artifacts
title: Detection Artifacts
sidebar_label: Detection Artifacts
slug: /practitioner-package/detection-artifacts
---

# Detection Artifacts

## Sigma Rule

File: `examples/rules/privileged-mfa-backup-deletion.yml`

```yaml
title: Privileged MFA Change Followed By Backup Deletion Attempt
id: 6f0d3a5c-04f1-4f3c-a708-7f94b8207b8d
status: test
description: Detects a privileged identity MFA change followed by suspicious backup vault deletion or protection weakening activity.
```

## Microsoft Sentinel KQL

File: `examples/queries/sentinel-kql-privileged-mfa-backup-deletion.kql`

```kusto
privilegedMfaChanges
| join kind=innerunique backupDeletionActivity on Actor
| where BackupTime between (MfaTime .. MfaTime + window)
```

## Splunk SPL

File: `examples/queries/splunk-cloud-identity-backup-deletion.spl`

```spl
| where saw_mfa_change=1 AND saw_backup_delete=1 AND last_time-first_time<=7200
```
