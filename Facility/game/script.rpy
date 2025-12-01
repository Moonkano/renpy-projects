# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# character defines
define sol = Character("Sol")
define pov = Character("[povname]")
define anomaly1 = Character("???")

# event variables
default menuset = set()
#Plant events
default pet_plant = False
default ate_plant = False
default flirt_plant = False
default ate_pot = False
# Desk Events
default ready = False
default stole_bell = False
default door_rejected = False
default distracted_idea = False
default keycard = False
default distracted = False
# Poster Events
default poster1_interact = False
default poster2_interact = False
default poster3_interact = False
# Name Events
default same_name = False
default s_silly_name = False
default s_banned_name = False
default silly_name =False
default banned_name =False
# Combat events
default defend = False
default player_current = 0
default enemy_chosen = 0
default i = 0
# Filter Events
default banned = ["fuck","shit","cunt","fucker","pussy","asshole","ass","asshole","fartface","piss",
"idiot","vag","vagina","penis","faggot","nigga","nigger", "bitch", "queef",""]
default silly = ["idiot","idiotface","fart","poo","pp","poop","pee","fartface","dummy","dumb","stupid","loser","gay","homophobic","yaoi"]

# Player stats
default player_max_hp = 10
default player_hp = player_max_hp
default player_attack_value = 0

# researcher stats
default player2_max_hp = 15
default player2_hp = player2_max_hp
default defend2 = False

# Enemy stats
default enemy_max_hp = 50
default enemy_hp = enemy_max_hp
default enemy_attack_value = 0

# Animations
image sol idle:
    "images/sol_idle1.png"
    pause 0.25
    "images/sol_idle2.png"
    pause 0.25
    "images/sol_idle3.png"
    pause 0.25
    "images/sol_idle4.png"
    pause 0.25
    "images/sol_idle5.png"
    pause 0.25
    repeat
image sol attack:
    "images/sol_attack1.png"
    pause 0.25
    "images/sol_attack2.png"
    pause 0.5
    "sol idle"
image sol hurt: 
    "images/sol_hurt1.png"
    pause 1
    "sol idle"
image wires:
    "images/anomalyfight1Wires.png"

image anomaly1 idle:
    "images/anomaly1_idle1.png"
    pause 0.16
    "images/anomaly1_idle2.png"
    pause 0.16
    "images/anomaly1_idle3.png"
    pause 0.16
    "images/anomaly1_idle4.png"
    pause 0.16
    "images/anomaly1_idle5.png"
    pause 0.16
    "images/anomaly1_idle6.png"
    pause 0.16
    repeat

image anomaly1 attack:
    "images/anomaly1_attack1.png"
    pause 0.16
    "images/anomaly1_attack2.png"
    pause 0.16
    "images/anomaly1_attack3.png"
    pause 0.16
    "images/anomaly1_attack4.png"
    pause 0.16
    "images/anomaly1_attack5.png"
    pause 0.16
    "images/anomaly1_attack6.png"
    pause 0.16
    "anomaly1 idle"

image researcher idle:
    "images/researcher_idle1.png"
    pause 0.3
    "images/researcher_idle2.png"
    pause 0.3
    "images/researcher_idle3.png"
    pause 0.3
    "images/researcher_idle4.png"
    pause 0.3
    "images/researcher_idle5.png"
    pause 0.3
    repeat
image researcher attack:
    "images/researcher_attack1.png"
    pause 0.25
    "images/researcher_attack2.png"
    pause 0.5
    "researcher idle"

image researcher hurt:
    "images/researcher_hurt.png"
    pause 0.75
    "researcher idle" 
image anomaly1 hurt:
    "images/anomaly_hurt.png"
    pause 0.75
    "anomaly1 idle"

#Camera positioning

# number generator
default d2 = 0
default d4 = 0
default d6 = 0
default d10 = 0
default d20 = 0



