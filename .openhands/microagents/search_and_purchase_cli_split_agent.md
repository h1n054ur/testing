---
triggers:
  - safely split purchase into search and purchase in CLI only
  - preserve menu functionality
  - show progress and output for CLI search
  - CLI purchase takes exact number only
agent: CodeActAgent
---

# 1) Load spec_search_and_purchase_cli_split
- tool_call: fetch_spec3{"spec_name":"spec_search_and_purchase_cli_split"}
  content: |
    ✅ Spec fetched. Standing by.

# 2) Set phase
set_phase3{"phase":"cli-command-split"}

# 3) In app/cli.py:
- Remove old "purchase" subcommand with --country, --area-code, --contains
- Add "search" subcommand:
  * --country (required)
  * --area-code (optional)
  * --contains (optional)
  * Create PurchaseFlow
  * Call search_numbers(...) with progress_callback
  * Use a local print loop (no new files) to display: index, number, city, state, type, price
- Add "purchase" subcommand:
  * <number> positional arg
  * Create PurchaseFlow
  * Call purchase_exact_number(number)
  * Print success/failure message

# 4) In app/core/purchase.py:
- Do not modify parameters or logic of search_numbers other than:
  * Accept and call progress_callback(count) when new numbers are added
- Add method purchase_exact_number(number: str):
  * Call self.twilio_gateway.purchase_number(number)
  * Return {"success": bool, "message": str}

# 5) Test CLI:
- pip install -e .
- twilio-manager search --country US --area-code 415
- twilio-manager purchase +14155552671
- Confirm search prints results and shows progress
- Confirm purchase prints confirmation
- Confirm interactive menu still works as-is

# 6) Log outcome
log_decision3{
  "context":"cli-command-split",
  "decision":"CLI commands 'search' and 'purchase' work independently without affecting menu logic. All behavior contained and safe."
}
