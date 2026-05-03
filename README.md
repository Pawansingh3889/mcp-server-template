# mcp-server-template

[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

A production-grade [cookiecutter](https://cookiecutter.readthedocs.io/) template for new MCP (Model Context Protocol) servers.

Scaffolds a Python MCP server in 30 seconds with the same shape used by [sql-sop-mcp](https://pypi.org/project/sql-sop-mcp/) and [sql-explorer-mcp](https://pypi.org/project/sql-explorer-mcp/).

## What you get

| File | What it does |
|---|---|
| `pyproject.toml` | hatchling build, FastMCP + pydantic + python-dotenv deps, dev extras with pytest + ruff |
| `src/<package>/server.py` | FastMCP server with two example tools (`hello`, `echo`) ready to replace |
| `tests/test_server.py` | pytest suite that calls your tools directly, plus instructions for MCP Inspector |
| `.github/workflows/ci.yml` | Python 3.10/3.11/3.12/3.13 matrix with ruff lint + pytest |
| `.github/workflows/release.yml` | Tag-driven PyPI publish via Trusted Publishing (OIDC, no API tokens) |
| `README.md` | Per-platform setup snippets for Claude Desktop, Cursor, MCP Inspector |
| `LICENSE` | MIT, Apache-2.0, or BSD-3-Clause -- you pick |
| `.env.example` | Template for local config (gitignored once copied to .env) |

## Why this template vs the others

- **Trusted Publishing PyPI workflow** baked in. Most MCP templates skip this; you get OIDC-based releases out of the box.
- **Real test scaffolding**, not just a `def test_dummy(): pass` placeholder.
- **Multi-Python CI matrix** out of the box (3.10 through 3.13).
- **MCP Inspector instructions** in the generated README so anyone cloning your repo can debug locally.
- **Optional sql-sop linter integration** for SQL-handling MCP servers.

## Use it

```bash
pip install cookiecutter
cookiecutter gh:Pawansingh3889/mcp-server-template
```

Cookiecutter will prompt for:

| Variable | What it sets |
|---|---|
| `project_name` | Display name (e.g. "Postgres MCP Server") |
| `project_slug` | PyPI / repo / CLI name (auto-derived from project_name) |
| `package_name` | Python package name (auto-derived from slug) |
| `description` | One-line description for PyPI |
| `author_name` / `author_email` | Your name and email |
| `github_username` | For URLs in pyproject.toml and README |
| `python_min_version` | Defaults to 3.10 |
| `license` | MIT / Apache-2.0 / BSD-3-Clause |
| `include_pypi_release_workflow` | yes / no |
| `include_sql_sop_linter` | yes / no -- adds sql-sop as a dev dependency |

After generation:

```bash
cd <your-project>
pip install -e ".[dev]"
pytest -v
```

You'll see two passing tests. Replace `hello` and `echo` in `src/<package>/server.py` with your real tools.

## Publish your generated server to PyPI

The release workflow uses [PyPI Trusted Publishing](https://docs.pypi.org/trusted-publishers/). One-time setup after you create the GitHub repo:

1. **Add a Pending Publisher** at https://pypi.org/manage/account/publishing/
   - Owner: `<your-github-username>`
   - Repository: `<your-project-slug>`
   - Workflow: `release.yml`
   - Environment: `release`
2. **Create a `release` environment** at `https://github.com/<you>/<repo>/settings/environments`

Then tag and push:

```bash
git tag v0.1.0
git push origin v0.1.0
```

The workflow builds, publishes to PyPI, and creates a GitHub Release with attached wheels.

## Wire your generated server into Claude Desktop

After `pip install -e .` (or `pip install <your-project>` from PyPI), add to `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac) or `%APPDATA%\Claude\claude_desktop_config.json` (Windows):

```json
{
  "mcpServers": {
    "<your-package>": {
      "command": "<your-project-slug>"
    }
  }
}
```

Restart Claude Desktop. Tools appear under Settings → Tools.

## Examples in the wild

Real MCP servers built using this template's pattern:

- [sql-sop-mcp](https://github.com/Pawansingh3889/sql-sop-mcp) -- SQL linter exposed as MCP
- [sql-explorer-mcp](https://github.com/Pawansingh3889/sql-explorer-mcp) -- multi-engine read-only SQL explorer with three-layer safety

## Contributing

PRs welcome. Particularly useful: alternative tool patterns (resources, prompts), better test scaffolding, additional optional integrations.

## License

MIT
