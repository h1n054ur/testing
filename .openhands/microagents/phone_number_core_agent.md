---
triggers:
  - build core phone logic
  - phone number list tools
agent: CodeActAgent
---

# 1) Load structure + logic rules
fetch_spec{"spec_name":"architecture"}
fetch_spec{"spec_name":"phone_number_core_spec"}

# 2) Declare phase
set_phase{"phase":"core-logic"}

# 3) Log result
log_decision{
  "context":"core-phone-number",
  "decision":"Centralized list logic for PhoneNumber into core to keep services/menus clean and composable."
}
