# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define sol = Character("Sol")
default menuset = set()
default pet_plant = False
default ate_plant = False
default flirt_plant = False
default ate_pot = False
default ready = False
default same_name = False
default stole_bell = False
default door_rejected = False
define pov = Character("[povname]")

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
        "The Door":
            jump door
    
    label plant:
        "You walk over to the plant and crouch beside it."
        "There's a nameplate on it: plantus the plant."
        menu plant_interact:

            set menuset
            "What will you do to the plant?"
            
            "Pet the plant":
                "You petted the plant gently."
                "You think you heard it purr?"
                $ pet_plant = True
                jump plant_interact
            "Eat the plant":
                $ ate_plant = True
                with fade
                "...????"
                "You stuffed the entire plant in your mouth."
                jump plant_interact
            "Flirt with the plant": 
                "You tell Plantus that you'd never leaf them for another."
                "Plantus blushes!"
                $ flirt_plant = True
                jump plant_interact
            "Eat the pot" if ate_plant:
                with fade
                "Within seconds, you have consumed the entire pot."
                "Are you proud of yourself?"
                $ ate_pot = True
                jump choiceLoopLobby
            "Return":
                jump choiceLoopLobby
        label after_plant:
            "You decide to leaf the plant alone."
            jump choiceLoopLobby
    
    label door:
        if door_rejected:
            "You try again to open the door, but are met with the same response as last time."
            "Maybe if he were distracted..."
            "Either way, you leave the door alone."
            jump choiceLoopLobby
        "You walk past the desk to the door. Your hand catches the doorknob, and you begin to turn the handle.."
        show sol surprised
        sol "UH, WAIT! wait wait wait wait-"
        "The man behind the counter springs into action, stepping forward and pressing a hand against the door to stop you from opening it."
        sol "You're, uhm. Not allowed back there. By yourself, anyway..."
        show sol neutral
        sol "Sorry."
        "You are ushered away from the door."
        hide sol
        $ door_rejected = True
        jump choiceLoopLobby

    label front_desk:
        "You walk over to the front desk."
        "There is a bell, and an odd looking man sitting behind the front desk.."
        menu desk_interact:
            "What will you do?"
            set menuset
            "Tell him you're ready to go" if ready:
                if stole_bell:
                    show sol irritated
                    sol ".... really?"
                    sol "Just... come with me."
                jump before_hallways
            "Ring the bell":
                if ready:
                    show sol happy
                    sol "Are you ready to start experimenting and... whatever else it is that we do here?!"
                    menu experiment:
                        "Yes":
                            jump before_hallways
                        "No":
                            show sol neutral
                            "You tell him that you're not ready yet."
                            "You walk away to continue your investigations."
                            hide sol
                            jump choiceLoopLobby
                elif stole_bell:
                    "You take the bell out of your pocket and hold it up."
                    "You slam your hand down onto it repeatedly, all the while making eye contact with him."
                    show sol neutral
                    sol "..."
                    show sol irritated
                    sol "...Hi"
                elif ate_pot:
                    show sol neutral 
                    sol "Hey, so uhm.. Before anything else..."
                    show sol irritated
                    sol "Did you eat. The plant. And its pot???"
                    sol "Because, I, uhm. Saw you. Do that."
                elif ate_plant:
                    show sol neutral
                    sol "Hey, so uhm...! Before anything else..."
                    show sol irritated
                    sol "Where did my plant go."
                elif flirt_plant:
                    show sol neutral
                    sol "..."
                    sol "Hey, so.. It's not really an official rule or anything, but."
                    show sol irritated
                    sol "Please don't flirt with the plants.."
                elif pet_plant:
                    show sol neutral
                    sol "Hello. I see you met plantus."
                    sol "Thank you for giving him some well deserved attention."
                else:
                    show sol neutral
                    sol "Ah, hello."
            "Steal the bell":
                "You don't think twice. You grab the bell and stuff it into your pocket."
                "The man behind the counter stares at you with a mix of disappointment and fear."
                if ready:
                    show sol irritated
                    sol "(Sigh.)"
                else:
                    show sol surprised
                    sol "....(I really hope you're not our new hire..)"
                    hide sol
                    $ stole_bell = True
                    jump desk_interact
            "Return": 
                "The man sits up in his chair, just about to greet you."
                "Unfortunately, you make a 180 degree turn and walk away before he can get a word in."
                jump choiceLoopLobby
    label after_desk_interact:
        show sol neutral
        sol "I assume you are here for the job? Although... I didn't get your name.."
        python:
            povname = renpy.input("What is your name?", length=32)
            povname = povname.strip()

            if not povname:
                povname = "Researcher"
            elif povname.lower() == "sol":
                same_name = True

        pov "You can call me [povname]."
        if same_name:
            show sol happy
            sol "Ha...? I guess we have the same name..!"
            menu rebel:
                "There can only be one.":
                    show sol surprised
                    sol "What?"
                    python:
                        sol = renpy.input("Rename this man.", length=32)
                        sol = sol.strip()

                        if not sol:
                            sol = "Sol"
                    if sol.lower() == "sol":
                        sol "NONONONO-"
                        show sol neutral
                        sol "Oh, you didn't go through with it."
                        show sol happy
                        sol "Ha..! Great. Thank you."
                    else:
                        sol "NONONONONONO...."
                        show sol irritated
                        sol "And you've already done it..."
                        sol "OK THEN. GREAT."
                "Haha, yeah!!!":
                    "This is going to get confusing."

        sol "Hm, well... Nice to meet you, [povname]."
        show sol neutral
        sol "Now, we should begin testing."
        menu proceed1:
            # add menu here to get to know character or to proceed
            "Okay":
                jump before_hallways
            "Hold on...":
                pov "I still want to look around."
                show sol neutral
                sol "Ah, sure, sure. Come back here when you're ready."
                $ ready = True
                hide sol
                jump choiceLoopLobby

    label chairs:
        "You see three chairs in the corner, ominously placed in a circle."
        menu chair_options:
            set menuset
            "What will you do?"

            "Sit down in the shadowed chair.":
                "You decide to sit down in the chair bathed in darkness."
                "You feel like a true lone wolf."
                "+1 AURA!"
                "....Just kidding."
                jump chair_options
            "Kick over the chairs":
                "You kick over the chairs in rebellion!"
                with vpunch
                "HELL YEAH!!!!"
                "..."
                "You quietly set them back up. The weight of your actions is too much!"
                jump chair_options
            "Take a chair.":
                "You decide to take a seat."
                "+1 Chair!"
                "....It's too heavy to carry around with you."
                "-1 Chair!"
                jump chair_options
            "Return":
                jump choiceLoopLobby
        jump choiceLoopLobby
    label posters:
        "You see three posters."
        "One explains the rules of this place, one is a Hangin In There cat poster, and the third one has some strange man on it."
        menu poster_interact:
            set menuset
            "What will you do?"
            "Examine Poster 1":
                "It's a list of the rules of this place."
                "1. Don't sue us. 2. Ignore any problems that you run into. 3. Love the company! Buy our merch today!"
                jump poster_interact
            "Examine Poster 2":
                "It's a cat clinging on to some kind of horizontal pole. Text reads 'Hang' in there!' You feel rather inspired."
                jump poster_interact
            "Examine Poster 3":
                "It's some strange man posed in the darkness with bold red text on the bottom of the poster reading 'YOUR SUPERIORS ARE WATCHING.'"
                "..It's kind of tacky."
                jump poster_interact
            "Return":
                jump choiceLoopLobby

    label before_hallways:
        show sol happy 
        sol "Well! Let's get going!"
        "He motions for you to follow as he dashes away through the door."
        "Reluctantly, you decide to follow him."
        jump hallways
        with fade

    label hallways: 
        scene hallways
        "You enter into the hallways."
        "It's rather dark (and maybe a little intimidating). You get the feeling you don't want to be caught alone here."
        show sol neutral
        sol "SO. It's your first day. I'm going to start you off with something easy."

    # This ends the game.

    return
