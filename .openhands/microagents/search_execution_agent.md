---
triggers:
  - implement search engine
  - search numbers loop
  - build number search logic
agent: CodeActAgent
---

# 1) Load architecture rules
fetch_spec2{"spec_name":"architecture_rules"}

# 2) Load search logic spec
fetch_spec2{"spec_name":"search_execution_spec"}

# 3) Set phase
set_phase{"phase":"purchase-flow"}

# 4) Implement search flow
In `use_cases/purchase_flow.py`, define:
- `run_purchase_flow(console)`
- Accepts inputs from menu
- Calls `number_service.search_numbers(...)` in a loop
- Deduplicates with `core.phone_number.deduplicate_numbers(...)`
- Stops when:
  - 500 total unique numbers OR
  - 3 requests return no new numbers
- Sleeps 1 second between each
- Passes results to results menu

# 5) Log outcome
log_decision{
  "context":"purchase-search",
  "decision":"Implemented looped number search engine with deduplication, retry limit, and handoff to results rendering."
}
