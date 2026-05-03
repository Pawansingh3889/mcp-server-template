"""Post-generation hook.

Runs after cookiecutter renders the template. Cleans up files that
the user opted out of via cookiecutter.json choices.
"""

from __future__ import annotations

import os
import shutil
from pathlib import Path

PROJECT_DIR = Path(os.getcwd())


def remove(path: Path) -> None:
    """Remove a file or directory if it exists."""
    if path.is_file() or path.is_symlink():
        path.unlink()
    elif path.is_dir():
        shutil.rmtree(path)


def main() -> None:
    include_pypi_release = "{{ cookiecutter.include_pypi_release_workflow }}" == "yes"

    if not include_pypi_release:
        remove(PROJECT_DIR / ".github" / "workflows" / "release.yml")
        print("[hook] Removed release.yml (include_pypi_release_workflow=no)")

    # Initialise git repo
    if not (PROJECT_DIR / ".git").exists():
        os.system("git init -q")
        os.system("git add .")
        print("[hook] Initialised git repo and staged files")

    print()
    print("Project generated. Next steps:")
    print()
    print("  cd {{ cookiecutter.project_slug }}")
    print("  pip install -e \".[dev]\"")
    print("  pytest -v")
    print()
    print("Then edit src/{{ cookiecutter.package_name }}/server.py to add your tools.")
    print()


if __name__ == "__main__":
    main()
