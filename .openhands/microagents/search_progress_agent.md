---
triggers:
  - build search progress menu
  - spinner ui
  - live search feedback
agent: CodeActAgent
---

# 1) Load architecture rules
fetch_spec2{"spec_name":"architecture_rules"}

# 2) Load progress menu spec
fetch_spec2{"spec_name":"search_progress_menu_spec"}

# 3) Set phase
set_phase{"phase":"purchase-flow"}

# 4) Implement search_progress_menu.py
In `interfaces/cli/menus/purchase/search_progress_menu.py`, define:
- `SearchProgressMenu` class (subclass of BaseMenu)
- `run_spinner()` → initializes rich Live layout
- `update_status(count, msg)` → updates result count + spinner line
- `stop_spinner()` → safely exits Live mode

All updates must be styled using:
- Red panel
- Spinner (rich.spinner.Spinner)
- Centered output

# 5) Log outcome
log_decision{
  "context":"purchase-progress",
  "decision":"Implemented rich spinner-based progress menu with dynamic result updates for the number search loop."
}
