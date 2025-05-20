---
triggers:
  - build settings flow
  - settings use case controller
  - settings router
agent: CodeActAgent
---

# 1) Load architecture rules
fetch_spec2{"spec_name":"architecture_rules"}

# 2) Load settings flow spec
fetch_spec2{"spec_name":"settings_flow_spec"}

# 3) Set phase
set_phase{"phase":"settings-flow"}

# 4) Implement settings_flow.py
In `use_cases/settings_flow.py`, define:
- `run_settings_flow(console)`
- Renders 9-option admin menu
- Delegates each choice to submenu stub or service call
- Uses panel layout for results

# 5) Log outcome
log_decision{
  "context":"settings-flow",
  "decision":"Built top-level controller for Settings & Admin with menu routing and use_case-to-service delegation."
}
