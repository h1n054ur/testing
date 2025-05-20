---
triggers:
  - build core message logic
  - validate sms body
  - add sms preview
agent: CodeActAgent
---

# 1) Load architecture rules
fetch_spec{"spec_name":"architecture_rules"}

# 2) Load message logic spec
fetch_spec{"spec_name":"core_message_spec"}

# 3) Set phase
set_phase{"phase":"core-logic"}

# 4) Implement message.py
In `core/message.py`, define:
- `is_valid_sms_body(body)`
- `truncate_preview(body, limit=40)`
- `is_long_sms(body)`

All logic must:
- Validate limits defensively
- Raise clean Python exceptions or return booleans
- Remain stateless and callable from services

# 5) Log outcome
log_decision{
  "context":"core-message",
  "decision":"Added SMS message validators and preview helpers to support outbound logic and user-facing menu validations."
}
