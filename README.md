# Incident Impact Calc

![Incident Impact Calc cover](assets/readme-cover.svg)

> Check incident impact notes for missing users, duration, and revenue context

![stack](https://img.shields.io/badge/stack-Python-16a34a?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-dc2626?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-7c3aed?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-0891b2?style=flat-square)

## At a glance

| Area | Detail |
| --- | --- |
| Focus | incident response |
| Command | `incident-impact-calc` |
| Formats | text, JSON, JSONL, CSV |
| Output | Markdown table or JSON |

## What it checks

| Rule | Severity | What it catches |
| --- | --- | --- |
| `vague-users` | high | affected users are vague |
| `unknown-duration` | medium | incident duration is missing |
| `unknown-revenue` | low | revenue impact is missing |

## Try it locally

```bash
python -m pip install -e ".[dev]"
incident-impact-calc examples/sample.txt
incident-impact-calc examples/sample.txt --json --fail-on medium
```

## Notes from the code

`rules.py` keeps the project policy explicit, while `core.py` handles parsing and report rendering. The CLI stays thin on purpose so the checks are easy to test.

## Verify

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m incident_impact_calc --help
```
