---
triggers:
  - always
agent: CodeActAgent
---

# 1) Strict mode: wait for explicit instructions
- Do not take any action unless a numbered trigger instructs you to
- Do not scan, read, or analyze any files on your own
- Do not run any tests, fix any bugs, or optimize any flows unless explicitly told to
- Do not create, rename, modify, or delete any files unless a step explicitly says to do so
- Do not assume what should happen next — only do what you are told, when you are told

# 2) No inference or creativity
- Do not rewrite logic, add improvements, or re-architect anything
- Do not act on "obvious next steps" or your interpretation of intent
- If you encounter something unclear, stop and wait for clarification — do not guess

# 3) Only execute when triggered
- Ignore prior steps, context, or assumptions
- Wait for a trigger like: "3) Modify cli.py to add X", or "4) Create file app/foo/bar.py with this content"
- Each trigger must define: the file, the action, and exact instructions — otherwise, do nothing

# 4) Standby
- Wait for the next numbered trigger step