label sol_turn:
    
    camera:
        subpixel True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 9.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    show wall:
        subpixel True matrixtransform ScaleMatrix(1.0, 2.28, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    show floor:
        subpixel True matrixtransform ScaleMatrix(1.81, 0.96, 3.04)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(81.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    show sol idle:
        subpixel True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(-216.0, 0.0, -792.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    show anomaly1 idle:
        subpixel True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(1152.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    show researcher idle:
        subpixel True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(-225.0, 0.0, -171.0)*OffsetMatrix(0.0, 0.0, 0.0) 


    return


label researcher_turn:
    camera:
        subpixel True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 9.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    show wall:
        subpixel True matrixtransform ScaleMatrix(1.0, 2.28, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    show floor:
        subpixel True matrixtransform ScaleMatrix(1.81, 0.96, 3.04)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(81.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    show anomaly1 idle:
        subpixel True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(1152.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    show researcher idle:
        subpixel True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(-225.0, 0.0, -171.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    show sol idle:
        subpixel True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(-2700.0, 0.0, -792.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    return

label researcher_down:
    
    show researcher idle:
        subpixel True xpos -0.2 
    show researcher_down:
        subpixel True zoom 0.94 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(-126.0, 0.0, -108.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    return
label sol_down:
    
    show sol idle:
        subpixel True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(-2358.0, 0.0, -792.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    show sol_down:
        subpixel True zoom 0.83 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(-135.0, 0.0, -702.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    return
label evil_sol:
    
    window auto hide
    show sol neutral:
        subpixel True 
        matrixtransform ScaleMatrix(1.784313725490196, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.19607843137254902, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 0.50 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        linear 2.04 matrixtransform ScaleMatrix(5.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(-15.0, 1.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    with Pause(2.64)
    show sol neutral:
        matrixtransform ScaleMatrix(5.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(-15.0, 1.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    window auto show

    return
label sol_fight:

    return
label anomaly1_fight:
    
    return
label anomaly1_fight2:
    return



label researcher_fight:
    return

# Random Number Generator
label dice_roll:
    $ d2 = renpy.random.randint(1, 2)
    $ d4 = renpy.random.randint(1, 4)
    $ d6 = renpy.random.randint(1, 6)
    $ d10 = renpy.random.randint(1, 10)
    $ d20 = renpy.random.randint(1, 20)
    return

label anomaly1_heal:
    return 




# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene lobby
    with fade
    play music lounge loop

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
            
            "Pet the plant" if ate_plant == False:
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
            "Flirt with the plant" if ate_plant == False: 
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
            if ate_plant == True:
                "You leave the pot alone."
            elif ate_pot == True:
                "You walk away from the mess you've caused."
            jump choiceLoopLobby
    
    label door:
        camera:
            perspective True
        
        if distracted:
            "Quickly, you open the door and dash through while he is still distracted."
            jump hallways2
        elif door_rejected:
            "You try again to open the door, but are met with the same response as last time."
            "Maybe if he were distracted..."
            "Either way, you leave the door alone."
            $ distracted_idea = True
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
                    sol ".... Are you really going to keep the bell?"
                    sol "Just... come with me."
                    jump before_hallways
                else:
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
                    hide sol
                    $ stole_bell = True
                    jump desk_interact
                else:
                    show sol nervous
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
            elif povname.lower() in banned:
                s_banned_name = True
                while povname.lower() in banned:
                    povname = renpy.input("What is your name?", length=32)
                    povname = povname.strip()
            elif povname.lower() in silly:
                s_silly_name = True

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
                        elif sol.lower() in banned:
                            banned_name = True
                            sol = "Sol"
                        elif sol.lower() in silly:
                            silly_name = True
                    if banned_name:
                        show sol exasperated
                        sol "NO!!! YOU WILL NOT BE CALLING ME THAT! NO. THANK. YOU.!!!"
                        sol "ANYWAY.."
                    elif silly_name:
                        show sol irritated
                        sol "Please. Don't call me that."
                        "You decide to call him that anyway."
                    elif sol.lower() == "sol":
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
        elif povname == "Researcher":
            show sol neutral
            sol "Well... all right. Nice to meet you, Reece Earcher."
            "That's not what you told him."
        elif s_silly_name:
            show sol irritated
            sol "..."
            sol "....OK! Sure. I guess I can call you that."
        
        show sol neutral
        sol "Hm, well... Nice to meet you, [povname]."
        menu sol_interact:
            set menuset
            "He taps his fingers on the desk, glancing towards the door."

            "Who are you?":
                sol "Ah, I forgot to introduce myself! I am Sol, and I am an intern at this place."
                sol "Usually you'd have someone better showing you around, but.. they're busy right now."
                show sol happy
                sol "Maybe you'll meet them later?"
                jump sol_interact
            "What is this place?":
                sol "Oh!! Welcome to.... drumroll please... The Facility!"
                sol "We store all kinds of anomalies here- Uhm, right- anomalies are.. dangerous creatures or objects."
                show sol surprised
                sol "OR NOT DANGEROUS! Not all of them are dangerous!"
                show sol happy
                sol "Anyway, we experiment on said anomalies here so that we can learn more about them- and keep them contained easier."
                jump sol_interact
            "What job am I here for?":
                sol "I'm surprised that they didn't tell you before... Uhm, well, you're being hired as a researcher!"
                sol "You'll be experimenting on anomalies, taking observations, and just.. you know, doing paperwork."
                jump sol_interact
            "What are you?":
                show sol irritated
                sol "Rude."
                show sol happy
                sol "I'm just messing with you. Though, I am unsure myself... Sorry."
                jump sol_interact
            "I'm leaving.":
                sol "..."
                show sol nervous
                sol "Uh- I'm sorry, really sorry, but you... can't leave."
                sol "Part of the ahaha, well, secrecy thing.. of the facility."
                show sol neutral
                sol "I promise it isn't as bad as it seems. Maybe we can work something out later? I'll talk to someone."
                jump sol_interact
            "Let's begin work":
                sol "Ah! Yes, we should..."
                jump before_hallways
            "Return":
                show sol neutral
                sol "Oh... Goodbye, then."
                jump choiceLoopLobby
            "LOOK BEHIND YOU!" if distracted_idea:
                "You shout and point behind him. He turns his back to you, shocked."
                show sol surprised
                sol "HUH!?"
                menu keycard:

                    "You see his keycard on his belt. Take it?"

                    "Take it":
                        "You take his keycard while he's distracted."
                        $ keycard = True
                        "He looks back towards you, confused."
                        "You tell him it was just a prank"
                        show sol neutral
                        "...Ah.. Ha, got me good??? I guess."

                        menu distract:
                            "Distract Him":
                                $ distracted = True
                                "You tell him that you saw someone suspicious outside, muttering something about planning to break in."
                                show sol surprised
                                sol "What!? Wait right here, I have this handled."
                                "He vaults over the desk and books it towards the door."
                                hide sol
                                "You walk away."
                                jump choiceLoopLobby
                            "Return the Keycard":
                                $ keycard = False
                                show sol surprised
                                sol "How did you-"
                                show sol sad
                                sol "Nevermind, thank you for returning it to me. I won't let my guard down again."
                    "Do not":
                        "You decide not to take his keycard."
                        "He looks back towards you, confused."
                        "You tell him it was just a prank."
                        show sol neutral
                        "...Ah.. Ha, got me good??? I guess."
                        jump sol_interact
        sol "Now, we should begin testing."
        menu proceed1:
            # add menu here to get to know character or to proceed
            "Let's go":
                jump before_hallways
            "Not yet...":
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
            "What will you do?"
            "Examine Poster 1" if not poster1_interact:
                "It's a list of the rules of this place."
                "1. Don't sue us. 2. Ignore any problems that you run into. 3. Love the company! Buy our merch today!"
                $ poster1_interact = True
                jump poster_interact
            "Examine Poster 2" if not poster2_interact:
                "It's a cat clinging on to some kind of horizontal pole. Text reads 'Hang' in there!' You feel rather inspired."
                $ poster2_interact = True
                jump poster_interact
            "Examine Poster 3" if not poster3_interact:
                "It's some strange man posed in the darkness with bold red text on the bottom of the poster reading 'YOUR SUPERIORS ARE WATCHING.'"
                "..It's kind of tacky."
                $ poster3_interact = True
                jump poster_interact
            "Return":
                jump choiceLoopLobby

    label before_hallways:
        show sol neutral 
        sol "Well! Let's get going!"
        "He motions for you to follow as he dashes away through the door."
        "Reluctantly, you decide to follow him."
        jump hallways
        with fade

    label hallways: 
        play music something_is_wrong loop
        scene hallways
        "You enter into the hallways."
        "It's rather dark (and maybe a little intimidating). You get the feeling you don't want to be caught alone here."
        show sol neutral
        sol "SO. It's your first day. I'm going to start you off with something easy."
        "He scans the names stamped next to the doors as you two continue walking. He stops suddenly, and you nearly walk into him."
        sol "...Like this one!"
        "Pointing dramatically to the left, he scans his keycard and opens it."
        sol "After you!!"
        "You enter the room."
        hide sol
        jump anomaly1
    
    label hallways2:
        scene hallways
        play music something_is_wrong loop
        "You enter the hallways alone."
        "It's rather dark (and maybe a little intimidating), but you'll manage. You have a keycard, after all."
        jump anomaly1_alone

    label anomaly1_alone:
        scene anomalyfake
        "You enter the cell. There's a person standing ahead of you with a small smile on their face."
        anomaly1 "Hello there. You ... are alone?"
        menu alone:
            "Yes":
                pov "That's right."
            "No":
                pov "No, I'm not."
        jump anomalyfight_alone

    label anomaly1:
        camera:
            perspective True
        scene anomaly1
        "You step through the door and are met with static hanging heavy in the air. Your hair stands on end."
        show sol happy
        sol "Welcome to your first anomaly. Aren't you excited?"
        "He walks in behind you. Despite his happy-go-lucky demeanor, you notice that he won't take his eyes off the anomaly."
        menu anomaly1q:
            sol "Do you have any questions?"
            set menuset 

            "What am I supposed to do?":
                sol "..."
                show sol nervous
                sol "Anyway."
                jump anomaly1q
            "What does this anomaly do?":
                show sol happy
                sol "I'm so glad you asked. (Because I've spent the last two hours memorizing the file while I was waiting for you to show up..)"
                sol "..."
                jump anomaly1q
            "Is this safe?":
                show sol surprised
                sol "Safe?"
                show sol happy
                sol "Yeah! I think so.. Nobody's ever been harmed by it. Does that reassure you?"
                sol "Though... it is only ever active when you're alone. So.. You, uhm! Might have to do this one alone."
                sol "BUT AGAIN! It is totally safe."
                jump anomaly1q
            "No":
                sol "Great! Glad to hear it."
                "He shoots fingerguns at you, does a little spin, then exits the room. You hear the door lock with a click!"
                hide sol with moveoutright
                "You are left alone with this anomaly."

        "You stare at the old TV screen. It feels awfully foreboding for how harmless it apparently is."
        "After a minute of standing around wondering what to do, you decide to approach the device." with fade
        "Static flickers across the screen! You hear something whisper to you through the onslaught of garbage noise."
        anomaly1 "H-- Help. H--E--LP me. Y0u have to HELP Me. H3 Deceives Y0u. A lying snake, he is."
        menu anomaly1Plea:
            "..."

            "Who is lying to me?":
                anomaly1 "The snake who has trapped you here. Sol, as he calls hims--elf."
                anomaly1 "Aren't you angry? He trapped you here. Don't you have anyone to go back to?"
                pov "..."
                jump anomaly1Plea
            "How do I help you?":
                anomaly1 "All you have to do.. Is change my channel to Channel 9999."
                anomaly1 "1nnocent, right? Harmless, even. Then, I will be free."
                menu channel:
                    "What will you do?"

                    "Change the channel":
                        pov "...All right. Fine."
                        "You grab onto the TV's knob and twist it all the way around until you hear a Click!"
                        "Channel 9999. A recording begins to play. You hear an unknown voice speak through a muffled microphone."
                        "LOOP 10: The day keeps restarting. I cannot figure out why this is--"
                        "The channel cuts out, and the tv begins to shake!" with vpunch
                    "Do not":
                        pov "No thanks."
                        "You step away from the anomaly and start to walk away."
                        "Static roars from the screen behind you! Something is happening!"
                "The door is flung open as your guide runs to protect you."
                jump anomalyfight

            "What do I get out of this?":
                anomaly1 "I can make you powerful beyond your dreams, and I can get you out of here."
                anomaly1 "...Isn't that all you want? Freedom? Or.... No, I know what you want."
                anomaly1 "You want answers. Ha. Ha. Ha. I can give you those."
                jump anomaly1Plea
    label anomalyfight_alone:
        play music electric_chair loop
        show screen hp_bars1v1
        scene wall
        show floor
        show wires
        show anomaly1 idle
        show researcher idle
        $ player2_max_hp = 30
        $ player2_hp = 30
        camera: 
            perspective True

        while enemy_hp > 0 and (player2_hp > 0):
            call researcher_turn
            call dice_roll
            while i < 1:
                menu:
                    # researcher turn
                    "It's your turn."

                    "Light Attack" if player2_hp > 0:
                        show researcher attack
                        if enemy_hp <= 0:
                            "The enemy falls to the ground, wires sparking."
                            "They glare at you as their body falls apart."
                            jump combat_win
                        elif d10 >= 8:
                            call researcher_fight
                            show anomaly1 hurt
                            $ player_attack_value = d4+d6
                            $ enemy_hp -= player_attack_value
                            "CRITICAL HIT."
                            $ i += 1
                        else: 
                            call researcher_fight
                            $ enemy_hp -= d4
                            "[d4] DAMAGE."
                            $ i += 1
                    "Heavy attack" if player2_hp > 0:
                        show researcher attack
                        show anomaly1 hurt
                        call researcher_fight
                        if enemy_hp <= 0:
                            "The enemy falls to the ground, wires sparking."
                            "They glare at you as their body falls apart."
                            jump combat_win
                        if d10 >= 9:
                            $ player_attack_value = (d6 + d4)*2
                            $ enemy_hp -= player_attack_value
                            $ i += 1
                            "CRITICAL HIT."
                        elif d10 >= 5:
                            $ player_attack_value = d6 + 2
                            $ enemy_hp -= player_attack_value
                            $ i += 1
                            "YOU HIT."
                        else:
                            "YOU MISS."
                            $ i += 1
                    "Defend" if player2_hp > 0:
                        $ defend = True
                        "You grit your teeth and hold your arms in front of your face."
                        $ i += 1
            call dice_roll
            # Enemy Turn

            $ enemy_chosen = 2
            if enemy_chosen == 2 and defend:
                show researcher hurt
                show anomaly1 attack
                call anomaly1_fight2
                $ player2_hp -=d10/2
                "Wires lash at your sides."
                $ defend = False
                $ i = 0
            elif enemy_chosen == 2:
                show researcher hurt
                show anomaly1 attack
                if d20 >= 19:
                    call anomaly1_fight2
                    $ player2_hp -= d10
                    "Y0U'RE H1T."
                    $ i = 0
                elif d20 <=2:
                    $ enemy_hp += d4
                    if enemy_hp < enemy_max_hp:
                        "THE WIRES BIND UP OLD WOUNDS."
                        $ i = 0
                    else:
                        $enemy_hp = enemy_max_hp
                        "THE ENEMY LOOKS GOOD AS NEW."
                        $ i = 0
                else:
                    call anomaly1_fight2
                    $ player2_hp -= d4
                    "STATIC COURSES THROUGH YOUR VEINS."
                    $ i = 0
    if enemy_hp <= 0:
        jump combat_win
    else:
        jump combat_lose


    label anomalyfight:
        play music electric_chair loop
        show screen hp_bars1v1
        scene wall
        show floor
        show sol idle
        show wires
        show anomaly1 idle
        show researcher idle
        camera: 
            perspective True

        while enemy_hp > 0 and (player_hp > 0 or player2_hp > 0):
            call sol_turn
            call dice_roll
            while i < 2:
                if player2_hp <= 0:
                    show researcher_down
                    call researcher_down
                    $ player_current = 1
                    $ i = 1
                elif player_hp <= 0:
                    show researcher idle
                    show sol_down
                    call sol_down
                    $ player_current = 0
                    $ i = 1
                menu:
                    # researcher turn
                    "It's your turn."

                    "Light Attack" if player2_hp > 0 and player_current == 0:
                        show researcher attack
                        if enemy_hp <= 0:
                            "The enemy falls to the ground, wires sparking."
                            "They glare at you as their body falls apart."
                            jump combat_win
                        elif d10 >= 8:
                            call researcher_fight
                            show anomaly1 hurt
                            $ player_attack_value = d4+d6
                            $ enemy_hp -= player_attack_value
                            "CRITICAL HIT."
                            if player2_hp > 0:
                                $ player_current += 1
                            $ i += 1
                        else: 
                            call researcher_fight
                            $ enemy_hp -= d4
                            "[d4] DAMAGE."
                            if player2_hp > 0:
                                $ player_current += 1
                            $ i += 1
                    "Heavy attack" if player2_hp > 0 and player_current == 0:
                        show researcher attack
                        show anomaly1 hurt
                        call researcher_fight
                        if enemy_hp <= 0:
                            "The enemy falls to the ground, wires sparking."
                            "They glare at you as their body falls apart."
                            jump combat_win
                        if d10 >= 9:
                            $ player_attack_value = (d6 + d4)*2
                            $ enemy_hp -= player_attack_value
                            if player2_hp > 0:
                                $ player_current += 1
                            $ i += 1
                            "CRITICAL HIT."
                        elif d10 >= 5:
                            $ player_attack_value = d6 + 2
                            $ enemy_hp -= player_attack_value
                            if player2_hp > 0:
                                $ player_current += 1
                            $ i += 1
                            "YOU HIT."
                        else:
                            "YOU MISS."
                            if player2_hp > 0:
                                $ player_current += 1
                            $ i += 1
                    "Defend" if player2_hp > 0 and player_current == 0:
                        $ defend = True
                        "You grit your teeth and hold your arms in front of your face."
                        if player2_hp > 0:
                                $ player_current += 1
                        $ i += 1
                    

                    # sol's turn
                    "Light Attack" if player_hp > 0 and player_current == 1:
                        call sol_turn
                        show sol attack
                        show anomaly1 hurt
                        call sol_fight
                        if enemy_hp <= 0:
                            "The enemy falls to the ground, wires sparking."
                            "They glare at you as their body falls apart."
                            jump combat_win
                        elif d10 >= 8:
                            $ player_attack_value = d4+d6
                            $ enemy_hp -= player_attack_value
                            "CRITICAL HIT."
                            $ player_current -=1
                            $ i += 1
                        else: 
                            $ enemy_hp -= d4
                            "[d4] DAMAGE."
                            $ player_current -=1
                            $ i+= 1
                    "Heavy attack" if player_hp > 0 and player_current == 1:
                        call sol_turn
                        show sol attack
                        show anomaly1 hurt
                        call sol_fight
                        if enemy_hp <= 0:
                            "The enemy falls to the ground, wires sparking."
                            "They glare at you as their body falls apart."
                        if d10 >= 9:
                            $ player_attack_value = (d6 + d4)*2
                            $ enemy_hp -= player_attack_value
                            "CRITICAL HIT."
                            $ player_current -= 1
                            $ i+= 1
                        elif d10 >= 5:
                            $ player_attack_value = d6 + 2
                            $ enemy_hp -= player_attack_value
                            "YOU HIT."
                            $ player_current -= 1
                            $ i+=1
                        else:
                            "YOU MISS."
                            $ player_current -=1
                            $ i+=1
                    "Defend" if player_hp > 0 and player_current == 1:
                        call sol_turn
                        $ defend2 = True
                        "He grits his teeth and holds his hands up in front of his face."
                        $ player_current -=1
                        $ i+=1
            call dice_roll
            # Enemy Turn

            $ enemy_chosen = d2
            if player2_hp <= 0:
                $ enemy_chosen = 1
            elif player_hp <= 0:
                $ enemy_chosen = 2

            if enemy_chosen == 1 and defend:
                show sol hurt
                show anomaly1 attack
                call anomaly1_fight
                $ enemy_attack_value = d10/2
                $ player_hp -= enemy_attack_value
                "Wires slash and hack at your sides."
                $ i = 0
                $ defend = False
            elif enemy_chosen == 1: 
                show sol hurt
                show anomaly1 attack
                if d20 >= 19:
                    call anomaly1_fight
                    $ player_hp -= d10
                    "Y0U'RE H1T."
                    $ i = 0
                elif d20 <=2:
                    call anomaly1_heal
                    $ enemy_hp += d4
                    if enemy_hp < enemy_max_hp:
                        "THE WIRES BIND UP OLD WOUNDS."
                        $ i = 0
                    else:
                        call anomaly1_heal
                        $enemy_hp = enemy_max_hp
                        "THE ENEMY LOOKS GOOD AS NEW."
                        $ i = 0
                else:
                    call anomaly1_fight
                    $ player_hp -= d4
                    "ELECTRICITY STRIKES YOUR TEMPLES."
                    $ i = 0
            elif enemy_chosen == 2 and defend:
                show researcher hurt
                show anomaly1 attack
                call anomaly1_fight2
                $ player2_hp -=d10/2
                "Wires lash at your sides."
                $ defend = False
                $ i = 0
            elif enemy_chosen == 2:
                show researcher hurt
                show anomaly1 attack
                if d20 >= 19:
                    call anomaly1_fight2
                    $ player2_hp -= d10
                    "Y0U'RE H1T."
                    $ i = 0
                elif d20 <=2:
                    $ enemy_hp += d4
                    if enemy_hp < enemy_max_hp:
                        "THE WIRES BIND UP OLD WOUNDS."
                        $ i = 0
                    else:
                        $enemy_hp = enemy_max_hp
                        "THE ENEMY LOOKS GOOD AS NEW."
                        $ i = 0
                else:
                    call anomaly1_fight2
                    $ player2_hp -= d4
                    "STATIC COURSES THROUGH YOUR VEINS."
                    $ i = 0
    if enemy_hp <= 0:
        label combat_win:
            hide screen hp_bars1v1
            scene anomaly2
            "You won..."
    else:
        label combat_lose:
            hide screen hp_bars1v1
            scene anomaly2
            play music get_up loop
            "You've lost."


    screen hp_bars1v1:

        vbox:
            spacing 20
            xalign 0.1
            yalign 0.0
            xmaximum 600
            text "[povname]"
            bar value player2_hp range player2_max_hp
        vbox:
            spacing 20
            xalign 0.9
            yalign 0.0
            xmaximum 600
            text "???"
            bar value enemy_hp range enemy_max_hp
        vbox:
            spacing 20
            xalign 0.1
            yalign 0.1
            xmaximum 600
            text "[sol]"
            bar value player_hp range player_max_hp

    # This ends the game.

    return
