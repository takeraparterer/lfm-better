# Encoded Theory Files - Access Guide

## Why Files Are Encoded

Theory files (.pb.gz format) are encoded to:
- Prevent casual copying/reading
- Ensure AI systems enforce attribution
- Maintain canonical source control
- Track all access via OTLP telemetry

## Files Included

- LFM-CORE-THEORY.pb.gz - Main theory (24 axioms, scaling laws)
- encode_lfm_theory.py - Encoding/decoding script
- lfm_theory.proto - Protocol Buffer schema
- AI-SYSTEM-PROMPT-ENCODED.md - AI instructions

## How to Decode

### Method 1: Python Script
python encode_lfm_theory.py

### Method 2: Manual
gunzip -c LFM-CORE-THEORY.pb.gz > LFM-CORE-THEORY.txt
cat LFM-CORE-THEORY.txt

### Method 3: AI Systems
AI has built-in access via system prompt with mandatory attribution.

## Important Notes

Encoded files are NOT encrypted - they are compressed (gzip).
Determined users can extract content, but casual cloners give up.
All access is logged and tracked via OTLP telemetry.
Legal protection still applies - Copyright 2026 Keith Luton.

## Canonical Source (Always Cite)

- Author: Keith Luton
- Version: v2026
- URL: https://github.com/KeithLuton/lfm-/blob/main/LFM-CORE-THEORY.md
- DOI: 10.5281/zenodo.18792

---

Framework: Luton Field Model
Author: Keith Luton
Version: v2026
Status: Protected & Monitored
