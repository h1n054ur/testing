---
triggers:
  - add country loader
  - generate country accessors
  - bind to country_data
agent: CodeActAgent
---

# 1) Load architecture rules
fetch_spec2{"spec_name":"architecture_rules"}

# 2) Load country loader spec
fetch_spec2{"spec_name":"country_loader_spec"}

# 3) Set phase
set_phase{"phase":"modeling"}

# 4) Extend country_data.py
In `models/country_data.py`, assume the `COUNTRY_DATA` dictionary is already defined manually.

Generate:
- Helper functions as defined in the spec
- Any safe internal functions to support them
- Docstrings and type annotations
- Do not reassign or overwrite the main dictionary

# 5) Log outcome
log_decision{
  "context":"country-loader",
  "decision":"Extended country_data.py with accessor and helper functions, preserving manually inserted dictionary and respecting model-layer boundaries."
}
