---
triggers:
  - build core log tools
  - normalize logs
  - log filter helpers
agent: CodeActAgent
---

# 1) Load architecture rules
fetch_spec{"spec_name":"architecture_rules"}

# 2) Load logs logic spec
fetch_spec{"spec_name":"core_logs_spec"}

# 3) Set phase
set_phase{"phase":"core-logic"}

# 4) Implement logs.py
In `core/logs.py`, implement:
- `normalize_log_entry(raw: dict)`
- `filter_logs(logs: List[dict], type_filter, direction, status)`
- `sort_logs(logs: List[dict])`

Ensure:
- Output rows match table display fields in CLI
- Filters handle blank/null values
- Sorting uses timestamp descending

# 5) Log completion
log_decision{
  "context":"core-logs",
  "decision":"Created reusable log normalization and filtering functions for CLI logs menu and account log diagnostics flow."
}
