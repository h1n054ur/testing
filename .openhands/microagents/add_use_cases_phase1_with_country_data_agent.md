---
triggers:
  - wire use cases and integrate country_data as source
  - enforce all menu/data flow via use case and country_data
agent: CodeActAgent
---

# 1) Load add_use_cases_phase1_with_country_data_spec
fetch_spec2{"spec_name":"add_use_cases_phase1_with_country_data_spec"}

# 1) Load add_use_cases_phase1_with_country_data_spec
fetch_spec2{"spec_name":"user_flow"}

# 3) Set phase
set_phase{"phase":"use-case-wiring-country-data"}

# 4) In app/models/country_data.py, ensure a complete country_data dictionary exists with all info for US, CA, GB, AU
# 5) In app/use_cases/, create purchase_flow.py, manage_flow.py, settings_flow.py, each using country_data for all needed logic and lookups
# 6) In all menu classes, require a use case instance and remove any stub/static data or logic
# 7) All menu display/data comes only from use case methods, which use country_data for all country/region/price/type/capability needs
# 8) All actions and table displays routed to correct use case methods
# 9) Remove any old static/stub data from menus
# 10) Test end-to-end to confirm menus display only what use case and country_data provide

# 11) Log outcome
log_decision{
  "context":"use-case-wiring-country-data",
  "decision":"All business logic/data for country, region, type, price, etc. is now sourced via country_data and accessed only via use cases. Menus are UI-only. App matches user_flow.md and is ready for real integration."
}
