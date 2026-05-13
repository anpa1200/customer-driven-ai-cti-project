# Sample Registers

These registers are synthetic examples for the Meridian Freight Group worked case.

## Files

- `evidence-register.csv` - evidence labels, sources, confidence, and acceptance state
- `pir-register.csv` - customer decision-linked intelligence requirement
- `sir-register.csv` - specific information requirements with closure criteria
- `detection-backlog.csv` - detection ownership, DRL, status, and priority
- `detection-health-register.csv` - pilot and production health tracking

## Register Rules

- Every SIR maps to a PIR.
- Every accepted assessment has an evidence row.
- Every detection has an owner, data source, DRL, and status.
- Undefined precision is recorded as `undefined`, not `0`, when there are no true positives.
