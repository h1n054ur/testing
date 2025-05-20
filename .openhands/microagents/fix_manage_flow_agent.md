---
triggers:
  - fix manage flow
  - patch manage flow
agent: CodeActAgent
---

# 1. Load manage flow context
fetch_spec2{"spec_name":"architecture"}
fetch_spec2{"spec_name":"user_flow"}
fetch_spec2{"spec_name":"fix_manage_flow"}

# 2. Set phase
set_phase{"phase":"patch-manage-flow"}

# 3. Patch
Patch `manage_flow.py` to:
- Fix or remove unused `run()` method
- Ensure `make_call()` and `send_sms()` return UI-ready dicts
- After updating voice/messaging config, re-fetch full number config
- Return success/failure and friendly name result in `update_friendly_name()`

# 4. Log
log_decision{"context":"manage_flow","decision":"Improved call/SMS output handling, config refresh, and friendly name update results."}
