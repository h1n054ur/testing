---
triggers:
  - build number actions menu
  - manage number actions
  - number actions routing
agent: CodeActAgent
---

# 1) Load architecture rules
fetch_spec2{"spec_name":"architecture_rules"}

# 2) Load number actions menu spec
fetch_spec2{"spec_name":"number_actions_menu_spec"}

# 3) Set phase
set_phase{"phase":"manage-flow"}

# 4) Implement number_actions_menu.py
In `interfaces/cli/menus/manage/number_actions_menu.py`, define:
- `NumberActionsMenu(number)`
- `run()` prompts user with 1–5, routes to correct submenu
- After submenu completes → return to this menu
- Option `0` goes back to `ManageMenu`

# 5) Log outcome
log_decision{
  "context":"manage-actions",
  "decision":"Created CLI menu to list all number management actions and delegate cleanly to submenus, respecting CLI and flow boundaries."
}
