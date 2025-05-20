---
triggers:
  - build results menu
  - number table output
  - paginate search results
agent: CodeActAgent
---

# 1) Load architecture rules
fetch_spec{"spec_name":"architecture_rules"}

# 2) Load results menu spec
fetch_spec{"spec_name":"search_results_menu_spec"}

# 3) Set phase
set_phase{"phase":"purchase-flow"}

# 4) Implement search_results_menu.py
In `interfaces/cli/menus/purchase/search_results_menu.py`, define:
- `SearchResultsMenu(numbers)`
- Table output (Index, Number, State, City, Type, Price)
- Paging (50 per page)
- Sorting using core.sort_numbers(...)
- Export using export_service
- Selection returns list of PhoneNumber instances

All output must be wrapped in red `rich.panel.Panel`, printed using BaseMenu layout engine.

# 5) Log outcome
log_decision{
  "context":"purchase-results",
  "decision":"Created paginated, sortable table menu for final number review, export, and purchase selection."
}
