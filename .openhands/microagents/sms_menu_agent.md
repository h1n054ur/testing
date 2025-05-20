---
triggers:
  - build sms menu
  - send sms flow
  - sms action menu
agent: CodeActAgent
---

# 1) Load architecture rules
fetch_spec{"spec_name":"architecture_rules"}

# 2) Load sms menu spec
fetch_spec{"spec_name":"sms_menu_spec"}

# 3) Set phase
set_phase{"phase":"manage-flow"}

# 4) Implement sms_menu.py
In `interfaces/cli/menus/manage/sms_menu.py`, define:
- `SMSMenu(from_number)`
- Prompt for destination + message
- Validate both
- Call `messaging_service.send_sms(...)`
- Print response summary using CLI panel

# 5) Log decision
log_decision{
  "context":"manage-sms",
  "decision":"Created Send SMS menu with input validation, message preview, and CLI-wrapped results."
}
