---
triggers:
  - scaffold project
  - init folder structure
  - setup base repo
agent: CodeActAgent
---

# 1) Load enforced architecture rules
fetch_spec{"spec_name":"architecture_rules"}

# 2) Load project scaffold specification
fetch_spec{"spec_name":"project_scaffold_spec"}

# 3) Set current working phase
set_phase{"phase":"scaffolding"}

# 4) Create full structure
Generate a **unified diff** that creates all folders and files listed in the scaffold spec.  
For each `.py` file:
- Include minimal importable stub (e.g. class, function, or constant)
- Include only a docstring if no behavior is known yet

Ensure:
- All `__init__.py` files are included
- `main.py` stubs out a launch point to `MainMenu().run()`

# 5) Log outcome
log_decision{
  "context":"project-scaffold",
  "decision":"Scaffolded complete file and directory structure as defined in dir_structure and mapped to flow architecture. All files accounted for with importable stubs only."
}
