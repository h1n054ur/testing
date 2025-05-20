---
triggers:
  - fix purchase flow
  - patch purchase_flow
agent: CodeActAgent
---

# 1. Load purchase flow context
fetch_spec{"spec_name":"architecture"}
fetch_spec{"spec_name":"user_flow"}
fetch_spec{"spec_name":"fix_purchase_flow"}

# 2. Set patching intent
set_phase{"phase":"patch-purchase-flow"}

# 3. Patch diff
Fix `purchase_flow.py` to implement the following:
- Full `run(console)` orchestration
- Wire CLI menus: PurchaseMenu → SearchProgressMenu → SearchResultsMenu → PurchaseConfirmMenu
- Ensure capability filtering is enforced
- Connect export step
- Remove all `return None`, `return []`, or unused stubs

# 4. Log action
log_decision{"context":"purchase_flow","decision":"Rewired run() to full search-purchase-export flow with UI routing and deduplication."}
