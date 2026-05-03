"""Tests for the {{ cookiecutter.package_name }} MCP server tools.

These call the tool functions directly. For full FastMCP integration tests
(actual stdin/stdout MCP protocol), use the MCP Inspector:
    npx @modelcontextprotocol/inspector {{ cookiecutter.project_slug }}
"""

from __future__ import annotations

from {{ cookiecutter.package_name }} import __version__
from {{ cookiecutter.package_name }}.server import echo, hello


class TestHello:
    def test_default_greeting(self):
        result = hello()
        assert result["greeting"] == "Hello, world!"
        assert result["version"] == __version__

    def test_custom_name(self):
        result = hello(name="Pawan")
        assert result["greeting"] == "Hello, Pawan!"


class TestEcho:
    def test_echoes_message(self):
        assert echo("test") == "test"

    def test_echoes_empty_string(self):
        assert echo("") == ""

    def test_echoes_unicode(self):
        assert echo("hello world") == "hello world"
