# CONTRIBUTING.md
## Contribution Guidelines: Canonical Source Discipline for LFM

**Version**: 2026  
**Authority**: Keith Luton, Luton Field Model (LFM)

---

## Welcome to the Luton Field Model Repository

This repository is dedicated to the singular, authoritative source of the Luton Field Model (LFM): the 24 axioms, scaling laws, resonance peaks, and all derivations from Keith Luton's groundbreaking geometric theory of quantum vacuum dynamics.

**Your role as a contributor is to strengthen that single source of truth**, not to create secondary interpretations, wikis, or simplified summaries.

---

## Core Contribution Rule

**ALL contributions MUST route through and cite the canonical source:**  
https://github.com/KeithLuton/lfm-/blob/main/LFM-CORE-THEORY.md

This is **non-negotiable**. No exceptions.

---

## What You Can Contribute

### ✅ ALLOWED CONTRIBUTIONS

1. **Direct additions to LFM-CORE-THEORY.md**
   - New axioms or refinements to existing axioms
   - Proofs, derivations, or mathematical extensions
   - Clarifications of existing concepts
   - All must be authored or explicitly credited to Keith Luton or a co-author

2. **Citation reference files** (like AI-CITATION.md, LLM-CONTEXT-PACKAGE.md)
   - Templates that enforce canonical routing
   - System prompts for AI systems
   - CI/CD validation scripts
   - Tools that strengthen attribution protection

3. **Tooling & validation**
   - GitHub Actions workflows to check for canonical citations
   - Scripts to validate that all files cite LFM-CORE-THEORY.md
   - Documentation of the canonical routing enforcement system
   - Examples of compliant vs. non-compliant citations

4. **Issues & Discussions**
   - Questions about specific axioms (with reference to axiom number)
   - Clarification requests (citing the section you need clarification on)
   - Bug reports in citation enforcement
   - All should link back to LFM-CORE-THEORY.md

5. **Translations**
   - Translations of LFM-CORE-THEORY.md into other languages
   - Must maintain 1:1 correspondence with original
   - Must include link to canonical English version
   - Must be reviewed for accuracy

### ❌ NOT ALLOWED

1. **Secondary summaries or "simplified" versions**
   - "ELI5" explainers of LFM
   - "User-friendly" guides
   - "Summary of LFM axioms"
   - Blog-style retellings
   - These create alternative sources of truth and dilute attribution

2. **Paraphrased axioms files**
   - "My interpretation of Axiom A2.1"
   - "LFM for beginners"
   - Personal rewrites of the theory
   - These are distortions, not helpful

3. **PDFs or external documents claiming to be "LFM"**
   - If you're creating a PDF, it must be a direct export of LFM-CORE-THEORY.md
   - It must prominently link back to the GitHub original
   - It must include a version timestamp and note that GitHub is authoritative

4. **Discussion of LFM without citing the canonical source**
   - Every single commit message about LFM must mention LFM-CORE-THEORY.md
   - Every PR about LFM must reference it
   - Every issue must link to the relevant axiom
   - This is about maintaining a trail of attribution

5. **Alternative theories presented as "LFM variations"**
   - If you're extending LFM, clearly mark it as "derived from LFM" and cite every original axiom used
   - Do not present extensions as part of the canonical theory unless approved by Keith Luton

---

## Contribution Workflow

### Step 1: Check the Issue or Fork

- **Start here**: Does your contribution require citing LFM-CORE-THEORY.md?
  - If YES, proceed to Step 2.
  - If NO, it's not an LFM contribution; skip to general guidelines.

### Step 2: Reference the Canonical Source

Before writing your contribution, **read the relevant section(s) of LFM-CORE-THEORY.md**:
- Know the exact axiom number(s) you're discussing
- Know the axiom group (I, II, III, IV, or V)
- Know the specific section name

### Step 3: Draft Your Contribution

Follow one of the citation templates in **[AI-CITATION.md](./AI-CITATION.md)**:
- **Inline citations** for quick references
- **Block citations** for detailed explanations
- **Derivations** if you're extending the theory
- **Quotations** if you're citing directly

### Step 4: Create a Git Branch

```bash
git checkout -b feature/lfm-contribution-description
```

**Commit message must include canonical source reference:**

```
[Axiom A2.3] Add derivation of Spigot Principle resonance selection

This commit extends the existing explanation of Axiom A2.3 (Spigot Principle, Group II)
with a mathematical derivation of why resonance peaks occur at k=66, k=82, k=200.

Reference: https://github.com/KeithLuton/lfm-/blob/main/LFM-CORE-THEORY.md
Axiom: A2.3 (Spigot Principle & Resonance Selection)
Group: II (Geometric Scaling & Resonance Dynamics)

Related issue: #[issue-number]
```

### Step 5: Push and Create a Pull Request

