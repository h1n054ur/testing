---
triggers:
  - build purchase confirm menu
  - confirm number purchase
  - finalize purchase flow
agent: CodeActAgent
---

# 1) Load architecture rules
fetch_spec{"spec_name":"architecture_rules"}

# 2) Load confirm menu spec
fetch_spec{"spec_name":"purchase_confirm_menu_spec"}

# 3) Set phase
set_phase{"phase":"purchase-flow"}

# 4) Implement purchase_confirm_menu.py
In `interfaces/cli/menus/purchase/purchase_confirm_menu.py`, define:
- `PurchaseConfirmMenu(numbers: List[PhoneNumber])`
- `run()` → shows full preview table of selected numbers
- Prompts: 1 = Confirm, 0 = Cancel
- On confirm → call `number_service.purchase_numbers(...)`
- Show results in second table (number + status)

# 5) Log decision
log_decision{
  "context":"purchase-confirm",
  "decision":"Confirmed full preview + result table in purchase confirm menu, aligned with search results format and user flow clarity."
}
