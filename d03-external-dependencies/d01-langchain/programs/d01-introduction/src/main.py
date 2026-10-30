# SECTION: Standard Library Imports

import os

# This allows you to type or paste an API key into the terminal without
# exposing the characters.
from getpass import getpass

# ______________________________________________________________________________

# SECTION: External Dependencies

# Allows Python to load environment variables that are declared
# in the `.env` file, into the environment
from dotenv import load_dotenv

from colorama import Fore, Style
# ______________________________________________________________________________


def main():

    # This loads the environment variables
    # `override=True` ensures that environment variables
    # declared in the `.env`
    load_dotenv(override=True)

    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY", "")

    if not os.environ["OPENAI_API_KEY"]:
        os.environ["OPENAI_API_KEY"] = getpass("Enter OpenAI API key:")
    else:
        print(
            f"{Fore.GREEN}OpenAI API key loaded from environment variable.{Style.RESET_ALL}"
        )

# ______________________________________________________________________________

if __name__ == "__main__":
    main()
