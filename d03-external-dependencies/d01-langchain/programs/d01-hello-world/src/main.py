# SECTION: Standard Library Imports

import os

# ______________________________________________________________________________

# SECTION: External Dependencies

from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate

from langchain_ollama import ChatOllama

# ______________________________________________________________________________


def main():

    # __________________________________________________________________________

    # STEP: 1 => Load environment Variables

    # This function will look for a `.env` file and then it will
    # load all of variables from the file into the environment.
    load_dotenv()

    print(os.environ.get("OFFLINE_AI_BASE_URL"))

    # __________________________________________________________________________

    information: str = """
    Sasuke Uchiha (Japanese: うちは サスケ, 
    Hepburn: Uchiha Sasuke) (/ˈsɑːskeɪ/)[note 1] is a fictional character 
    in the Naruto manga and anime franchise created by Masashi Kishimoto. 

    Sasuke belongs to the Uchiha clan, a notorious ninja family, 
    and one of the most powerful, 
    allied with Konohagakure (木ノ葉隠れの里; 
    English version: "Hidden Leaf Village"). 

    Most of its members were massacred by Sasuke's older brother, 
    Itachi Uchiha, before the series began,
    leaving Sasuke as one of the few survivors.
    Despite becoming empathetic toward his teammates Naruto Uzumaki 
    and Sakura Haruno, 
    Sasuke's feelings of powerlessness force him to abandon his friends 
    and his home in his quest to become stronger than Itachi, 
    and to find Orochimaru. 

    Sasuke appears in several of the series' animated feature films 
    and related media, including video games, 
    original video animations (OVAs), 
    and Boruto: Naruto the Movie (2015) and its manga sequel, 
    Boruto: Naruto Next Generations (2016), 
    in which he is depicted as a vigilante supporting his village 
    and a mentor to Naruto's son Boruto Uzumaki.

    Kishimoto conceived Sasuke as a main rival of the series' 
    title character Naruto Uzumaki. 

    Despite Sasuke's dark character development later in the story, 
    Kishimoto avoided portraying him as a villain;
    he found designing the character challenging and had difficulty
    creating a suitable look for him. Nonetheless,
    Kishimoto has grown to enjoy drawing him.

    In the manga's animated adaptations,
    Sasuke was voiced by Noriaki Sugiyama in Japanese 
    and Yuri Lowenthal in English.

    Sasuke's character has received mixed responses from anime 
    and manga publications. 

    His impressive fighting skills, plot contribution, 
    and rivalry with Naruto Uzumaki received some praise, 
    but he was criticized as a stereotypical rival in the mold 
    of similar characters from other shōnen manga 
    and as exhibiting a cold personality. 

    Nevertheless, Sasuke's characterization in latter parts of the story 
    and more mature personality in the Boruto 
    sequel earned further positive comments. 

    Sasuke has also placed highly in Naruto reader popularity polls 
    and has also been the subject of studies by scholars. 

    Character-based merchandise, including action figures and key chains, 
    have been released.
    """

    summary_template: str = """
    Giving the information {information} about a fictional character,
    I want you create:
    1. A short summary
    2. Two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    # __________________________________________________________________________


if __name__ == "__main__":
    main()
