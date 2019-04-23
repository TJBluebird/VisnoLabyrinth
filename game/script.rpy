init:

    #define player "e-name" and will input from user
    define player = Character("[e_name]", color="#f44242")

    #define characters
    define mother = Character("Mother", color="#f4ee42")

    #define background images
    image bg Home = "images/bg_001.png"
    image bg Home_Inside = "images/bg_002.png"
    image bg Crossroads = "images/bg_003.png"
    image bg Bridge = "images/bg_004.png"
    image bg Swamp = "images/bg_005.png"
    image bg Labyrinth = "images/bg_006.png"
    image bg Junction = "images/bg_007.png"
    image bg Sirens = "images/bg_008.png"
    image bg Chimera = "images/bg_009.png"
    image bg Minotaur = "images/bg_010.png"
    image bg Witch = "images/bg_011.png"

    define water_point = 0
    define earth_point = 0
    define blood_point = 0

    define crossroad_option = 0
    define chimera_option = 0
    define bridge_option = 0
    define junction_option = 0
    define minotaur_option = 0
    define minotaur_attack_option = 0
    define witch_option = 0
    define sirens_option = 0
    define swamp_option = 0
    define decline_skull_option = 0



screen test:
    frame:
        xpadding 40
        ypadding 40
        vbox:
            text "Type your name"
            input
        align(.5, .5)




