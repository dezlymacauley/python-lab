# SECTION: Standard Library Imports

import os

# ______________________________________________________________________________

# SECTION: External Dependencies

from dotenv import load_dotenv

# ______________________________________________________________________________


def main():

    #__________________________________________________________________________

    # STEP: 1 => Load environment Variables

    # This function will look for a `.env` file and then it will
    # load all of variables from the file into the environment.
    load_dotenv()

    print(os.environ.get("OFFLINE_AI_BASE_URL"))

    #__________________________________________________________________________

if __name__ == "__main__":
    main()
