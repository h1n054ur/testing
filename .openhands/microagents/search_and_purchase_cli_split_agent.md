---
triggers:
  - split purchase command into search and purchase
  - show progress and output for search
  - purchase requires exact number
agent: CodeActAgent
---

# 1) Load spec_search_and_purchase_cli_split
fetch_spec3{"spec_name":"spec_search_and_purchase_cli_split"}

# 2) Set phase
set_phase3{"phase":"cli-command-split"}

# 3) In app/cli.py:
- Remove old "purchase" command with --country, --area-code, --contains
- Add "search" subcommand:
  * --country (required)
  * --area-code (optional)
  * --contains (optional)
  * Call PurchaseFlow.search_numbers(...) with progress_callback
  * Print table of results (index, number, city, state, type, price)
- Add "purchase" subcommand:
  * <number> positional arg
  * Call PurchaseFlow.purchase_exact_number(number)
  * Print success/failure to stdout

# 4) In app/core/purchase.py:
- Ensure search_numbers accepts and uses progress_callback(count)
- search_results must contain: index, number, city, state, type, price
- Add method purchase_exact_number(number)
  * Calls twilio_gateway.purchase_number(number)
  * Returns {"success": bool, "message": str}

# 5) In app/utils/print_table.py (new):
- Add print_search_results_table(results)
  * Accepts list of dicts, prints formatted table to stdout

# 6) Test CLI:
- pip install -e .
- twilio-manager search --country US --area-code 415
- twilio-manager purchase +14155552671
- Confirm search shows progress + results
- Confirm purchase prints success or failure

# 7) Log outcome
log_decision3{
  "context":"cli-command-split",
  "decision":"Split completed. search and purchase commands work independently, use PurchaseFlow, and display output correctly. No other CLI behavior changed."
}
