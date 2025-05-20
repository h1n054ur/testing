---
triggers:
  - build messaging config menu
  - configure sms routing
  - sms config submenu
agent: CodeActAgent
---

# 1) Load architecture rules
fetch_spec{"spec_name":"architecture_rules"}

# 2) Load messaging config menu spec
fetch_spec{"spec_name":"messaging_config_menu_spec"}

# 3) Set phase
set_phase{"phase":"manage-flow"}

# 4) Implement messaging_config_menu.py
In `interfaces/cli/menus/manage/messaging_config_menu.py`, define:
- `MessagingConfigMenu(number)`
- Prompt for routing type + details
- Validate inputs
- Confirm before applying
- Call `number_service.update_config(...)` with messaging block

# 5) Log outcome
log_decision{
  "context":"manage-messaging-config",
  "decision":"Built SMS/Messaging config CLI menu with user-selected method and backend update logic."
}