label start:

    #Input player's name
    centered "{color=#024eff}Please enter your name:{/color}"
    call screen test
    $ e_name = _return

    #HOME
    scene bg Home_Inside with dissolve
    centered "{size=50}{color=#f4e842}Home{/size}{/color}"
    "The odor of sage fills your nostrils as you enter your home. Once, the first thing you smelled would have been breakfast prepared by your mother. That’s your job now, along with all the other chores that she would have once done."
    "It’s already been a long morning. You’ve fed the chickens, collected the eggs, mucked out the stable and tended to the garden and now it’s time to check on your mother before you make breakfast."
    "You approach the bedroom door, hesitating as you always do because today might be the day you go in and find her cold to the touch. You hear a hacking cough through the door and you let out a relieved breath. Today is not the day."
    "You open the door and step inside."
    "The smell of sage is stronger inside her bedroom. It hangs in bunches from the rafters in here to ease her suffering."
    player "Good Morning Mother, are you well?"
    "You know the answer to the question without needing to ask. Her once Golden hair has gone grey. Her skin is pale and haggard. She is now so weak she cannot get out of bed."
    "Still she smiles when she sees you and beckons you closer."
    mother "As well as I can be, dearest child."
    "The answer is the one that she gives every morning, but still you sense that something is different about this morning. For once she is not trying to hide the weakness in her voice or the shaking of her hands."
    "It’s hard for you to understand how such a strong, energetic woman could have been robbed of all her strength and become so frail in just one winter."
    mother "Listen to me closely"
    "Her voice pulls you out of your thoughts. She takes your hand and draws you closer to her, the intensity of her gaze causes a knot of fear to form in your stomach."
    mother "You know as well as I do that I am not much longer for this world"
    "Your stomach drops and grief fills you. You have been worried about it for some time, but to hear her say the words aloud makes them so much more real. You shake your head and start to deny her words."
    mother "Don’t try to deny it, my love. We’ve both known that it was coming. I have seen it in the way you speak to me, in the way you hug me as if every time will be the last."
    player "Yes, Mother"
    "You drop your head so she can’t see the tears in your eyes."
    mother "I have a task that I need you to perform before I depart.  You must visit your uncle and bring him to me.  Your father’s brother has always been a fine and capable man, and visited often before your father passed away, though you may be too young to remember"

    centered "{color=#024eff}What's your decision?{/color}"

    #(1)Branch: Leave or stay?
    menu:
        "1. You decide to stay with your mother":
            jump stay
        "2. You decide to go":
            jump leave

    #(1)-1.Stay - Story End
    label stay:
        player "I won’t leave you mother!"
        "You know that if you leave now, you will never see her again. Your mother seems to understand, and wraps her arms around you and does not try to talk you out of your decision."
        "In the coming days you try all the remedies that you know, but despite all of your efforts your mother’s condition steadily worsens. She is soon unable to even speak and you know no other way to ease her suffering."
        "You are by her bedside for her final moments, holding her hand in the hope that you bring her some comfort."
        player "I love you, Mother. Goodbye."
        centered "{size=50}{color=#f4e842}END{/size}{/color}"
        return

    #(1)-2.Leave - journey start
    label leave:
    "You know that this is likely your mother’s dying wish and you  cannot bring yourself to deny her."
    player "I don’t remember him. But I will fetch him for you, if it is what you want. Where does he live, Mother?"
    mother "In a cottage on the other side of the forest, Dear. Now please go and make haste.  Mark that you do not forget the ritual, else the darkness inhabiting that forest will find you."
    "Hugging her for what you know might be the last time, you leave the room but before you shut the door behind you, you hear your mother call out"
    mother "I know you don’t like it, but do not forget the dove!"

    #Garden
    scene bg Home with dissolve
    centered "{size=50}{color=#f4e842}Garden{/size}{/color}"
    "You go into the Garden do do as your Mother wishes. Filled with a sudden sense of dread, you look around yourself, trying to take it all in like it is the last time you will ever see it."
    "It is a modest home, small by most standards, but you love it dearly. It was built entirely by your Father before he passed. You smile when you remember how proud the timbered roof had made him."
    "Your eyes fall on the Shrine nestled against the outer wall of the house and you need to fight down a feeling of revulsion. You know that the purpose of the Shrine is to hide the house from view of those that lurk in the woods and to protect the family from any evil that they might do."
    "But you have never seen anything evil in the woods, and so you don’t understand why such ugly things are necessary. Every time you watch your mother sacrifice a Dove you feel sick. Why should those cute doves need to pay for your family’s superstitions?"
    "Trying to give yourself courage, you take a deep breath. You cannot help but notice how old the Shrine is. As a child you never questioned it, but it looks like it has stood there far longer than the house itself."
    "Worn down by countless years of wind and rain you can barely make out the depiction of three faces carved into the stone. Below them, the depiction of an old crone is less weathered. Her face deeply wrinkled, her head cowled."
    "You let out a deep sigh and berate yourself for procrastinating. If you hope to ever see your mother again, you must leave now."

    ##Water ritual
    player "Lo to the Watcher, with power to see"
    menu:
        "1. You offer water":
            $ water_point = 1

        "2. You chose not to offer water":
            $ water_point = 2

    label result_water:
        if water_point == 1:
            "You sprinkle a few drops of water from your flask onto the shrine. The droplets seem to fall in slow motion onto the surface and like always, appear to veer towards the three faces."
            "No water spills onto the ground or pools in the base of the shrine. You know it is impossible, but it is like the stone absorbs the water."
        elif water_point == 2:
            "You are not certain how long you will need to travel to reach your Uncle’s home and you may need all the water you can carry. It seems wasteful to pour it all over the old statue. You decide it would be better to save all the water you can for your journey."
            "You are sure that the words are more than enough to satisfy the ritual."

    ##Earth ritual
    player "Lo to the Watcher, with power to see"
    menu:
        "1. You offer earth":
            $ earth_point = 1

        "2. You chose not to offer earth":
            $ earth_point = 2

    label result_earth:
        if earth_point == 1:
            "You scoop up a handful of loose soil and scatter it across the stone. Just like the water, the grains of dirt seem to fall in slow motion. They tumble as if guided by an unseen hand and land in a neat pile at the base of the altar."
            "The wind seems to slow and even the birds in the trees seem unwilling to make a sound. Giving your surroundings a funerary quality."
            "A shudder passes through you as, for the first time, you realise that the pile looks remarkably like a freshly dug grave."
        elif earth_point == 2:
            "You feel as if this is a waste of time, much better spent if you were already on your way.  Forgoing the offering of earth, you hurriedly continue with the ceremony."

    ##Blood ritual
    player "Lo to the Crone, who darkens the path"
    menu:
        "1. You offer the blood":
            $ blood_point = 1

        "2. You chose not to offer the blood":
            $ blood_point = 2

    label result_blood:
        if blood_point == 1:
            "You open the door of a nearby aviary. The doves, as if knowing what is to come, shy away from your hand. You quickly capture the closest and cradle it to your chest in one hand. You carefully close and fasten the door before taking the dove to the shrine."
            player "I'm sorry."
            "You whisper and stroke the dove for a moment. Then, you take out your skinning knife and quickly end the Dove’s life, ensuring that the spilled blood lands on the shrine so that this horrible act is, at least, not wasted."
            "The blood trickles down the surface of the Shrine, seeming to flow toward the depiction of the old woman. Somehow spreading across the relief, making it appear particularly horrific."
        elif blood_point == 2:
            "No. You will not do it. Those poor doves have done nothing to deserve such a fate and you will have take no further part in their death. You continue on with the ceremony, inwardly smiling at the sound of the Doves cooing as if in gratitude."

    ##Ritual end
    player "Lo to the Three, that we may pass free"
    "With the end of the ceremony you are free to start your journey. You look back at your home one last time and start out."

    #CORSSROAD
    scene bg Crossroads with dissolve
    centered "{size=50}{color=#f4e842}CROSSROAD{/size}{/color}"
    "You come upon a crossroad with the option to travel left towards the bridge or right, towards the swamps"

    #(2)Branch: Bridge or Swamp?
    menu:
        "1. Left to Bridge":
            $ crossroad_option = 1

        "2. Right to Swamp":
            $ crossroad_option = 2

    label crossroad_result:
        if crossroad_option == 1:
            jump bridge

        elif crossroad_option == 2:
            jump swamp

    #(2)-1. Bridge
    label bridge:
    scene bg Bridge with dissolve
    centered "{size=50}{color=#f4e842}BRIDGE{/size}{/color}"
    "You come across an unfriendly troll that invariably attacks you."

    #(3)Branch: Troll or Hectate
    menu:
        "1. Troll eats you":
            $ bridge_option = 1

        "2. Saved by Hectate":
            $ bridge_option = 2

    label bridge_result:
        if bridge_option == 1:
            jump troll

        elif bridge_option == 2:
            jump hectate

    #(3)-1. Troll
    label troll:
        "Your decision resultes in death at the hands (or the mouth) of a troll."
        return

    #(3)-2. Hectate
    label hectate:
        "You are saved from the troll by the Goddess Hecate who in turn takes you directly to the Labyrinth entrance"

    #LABYRINTH ENTRANCE
    label labyrinth_entrance:
    scene bg Labyrinth with dissolve
    centered "{size=50}{color=#f4e842}Labyrinth Entrance{/size}{/color}"
    "You arrive at the Labyrinth entrance with either the Skull, Goddess or Witch (Huntress) companion.\nWitch (Huntress) dissappears leaving the player to find their own way.\nGoddess dissappears but can appear later.\nSkull stays with the player"

    #JUNCTION
    scene bg Junction with dissolve
    centered "{size=50}{color=#f4e842}Junction{/size}{/color}"
    "You are met with the choice of going left or right at the outset of the Labyrinth.\nLeft leading to the Chimera.\nRight leading to the Sirens."

    #(4)Branch: Chimera or Sirens
    menu:
        "1. Left to Chimera":
            $ junction_option = 1
        "2. Right to Sirens":
            $ junction_option = 2

    label junction_result:
        if junction_option == 1:
            jump chimera_puzzle

        elif junction_option == 2:
            jump sirens

    ####################################Puzzle-Start##########################
    label chimera_puzzle:
        scene bg Chimera with dissolve
