---
id: replay-example
title: Replay Example
sidebar_label: Replay Example
slug: /practitioner-package/replay-example
---

# Replay Example

The replay example uses the synthetic dataset in `examples/datasets/cloud_identity_events.csv`.

Run:

```bash
python3 examples/replay/replay-cloud-identity.py
```

Expected result:

```json
{
  "event_count": 8,
  "alert_count": 1,
  "result": "detected"
}
```

The replay script writes `examples/replay/replay-result.json`.
