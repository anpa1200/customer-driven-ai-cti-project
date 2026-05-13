---
id: attack-mappings
title: ATT&CK and D3FEND Mappings
sidebar_label: ATT&CK / D3FEND
slug: /standard/attack-mappings
---

# ATT&CK and D3FEND Mappings

The worked case includes a concrete mapping file:

`examples/attack-mappings/det-001-attack-d3fend.yaml`

## DET-001 Mapping

| Model | ID | Name |
|---|---|---|
| ATT&CK tactic | TA0003 | Persistence |
| ATT&CK technique | T1098 | Account Manipulation |
| Related ATT&CK technique | T1485 | Data Destruction |
| Related ATT&CK technique | T1490 | Inhibit System Recovery |
| D3FEND | D3-AM | Account Monitoring |
| D3FEND | D3-LAM | Log Analysis |
| D3FEND | D3-CAM | Cloud Account Monitoring |

## Mapping Rules

- Every detection **MUST** map to at least one ATT&CK technique.
- Every production candidate **SHOULD** map to at least one defensive countermeasure.
- Mapping confidence **MUST** be documented when the technique is inferred rather than directly observed.
