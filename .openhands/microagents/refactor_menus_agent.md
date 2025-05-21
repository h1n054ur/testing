---
triggers:
  - refactor flat menu directory and fix guided flows
  - enforce menu styling and direct flows
  - update all imports and menu calls
agent: CodeActAgent
---

# 1) Load flat directory menu refactor spec
fetch_spec3{"spec_name":"refactor_menus_spec"}

# 2) Set phase
set_phase3{"phase":"refactor-menus-flat"}

# 3) For each menu file:
# - Move menu file to /app/interfaces/cli/, delete all subfolders
# - Update all import lines to reflect the flat directory
# - In base_menu.py, update show_panel to match visual spec (red, centered, correct width)
# - In main_menu.py, ensure pressing 1 or 2 launches PurchaseMenu/ManageMenu directly (no double action)
# - In purchase_menu.py and manage_menu.py, start with first actionable menu step, not an extra menu
# - Delete any now-unused menu files
# - In settings_menu.py, fix options to match user_flow.md
# - Audit and fix imports in every menu file as needed
# - Test navigation and panel style throughout

# 4) Log outcome
log_decision3{
  "context":"refactor-menus-flat",
  "decision":"All menus are now in a flat CLI directory, top-level menus remain as controllers, flows begin at first real step, all imports and panels fixed, and visuals match reference."
}
