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

from google import genai

from langchain.chat_models import init_chat_model

# ______________________________________________________________________________


def main():

    # _________________________________________________________________________

    # SUB_SECTION: 1 => Load the environment variables

    # This loads the environment variables
    # `override=True` ensures that environment variables
    # declared in the `.env`
    load_dotenv(override=True)

    os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY", "")

    if not os.environ["GEMINI_API_KEY"]:
        os.environ["GEMINI_API_KEY"] = getpass("Enter Gemini API key:")
    else:
        print(
            f"{Fore.GREEN}"
            "Gemini API key loaded from environment variable."
            f"{Style.RESET_ALL}"
        )

    # _________________________________________________________________________

    # NOTE: Use this to check which models are available

    # print()
    #
    # client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    # for m in client.models.list():
    #     print(m.name)

    # _________________________________________________________________________

    # SUB_SECTION: 3 => Use the model

    from langchain.chat_models import init_chat_model

    model = init_chat_model(
        model="gemini-3.6-flash",
        model_provider="google_genai",
        temperature=0, # This makes the model's responses less random
        max_retries=2,
        timeout=20,
    )

    response = model.invoke("Why do parrots talk?")
    print(f"{Fore.CYAN}Response from model: {Style.RESET_ALL}{response}")

    # _________________________________________________________________________


if __name__ == "__main__":
    main()
