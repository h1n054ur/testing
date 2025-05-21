---
triggers:
  - add rich tables to menu steps
  - upgrade search results and logs to use tables
  - implement show_table in base menu
agent: CodeActAgent
---

# 1) Load add tables to menus spec
fetch_spec3{"spec_name":"add_tables_to_menus_spec"}

# 2) Load add tables to menus spec
fetch_spec3{"spec_name":"user_flow"}

# 3) Set phase
set_phase3{"phase":"add-rich-tables"}

# 4) In base_menu.py, add show_table helper as described
# 5) In purchase_menu.py, replace search results options with show_table() for paged results
# 6) In manage_menu.py, use show_table() for active numbers and logs (messaging, call)
# 7) In settings_menu.py, show account logs as a table with correct headings
# 8) Update imports and calls for new helper
# 9) Remove old option-list code in those steps
# 10) Test every table for headings, nav instructions, and prompt

# 11) Log outcome
log_decision3{
  "context":"add-rich-tables",
  "decision":"All menu steps that display tabular data now use Rich tables with correct headings, paging, and nav instructions. Code and UI are ready for real data and use cases."
}

