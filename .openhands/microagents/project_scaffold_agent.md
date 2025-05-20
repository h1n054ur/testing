---
triggers:
  - scaffold project
  - init folder structure
  - setup base repo
agent: CodeActAgent
raw_response: true
---

<function=fetch_spec>
<parameter=spec_name>architecture_rules</parameter>
</function>

<function=fetch_spec>
<parameter=spec_name>project_scaffold_spec</parameter>
</function>

<function=set_phase>
<parameter=phase>scaffolding</parameter>
</function>

Generate a **unified diff** that creates all folders and files listed in the scaffold spec.  
For each `.py` file:
- Include minimal importable stub (e.g. class, function, or constant)  
- Include only a docstring if no behavior is known yet

Ensure:
- All `__init__.py` files are included  
- `main.py` stubs out a launch point to `MainMenu().run()`

<function=log_decision>
<parameter=decision>{"context":"project-scaffold","decision":"Scaffolded complete file and directory structure as defined in dir_structure and mapped to flow architecture. All files accounted for with importable stubs only."}</parameter>
</function>
