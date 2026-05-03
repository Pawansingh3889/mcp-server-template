# {{ cookiecutter.project_name }}

[![PyPI](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }})](https://pypi.org/project/{{ cookiecutter.project_slug }}/)
[![Python](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug }})](https://pypi.org/project/{{ cookiecutter.project_slug }}/)
[![License]({% if cookiecutter.license == "MIT" %}https://img.shields.io/badge/license-MIT-blue{% elif cookiecutter.license == "Apache-2.0" %}https://img.shields.io/badge/license-Apache--2.0-blue{% else %}https://img.shields.io/badge/license-BSD--3--Clause-blue{% endif %})](LICENSE)

{{ cookiecutter.description }}

## Install

```bash
pip install {{ cookiecutter.project_slug }}
# or
pipx install {{ cookiecutter.project_slug }}
```

## Tools exposed to the LLM

| Tool | Purpose |
|---|---|
| `hello(name?)` | Example greeting tool |
| `echo(message)` | Echo back input -- connection sanity check |

Replace these with your actual tools by editing `src/{{ cookiecutter.package_name }}/server.py`.

## Run

### Claude Desktop

Add to `~/Library/Application Support/Claude/claude_desktop_config.json` (Mac) or `%APPDATA%\Claude\claude_desktop_config.json` (Windows):

```json
{
  "mcpServers": {
    "{{ cookiecutter.package_name }}": {
      "command": "{{ cookiecutter.project_slug }}"
    }
  }
}
```

Restart Claude Desktop. Tools appear under Settings → Tools.

### Cursor

Add to `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "{{ cookiecutter.package_name }}": {
      "command": "{{ cookiecutter.project_slug }}"
    }
  }
}
```

### Standalone (debug)

```bash
{{ cookiecutter.project_slug }}
```

Use the [MCP Inspector](https://github.com/modelcontextprotocol/inspector) for interactive testing:

```bash
npx @modelcontextprotocol/inspector {{ cookiecutter.project_slug }}
```

## Development

```bash
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
cd {{ cookiecutter.project_slug }}
pip install -e ".[dev]"
pytest -v
```

## License

{{ cookiecutter.license }}
