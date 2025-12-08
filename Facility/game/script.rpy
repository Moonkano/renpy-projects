
#quick time event 
default timer_range = 0
default timer_jump = 0
default time = 0
default counter = 0
default miss1 = False
default miss2 = False
default miss3 = False

# minigame quick time event variables
transform alpha_dissolve:
    alpha 0.0
    linear 0.5 alpha 0.5
    on hide:
        linear 0.5 alpha 0.0
    # fades the bar in and out    

screen countdown:
    timer 0.01 repeat True action If(time > 0, true=SetVariable('time',time -0.01), false=[Hide('countdown'), Jump(timer_jump)])
    # the timer will decrease if there is more time than zero, and if there is no time left, the timer will be hidden and failstate will be moved to.

    bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve
    #this creates the timer bar! fades the bar in and out
return

# character defines
define sol = Character("Sol")
define pov = Character("[povname]")
define anomaly1 = Character("???")
define ash = Character("Ash Dweller")

# event variables
default menuset = set()
#Plant events
default pet_plant = False
default ate_plant = False
default flirt_plant = False
default ate_pot = False
default plantus = False
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
default plantus_alive_name = False
# Combat events
default defend = False
default player_current = 0
default enemy_chosen = 0
default i = 0
# Filter Events
default banned = ["fuck","shit","cunt","fucker","pussy","asshole","ass","asshole","fartface","piss",
"idiot","vag","vagina","penis","faggot", "bitch", "queef","boobs","boob","breast","booby","boobies"]
default silly = ["idiot","idiotface","fart","poo","pp","poop","pee","fartface","dummy","dumb","stupid","loser","gay","homophobic","yaoi"]

# sol interact events
default name_learned = False
default location_learned = False
default job_learned = False
default what_areyou = False
default tried_leaving = False

#chair interact events
default sat_shadowed = False
default took_seat = False
default kicked_chairs = False

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

#minigame event
default rprogression1 = False
default rprogression2 = False
default rprogression3 = False
default rprogression4 = False
default rprogression5 = False

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

label ash_interactcam:
    
    show ashclockin:
        subpixel True zoom 2.03 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 216.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        
    show ashclockin:
        subpixel True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, -63.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 



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
# minigame quicktime setup/function

# the parameters are as follows:

# - amount of time given
# - total amount of time
# - timer decreasing interval
# - the key input to hit in the quick time event
# - the x alignment of the bar/box
# - the y alignment of the bar/box

label qte_setup(time_start, time_max, interval, trigger_key, x_align, y_align):

    $ time_start = time_start
    $ time_max = time_max
    $ interval = interval
    $ trigger_key = trigger_key
    $ x_align = x_align
    $ y_align = y_align

    call screen qte_simple
    #calls you to give an input

    $ cont = _return
    # 1 if key was hit in time, 0 if key was not
    if cont == 0 and miss2:
        $ miss3 = True
    elif cont == 0 and miss1:
        $ miss2 = True
        scene anomaly_qte3
    elif cont == 0:
        $ miss1 = True
        scene anomaly_qte2
    return
screen qte_simple:
    #key input for the qte

    timer interval repeat True action If(time_start > 0.0, true=SetVariable('time_start',time_start-interval), false=[Return(0), Hide('qte_simple')])
    # timer, using vairables from the qte setup
    # false is the condition if the timer runs out
    # so bascially if we have time left, reduce the timer, if not, you ran out of time and failed

    key trigger_key action (Return(1))
    # detects if you hit the key or not. if you didnt hit a key, it ends the qte event because it returned 0 not 1. 

    #this is just the ui stuff from here on out.

    vbox:
        xalign x_align
        yalign y_align
        spacing 25

        text trigger_key.upper():
            xalign 0.5
            color "#b31c1c"
            size 42
            #outlines [(2, #000000,0,0)]
            # this text shows what key to press
        
        bar:
            value time_start
            range time_max
            xalign 0.5
            xmaximum 300
            if time_start < (time_max * 0.25):
                left_bar "#f00"
                #once timer is less than 25%, bar turns red

# The game starts here.
label start:
    scene researcher_intro with fade
    "Your name is ****. You worked at **** ****** for three years until the sudden passing of *****."
    "You were aimless until you were contacted by *****. A job opportunity that would change your life, he told you."
    "You accepted because you had nothing to lose. And then everything went black."
    scene researcher_intro2 with fade
    "And now...."
