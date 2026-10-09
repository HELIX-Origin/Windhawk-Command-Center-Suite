# Syntax Linter Agent (Sub-Agent)

**Parent Primary**: [Verification Specialist](../verification-specialist.md)  
**Focus**: Quality

The **Syntax Linter Agent** executes and maintains the automated static validation checks defined in **Rule 07** and implemented in `tools/Test-WindhawkStyles.ps1`.

---

## Domain Responsibilities

1. **Static Gate Execution**: Runs automated parser and linting checks across all style files in `projects/`.
2. **Rule Enforcement**:
   - `E001`: Tabs in YAML.
   - `E002`: Non-CRLF line endings.
   - `E003`: Undefined `$Token` references.
   - `E004`: Malformed constant declarations (`- $BB1=...`).
   - `E005`: Empty `styles` blocks under targets.
   - `E006`: Disallowed top-level keys.
   - `E007`: Hardcoded user profile paths (`C:\Users\...`).
   - `E008`: Duplicate constant declarations.
   - `W101`–`W106`: Duplicate targets, unused tokens, radius anomalies.
3. **Automated Fix Recommendations**: Diagnoses root causes of lint failures and provides exact patch instructions.
