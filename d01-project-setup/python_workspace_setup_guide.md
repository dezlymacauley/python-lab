# Python Workspace Setup Guide
_______________________________________________________________________________

Create the project directory
```bash
mkdir python-workspace
```
_______________________________________________________________________________

Enter the project directory
```bash
cd python-workspace
```
_______________________________________________________________________________

Set the project to use the latest version of `uv` (package manager)
```bash
mise use uv@latest
```
_______________________________________________________________________________

Set the project to use the latest version of `ruff` (code formatter)
```bash
mise use ruff@latest
```
_______________________________________________________________________________

Set the project to use the latest version of `eza` (project structure viewer)
```bash
mise use eza@latest
```
_______________________________________________________________________________

Decide which version of Python you want to use in your workspace. 

Please note that all of the programs in your Python workspace will use this
Python version.
_______________________________________________________________________________

You can use `mise` to check what is the version number 
of the latest available Python that you can use in a project.
```bash
mise latest python
```
_______________________________________________________________________________

If you want to view a list of valid Python versions that you can use,
run this command:
```bash
mise ls-remote python
```
_______________________________________________________________________________

For this guide, I'll be using Python `3.15.1`
_______________________________________________________________________________

Update the `mise.toml` file in the project to look like this
```toml
[env]
WORKSPACE_PYTHON_VERSION = "3.15.1" 
#______________________________________________________________________________

[tools]
eza = "latest"
ruff = "latest"
uv = "latest"
#______________________________________________________________________________

[settings]
python.uv_venv_auto = "source"
#______________________________________________________________________________

[tasks.clean]
description = "🧼 Delete cache and dependencies | alias = clean"
quiet = true
run = """

rm -rf __pycache__
rm -rf .ruff_cache
rm -rf .venv

"""
#______________________________________________________________________________

[tasks.format]
description = "📜 Run the code formatter on the project | alias = format"
quiet = true
run = """

ruff format .

"""
#______________________________________________________________________________

[tasks.setup]
description = "🚀 Setup the project | alias = setup"
quiet = true
run = """

# Ensure that this is a clean build of the virtual environment
rm -rf __pycache__
rm -rf .ruff_cache
rm -rf .venv

# Rebuild the the virtual environment and install the dependencies
uv sync
cd ..
cd -

"""
#______________________________________________________________________________

[tasks.structure]
description = "🌲 View the project structure | alias = structure"
quiet = true
run = """

eza --tree --git-ignore

"""
#______________________________________________________________________________

[shell_alias]
clean = "mise run clean"
format = "mise run format"
run = "python src/main.py"
setup = "mise run setup"
structure = "mise run structure"
#______________________________________________________________________________
```
_______________________________________________________________________________

Create a `.gitignore` file
```sh
touch .gitignore
```
_______________________________________________________________________________

Add this to the `.gitignore` file

```gitignore
# Project Dependencies
.venv/

# Code Formatter Cache
.ruff_cache/ 

# Python Module Bytecode Cache
__pycache__/
```
_______________________________________________________________________________

Create a `ruff.toml` file to configure the `ruff` formatter
```sh
touch ruff.toml
```
_______________________________________________________________________________

Add this to the `ruff.toml` file
```toml
line-length = 80
```
_______________________________________________________________________________

Intialize the workspace usinge `uv`
```bash
uv init --bare -p "$WORKSPACE_PYTHON_VERSION"
```

#### Note:
This command will do the following:
1. Use `mise` to get the version number of the latest available Python
2. Then `uv` will create a `pyproject.toml` file to store that version number.

- This file only records the version of Python that is used,
it does not set the Python version recorded.
_______________________________________________________________________________

Create a `programs` directory
```bash
mkdir programs
```
_______________________________________________________________________________

Update the `pyproject.toml` file to look like this
```bash
[project]
name = "python-workspace"
version = "0.1.0"
requires-python = ">=3.15.1"

[tool.uv]
package = false

[tool.uv.workspace]
members = ["programs/*"]
```
_______________________________________________________________________________

Create a `.python-version` file
```bash
echo "$WORKSPACE_PYTHON_VERSION" > .python-version
```

#### Note:
- This file will be used by `uv` to create a Python Virtual Environment,
when the `uv sync` command is used later in this guide.
_______________________________________________________________________________

Create a Python Virtual Environment
```bash
uv venv -p "$WORKSPACE_PYTHON_VERSION"
```
_______________________________________________________________________________

Activate the Python Virtual Environment

```sh
uv sync
cd ..
cd -
```

#### Note
- Because of line `python.uv_venv_auto = "source"` in the `mise.toml` file,
you only need to activate the virtual enviroment once.

- Whenever you enter the project directory, 
`mise` will ensure that `uv` sources the `.venv` directory so that 
the project automatically uses the correct version of Python.

- There is no need to deactivate the the `.venv` directory either.
mise will automatically deactivate it when you exit the project directory.
_______________________________________________________________________________

To confirm that your project is using the correct version of Python, 
run this:
```sh
python --version
which python | sed "s|$PWD/||"
```

#### Note:
- The import thing to pay attention to is this `.venv/bin/python`
- That is what confirms that your project is using the virtual enviroment
that was set by uv.
```
.venv/bin/python
```
_______________________________________________________________________________

## How to add programs to the workspace

_______________________________________________________________________________

In this guide I'm going to add two programs,
which I will call `d01` and `d02`

All of the programs in the workspace will share the same Python version,
and use the same Python Virtual enviroment.

So the first thing to do is to get the specific version of Python that was
recorded in your `.python-version` file

_______________________________________________________________________________

This is how to add the first program, `d01`
```bash
mkdir programs/d01

cd programs/d01
    uv init --bare -p "$WORKSPACE_PYTHON_VERSION"
    mkdir src
    touch src/main.py
cd ../..
```
_______________________________________________________________________________

This is how to add the second program, `d02`
```bash
mkdir programs/d02

cd programs/d02
    uv init --bare -p "$WORKSPACE_PYTHON_VERSION"
    mkdir src
    touch src/main.py
cd ../..
```
_______________________________________________________________________________

Add this to the `programs/d01/src/main.py` file
```python
def main():
    print()
    print("This is d01")
    print()


if __name__ == "__main__":
    main()
```
_______________________________________________________________________________

Add this to the `programs/d02/src/main.py` file
```python
def main():
    print()
    print("This is d02")
    print()


if __name__ == "__main__":
    main()
```
_______________________________________________________________________________

Run this command to see the list of `mise tasks` in your project
```bash
mise tasks
```

You should see an output like this
```
Name       Description
clean      🧼 Delete cache and dependencies | alias = clean
format     📜 Run the code formatter on the project | alias = format
setup      🚀 Setup the project | alias = setup
structure  🌲 View the project structure | alias = structure
```
_______________________________________________________________________________

To view the project structure, just run this command:
```bash
structure
```

This should be the project structure
```
.
├── mise.toml
├── programs
│   ├── d01
│   │   ├── pyproject.toml
│   │   └── src
│   │       └── main.py
│   └── d02
│       ├── pyproject.toml
│       └── src
│           └── main.py
├── pyproject.toml
├── ruff.toml
└── uv.lock
```
_______________________________________________________________________________

To run a program, simply navigate to the directory use the `run` command.

E.g. To run the program `d01`

```bash
cd programs/d01
run
```
_______________________________________________________________________________