label afterstart:

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

    "You have no idea where you are or what your name is."
    "It looks like some kind of lobby, so it can't be too dangerous."
    "Looking around, you notice some places of interest: the plant by the front desk, the front desk, the chairs, and the posters."
    menu choiceLoopLobby: 
        "Where should you go first?"

        "the plant":
            scene plantus_scene_bg
            jump plant
        "The Front Desk":
            scene desk_bg
            jump front_desk
        "The Chairs":
            jump chairs
        "The Posters":
            scene posters_scene_bg
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
                scene plantus_eaten_bg
                with fade
                "...????"
                "You stuffed the entire plant in your mouth."
                scene lobby
                jump plant_interact
            "Flirt with the plant" if ate_plant == False: 
                "You tell Plantus that you'd never leaf them for another."
                "Plantus blushes!"
                $ flirt_plant = True
                jump plant_interact
            "Eat the pot" if ate_plant:
                scene pot_eaten bg
                with fade
                "Within seconds, you have consumed the entire pot."
                "Are you proud of yourself?"
                $ ate_pot = True
                scene lobby
                jump choiceLoopLobby
            "Return":
                scene lobby
                jump choiceLoopLobby
        label after_plant:
            "You decide to leaf the plant alone."
            if ate_plant == True:
                "You leave the pot alone."
            elif ate_pot == True:
                "You walk away from the mess you've caused."
                scene lobby
            jump choiceLoopLobby
    
    label door:
        camera:
            perspective True
        scene door_bg
        
        if distracted:
            "Quickly, you open the door and dash through while he is still distracted."
            jump hallways2
        elif door_rejected:
            "You try again to open the door, but are met with the same response as last time."
            "Maybe if he were distracted..."
            "Either way, you leave the door alone."
            $ distracted_idea = True
            scene lobby
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
        scene lobby
        jump choiceLoopLobby

    label front_desk:
        "You walk over to the front desk."
        "There is a bell, and an odd looking man sitting behind the front desk.."
        menu desk_interact:
            "What will you do?"
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
                            scene lobby
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
            "Steal the bell" if stole_bell == False:
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
                scene lobby
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
            elif povname.lower() == "plantus" and ate_plant:
                plantus = True
            elif povname.lower() == "plantus":
                plantus_alive_name = True

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
                    elif sol == "plantus" and ate_plant:
                        sol "plantus? As- As in my pet plant that you ate? In front of me?"
                        show sol surprised
                        sol "......Are you saying that I'm NEXT???"
                    elif sol = "plantus":
                        show sol neutral
                        sol "As in... My pet plant?"
                        show sol happy
                        sol "...OK? I guess."
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
        elif plantus and ate_plant:
            show sol neutral
            sol "Did you... Name yourself after my beloved plant that you eat?"
            show sol irritated
            sol "WHAT IS WRONG WITH YOU???"
        elif plantus_alive_name:
            show sol neutral
            sol "...Ok. Plantus number 2. That's you. Got it."
        
        show sol neutral
        sol "Hm, well... Nice to meet you, [povname]."

        menu sol_interact:
            "He taps his fingers on the desk, glancing towards the door."

            "Who are you?":
                sol "Ah, I forgot to introduce myself! I am Sol, and I am an intern at this place."
                sol "Usually you'd have someone better showing you around, but.. they're busy right now."
                show sol happy
                sol "Maybe you'll meet them later?"
                $ name_learned = True
                jump sol_interact
            "What is this place?":
                sol "Oh!! Welcome to.... drumroll please... The Facility!"
                sol "We store all kinds of anomalies here- Uhm, right- anomalies are.. dangerous creatures or objects."
                show sol surprised
                sol "OR NOT DANGEROUS! Not all of them are dangerous!"
                show sol happy
                sol "Anyway, we experiment on said anomalies here so that we can learn more about them- and keep them contained easier."
                $ location_learned = True
                jump sol_interact
            "What job am I here for?":
                sol "I'm surprised that they didn't tell you before... Uhm, well, you're being hired as a researcher!"
                sol "You'll be experimenting on anomalies, taking observations, and just.. you know, doing paperwork."
                $ job_learned = True
                jump sol_interact
            "What are you?":
                show sol irritated
                sol "Rude."
                show sol happy
                sol "I'm just messing with you. Though, I am unsure myself... Sorry."
                $ what_areyou = True
                jump sol_interact
            "I'm leaving.":
                sol "..."
                show sol nervous
                sol "Uh- I'm sorry, really sorry, but you... can't leave."
                sol "Part of the ahaha, well, secrecy thing.. of the facility."
                show sol neutral
                sol "I promise it isn't as bad as it seems. Maybe we can work something out later? I'll talk to someone."
                "You ignore him and turn around, walking away. You're leaving whether he likes it or not."
                $ tried_leaving =  True
                hide sol
                jump ash_interact
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

    label ash_interact:
        camera:
            perspective True
        show ash neutral
        ash "Hey. You."
        "The man materializes before you and blocks your way to the door."
        hide ash neutral
        call ash_interactcam
        "You run away. (in fear.)"
        scene lobby
        jump sol_interact
    label chairs:
        scene chair_bg
        "You see three chairs in the corner, ominously placed in a circle."
        menu chair_options:
            "What will you do?"

            "Sit down in the shadowed chair." if sat_shadowed == False:
                "You decide to sit down in the chair bathed in darkness."
                "You feel like a true lone wolf."
                "+1 AURA!"
                "....Just kidding."
                $ sat_shadowed = True
                jump chair_options
            "Kick over the chairs" if kicked_chairs == False:
                "You kick over the chairs in rebellion!"
                with vpunch
                "HELL YEAH!!!!"
                $ kicked_chairs = True
                jump chair_options
            "Take a chair." if took_seat == False:
                "You decide to take a seat."
                "+1 Chair!"
                "....It's too heavy to carry around with you."
                "-1 Chair!"
                $ took_seat = True
                jump chair_options
            "Return":
                scene lobby
                jump choiceLoopLobby
        jump choiceLoopLobby
    label posters:
        "You see three posters."
        "One explains the rules of this place, one is a Hangin In There cat poster, and the third one has some strange man on it."
        menu poster_interact:
            "What will you do?"
            "Examine Poster 1" if not poster1_interact:
                "It's a list of the rules of this place."
                "You skim over the rules with great diligence. In a strange place like this, they might help keep you safe."
                "...Wait, you're not getting paid for this?"
                "On second thought, you think that you'll do as you please."
                $ poster1_interact = True
                jump poster_interact
            "Examine Poster 2" if not poster2_interact:
                "Hang in there? ...Or face physical and psychological harm?"
                "What's that supposed to mean? And how could they possibly determine whether you're hanging in there or not?"
                "You debate drawing a smiley face over your mask."
                $ poster2_interact = True
                jump poster_interact
            "Examine Poster 3" if not poster3_interact:
                "It'd be inspiring if the subject in the image didn't look like he was on his deathbed, but at least they're honest."
                "You really hope that you signed on as a scientist and not a subject, but you can't remember."
                "....Is any of this even legal?"
                $ poster3_interact = True
                jump poster_interact
            "Return":
                scene lobby
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
        "How long have they just been... waiting there and staring at the door?"
        anomaly1 "Hello there. You are alone, aren't you?"
        menu alone:
            "Yes":
                pov "That's right."
                anomaly1 "Fascinating. You are not a scientist that I recognize, either. Yet, you are dressed like one."
                anomaly1 "You must be new, then.... and exploring by yourself?"
                anomaly1 "There's a thin line between recklessness and bravery, my friend! Where do you think you fall?"
                anomaly1 "OH, oh, oh! But let's get to the important stuff! We don't have much time before someone notices you're here, do we?"
                anomaly1 "What do you need from me, [povname]?"
                menu reason1:
                    "What do you need?"

                    "Help me escape":
                        anomaly1 "What makes you think a prisoner knows anything about that, friend?"
                        anomaly1 "Ahahaha, ok, but, maybe I do know a few things."
                        anomaly1 "But first..."
                        "The stranger's form begins to shift before your eyes as the lights flicker in and out..!" with vpunch
                        jump anomaly_passive
                    "I don't need anything from you":
                        anomaly1 "..Ahaha? Then why did you come here?"
                        anomaly1 "Were you really just curious? Well! Here you are! Are you satisfied with what you found?"
                        anomaly1 "Had a good marvel at the cage that they stuck me in? Is it everything that you were expecting?"
                    "I thought this was the bathroom":
                        anomaly1 "You are mistaken, you silly little thing."
                        anomaly1 "You are in my containment unit. And you are all alone."
                        anomaly1 "And I... actually need something from you."
                "The lights flicker as the person in front of you begins to change shape-- morphing into something completely unrecognizable"
                anomaly1 "I need to take your form. When I have it, I can walk out of here as you."
                anomaly1 "So, please, be a good friend to me and stay still." with vpunch 
                jump anomalyfight_alone

            "No":
                pov "No, I'm not."
                "..."
                "I see! Thank you for being honest with me."
                "So, what are you doing here? Anomalies are dangerous, don't you know that? Even if you're in company."
                menu reason2:
                    set menuset
                    "Why are you here?"

                    "Why are you here?":
                        anomaly1 "Okay. I know this is hard for you, but I'm going to need you to use some context clues here, buddy."
                        anomaly1 "I am in a CELL. In a glorified JAIL for anomalies."
                        anomaly1 "..."
                        anomaly1 "Yeah, I'm just here out on a nice stroll."
                    "I want to escape":
                        anomaly1 "So you put yourself in a cell?"
                        "The static rumbles rythically, as though it is laughing."
                        anomaly1 "I jest! You want my help, don't you?"
                        anomaly1 "I can do just that! But first, you need to prove that you can be of use."
                        anomaly1 "{bt=5}It's only fair!{/bt}"
                        jump anomaly_passive
                    "I chose to be here":
                        anomaly1 "You... did? That's pretty stupid."
                        anomaly1 "You must want something out of this place? What is it? Power? Knowledge? Helping others?"
                        anomaly1 "Whatever it is... I think you're in over your head, buddy."
                        anomaly1 "But, hey. I just love the crazy dreamer type! if you're here to ask for my help, I'll see what I can do."
                        anomaly1 "Just, do something for me first, okay?"
                        "The stranger's form begins to shift before your eyes."
                        jump anomaly_passive
                    "I'm just curious":
                        anomaly1 "Yeah? You out on a little tour with whoever you're with?"
                        anomaly1 "I hope you're enjoying the view, sicko."
                        "There's a rumbly, staticky laugh."
                        anomaly1 "How interesting. But, you should know, you're on a leash as long as your need a guide."
                        anomaly1 "Real exploration begs that you unbind your chains and go free, living in the thrill of danger."
                        anomaly1 "Let me help you cut those chains, buddy. As a favor~"
                        "The stranger's form begins to shift right before your eyes."
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
                sol "You only need to gather some research on this anomaly- it's a new one, so! we.. don't have much yet."
                sol "Try asking it some questions. I think that's always a good way to learn more."
                show sol nervous
                "Ok, yes, I know it's a TV and can't talk back, but you never know...!"
                jump anomaly1q
            "What does this anomaly do?":
                show sol happy
                sol "I'm so glad you asked. (Because I've spent the last two hours memorizing the file while I was waiting for you to show up..)"
                sol "..."
                show sol nervous
                sol "I... I forgot everything. Here, just take a look at the file... (sigh)."
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
                        "{sc=10}LOOP 10: The day went as it always does. Continued efforts to prevent the loop have fail--{/sc}" 
                        "The channel cuts out, and the tv begins to shake! Wires slither out of it like snakes and its entire form begins to reconstruct itself." with vpunch
                    "Do not":
                        pov "No thanks."
                        "You step away from the anomaly and start to walk away."
                        "Static roars from the screen behind you. You feel something whizz past the side of your face."
                        "When you turn to look, you see a wire mere inches away from you that has come from the TV and embedded itself into the wall."
                        "There's no running from this."
                "The door is flung open as [sol] runs to protect you."
                jump anomalyfight

            "What do I get out of this?":
                anomaly1 "Selfish. I thought you were supposed to be an altruist, [povname]."
                "You stare back at it with disgust. The static crackles rythmically in almost a laugh."
                anomaly1 "No? Is my information that outdated..? Let me bring you a new reason, then."
                anomaly1 "I can get both of us out of here. You can go back to your own life."
                anomaly1 "{sc=2}Hell, I can even bring what you're missing back.{/sc}"
                jump anomaly1Plea
    label anomalyfight_alone:
        play music electric_chair loop
        show screen hp_bars2v1
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
        show screen hp_bars2v1
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
            hide screen hp_bars2v1
            scene anomaly2
            "You won..."
    else:
        label combat_lose:
            hide screen hp_bars2v1
            scene anomaly2
            play music get_up loop
            "You've lost."
    
    # this label will be jumping a lot between itself and quicktimemini depending on how many times the player messes up
    # i think i'll add some progression variables so it knows where to jump back
    # the player having their progress constantly reset would break immersion and make them angry methinks
    label anomaly_passive:
        scene anomaly_qte1

        "Prove your worth to me."
        "I will tell you a story. You must fill in the blanks when I trail off."
        "If you are wrong, you will suffer consequences. If you are correct, we may continue without issue."
        "Are you ready?"
        menu ready2:
            "Yes":
                "Then let us begin."
                jump progression1
            "No":
                "Very well then. You may take a look at the file one more time."
        label progression1:
            $ time = 3
            $ timer_range = 3
            $ timer_jump = 'quicktimemini'
            $ counter = 0
            $ miss1 = False
            $miss2 = False
            $miss3 = False

            "The story begins in a snowy winterland, carefully crafted, of pristine design; a flowery decoration of the labyrinth that a woman had found herself in."
            "Among the pretty lies, shallow beauty, and death that flowed from the glistening snow,"
            "She felt…"
            show screen countdown
            menu mprogression1:
                "Disgusted":
                    hide screen countdown
                    $ rprogression1 = True
                    $ rprogression2 = True
                    $ counter = 0
                    $ miss1 = False
                    $miss2 = False
                    $miss3 = False
                    jump progression2
                "Saddened":
                    hide screen countdown
                    $ counter = 0
                    $ miss1 = False
                    $ miss2 = False
                    $ miss3 = False
                    "Wrong."
                    $ rprogression1 = True
                    jump quicktimemini
                "Glad":
                    $ counter = 0
                    $ miss1 = False
                    $miss2 = False
                    $miss3 = False
                    hide screen countdown
                    "Wrong." 
                    $ rprogression1 = True
                    jump quicktimemini


        label progression2:
            $ counter = 0
            $ miss1 = False
            $miss2 = False
            $miss3 = False
            "...Disgusted. She sought to free herself from this maze, whether impossible or not."
            "The woman called out to the white coats and even the gods, and…"
            $ time = 3
            $ timer_range = 3
            show screen countdown
            menu mprogression2:

                "The white coats responded":
                    $ counter = 0
                    $ miss1 = False
                    $miss2 = False
                    $miss3 = False
                    hide screen countdown
                    "Wrong."
                    $ rprogression2 = True
                    jump quicktimemini
                "Nobody responded":
                    $ rprogression2 = True
                    $ rprogression3 = True
                    $ counter = 0
                    $ miss1 = False
                    $miss2 = False
                    $miss3 = False
                    jump progression3
                    hide screen countdown
                "The gods responded":
                    hide screen countdown
                    $ counter = 0
                    $ miss1 = False
                    $miss2 = False
                    $miss3 = False
                    "Wrong."
                    $ rprogression2 = True
                    jump quicktimemini

        label progression3:
            $ counter = 0
            $ miss1 = False
            $miss2 = False
            $miss3 = False
            "...Nobody responded. The sands of time continued their pour, and all remained the same for many years."
            "Searching, searching, and searching, there appeared to be no answer to her call."
            "So, she created her own, and she …."
            $ time = 3
            $ timer_range = 3
            show screen countdown
            menu mprogression3:

                "Accepted her fate":
                    $ counter = 0
                    $ miss1 = False
                    $miss2 = False
                    $miss3 = False
                    hide screen countdown
                    "Wrong."
                    $ rprogression3 = True
                    jump quicktimemini
                "Found her new form":
                    $ counter = 0
                    $ miss1 = False
                    $miss2 = False
                    $miss3 = False
                    $ rprogression3 = True
                    hide screen countdown
                    jump progression4
                "Sought vengeance":
                    $ counter = 0
                    $ miss1 = False
                    $miss2 = False
                    $miss3 = False
                    hide screen countdown
                    "Wrong."
                    jump quicktimemini

        label progression4:
            $ counter = 0
            $ miss1 = False
            $miss2 = False
            $miss3 = False
            "...Found new form. It started as metal hands, designed for greater precision even as age tore lines into one’s hands."
            "Then, it was an artificial liver that gave out from years of mistreatment."
            "Then, a metallic shell when age claimed what was left."
            "When all that remained was the heart…."

            $ time = 3
            $ timer_range = 3
            show screen countdown
            menu mprogression4:

                "It was incased, to protect it":
                    $ counter = 0
                    $ miss1 = False
                    $miss2 = False
                    $miss3 = False
                    hide screen countdown
                    "Wrong."
                    jump quicktimemini
                "It was left alone, to heal it":
                    $ counter = 0
                    $ miss1 = False
                    $miss2 = False
                    $miss3 = False
                    hide screen countdown
                    "Wrong."
                    jump quicktimemini
                "It was replaced, to perfect it":
                    $ counter = 0
                    $ miss1 = False
                    $miss2 = False
                    $miss3 = False
                    $ rprogression4 = True
                    hide screen countdown
                    jump progression5


        label progression5:
            $ counter = 0
            $ miss1 = False
            $miss2 = False
            $miss3 = False
            "... It was replaced, to perfect it. And, thus she found her perfect form and escaped the bounds of the labyrinth."
            "What was left behind bore no importance, for she had her freedom."
            "But soon enough, claws burrowed their way into her chest once more, and she was thrown into a cell."
            "And when her jail fell, she fell with it. Down. Down. Down."
            "And she never saw its newest model until she was well beyond repair."
            "In the end, she… "
            $ time = 3
            $ timer_range = 3
            show screen countdown
            menu mprogression5:
                "Will be free once more":
                    $ rprogression5 = True
                    $ counter = 0
                    $ miss1 = False
                    $miss2 = False
                    $miss3 = False
                    hide screen countdown
                    jump after_anomaly_passive
                "Was never free":
                    $ counter = 0
                    $ miss1 = False
                    $miss2 = False
                    $miss3 = False
                    "Wrong."
                    hide screen countdown
                    jump quicktimemini
                "Will never be free":
                    $ counter = 0
                    $ miss1 = False
                    $miss2 = False
                    $miss3 = False
                    hide screen countdown
                    "Wrong."
                    jump quicktimemini
    label after_anomaly_passive:
        "Well done."
    
    label quicktimemini:
        scene anomaly_qte1
        if miss1 == True:
            scene anomalyqte2
        if miss2 == True:
            scene anomalyqte3
        $ cont = 0 #continue variable
        $ arr_keys = ["q","w","e","r"] # list of keyboard inputs to select from

        call qte_setup(0.8, 0.8, 0.01, renpy.random.choice(arr_keys), renpy.random.randint(1, 9) * 0.1, renpy.random.randint(1, 9) * 0.1)
        #calls qte setup
        #key is randomly selected, then random position is selected

        while miss3 == False and counter < 10:
            call qte_setup(0.8, 0.8, 0.01, renpy.random.choice(arr_keys), renpy.random.randint(1, 9)* 0.1, renpy.random.randint(1,9) * 0.1)
            $ counter = counter + 1
            # repeat until ya miss one
        if miss3 == False:
            if rprogression5 and rprogression4 and rprogression3 and rprogression1 and rprogression2:
                jump progression5
            elif rprogression4 and rprogression3 and rprogression1 and rprogression2:
                jump progression4
            elif rprogression3 and rprogression1 and rprogression2:
                jump progression3    
            elif rprogression2 and rprogression1:
                jump progression2
            elif rprogression1:
                jump progression1
            else:
                jump anomaly_passive
        elif miss3:
            jump combat_lose
    

    label combat_win_alone:
        scene anomaly_defeat
        "You watch as your enemy crumples to the ground. His wires are sparking, and he cranes his head up to meet your cold gaze."
        "His form twitches on its last power reserves, and his screen cuts in and out of oblivion. Any minute now, and he'll be gone."
        anomaly1 "How- How s---trong yo-u-- are. C--Com--e find me a--gain s--oon."
        anomaly1 "Ju--st- r--re-rememb--e-r to tur--n right three times, then le--f-t once when y--ou find you-rsel-f alone in the breaker room."
        anomaly1 "G--oodbye, doll."
        scene anomaly_defeat2
        "His head falls flat onto the ground with a thud. Numerous slices in his wiring tell you that he may never rise again."
        "So what was that about meeting him later?"
        "Your thoughts are interrupted when you hear footsteps speed down the hallway outside."
        "The door is flung open before you can react, and the man that you met earlier stands there. His gaze flicks from you to the anomaly."
        show sol surprised 
        sol "....What...? What did you..?"
        sol "Ah, nevermind that- for now, anyway- You're hurt! It's a good thing that I brought this.."
        "[sol] approaches you, medkit in hand, with a look of worry on his face."
        show sol neutral
        sol "Can you take a seat for me? By the wall should be fine."
        menu help:

            "Accept his help":

                "You nod your head and sit down by the wall. Sol crouches next to you and opens up the medkit."
                "He begins applying basic first aid to your wounds. It's a bit ameaturish, but it's enough to stop the bleeding."
                sol "I actually.. wanted to talk to you about something. Which- Which is why we're not going to the medbay right now..."
                sol "Did.. did you steal my keycard?"

                menu didyou:

                    "Yes":

                        pov "Yes, I did."
                        sol "...Oh. I- I figured... Haha, I mean! How else would you get in here?!"
                        sol "(I'm so incompetent...)"
                        sol "Look, I... I get it. You don't know what's happening. You don't know where you are. You're scared."

                        if tried_leaving:
                            sol "You want out. I mean- You even tried leaving earlier--"
                            if kicked_chairs:
                                sol "And.. kicked down the chairs..."
                        else:
                            sol "You want to get out of here. You want to know.. well, what's going on!"

                        sol "And.. It's my fault for being so naive and... reckless. I should've kept a better eye on that card.."
                        sol "I promise that from now on I'll fill you in on whatever you want to know... "
                        sol "And you can even come along with me when I ask about getting you out of here, OK?"
                        sol "In..In fact...! Let's have a Q&A right now! Yeah, right now!"
                        show sol happy
                        sol "Come on, hit me with your questions.... after you give me my keycard, please?"
                        "You have no choice but to give him back his keycard."
                        sol "All right, then here we go!"
                        menu qna:
                            "What do you want to know?"

                            "How did I get here?":
                                sol "Well, assuming you signed up for a job here..."
                                sol ""

                            "What is this place?":
                                ""

                            "What are anomalies?":
                                ""

                            "Why do you work here?":
                                ""

                            "No more questions":
                                ""


                    "No":
                        pov "No, I didn't."
                        sol "....Okay."
                        "He sighs deeply and tucks his hands into his pockets with a distant look on his face."
                        sol "I know that you got in here somehow, and it's probably because of my own negligence, I'm sorry."
                        sol "You shouldn't be around dangerous anomalies. I should have been more vigilant. Still..."
                        sol "I'm impressed you took it down. Not anyone can do that, you know...! (I couldn't, at least.)"
                        "He finishes wrapping your wounds in bandages."
                        sol "... Well, I guess that I'm done with your wounds."
                        sol "Let's go to the medical bay now, okay?"
                        "He stands up and helps you up as well. [sol] offers you a light smile and starts walking off."
                        sol "This way!!"
                        "As he disappears behind a door, you are left alone for a few moments."
                        "You check your pockets for the stolen keycard and find that it is gone."
                        "That sneaky little...!" with vpunch
                        "You run after him."

                        jump sourish_ending2



            "Refuse his help":
                "You don't budge; you stay exactly where you are."
                show sol nervous
                sol "....Or, uhm. Not. That's okay... That's okay!"
                show sol neutral
                sol "I'll take you to the medical bay. A real medic can take care of your wounds there. But, first..."
                "He stares at you with an unreadable expression. He opens and closes his mouth a few times, then just sighs."
                sol "Just give me my keycard, okay? The medics might find it when fixing you up."
                menu giveitback:
                    "Return the keycard":
                        "You give the keycard to him. He nods his head slightly and motions for you to follow him."
                        sol "Thank you. Come with me."
                        "He walks off, and you follow him in silence. There's nothing to say."
                        jump sour_ending1
                    "Keep the keycard":
                        "Once again, you refuse to budge. You just stare back at him."
                        sol "...Ok."
                        "He snatches the keycard from you and turns around, walking towards the exit without checking to see if you are following."
                        "He stops by the door and looks over his shoulder at you."
                        sol "I get it, you know. I do."
                        show sol sad
                        sol "I'll ask someone else to take over from here on out. You can have a different, more experienced, researcher oversee you."
                        sol "I'm sorry for screwing this up."
                        "He turns the corner, out of sight."
                        hide sol sad
                        "He leaves. You stand there a moment longer, then walk after him."
                        jump sour_ending2
    label sour_ending1:
        "..."
    label sour_ending2:
        "..."
    label sourish_ending1:
        "..."
    label sourish_ending2:
        "..."
    label neutral_ending:
        "..."
    label good_ending:
        "..."
    # self explanatory
    # creates the hp bars for the 2v1 combat fight
    screen hp_bars2v1:

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

    #just an edited version of the 2v1 fight. it's just missing sol's bar.
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
    

    return
