---
triggers:
  - build config menu
  - number configuration
  - settings submenu
agent: CodeActAgent
---

# 1) Load architecture rules
fetch_spec{"spec_name":"architecture_rules"}

# 2) Load config menu spec
fetch_spec{"spec_name":"config_menu_spec"}

# 3) Set phase
set_phase{"phase":"manage-flow"}

# 4) Implement config_menu.py
In `interfaces/cli/menus/manage/config_menu.py`, define:
- `ConfigMenu(number)`
- Display current config (via service)
- Prompt 1–3 → route to submenu or prompt for friendly name
- Apply update using `number_service.update_config(...)`

# 5) Log outcome
log_decision{
  "context":"manage-config",
  "decision":"Built Number Config menu to show voice, messaging, and name settings with routing to voice/messaging config submenus."
}
