---
triggers:
  - scaffold project
  - init folder structure
  - setup base repo
agent: CodeActAgent
tools:
  - fetch_spec
  - set_phase
  - log_decision
---

# 1) Load enforced architecture rules
fetch_spec{"spec_name":"architecture_rules"}

# 2) Load project scaffold specification
fetch_spec{"spec_name":"project_scaffold_spec"}

# 3) Set the current phase to scaffolding
set_phase{"phase":"scaffolding"}

# 4) Scaffold project file and folder structure

Create the following files and folders under the root directory `twilio-manager/`:

- Folders: `search_results/`, `app/`, and all subfolders described below.
- For each folder, create an `__init__.py` file if it's a Python package.
- For each `.py` file listed, create the file and include a minimal valid Python stub:
    - Either a class, function, or constant
    - Include a descriptive docstring
- Do not include full implementations. Keep logic minimal or empty.
- In `main.py`, add code that imports `MainMenu` and calls `.run()`.

Use `exec_bash` to create directories and `eval_python` or `FileEditAction` to write files.

# 5) Log success
log_decision{
  "context": "project-scaffold",
  "decision": "Scaffolded full file and folder structure using architecture spec. Each file has a placeholder stub or docstring. main.py stubs MainMenu().run()."
}
