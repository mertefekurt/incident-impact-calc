![Incident Impact Calc cover](assets/readme-cover.svg)

# Incident Impact Calc

> Check incident impact notes for missing users, duration, and revenue context

This is a review desk for incident response. The useful part is not a dashboard; it is the tiny repeatable moment where vague records become specific findings.

## Finding catalog for `incident-impact-calc`

| Finding | Level | Why it matters |
| --- | --- | --- |
| `vague-users` | high | affected users are vague |
| `unknown-duration` | medium | incident duration is missing |
| `unknown-revenue` | low | revenue impact is missing |

## Try the sample

```bash
git clone https://github.com/mertefekurt/incident-impact-calc.git
cd incident-impact-calc
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

```bash
incident-impact-calc examples/sample.txt
incident-impact-calc examples/sample.txt --json
```

## Reading the output

- Markdown is meant for humans reviewing a change.
- JSON is meant for CI, scripts, or saved reports.
- `--fail-on` lets the repo decide how strict a gate should be.
