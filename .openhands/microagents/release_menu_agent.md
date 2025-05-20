---
triggers:
  - build release menu
  - confirm release
  - number release menu
agent: CodeActAgent
---

# 1) Load architecture rules
fetch_spec{"spec_name":"architecture_rules"}

# 2) Load release menu spec
fetch_spec{"spec_name":"release_menu_spec"}

# 3) Set phase
set_phase{"phase":"manage-flow"}

# 4) Implement release_menu.py
In `interfaces/cli/menus/manage/release_menu.py`, define:
- `ReleaseMenu(number)`
- Display confirmation prompt
- If user selects `1`, call `number_service.release_number(...)`
- Show success/failure message in styled panel

# 5) Log outcome
log_decision{
  "context":"manage-release",
  "decision":"Created CLI confirmation menu to release a number using service call and defensive prompt flow."
}
