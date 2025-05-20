---
triggers:
  - build voice config menu
  - configure voice routing
  - voice setup menu
agent: CodeActAgent
---

# 1) Load architecture rules
fetch_spec2{"spec_name":"architecture_rules"}

# 2) Load voice config menu spec
fetch_spec2{"spec_name":"voice_config_menu_spec"}

# 3) Set phase
set_phase{"phase":"manage-flow"}

# 4) Implement voice_config_menu.py
In `interfaces/cli/menus/manage/voice_config_menu.py`, define:
- `VoiceConfigMenu(number)`
- Prompt for method → input fields
- Validate with `core.call.validate_voice_config(...)`
- Call `number_service.update_config(...)` with voice block

# 5) Log outcome
log_decision{
  "context":"manage-voice-config",
  "decision":"Created Voice Config CLI menu to update routing settings using structured input, validation, and service update."
}
