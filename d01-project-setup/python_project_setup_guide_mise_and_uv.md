# Python Project Setup Guide (mise and uv)
_______________________________________________________________________________

Create the project directory
```bash
mkdir python-project-mise-uv
```
_______________________________________________________________________________

Enter the project directory
```bash
cd python-project-mise-uv
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

You should now have a `mise.toml` file in the project
_______________________________________________________________________________

Update the `mise.toml` file in the project to look like this
```toml
[tools]
ruff = "latest"
uv = "latest"

[settings]
python.uv_venv_auto = "source"
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



_______________________________________________________________________________
