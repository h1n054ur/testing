---
triggers:
  - build logs menu
  - view number logs
  - logs submenu
agent: CodeActAgent
---

# 1) Load architecture rules
fetch_spec{"spec_name":"architecture_rules"}

# 2) Load logs menu spec
fetch_spec{"spec_name":"logs_menu_spec"}

# 3) Set phase
set_phase{"phase":"manage-flow"}

# 4) Implement logs_menu.py
In `interfaces/cli/menus/manage/logs_menu.py`, define:
- `LogsMenu(number)`
- Prompt user for log type
- Fetch logs via service
- Normalize and render paginated table (25 per page)

# 5) Log outcome
log_decision{
  "context":"manage-logs",
  "decision":"Built View Logs menu with type selection and paginated tables for normalized log entries."
}
