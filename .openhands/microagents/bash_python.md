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

- `execute_bash2` → For all shell operations (mv, cp, mkdir, rm, cat, ls, etc.)
- `eval_python2` → For parsing, file content replacement, or logic-based manipulation

---

### 🛠 WHEN TO USE

| Action                        | Use                   |
|------------------------------|------------------------|
| Move or rename a file        | `execute_bash2` + `mv` |
| Copy a file or folder        | `execute_bash2` + `cp` |
| Create folders               | `execute_bash2` + `mkdir -p` |
| Delete files or folders      | `execute_bash2` + `rm` |
| Read/inspect a file          | `cat` or Python in `eval_python2` |
| Replace/edit file content    | Python in `eval_python2` |

---

### ❌ DO NOT

- ❌ Use `read_file2`, `create_file2`, or `list_files2` unless absolutely necessary
- ❌ Simulate shell operations — always execute them

---

### 💡 EXAMPLES

**Rename a file:**
```json
execute_bash2{
  "command": "mv ./workspace/old.py ./workspace/new.py"
}
```

**Read contents:**
```json
eval_python2{
  "code": "with open('./workspace/example.py') as f: print(f.read())"
}
```

---
