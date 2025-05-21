---
triggers:
  - refactor menus for guided flows and visual fixes
  - enforce menu and panel style
  - remove extra menu steps
agent: CodeActAgent
---

# 1) Load refactor menus for guided flows and visual fixes spec
fetch_spec3{"spec_name":"refactor_menus_spec"}

# 2) Load user flow spec
fetch_spec3{"spec_name":"user_flow"}

# 3) Set phase
set_phase3{"phase":"refactor-menus-guided"}

# 4) Refactor menus and panel style:
# - Update BaseMenu panel to match reference (red, centered, snug, padded)
# - Remove any redundant intermediate menus from Purchase and Manage flows; first step of each is a menu/table as per user_flow.md
# - For Purchase flow: pressing 1 from Main Menu goes directly to country selection menu, then subsequent steps are each a menu/table
# - For Manage flow: pressing 2 from Main Menu shows numbers table immediately, then number actions menu
# - Settings remains a standard menu, with wording/order fixed to match user_flow.md
# - Remove/merge any unnecessary menu files, fix imports throughout
# - Test to confirm visuals, menu order, and stepwise guided flows

# 5) Log outcome
log_decision3{
  "context":"refactor-menus-guided",
  "decision":"All menus and flows refactored for true guided sequence with menu/table UIs, panel is red and visually centered/snug, and no double actions or blank prompts remain."
}
