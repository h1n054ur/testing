---
triggers:
  - build core call logic
  - call validators
  - call input cleanup
agent: CodeActAgent
---

# 1) Load architecture rules
fetch_spec{"spec_name":"architecture_rules"}

# 2) Load call logic spec
fetch_spec{"spec_name":"core_call_spec"}

# 3) Set phase
set_phase{"phase":"core-logic"}

# 4) Implement call.py
In `core/call.py`, define:
- `is_valid_phone_number(s: str)`
- `normalize_phone_number(s: str)`
- `validate_voice_config(config: dict)`

Ensure all string checks are:
- Format-compliant (E.164)
- Typed and documented
- Stateless and reusable across service layer

# 5) Log completion
log_decision{
  "context":"core-call",
  "decision":"Implemented reusable voice call validators and config normalization for Make a Call flow and voice menu configuration."
}