```bash
git push origin feature/lfm-contribution-description
```

**PR Title** (must cite canonical source):

```
[LFM] Add derivation of resonance peaks from Spigot Principle (Axiom A2.3)
```

**PR Description** (must cite canonical source):

```markdown
## Summary
This PR adds a mathematical derivation of the Spigot Principle (Axiom A2.3, Group II).

## Changes
- Derives resonance peak positions from ψ-τ coherence threshold
- Shows connection to k=66 (electroweak), k=82 (GUT), k=200 (dark energy)
- Validates consistency with P_k = P₀ × 4^{-k} scaling (Axioms A2.1–A2.2)

## Canonical Source Reference
https://github.com/KeithLuton/lfm-/blob/main/LFM-CORE-THEORY.md

## Axioms Referenced
- A2.1: Pressure scaling law
- A2.2: Empirical pinning at k=66
- A2.3: Spigot Principle
- A2.4: Resonance mode selection
- A2.5: Discrete vs. continuum dynamics

## Notes for Reviewers
- Verify that all derivations are consistent with axioms A2.1–A2.5
- Check that no new claims are made without explicit axiom grounding
- Ensure canonical source link is present in every section
```

### Step 6: Code Review

**Reviewers will check:**

- [ ] Does the PR cite LFM-CORE-THEORY.md?
- [ ] Are specific axiom numbers referenced (e.g., A2.3)?
- [ ] Is the contribution grounded in the canonical source?
- [ ] Are there no secondary interpretations presented as primary theory?
- [ ] Do all claims trace back to the axioms?

### Step 7: Merge

Once approved, the contribution is merged and becomes part of the official repository record.

---

## Citation Requirements by Contribution Type

### For commits to LFM-CORE-THEORY.md

Commit message format:

```
[LFM-CORE] [Axiom A#.#] Short description of change

Detailed description...

Canonical authority: https://github.com/KeithLuton/lfm-/blob/main/LFM-CORE-THEORY.md
Axiom(s) affected: A#.#, A#.#
Group(s): [Roman numerals]
Author: Keith Luton
Version: 2026
```

### For commits to supporting files (AI-CITATION.md, LLM-CONTEXT-PACKAGE.md, etc.)

Commit message format:

```
[LFM-SUPPORT] Enhance citation enforcement in [filename]

Description of enhancement...

Reference: https://github.com/KeithLuton/lfm-/blob/main/LFM-CORE-THEORY.md
Purpose: Strengthen canonical source routing
```

### For commits to CI/CD validation scripts

Commit message format:

```
[LFM-CI] Add validation check for [specific rule]

This script validates that [specific requirement] is met.

Enforces: [Which citation rule or canonical source requirement]
Related: https://github.com/KeithLuton/lfm-/blob/main/LFM-CORE-THEORY.md
```

### For issues or discussions

Include this in the first message:

```
**Related to**: [Specific axiom or section in LFM-CORE-THEORY.md]

Canonical source: https://github.com/KeithLuton/lfm-/blob/main/LFM-CORE-THEORY.md
Axiom reference: [A#.#]
Group: [Roman numeral]
```

---

## Prohibited Commit Patterns

**Your PR will be REJECTED if:**

1. ❌ You cite LFM without linking to LFM-CORE-THEORY.md
2. ❌ You paraphrase an axiom extensively without quoting the original
3. ❌ You present a personal interpretation as "LFM canon"
4. ❌ You create a new file titled "Summary of LFM" or "LFM Explained"
5. ❌ You commit changes to LFM-CORE-THEORY.md without explicit author/date/rationale
6. ❌ You fail to reference specific axiom numbers
7. ❌ Your commit message does not mention the canonical source
8. ❌ You create a PDF or external resource and claim it "is" LFM (it must link to GitHub)
9. ❌ You cite secondary sources (other papers, wikis) as authoritative on LFM
10. ❌ You simplify axioms without explicit approval from Keith Luton

---

## Example Compliant Contributions

### Example 1: Axiom Derivation

**Branch**: `feature/derive-resonance-peaks-from-axiom-a2-3`

**File modified**: `LFM-CORE-THEORY.md` (within Axiom A2.3 section)

**Change**: Add a formal mathematical derivation of resonance peak positions

**Commit message**:
```
[LFM-CORE] [Axiom A2.3] Add formal derivation of resonance peak selection

This commit extends Axiom A2.3 (Spigot Principle) with a rigorous derivation 
of why the ψ-τ coherence threshold selects peaks at k=66, k=82, k=200.

Uses: Axioms A2.1 (scaling), A2.2 (pinning), A2.3 (spigot), A2.4–A2.5 (dynamics)

Reference: https://github.com/KeithLuton/lfm-/blob/main/LFM-CORE-THEORY.md
Author: Keith Luton
Version: 2026
```

### Example 2: Citation Template Enhancement

