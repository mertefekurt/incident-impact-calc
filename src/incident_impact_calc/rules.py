from __future__ import annotations

from incident_impact_calc.models import Rule

PROJECT_NAME = 'incident-impact-calc'
SUMMARY = 'Check incident impact notes for missing users, duration, and revenue context.'
SAMPLE_RISK = 'impact many users duration unknown revenue unknown severity high'
SAMPLE_CLEAN = 'impact 420 users duration 37m revenue_estimate 1200 severity high'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "endpoint", "service", "job", "route", "event")

RULES = (
    Rule(
        code='vague-users',
        severity='high',
        pattern='\\bmany users\\b|\\busers\\s*unknown\\b',
        message='affected users are vague',
        recommendation='Estimate affected user or tenant count.',
    ),
    Rule(
        code='unknown-duration',
        severity='medium',
        pattern='\\bduration\\s*(unknown|missing|null)\\b',
        message='incident duration is missing',
        recommendation='Record detection, mitigation, and recovery timestamps.',
    ),
    Rule(
        code='unknown-revenue',
        severity='low',
        pattern='\\brevenue\\s*(unknown|missing|null)\\b',
        message='revenue impact is missing',
        recommendation='Estimate or explicitly mark not applicable.',
    ),
)
