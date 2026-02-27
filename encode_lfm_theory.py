#!/usr/bin/env python3
import os
import gzip
import time

print("LFM THEORY ENCODER")
print("=" * 70)

# Read the theory file
theory_file = "LFM-CORE-THEORY.md"
if not os.path.exists(theory_file):
    print(f"ERROR: {theory_file} not found")
    exit(1)

with open(theory_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Create metadata
metadata = f"""
AUTHOR: Keith Luton
VERSION: v2026
DOI: 10.5281/zenodo.18792
URL: https://github.com/KeithLuton/lfm-/blob/main/LFM-CORE-THEORY.md
TIMESTAMP: {int(time.time())}
FRAMEWORK: Luton Field Model
---
{content}
"""

# Compress with gzip
output_file = "LFM-CORE-THEORY.pb.gz"
with gzip.open(output_file, 'wb') as f:
    f.write(metadata.encode('utf-8'))

file_size = os.path.getsize(output_file)
print(f"✅ Encoded: {theory_file} → {output_file}")
print(f"   File size: {file_size} bytes")
print()
print("Encoded file is now unreadable to casual users")
print("AI systems can decode it with gzip + extraction")
print()
