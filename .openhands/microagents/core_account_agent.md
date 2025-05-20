---
triggers:
  - build core account
  - sid helpers
  - label format function
agent: CodeActAgent
---

# 1) Load architecture rules
fetch_spec2{"spec_name":"architecture_rules"}

# 2) Load core account logic spec
fetch_spec2{"spec_name":"core_account_spec"}

# 3) Set phase
set_phase{"phase":"core-logic"}

# 4) Implement account.py
In `core/account.py`, implement:
- `is_valid_sid(s: str)`
- `normalize_sid(s: str)`
- `format_account_label(sid: str, label: Optional[str])`

Ensure:
- All logic is pure
- All string handling is safe and defensive
- Function-level docstrings included

# 5) Log completion
log_decision{
  "context":"core-account",
  "decision":"Implemented SID validation and label formatting helpers to support CLI banners and subaccount switching in user flow."
}
