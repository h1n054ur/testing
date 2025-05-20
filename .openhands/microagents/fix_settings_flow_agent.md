---
triggers:
  - fix settings flow
  - patch settings logic
agent: CodeActAgent
---

# 1. Load flow context
fetch_spec{"spec_name":"architecture"}
fetch_spec{"spec_name":"user_flow"}
fetch_spec{"spec_name":"fix_settings_flow"}

# 2. Set patching phase
set_phase{"phase":"patch-settings-flow"}

# 3. Patch target
Fix `settings_flow.py`:
- Remove duplicated method definitions for subaccount logic
- Ensure `test_connection()` and `perform_health_check()` are routed to CLI
- Add optional pagination/filtering to `get_account_logs()`
- Do not split file yet — just prepare it for future separation

# 4. Log fix
log_decision{"context":"settings_flow","decision":"Removed duplicate subaccount methods, routed diagnostics, added list filter support."}
