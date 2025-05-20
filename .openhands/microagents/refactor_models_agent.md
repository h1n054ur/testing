---
triggers:
  - migrate core to models
  - clean model layer
  - move classes to models
agent: CodeRefactorAgent
---

# 1) Load architecture spec
fetch_spec2{"spec_name":"architecture"}

# 2) Load refactor spec
fetch_spec2{"spec_name":"refactor_models_spec"}

# 3) Set phase
set_phase{"phase":"model-refactor"}

# 4) Refactor plan
Scan:
- `core/account.py`
- `core/message.py`
- `core/phone_number.py`

If structural logic (e.g., PhoneNumber class, Account formatting, Message previews) is found:
- Move it to matching file in `models/`
- Replace with model import in `core/`

# 5) Log outcome
log_decision{
  "context":"refactor-core-to-models",
  "decision":"Moved entity-specific logic and data classes from core to models layer to restore separation of concerns."
}
