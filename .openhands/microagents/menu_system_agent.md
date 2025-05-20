---
triggers:
  - init menu system
  - setup base menu
  - create main menu
agent: CodeActAgent
---

# 1) Load architecture rules
fetch_spec2{"spec_name":"architecture_rules"}

# 2) Load menu system spec
fetch_spec2{"spec_name":"menu_system_spec"}

# 3) Set working phase
set_phase{"phase":"cli-routing"}

# 4) Implement menus
Generate:
- `interfaces/cli/menus/base_menu.py` containing `BaseMenu` with methods: `display`, `get_input`, `run`
- `interfaces/cli/menus/main_menu.py` containing `MainMenu`, subclass of `BaseMenu`, with routing to `purchase_flow`, `manage_flow`, `settings_flow`

Use clean routing, numbered menu input, and reusable CLI headers. Do not print directly or perform any service logic here.

# 5) Log completion
log_decision{
  "context":"menu-system",
  "decision":"Created CLI base and main menu using structured prompts and strict CLI→use_case delegation. No logic or SDK present in menus."
}