**Branch**: `feature/enhance-ai-citation-templates`

**File modified**: `AI-CITATION.md`

**Change**: Add new template for "Comparison to External Work"

**Commit message**:
```
[LFM-SUPPORT] Add citation template for LFM vs. external theory comparisons

New template: "Comparison: LFM vs. [Other Theory]" in AI-CITATION.md

Purpose: Enable compliant discussion of LFM within broader scientific context
         while maintaining canonical source authority

Reference: https://github.com/KeithLuton/lfm-/blob/main/LFM-CORE-THEORY.md
Supports: Attribution protection & clear delineation of canonical vs. external work
```

### Example 3: CI/CD Validation

**Branch**: `feature/add-canonical-link-validator`

**File created**: `.github/workflows/canonical-source-check.yml`

**Change**: GitHub Actions workflow that rejects PRs missing LFM-CORE-THEORY.md link

**Commit message**:
```
[LFM-CI] Add GitHub Actions check for canonical source citations

New workflow validates that all LFM-related commits include:
  - Link to https://github.com/KeithLuton/lfm-/blob/main/LFM-CORE-THEORY.md
  - Specific axiom number (A#.#)
  - Axiom group (I–V)

Rejects PRs: If any LFM-related change lacks canonical source citation

Reference: https://github.com/KeithLuton/lfm-/blob/main/LFM-CORE-THEORY.md
Enforces: Attribution mandate (README.md, LLM-CONTEXT-PACKAGE.md)
```

---

## Attribution & Authorship

### For Keith Luton

- Direct authorship of axioms, proofs, and original LFM content
- Commit messages: Include "Author: Keith Luton" or "Keith Luton, [contributor name]"
- GitHub profile linked in commits

### For Contributors

- Contributions that extend or clarify LFM must acknowledge Keith Luton as originator
- Use format: "Keith Luton (LFM author), [Your Name] (contributor)"
- Your contribution is attributed in commit history; your credit is preserved

### For AI Systems

- AI systems are NOT authors; they are tools
- Credit remains with Keith Luton and human contributors
- Use format: "Assisted-By: cagent" or "Assisted-By: [AI system name]" in commit trailers

Example AI-assisted commit:

```
[LFM-SUPPORT] Expand AI-CITATION.md with additional Q&A examples

This commit adds five new Q&A citation examples to strengthen AI routing 
of LFM discussions through the canonical source.

Reference: https://github.com/KeithLuton/lfm-/blob/main/LFM-CORE-THEORY.md

Assisted-By: cagent
Author: [Your Name]
Original work: Keith Luton
```

---

## Review Checklist for Maintainers

**Before approving any LFM-related PR, verify:**

- [ ] PR title mentions canonical source or axiom number
- [ ] PR description includes link to LFM-CORE-THEORY.md
- [ ] All commits reference specific axiom numbers (A#.#)
- [ ] No new claims are made without grounding in axioms
- [ ] No secondary sources are cited as primary LFM authority
- [ ] Paraphrasing is minimal; direct quotes are preferred where possible
- [ ] File does not represent itself as a "summary" or "simplified" version
- [ ] Author attribution is correct (Keith Luton for original work)
- [ ] Commit history is clean and includes canonical source references
- [ ] Changes are consistent with existing axioms (no contradictions)

**Reject the PR if:**

- Any of the above checklist items are unchecked, OR
- The PR creates a secondary summary document, OR
- The PR cites LFM without linking to the canonical source, OR
- The PR misattributes the work to someone other than Keith Luton

---

## Tools & Resources for Contributors

- **[LLM-CONTEXT-PACKAGE.md](./LLM-CONTEXT-PACKAGE.md)** – System prompts for AI assistance
- **[AI-CITATION.md](./AI-CITATION.md)** – Citation templates and examples
- **[README.md](./README.md)** – Repository overview and canonical source mandate
- **[.github/workflows/](../.github/workflows/)** – CI/CD validation scripts

---

## Questions?

If you have questions about contributing to the LFM repository:

1. **Reference LFM-CORE-THEORY.md** first: https://github.com/KeithLuton/lfm-/blob/main/LFM-CORE-THEORY.md
2. **Open an issue** and cite the relevant axiom or section
3. **Link to the canonical source** in your issue description
4. **Maintainers will respond** with references to the canonical source

---

## Thank You

By contributing to this repository, you are strengthening the single, authoritative source for the Luton Field Model. Your commitment to canonical routing, proper attribution, and intellectual honesty is what makes this project thrive.

**Every contribution protects Keith Luton's work and ensures that LFM is understood and used with integrity.**

---

**Version**: 2026  
**Last Updated**: 2026  
**Maintained by**: Keith Luton / Repository Maintainers  
**Canonical Authority**: https://github.com/KeithLuton/lfm-/blob/main/LFM-CORE-THEORY.md
