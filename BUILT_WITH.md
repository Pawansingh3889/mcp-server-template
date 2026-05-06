# Built with mcp-server-template

This page lists MCP servers built using (or shaped by) this cookiecutter template. PRs welcome — see [How to add yours](#how-to-add-yours) below.

## Servers

### [sql-sop-mcp](https://github.com/Pawansingh3889/sql-sop-mcp)

Wraps the [sql-sop](https://pypi.org/project/sql-sop/) SQL linter as an MCP server. Exposes one tool, `lint_sql`, that returns structured findings (rule code, severity, line, column, message). Useful for asking Claude or Cursor to lint SQL inline before committing.

- Author: [@Pawansingh3889](https://github.com/Pawansingh3889)
- PyPI: [sql-sop-mcp](https://pypi.org/project/sql-sop-mcp/)
- Tools: 1 (`lint_sql`)

### [sql-explorer-mcp](https://github.com/Pawansingh3889/sql-explorer-mcp)

Read-only multi-engine SQL MCP for SQL Server, Postgres, and SQLite. Three-layer safety stack: driver-level read-only flag, sqlglot AST validation rejecting anything that isn't exactly one SELECT, and sql-sop linter pass blocking error-severity findings. Multi-server YAML config.

- Author: [@Pawansingh3889](https://github.com/Pawansingh3889)
- PyPI: [sql-explorer-mcp](https://pypi.org/project/sql-explorer-mcp/)
- Tools: 7 (`list_servers`, `list_databases`, `list_tables`, `describe_table`, `get_table_sample`, `run_query`, `explain_query`, `search_objects`)

## How to add yours

If you generated your server with this template (or modelled it on the same shape), open a PR adding an entry to the **Servers** section above. Keep entries short:

- Linked title (repo URL)
- One paragraph describing what it does and why it's useful
- Author handle
- PyPI link if published
- Tool count or list

Sort entries alphabetically by repo name. We'll keep this file shallow and link out to your README for the detail.
