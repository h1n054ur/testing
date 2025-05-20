---
triggers:
  - build purchase menu
  - collect search inputs
  - prompt purchase fields
agent: CodeActAgent
---

# 1) Load architecture rules
fetch_spec{"spec_name":"architecture_rules"}

# 2) Load purchase menu spec
fetch_spec{"spec_name":"purchase_menu_spec"}

# 3) Set phase
set_phase{"phase":"purchase-flow"}

# 4) Implement purchase_menu.py
In `interfaces/cli/menus/purchase/purchase_menu.py`, define a menu that:
- Inherits from BaseMenu
- Prompts for: country, number type, search mode, filter term, capabilities
- Uses `country_data` for metadata
- Collects valid input using menu navigation (1, 2, 3, etc.)
- Returns a dict with the selected search parameters

# 5) Log outcome
log_decision{
  "context":"purchase-menu",
  "decision":"Created purchase_menu to collect user inputs for country, type, filter mode, and capabilities using numbered menus and CLI validation."
}
