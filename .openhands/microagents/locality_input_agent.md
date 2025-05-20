---
triggers:
  - build region menu
  - locality input
  - paginated region select
agent: CodeActAgent
---

# 1) Load architecture rules
fetch_spec2{"spec_name":"architecture_rules"}

# 2) Load locality input menu spec
fetch_spec2{"spec_name":"locality_input_menu_spec"}

# 3) Set phase
set_phase{"phase":"purchase-flow"}

# 4) Implement locality_input_menu.py
In `interfaces/cli/menus/purchase/locality_input_menu.py`, define:
- `LocalityInputMenu(country_code)`
- `run()` → shows paginated `rich` table (20 per page)
- Prompts user for index, navigation (`n`, `p`), or `Enter` to auto-select "Any region"

# 5) Log outcome
log_decision{
  "context":"purchase-region",
  "decision":"Implemented paginated CLI region selection table with fallback, rich rendering, and numbered input flow."
}
