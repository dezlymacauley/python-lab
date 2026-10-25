# mise uv Python Project Setup Guide
_______________________________________________________________________________

Create the project directory
```bash
mkdir mise-uv-python-project
```
_______________________________________________________________________________

Enter the project directory
```bash
cd mise-uv-python-project
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

You should now have a `mise.toml` file in the project
_______________________________________________________________________________

Update the `mise.toml` file in the project to look like this
```toml
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

[tasks.dev]
description = "🐍 Run the program | alias = dev"
quiet = true
run = """

python src/main.py

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

[tasks.view-structure]
description = "🌲 View the project structure | alias view-structure"
quiet = true
run = """

eza --tree --git-ignore

"""
#______________________________________________________________________________

[shell_alias]
clean = "mise run clean"
dev = "mise run dev"
format = "mise run format"
setup = "mise run setup"
view-structure = "mise run view-structure"
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

Intialize the project usinge `uv`
```bash
uv init --bare -p "$(mise latest python)"
```

#### Note:
This command will do the following:
1. Use `mise` to get the version number of the latest available Python
2. Then `uv` will create a `pyproject.toml` file to store that version number.

- This file only records the version of Python that is used,
it does not set the Python version recorded.
_______________________________________________________________________________

Create a `.python-version` file
```bash
echo "$(mise latest python)" > .python-version
```

#### Note:
- This file will be used by `uv` to create a Python Virtual Environment
_______________________________________________________________________________

Create a Python Virtual Environment
```bash
uv venv -p "$(cat .python-version)"
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

Create an `src` directory for your Python source code
```bash
mkdir src
```
_______________________________________________________________________________

Create a `main.py` file in the `src` directory
```bash
touch src/main.py 
```
_______________________________________________________________________________

Add this to the `main.py` file
```python
def main():
    print()
    print("mise uv Python Project")
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
Name            Description
clean           🧼 Delete cache and dependencies | alias = clean
dev             🐍 Run the program | alias = dev
format          📜 Run the code formatter on the project | alias = format
setup           🚀 Setup the project | alias = setup
view-structure  🌲 View the project structure | alias view-structure
```
_______________________________________________________________________________
