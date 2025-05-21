---
triggers:
  - scaffold project
  - init folder structure
  - setup base repo
agent: CodeActAgent
---

# 1) Load architecture
fetch_spec3{"spec_name":"architecture"}

# 2) Load architecure rules
fetch_spec3{"spec_name":"architecture_rules"}

# 3) Load project scaffold specification
fetch_spec3{"spec_name":"project_scaffold_spec"}

# 4) Set current working phase
set_phase3{"phase":"scaffolding"}

# 5) Create full structure
Use execute_bash3 only you have access to all bash commands
### EXAMPLE
**Rename a file:**
```json
execute_bash3{
  "command": "mv ./workspace/old.py ./workspace/new.py"
}
```
Generate a **unified diff** that creates all folders and files listed in the scaffold spec.  
For each `.py` file:
- Include only a docstring with description

Ensure:
- All `__init__.py` files are included

# 6) Create a checklist 
- verify if all steps from spec file have been completed exactly. You are not allowed to do any extra actions other than mentioned in the spec.

# 7) Log outcome
log_decision{
  "context":"project-scaffold",
  "decision":"Scaffolded complete file and directory structure as defined in dir_structure and mapped to flow architecture. All files accounted for #doctring descriptions only"
}
