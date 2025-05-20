---
triggers:
  - build manage menu
  - view active numbers
  - manage flow menu
agent: CodeActAgent
---

# 1) Load architecture rules
fetch_spec{"spec_name":"architecture_rules"}

# 2) Load manage menu spec
fetch_spec{"spec_name":"manage_menu_spec"}

# 3) Set phase
set_phase{"phase":"manage-flow"}

# 4) Implement manage_menu.py
In `interfaces/cli/menus/manage/manage_menu.py`, define:
- `ManageMenu(BaseMenu)`
- `run()` fetches owned numbers (via number_service)
- Display in paginated table (10 per page)
- Prompt user for:
  - Number index → triggers number_actions_menu
  - `n`, `p`, or `0`

# 5) Log outcome
log_decision{
  "context":"manage-menu",
  "decision":"Implemented number table with selection UI for manage flow using paginated layout and service-level delegation."
}
