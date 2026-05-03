"""FastMCP server entry point.

Replace the example tools below with your own. Each @mcp.tool() decorated
function becomes callable from the LLM.

For richer parameter descriptions and validation (visible to the LLM),
wrap parameters with typing.Annotated + pydantic.Field, e.g.:

    from typing import Annotated
    from pydantic import Field

    @mcp.tool()
    def search(
        query: Annotated[str, Field(description="Search query, max 200 chars")],
        limit: Annotated[int, Field(ge=1, le=100, description="Max results")] = 10,
    ) -> list[dict]:
        ...

The example tools below use plain defaults to stay minimal and testable.
"""

from __future__ import annotations

from dotenv import load_dotenv
from fastmcp import FastMCP

from {{ cookiecutter.package_name }} import __version__

load_dotenv()

mcp = FastMCP("{{ cookiecutter.project_slug }}")


@mcp.tool()
def hello(name: str = "world") -> dict:
    """Example tool. Returns a greeting and the server version."""
    return {"greeting": f"Hello, {name}!", "version": __version__}


@mcp.tool()
def echo(message: str) -> str:
    """Echo back the input message. Useful as a connection sanity check."""
    return message


def main() -> None:
    """Entry point for the {{ cookiecutter.project_slug }} script."""
    mcp.run()


if __name__ == "__main__":
    main()
