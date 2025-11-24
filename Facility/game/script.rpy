# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define sol = Character("Sol")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene lobby
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    "You awake in an unfamiliar building with no recollection of how you got here or who you are."
    "Is this some kind of lobby?"
    "You're not sure."
    "Looking around, you notice some places of interest: the plant by the front desk, the front desk, the chairs, and the posters."
    menu choiceLoopLobby: 
        "Where should you go first?"

        "the plant":
            jump plant
        "The Front Desk":
            jump front_desk
        "The Chairs":
            jump chairs
        "The Posters":
            jump posters
    
    label plant:
        "You walk over to the plant and crouch beside it."
        "There's a nameplate on it: plantus the plant."
        menu plant_interact:
            "What will you do to the plant?"

            "Pet the plant":
                "You petted the plant gently."
                "You think you heard it purr?"
                $ pet_plant = True
            "Eat the plant":
                "...????"
                "You stuffed the entire plant in your mouth."
                $ ate_plant = True
            "Flirt with the plant": 
                "You tell Plantus that you'd never leaf them for another."
                "Plantus blushes!"
                $ flirt_plant = True
        label after_plant:
            "You decide to leave the plant alone."
            jump choiceLoopLobby
    label front_desk:
        "You walk over to the front desk."
        "There is a bell."
        jump choiceLoopLobby
    label chairs:
        "You see three chairs in the corner, ominously placed in a circle."
        jump choiceLoopLobby
    label posters:
        "You see three posters."
        "One explains the rules of this place, one is a Hangin In There cat poster, and the third one has some strange man on it."
        jump choiceLoopLobby

    # This ends the game.

    return
