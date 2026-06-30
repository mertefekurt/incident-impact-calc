# incident-impact-calc

**Ops Handoff.** Check incident impact notes for missing users, duration, and revenue context.

## Who Uses It

Incident reviews need clear impact statements. This CLI flags vague impact notes before a postmortem is finalized.

## What To Provide

`incident-impact-calc` accepts incident impact notes or postmortem draft text in text, JSON, JSONL, or CSV form.

## What Comes Back

```bash
python -m pip install -e ".[dev]"
incident-impact-calc examples/sample.txt
incident-impact-calc examples/sample.txt --json --fail-on medium
```

## Escalation

| Rule | Severity | Meaning |
|---|---:|---|
| `vague-users` | high | affected users are vague |
| `unknown-duration` | medium | incident duration is missing |
| `unknown-revenue` | low | revenue impact is missing |

## Tests

```bash
ruff check .
pytest
python -m incident_impact_calc --help
```

License: MIT

### Example Input

```text
impact many users duration unknown revenue unknown severity high
```

### Architecture

`cli.py` reads files, `core.py` evaluates records, and `rules.py` keeps the incident-impact-calc policy surface explicit.