label puzzle:

    python:
        k = Puzzle()
        k.set_sensitive(False)
        k.show()

label quick_continue:
    
    while True:

        python:
        
            ui.textbutton("Give Up", ui.jumps("giveup"), xalign=.02, yalign=.98)
            k.set_sensitive(True)
            event = k.interact()

            if event:
                renpy.checkpoint()
            
            k.set_sensitive(False)
        # e "[event]"
        if event == "win":
            jump win


label win:

    "Finished!"
    
    "Congratulations!"
    python:
        k.hide()
    jump chimera

label giveup:

    $ k.set_sensitive(False)
    
    menu:
        "Are you sure you want to give up?"

        "Yes":

            "Oh well, better luck next time."
            python:
                k.hide()
            jump chimera

        "No":
            python:
                k.hide()
            jump puzzle

label newgame:

    menu:    
        "Would you like to try again?"

        "Yes":
            pass

        "No":
            "Well, I hope to see you again soon."
            jump chimera

    "Okay, here we go!"
    
    scene bg table

    python:
        k = Puzzle()
        k.sensitive = False
        k.show()    

    jump continue    
    ####################################Puzzle-End##########################         

    #(4)-1. Chimera
    label chimera:
        scene bg Chimera with dissolve
        centered "{size=50}{color=#f4e842}CHIMERA{/size}{/color}"
        "You encounter a Chimera with intention to eat you.\nYou may argue and convince the Chimera not to do so.\nAsk for assistance from your companion or beg for your life."

    #(5)Branch: Death or Minotaur or Argue
    menu:
        "1. Beg for your life":
            $ chimera_option = 1

        "2. Ask for assistance":
            $ chimera_option = 2
        "3. Argue":
            $ chimera_option = 3

    label chimera_result:
        if chimera_option == 1:
            "Ends in Death"
            return

        elif chimera_option == 2 or 3:
            "Leads to Minotaur"
            jump minotaur


    #(5)-1. Minotaur
    label minotaur:
        scene bg Minotaur with dissolve
        centered "{size=50}{color=#f4e842}MINOTAUR{/size}{/color}"
        "You encounter a Minotaur with sole purpose to guard the apple.\n Considering you a threat to it, it begins to attack."

    #(6)Branch: 'Reason With it' or 'I am only here for a rest'
    menu:
        "1. Try to reason with it":
            $ minotaur_option = 1

        "2. Here for a rest and a further choice":
            $ minotaur_option = 2


    label minotaur_result:
        if minotaur_option == 1:
            "You encounter the Witch"
            jump witch

        elif minotaur_option == 2:
            "The Minotaur attacks in earnest. "
            jump minotaur_attack

    #(6)-1. Minotaur Attack
    label minotaur_attack:
        centered "{size=50}{color=#f4e842}MINOTAUR ATTACK{/size}{/color}"

    #(7)Branch: Dodge or 'Remain Still'
    menu:
        "1. Dodge":
            $ minotaur_attack_option = 1

        "2. Remain Still":
            $ minotaur_attack_option = 2


    label minotaur_attack_result:
        if minotaur_attack_option == 1:
            "The Minotaur's charge slams into you, ending your life."
            return

        elif minotaur_attack_option == 2:
            "You encounter the Witch"
            jump witch


    label witch:
        scene bg Witch with dissolve
        centered "{size=50}{color=#f4e842}WITCH{/size}{/color}"
        "There are 3 options"

    #(8)Branch: Good Endig or Neutral Ending or Bad Ending
    menu:
        "1. Good Ending":
            $ witch_option = 1

        "2. Neutral Ending ":
            $ witch_option = 2

        "3. Bad Ending ":
            $ witch_option = 3

    label witch_result:
        if witch_option == 1:
            #"Good"
            jump good_ending

        elif witch_option == 2:
            #"Neutral"
            jump neutral_ending

        elif witch_option == 3:
            #"Bad"
            jump bad_ending

    #(8)-1. Good Ending
    label good_ending:
        centered "{size=50}{color=#f4e842}GOOD ENDING{/size}{/color}"
        return

    #(8)-2. Neutral Ending
    label neutral_ending:
        centered "{size=50}{color=#f4e842}NEUTRAL ENDING{/size}{/color}"
        return

    #(8)-3. Bad Ending
    label bad_ending:
        centered "{size=50}{color=#f4e842}BAD ENDING{/size}{/color}"
        return




    #(4)-2.Sirens
    label sirens:
        scene bg Sirens with dissolve
        centered "{size=50}{color=#f4e842}SIRENS{/size}{/color}"
        "You encounter Sirens, eventuating in the riding of a boat."

     #(9)Branch: Drawn or Tricked/Drown or Minotaur
    menu:
        "1. Option1":
            $ sirens_option = 1

        "2. Option2 ":
            $ sirens_option = 2

        "3. Option3 ":
            $ sirens_option = 3

    label sirens_result:
        if sirens_option == 1:
            "Drawn"
            return

        elif sirens_option == 2:
            "Tricked/Drawn"
            jump neutral_ending

        elif sirens_option == 3:
            "Leads to Minotaur"
            jump minotaur




    #(2)-2.swamp
    label swamp:
        scene bg Swamp with dissolve
        centered "{size=50}{color=#f4e842}SWAMP{/size}{/color}"
        "Swamp: You arrive at a swamp and meet a talkative skull,\npromising that it can help your mother with a golden apple.\nPartnering with the skull takes you to the Labyrinth entrance."

    #(9)Branch: 'Partner with Skull' or 'Decline Skull'
    menu:
        "1. Partner with Skull":
            $ swamp_option = 1

        "2. Decline Skull":
            $ swamp_option = 2

    label swamp_result:
        if swamp_option == 1:
            jump labyrinth_entrance

        elif swamp_option == 2:
            jump decline_skull

    label decline_skull:
        centered "{size=50}{color=#f4e842}DECLINE SKULL{/size}{/color}"
        "Declining assistance from the skull,\nyou may exit the woods to your uncles home or press on,\neventually meeting the witch (in disguise)"

    #(10)Branch: 'Exit Woods' or 'Continue On'
    menu:
        "1. Exit Woods":
            $ decline_skull_option = 1

        "2. Continue On":
            $ decline_skull_option = 2

    label decline_skull_result:
        if decline_skull_option == 1:
            "You exit the woods, seeing your uncles home"
            return

        elif decline_skull_option == 2:
            "Meet Witch"
            jump meet_witch

    label meet_witch:
        centered "{size=50}{color=#f4e842}MEET WITCH{/size}{/color}"
        "You meet the Witch (disguised as a huntress) who leads you to the Labyrinth Entrance."
        jump labyrinth_entrance



return
