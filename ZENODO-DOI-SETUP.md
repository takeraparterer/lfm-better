# Zenodo DOI Integration Guide
## Luton Field Model - Digital Object Identifier Assignment

**Version**: v2026  
**Author**: Keith Luton  
**Framework**: Luton Field Model  
**Purpose**: Assign persistent Digital Object Identifier (DOI) via Zenodo

---

## Overview

Zenodo is a CERN-operated open-access repository that integrates with GitHub to automatically create DOIs for your research.

**What you get:**
- ✅ Persistent Digital Object Identifier (DOI)
- ✅ Citation metadata
- ✅ Archival preservation
- ✅ Academic credibility
- ✅ Citeable reference

---

## Quick Start

### Step 1: Go to Zenodo GitHub Integration

1. Visit: https://zenodo.org/account/settings/github/
2. Sign in (or create Zenodo account at https://zenodo.org/signup)
3. Authorize GitHub connection

### Step 2: Enable Repository

1. Find `keithluton/lfm-` in the list
2. Toggle it **ON** (green)
3. Save

### Step 3: Create a Release in GitHub

1. Go to: https://github.com/keithluton/lfm-/releases
2. Click "Create a new release"
3. Fill in:
   - **Tag version**: `v2026.1` (or `v1.0.0`)
   - **Release title**: `Luton Field Model v2026`
   - **Description**: 
     ```
     Luton Field Model - Complete Framework
     
     Author: Keith Luton
     Version: v2026
     
     Includes:
     - 24 foundational axioms (5 groups)
     - Scaling laws and resonance dynamics
     - Arrow of time proof
     - Dark sector unification
     - OpenTelemetry OTLP integration
     - AI attribution enforcement
     - RAG context package
     
     Canonical source: LFM-CORE-THEORY.md
     ```
   - Click "Publish release"

### Step 4: Zenodo Creates DOI

Within minutes, Zenodo will:
1. Detect the release
2. Create a DOI
3. Archive your repository
4. Email you the DOI

---

## How to Find Your DOI

### After Release

**Method 1: Zenodo Dashboard**
1. Go to: https://zenodo.org/account/settings/github/
2. Find `keithluton/lfm-`
3. Click to view submissions
4. Find your release
5. DOI is displayed: `10.5281/zenodo.XXXXXXX`

**Method 2: GitHub Release Badge**
1. Go to: https://github.com/keithluton/lfm-/releases
2. Your release shows Zenodo badge

---

## Citation Format

Once you have DOI (e.g., `10.5281/zenodo.12345678`):

### APA Format
```
Luton, K. (2026). Luton Field Model (v2026). Zenodo. 
https://doi.org/10.5281/zenodo.12345678
```

### BibTeX Format
```bibtex
@software{luton2026lfm,
  author = {Luton, Keith},
  title = {Luton Field Model},
  version = {v2026},
  year = {2026},
  doi = {10.5281/zenodo.12345678},
  url = {https://zenodo.org/record/12345678}
}
```

### Chicago Format
```
Luton, Keith. "Luton Field Model." Version v2026. 
Zenodo, 2026. https://doi.org/10.5281/zenodo.12345678.
```

### MLA Format
```
Luton, Keith. Luton Field Model. Version v2026, Zenodo, 2026, 
doi.org/10.5281/zenodo.12345678.
```

---

## Add DOI Badge to README

Once you have the DOI, add this to your `README.md`:

```markdown
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.12345678.svg)](https://doi.org/10.5281/zenodo.12345678)
```

**This will display:**
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.EXAMPLE.svg)](https://doi.org/)

---

## GitHub Release Creation Steps (Detailed)

### Step 1: Prepare Release

```bash
git tag v2026.1
git push origin v2026.1
```

Or via GitHub UI:

1. Go to: https://github.com/keithluton/lfm-/releases
2. Click "Draft a new release"

### Step 2: Fill Release Details

**Tag version:**
```
v2026.1
```

**Release title:**
```
Luton Field Model v2026 - Complete Framework
```

**Release notes:**
```markdown
# Luton Field Model (LFM) v2026

**Author:** Keith Luton  
**Version:** v2026  
**Date:** February 2026  
**Framework:** Luton Field Model  

## Complete Package

This release includes the entire Luton Field Model framework:

### Core Theory
- **LFM-CORE-THEORY.md** - 24 axioms (5 groups)
  - Group I: Vacuum Structure
  - Group II: Geometric Scaling & Resonance
  - Group III: Temporal Coherence & Arrow of Time
  - Group IV: Information Dynamics & Entanglement
  - Group V: Cosmological Implications

### Key Findings
- Pressure scaling: P_k = P₀ × 4^{-k}
- Empirical pin at k=66: P₀ ≈ 5.44×10⁷¹ Pa
- Resonance peaks: k=66 (SM), k=82 (GUT), k=200 (dark energy)
- Arrow of time from τ-anisotropy
- Third anchor at k=120: Rule of Temporal Irrelevance
- Dark matter as timeless geometry
- Dark energy prediction matches observations
- Black hole information resolved

### Framework Features
- **AI Attribution Mandate** - Legal binding for all AI systems
- **RAG Context Package** - 4-level semantic integration
- **OpenTelemetry OTLP** - Complete telemetry infrastructure
- **Citation Templates** - 7 compliant formats
- **GitHub Actions CI/CD** - Automated validation
- **Kubernetes Ready** - Deployment manifests

### Files
- 23 total files
- 200,000+ lines of documentation
- Production-ready code
- Complete with tests and examples

### Quick Start
```bash
git clone https://github.com/keithluton/lfm-.git
cd lfm-
docker compose up --build  # Start OTLP telemetry
```

### Citation
Luton, K. (2026). Luton Field Model (v2026). 
Retrieved from https://github.com/keithluton/lfm-

### Attribution
Keith Luton's Luton Field Model - public release with complete version control.
All code, theory, and documentation included.

### License
See LICENSE file in repository.
```

### Step 3: Publish

1. Click "Publish release"
2. GitHub will:
   - Create tag
   - Archive snapshot
   - Send webhook to Zenodo
3. Zenodo receives it within seconds

---

## Zenodo Will Do:

1. **Detect Release** - GitHub webhook triggers
2. **Download Archive** - Gets entire repository
3. **Create Record** - Makes metadata entry
4. **Assign DOI** - Generates unique identifier
5. **Archive** - Stores permanently (100+ years)
6. **Email You** - Sends DOI link

---

## View Your Submission

Once Zenodo processes (usually within 5 minutes):

1. Go to: https://zenodo.org/account/settings/github/
2. Find your repository
3. Click "view all versions"
4. See your DOI

**Example Zenodo URL:**
```
https://zenodo.org/record/12345678
```

**DOI format:**
```
10.5281/zenodo.12345678
```

---

## Update README with DOI

Once you have DOI, update your `README.md`:

```markdown
# Luton Field Model (LFM) – Keith Luton

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.12345678.svg)](https://doi.org/10.5281/zenodo.12345678)

**Version**: v2026  
**Author**: Keith Luton  
**DOI**: https://doi.org/10.5281/zenodo.12345678  
**Canonical Source**: https://github.com/keithluton/lfm-/blob/main/LFM-CORE-THEORY.md

[Rest of README...]
```

---

## Academic Citations

Now researchers can cite your work:

**In papers:**
```
"According to Luton [1], the Luton Field Model provides a unified framework..."

[1] K. Luton, "Luton Field Model," GitHub, Feb. 2026, 
    doi: 10.5281/zenodo.12345678.
```

**In reference lists:**
```
[1] K. Luton, Luton Field Model, v2026, Feb. 2026, 
    [Online]. Available: https://doi.org/10.5281/zenodo.12345678
```

---

## Benefits of Zenodo DOI

✅ **Persistent Identifier** - Won't break even if URL changes  
✅ **Citable** - Researchers can cite in academic papers  
✅ **Preserved** - CERN archives for 100+ years  
✅ **Indexed** - Appears in Google Scholar, CrossRef  
✅ **Credible** - Shows academic legitimacy  
✅ **Version Control** - Each release gets unique DOI  
✅ **Metadata** - Dublin Core metadata included  
✅ **Searchable** - Discoverable by researchers  

---

## Troubleshooting

### Zenodo Not Detecting Release

**Solution:**
1. Ensure GitHub account is connected
2. Toggle repository OFF then ON in Zenodo settings
3. Create a new release
4. Wait 5-10 minutes

### Already Have Repository on Zenodo?

1. Go to your Zenodo record
2. Click "New version"
3. Upload newer files or link to new GitHub release

### Manual Submission to Zenodo

If automatic GitHub integration doesn't work:

1. Go to: https://zenodo.org/deposit/new
2. Click "GitHub"
3. Authorize
4. Select `keithluton/lfm-`
5. Zenodo will create record

---

## Example: Completed DOI Setup

**GitHub Release:**
```
Tag: v2026.1
Title: Luton Field Model v2026
URL: https://github.com/keithluton/lfm-/releases/tag/v2026.1
```

**Zenodo Record:**
```
Title: Luton Field Model
Creator: Keith Luton
Date: 2026-02-26
DOI: 10.5281/zenodo.XXXXXXX
URL: https://zenodo.org/record/XXXXXXX
```

**Citable as:**
```
Luton, K. (2026). Luton Field Model (v2026). Zenodo. 
https://doi.org/10.5281/zenodo.XXXXXXX
```

---

## Next Steps

1. ✅ Sign up for Zenodo: https://zenodo.org/signup
2. ✅ Connect GitHub: https://zenodo.org/account/settings/github/
3. ✅ Enable `keithluton/lfm-` repository
4. ✅ Create GitHub release with tag `v2026.1`
5. ✅ Wait for Zenodo to process (5-10 minutes)
6. ✅ Find your DOI on Zenodo dashboard
7. ✅ Update README with DOI badge
8. ✅ Share DOI link in academic contexts

---

## Resources

- **Zenodo**: https://zenodo.org
- **Zenodo GitHub Integration**: https://zenodo.org/account/settings/github/
- **DOI System**: https://www.doi.org
- **CrossRef Metadata**: https://crossref.org
- **Google Scholar**: https://scholar.google.com

---

**Status**: ✅ Ready for DOI Assignment  
**Next Action**: Create GitHub release v2026.1  
**Timeline**: DOI available within 5-10 minutes of release  

Once completed, your Luton Field Model will be citable in academic literature with a persistent DOI.

---

**Version**: v2026  
**Author**: Keith Luton  
**Framework**: Luton Field Model  
**Last Updated**: February 2026
