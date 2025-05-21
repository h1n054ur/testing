---
triggers:
  - wire up all menus with rich
  - implement full menu navigation
  - connect all menus with BaseMenu and styling
agent: CodeActAgent
---

# 1) Load full menu wiring and styling spec (with consistent Back/Exit)
fetch_spec3{"spec_name":"rich_menu_wiring_full_consistent_back_spec"}

# 2) Set phase
set_phase3{"phase":"rich-menu-wiring"}

# 3) Execute full menu wiring and styling
# - In base_menu.py, implement show_panel(), show_spinner(), and prompt() helpers as per spec
# - For every menu and submenu listed in architecture.md and user_flow.md, implement its class to inherit from BaseMenu and use show_panel for all display
# - Ensure all menus/submenus use "0. Back" except main menu ("0. Exit"), as specified
# - For search progress, use show_spinner from BaseMenu
# - Do not add feature/business logic or unrelated changes

# 4) Log outcome
log_decision3{
  "context":"rich-menu-wiring",
  "decision":"All menus and submenus now inherit from BaseMenu, use Rich for styling, and implement consistent '0. Back'/'0. Exit' options as specified in the spec and source docs. No extra logic added."
}
