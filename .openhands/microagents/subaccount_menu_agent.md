---
triggers:
  - build subaccount menu
  - manage subaccounts
  - switch twilio account
agent: CodeActAgent
---

# 1) Load architecture rules
fetch_spec2{"spec_name":"architecture_rules"}

# 2) Load subaccount menu spec
fetch_spec2{"spec_name":"subaccount_menu_spec"}

# 3) Set phase
set_phase{"phase":"settings-flow"}

# 4) Implement subaccount_menu.py
In `interfaces/cli/menus/settings/subaccount_menu.py`, define:
- `SubaccountMenu(BaseMenu)`
- Fetch list → render table
- Prompt for switch → call `account_service.switch_subaccount(...)`
- Optionally mock creation flow
- Reflect current SID/label in banner

# 5) Log outcome
log_decision{
  "context":"settings-subaccount",
  "decision":"Built CLI menu to view, switch, and mock-create subaccounts with routing to service layer for SID handling."
}
