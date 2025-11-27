# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# character defines
define sol = Character("Sol")
define pov = Character("[povname]")

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
default defend = True
# Filter Events
default banned = ["fuck","shit","cunt","fucker","pussy","asshole","ass","asshole","fartface","piss",
"idiot","vag","vagina","penis","faggot","nigga","nigger"]
default silly = ["idiot","idiotface","fart","poo","pp","poop","pee","fartface","dummy","dumb","stupid","loser"]

# Player stats
default player_max_hp = 100
default player_hp = player_max_hp

# Enemy stats
default enemy_max_hp = 50
default enemy_hp = enemy_max_hp


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
            sol "Ah.. Not going to tell me? That's fine."
            sol "I'll just call you... Researcher!"
            povname "..."
            "You suppose you are fine with this name."
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
                show sol sad
                sol "Uh- I'm sorry, really sorry, but you... can't leave."
                sol "Part of the ahaha, well, secrecy thing.. of the facility."
                show sol neutral
                sol "I promise it isn't as bad as it seems. Maybe we can work something out later? I'll talk to someone."
                jump sol_interact
            "Let's begin work":
                sol "Ah! Yes, we should..."
                jump before_hallways
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
        "You enter the hallways alone."
        "It's rather dark (and maybe a little intimidating), but you'll manage. You have a keycard, after all."

    label anomaly1:
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
                show sol surprised
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

    label anomaly2:
        scene anomaly2
        while player_hp > 0:

            menu:
                # Player Turn
                "Attack":
                    $ enemy_hp -= 11
                    "You strike at the enemy. Enemy HP: [enemy_hp]"
                    if enemy_hp <= 0:
                        "The enemy falls to the ground, wires sparking."
                        "They glare at you as their body falls apart."
                        jump combat_win
                "Defend":
                    $ defend = True
                    "You grit your teeth and hold your arms in front of your face."
            # Enemy Turn
            if defend:
                $ player_hp -= 6
                "Wires slash and hack at your sides. You lost 6 HP! Remaining: [player_hp]"
            else: 
                $ player_hp -= 11
                "Electricity strikes your temples. You lost 11 HP! Remaining: [player_hp]"

    label combat_win:
        scene anomaly2
        "You won..."

    # This ends the game.

    return
