# SECTION: Standard Library Imports

# import os

# ______________________________________________________________________________

# SECTION: External Dependencies

from re import search
from dotenv import load_dotenv

from langchain.agents import create_agent

# A `tool` is a function that an agent can execute.
# To be more specific,
# its a function to make API calls

# To create a `tool`, you use the tool decorator.
from langchain.tools import tool

from langchain_core.messages import HumanMessage

from langchain_ollama import ChatOllama

# from langchain_core.prompts import PromptTemplate
#
# from langchain_ollama import ChatOllama

# ______________________________________________________________________________

# STEP: 1 => Create a search function

# `@tool` is a Python decorator that turns a regular Python function into
# a LangChain `tool`. In LangChain, a `tool` is a function that can be used
# by an `AI Agent` to perform actions such as API calls,
# reading from a database etc. 
@tool
def search_internet(query: str) -> str:
    """
    Search the internet

    Usage:
        query: The thing that you want to search for

    Returns:
        A string that contains the results
    """
    print(f"Searching for {query}")
    return "Tokyo weather is sunny"

def main():
    search_internet("Tokyo")

    # __________________________________________________________________________

    # STEP: 2 => Load environment Variables

    # This function will look for a `.env` file and then it will
    # load all of variables from the file into the environment.
    load_dotenv()

    # __________________________________________________________________________

    # STEP: 3 => Add the llm to the program

    llm = ChatOllama()


    # __________________________________________________________________________


if __name__ == "__main__":
    main()
