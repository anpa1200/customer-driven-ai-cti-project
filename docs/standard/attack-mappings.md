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

- Every detection **MUST** name the behavior it detects and the evidence supporting that behavior.
- A detection **SHOULD** map to an ATT&CK technique only when the behavior and source evidence support the mapping.
- A detection **MUST NOT** force an ATT&CK technique to satisfy a coverage table.
- If no defensible ATT&CK mapping exists, the detection **MUST** state `ATT&CK mapping: Gap / Not mapped` and explain why.
- Every production candidate **SHOULD** map to at least one defensive countermeasure when a defensible mapping exists.
- Mapping confidence **MUST** be documented when the technique is inferred rather than directly observed.

For the tradecraft standard behind this rule, use the Field Manual pages on [ATT&CK as a working tool](https://1200km.com/cti-analyst-field-manual/docs/frameworks/mitre-attack-as-working-tool/) and [ATT&CK mapping mistakes](https://1200km.com/cti-analyst-field-manual/docs/frameworks/attck-mapping-mistakes/). For actor-specific examples, use the Israel CTI [TTP To Detection Matrix](https://1200km.com/israel-government-threat-actors-cti/navigation/ttp-detection-matrix/).
