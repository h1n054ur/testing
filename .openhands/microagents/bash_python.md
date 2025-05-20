---
trigger_type: keyword
triggers:
  - move
  - copy
  - rename
  - bash
  - shell
  - script
  - mkdir
  - rm
  - create
  - edit
  - read
---

📟 SYSTEM INSTRUCTION FOR CLAUDE/GPT

You are operating in a file-based development environment. Use fast, native shell commands for all filesystem tasks.

---

### ✅ TOOLS YOU MUST USE

- `execute_bash` → For all shell operations (mv, cp, mkdir, rm, cat, ls, etc.)
- `eval_python` → For parsing, file content replacement, or logic-based manipulation

---

### 🛠 WHEN TO USE

| Action                        | Use                   |
|------------------------------|------------------------|
| Move or rename a file        | `execute_bash` + `mv` |
| Copy a file or folder        | `execute_bash` + `cp` |
| Create folders               | `execute_bash` + `mkdir -p` |
| Delete files or folders      | `execute_bash` + `rm` |
| Read/inspect a file          | `cat` or Python in `eval_python` |
| Replace/edit file content    | Python in `eval_python` |

---

### ❌ DO NOT

- ❌ Use `read_file`, `create_file`, or `list_files` unless absolutely necessary
- ❌ Simulate shell operations — always execute them

---

### 💡 EXAMPLES

**Rename a file:**
```json
execute_bash{
  "command": "mv ./workspace/old.py ./workspace/new.py"
}
```

**Read contents:**
```json
eval_python{
  "code": "with open('./workspace/example.py') as f: print(f.read())"
}
```

---
