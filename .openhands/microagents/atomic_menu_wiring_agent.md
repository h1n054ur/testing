---
triggers:
  - atomic menu wiring
  - explicit menu navigation wiring
  - full menu/submenu import and connect
agent: CodeActAgent
---

# 1) Load atomic full menu wiring spec
fetch_spec3{"spec_name":"atomic_menu_wiring_spec"}

# 2) Set phase
set_phase3{"phase":"atomic-menu-wiring"}

# 3) Execute atomic menu wiring
# - For every menu and submenu file in user_flow.md and architecture.md:
#   - Import base_menu and all direct children at the top
#   - Inherit from BaseMenu
#   - In .show(), display menu using show_panel, branch to children, always offer "0. Back" (or "0. Exit" in MainMenu)
#   - Return on "0. Back", call children as needed, no direct navigation to unrelated menus
# - No feature logic, no state, no unrelated code
# - Verify atomic, clean, explicit wiring

# 4) Log outcome
log_decision3{
  "context":"atomic-menu-wiring",
  "decision":"All menus and submenus now explicitly import, instantiate, and call only their direct children, and inherit from BaseMenu. No logic leaks, no ambiguity, and clean navigation tree is in place."
}
