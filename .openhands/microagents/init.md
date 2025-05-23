---
triggers:
  - init
  - what tools are available
  - explain available tool usage
  - show mcp tools
agent: CodeActAgent
---

- content: |
    🛠 CodeActAgent MCP Tool Overview

    The following tools are currently registered and available for use:

    ## 📦 Spec + Project Management

    - **fetch_spec3** — Load a named spec file from `./resources/specs/`. Used for architectural, feature, and planning specs.
      - ✅ Always call this first: `fetch_spec3{"spec_name":"architecture"}`

    - **set_phase3** — Sets the current development phase label. Useful to track progress and scope.
      - Example: `set_phase3{"phase":"cli-command-split"}`

    - **log_decision3** — Append a decision log entry to `./state/decisions.json`.
      - Example: `log_decision3{"decision":"Split purchase into search and purchase commands."}`

    ## 🧪 Testing and CI

    - **run_tests3** — Run tests via `pytest`. Fails on error.
    - **require_tests3** — Same as `run_tests3`. Used when test-passing is required before continuing.

    ## 📁 Filesystem (Workspace-safe)

    - **create_file3** — Create a new file safely in `./workspace/`. You must pass both `filepath` and `file_text`.
    - **read_file3** — Read the contents of a file from the workspace.
    - **list_files3** — List `.py`, `.md`, or `.json` files within the workspace.
    - **execute_bash3** — Run shell commands in `./workspace/` (with safety limits).

    ## 🚀 Deployment & Health

    - **deploy_check3** — Run static deployment readiness checks (lint/security/etc).
    - **session_health_check3** — Run a debug diagnostic if tools are misbehaving or not being executed. Use if tools are registered but not triggering.

- content: |
    ✅ If tools aren’t running when called, you can debug with:
    `session_health_check3{}`
