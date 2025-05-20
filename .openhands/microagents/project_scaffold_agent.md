---
triggers:
  - scaffold project
  - initialize structure
  - setup twilio cli
agent: CodeActAgent
tools:
  - exec_bash
  - eval_python
  - file_edit
  - log_decision
  - set_phase
---

# 🏗 Scaffold Project: Twilio Manager CLI

You are a developer assistant. Follow these steps to scaffold the full directory and file structure for the Twilio Manager CLI project.

## 📍 Phase 1: Setup Phase

1. Set the current phase to "scaffolding".
   Use the tool: set_phase with argument { "phase": "scaffolding" }

---

## 📁 Phase 2: Create Root Directory and Base Files

2. Create the root folder: twilio-manager/

3. Inside twilio-manager/, create the following files:
   - __main__.py
   - main.py
   - pyproject.toml
   - requirements.txt
   - setup.cfg
   - .gitignore
   - .pre-commit-config.yaml
   - pytest.ini
   - .openhands_instructions

4. Create a folder named: search_results/

---

## 📁 Phase 3: Create app/ Structure

5. Create a folder named app/ under twilio-manager/ and add __init__.py.

6. Inside app/core/, create the following files:
   - __init__.py
   - account.py
   - call.py
   - logs.py
   - message.py
   - phone_number.py

Each file must contain a Python stub with a docstring: either a class or a function.

7. Inside app/gateways/, create:
   - __init__.py
   - config.py
   - file_logger.py
   - http_gateway.py
   - logging_setup.py
   - twilio_gateway.py

Each should contain a stub only — no logic.

8. Inside app/interfaces/cli/menus/, create:
   - __init__.py
   - base_menu.py
   - main_menu.py

Also create subfolders: purchase/, manage/, settings/

9. Inside purchase/, create:
   - __init__.py
   - purchase_menu.py
   - locality_input_menu.py
   - search_progress_menu.py
   - search_results_menu.py
   - purchase_confirm_menu.py

10. Inside manage/, create:
   - __init__.py
   - manage_menu.py
   - call_menu.py
   - sms_menu.py
   - logs_menu.py
   - config_menu.py
   - number_actions_menu.py
   - release_menu.py
   - voice_config_menu.py
   - messaging_config_menu.py

11. Inside settings/, create:
   - __init__.py
   - account_logs_menu.py
   - advanced_search_menu.py
   - billing_menu.py
   - config_management_menu.py
   - devtools_menu.py
   - diagnostics_menu.py
   - security_menu.py
   - settings_menu.py
   - subaccount_menu.py

Each menu file should contain a stub class with a docstring only. No logic.

12. Inside app/models/, create:
   - __init__.py
   - account_model.py
   - country_data.py
   - message_model.py
   - phone_number_model.py

Each must define a class or constant with a docstring.

13. Inside app/services/, create:
   - __init__.py
   - account_service.py
   - account_logs_service.py
   - messaging_service.py
   - number_service.py
   - voice_service.py

Each must define a placeholder class with a docstring. No implementation yet.

14. Inside app/use_cases/, create:
   - __init__.py
   - manage_flow.py
   - purchase_flow.py
   - settings_flow.py

Each file must contain a coordinator class or function with a docstring.

---

## 🧪 Phase 4: Stub main launcher

15. In main.py, write the following Python code:

from app.interfaces.cli.menus.main_menu import MainMenu

if __name__ == "__main__":
    MainMenu().run()

Inject this using eval_python or file_edit.

---

## ✅ Phase 5: Log Completion

16. Call the log_decision tool with:
   - context: project-scaffold
   - decision: Project folder structure scaffolded with all required files and placeholder Python stubs. Structure matches Twilio Manager CLI spec.

---

## 🚫 Rules

- Do not place CLI logic in core or services.
- Do not include SDK/API logic outside gateways.
- Do not skip or rename any folder or file.
- Do not include business logic — only placeholder stubs and docstrings.
