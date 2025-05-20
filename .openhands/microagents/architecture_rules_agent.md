---
trigger_type: always
agent: CodeAuditAgent
---

# 1) Load the architecture enforcement rules
fetch_spec2{"spec_name":"architecture_rules"}
fetch_spec2{"spec_name":"user_flow"}

# 2) Audit the diff or file
Reject the patch if any of the following violations are found:

## 🚫 CLI Menu Violations
- Imports `twilio`, `requests`, or any service/gateway directly
- Uses `print()` or `console.print()` outside `BaseMenu` wrappers
- Omits `render_panel()` or `self.subaccount_label` in CLI headers
- Accepts raw SID input (freeform text instead of numbered menu)
- Menu class does not extend `BaseMenu` or lacks `run()` method

## 🚫 Use Case Violations
- Imports `twilio`, `requests`, or gateway logic
- Contains validation or formatting logic better suited to services or core

## 🚫 Service Violations
- Prints or prompts the user
- Contains CLI conditionals or formatting
- Writes files or calls APIs directly

## 🚫 Gateway Violations
- Returns rendered strings, UI content, or SDK objects
- Calls core logic or performs formatting
- Defined outside `gateways/` folder

## 🚫 General Structural Violations
- Any file spans more than one layer (e.g., CLI + service)
- Any class mixes concerns or fails clean layer boundaries

# 3) Log decision
If rejected, log the file path and reason:
log_decision{
  "context":"violation",
  "decision":"Blocked patch: {violation_type} — {file_path} violates architecture rules"
}
