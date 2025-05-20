---
triggers:
  - build services
  - implement service layer
  - add logic services
agent: CodeActAgent
---

# 1) Load architecture rules
fetch_spec2{"spec_name":"architecture_rules"}

# 2) Load service layer spec
fetch_spec2{"spec_name":"service_layer_spec"}

# 3) Set phase
set_phase{"phase":"services"}

# 4) Implement:
- `number_service.py`
- `messaging_service.py`
- `voice_service.py`
- `account_service.py`
- `account_logs_service.py`

Each function must call gateway methods and return clean types (dict, bool, list). All validation and formatting to be done using core helpers.

# 5) Log result
log_decision{
  "context":"services",
  "decision":"Wired domain logic services for each use_case and connected them to gateways using clean call boundaries."
}
