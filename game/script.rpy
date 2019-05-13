init python:

    from time import localtime, strftime
    import time



init:

    image mother = "images/Sick mum_re.png"   
    image happy_mother = "images/Happy Mum.png" 
    image sad_girl = "images/Sad Girl_re.png"    
    image happy_girl = "images/Happy Girl.png"
    image bones_bof = "images/Bones Bog"

    image troll = "images/Troll.png"
    image huntress = "images/Huntress.png"
    image huntress_dark = "images/Huntress dark form"
    image hectate_angry = "images/Angry Hectate"
    image hectate_calm = "images/Normal Hectate"
    image hectate_insane = "images/Hectate Crazy"
    image minotaur = "images/Minotaur"
    image treewitch = "images/Witch Tree"

    #User's point
    define user_point = 0

    #define player "e-name" and will input from user
    define player = Character("[e_name]", color="#f44242")

    #define characters
    define mother = Character("Mother", color="#f4ee42")
    define troll = Character("Troll", color="#f4ee42")
    define huntress = Character("Huntress", color="#567756")
    define hectate_calm = Character("Hectate_Calm", color="#bf80b2")
    define hectate_angry = Character("Hectate_Angry", color="#42f4a7")
    define hectate_insane = Character("Hectate_Insane", color="#4f3333")
    define bones = Character('', image = 'bones')
    define mermaid = Character("Mermaid", color="#f4ee42")
    define chimera = Character("Chimera", color="#f4ee42")
    define minotaur = Character("Minotaur", color="#f4ee42")
    define treewitch = Character("TreeWitch", color="#4f3333")

    image side bones = "images/bones_side.png"

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
    image bg credits = "images/credits.png"

    define water_point = 0
    define neither_point = 0
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
    define junction_option_with_skull = 0
    define sirens_option_with_hectate = 0
    define company_with_skull = 0
    define company_with_hectate = 0
    define chimera_skull_option = 0
    define chimera_hectate_option = 0
    define chimera_visit = 0
    define sirens_visit = 0

    #Add points when Mermaid Song Quizz failed
    define MermaidSong_fail = 0

    #Clickable buttons on crossroads scene
    screen imagemap:
        imagemap:
            ground "images/crossroad.png"
            hover "images/crossroad-hover.png"
            hotspot (339, 87, 390, 189) action Jump("swamp")
            hotspot (360, 266, 376, 174) action Jump("bridge")

    #Mermaid Song image define
    image movie = Movie(size=(800, 600), xpos=.5, ypos=.8)

    #Clickable buttons on Sirens scene with Mermaid Song quizz
    screen imagemap2:
        imagemap:
            ground "images/MermaidSong.png"
            hover "images/MermaidSong-hover.png"
            hotspot (240, 35, 815, 101) action Jump("sirnes_dead")
            hotspot (244, 155, 814, 97) action Jump("sirnes_dead")
            hotspot ((244, 285, 815, 98)) action Jump("sirnes_dead")
            hotspot ((238, 407, 819, 100)) action Jump("sirens3")

    #Clickable buttons on Sirens scene with Mermaid Song quizz
    screen imagemap_with_skull:
        imagemap:
            ground "images/MermaidSong.png"
            hover "images/MermaidSong-hover.png"
            hotspot (240, 35, 815, 101) action Jump("sirnes_dead")
            hotspot (244, 155, 814, 97) action Jump("sirnes_dead")
            hotspot ((244, 285, 815, 98)) action Jump("sirnes_dead")
            hotspot ((238, 407, 819, 100)) action Jump("sirens_with_skull2")

    #Clickable buttons on Sirens scene with Mermaid Song quizz
    screen imagemap_with_hectate:
        imagemap:
            ground "images/MermaidSong.png"
            hover "images/MermaidSong-hover.png"
            hotspot (240, 35, 815, 101) action Jump("sirnes_dead")
            hotspot (244, 155, 814, 97) action Jump("sirnes_dead")
            hotspot ((244, 285, 815, 98)) action Jump("sirnes_dead")
            hotspot ((238, 407, 819, 100)) action Jump("sirens_with_hectate2")

    screen imagemap_with_huntress:
        imagemap:
            ground "images/MermaidSong.png"
            hover "images/MermaidSong-hover.png"
            hotspot (240, 35, 815, 101) action Jump("sirnes_dead")
            hotspot (244, 155, 814, 97) action Jump("sirnes_dead")
            hotspot ((244, 285, 815, 98)) action Jump("sirnes_dead")
            hotspot ((238, 407, 819, 100)) action Jump("sirens_with_huntress2")



    python:
        renpy.music.register_channel("Fire", mixer="sfx")
        renpy.music.register_channel("outsideHome", mixer="sfx")
        renpy.music.register_channel("crossroads", mixer="sfx")
        renpy.music.register_channel("bridge", mixer="sfx")
        renpy.music.register_channel("swamp", mixer="sfx")
        renpy.music.register_channel("entrance", mixer="sfx")
        renpy.music.register_channel("Bull", mixer="sfx")
        renpy.music.register_channel("thunder", mixer="sfx")
        renpy.music.register_channel("waves", mixer="sfx")


#Frame for input user's name
screen test:
    frame:
        xpadding 40
        ypadding 40
        vbox:
            text "Type your name"
            input
        align(.5, .5)

screen display_user_point:
    frame:
        text "Points: [user_point]"



label start:

    #Input player's name
    centered "{color=#024eff}Please enter your name:{/color}"
    call screen test
    $ e_name = _return

    show screen display_user_point

    #play background music
    play music "sound/BackgroundMusic.mp3" fadein 1.5

    #play Fire.mp3 sound
    play Fire "sound/Fire.mp3" fadein 2.0

    #HOME
    scene bg Home_Inside with dissolve
    centered "{size=50}{color=#f4e842}Home{/size}{/color}"
    #show sad_girl at left with dissolve
    "The odor of sage fills your nostrils as you enter your home. Once, the first thing you smelled would have been breakfast prepared by your mother. That’s your job now, along with all the other chores that she would have once done."
    "It’s already been a long morning. You’ve fed the chickens, collected the eggs, mucked out the stable and tended to the garden and now it’s time to check on your mother before you make breakfast."
    "You approach the bedroom door, hesitating as you always do because today might be the day you go in and find her cold to the touch. You hear a hacking cough through the door and you let out a relieved breath. Today is not the day."
    "You open the door and step inside."
    "The smell of sage is stronger inside her bedroom. It hangs in bunches from the rafters in here to ease her suffering."
    player "Good Morning Mother, are you well?"
    "You know the answer to the question without needing to ask. Her once Golden hair has gone grey. Her skin is pale and haggard. She is now so weak she cannot get out of bed."
    "Still she smiles when she sees you and beckons you closer."
    show mother at right with dissolve
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
        scene bg credits with dissolve
        centered "{size=50}{color=#f4e842}END{/size}{/color}"
        return

    #(1)-2.Leave - journey start
    label leave:
    "You know that this is likely your mother’s dying wish and you  cannot bring yourself to deny her."
    player "I don’t remember him. But I will fetch him for you, if it is what you want. Where does he live, Mother?"
    mother "In a cottage on the other side of the forest, Dear. Now please go and make haste.  Mark that you do not forget the ritual, else the darkness inhabiting that forest will find you."
    "Hugging her for what you know might be the last time, you leave the room but before you shut the door behind you, you hear your mother call out"
    mother "I know you don’t like it, but do not forget the dove!"

    #Sound Fire.mp3 Stop
    stop Fire fadeout 2.0

    #Garden
    scene bg Home with dissolve

    #play outsideHome.mp3 sound
    play outsideHome "sound/outsideHome.mp3" fadein 2.0

    centered "{size=50}{color=#f4e842}Garden{/size}{/color}"
    "You go into the Garden do do as your Mother wishes. Filled with a sudden sense of dread, you look around yourself, trying to take it all in like it is the last time you will ever see it."
    "It is a modest home, small by most standards, but you love it dearly. It was built entirely by your Father before he passed. You smile when you remember how proud the timbered roof had made him."
    "Your eyes fall on the Shrine nestled against the outer wall of the house and you need to fight down a feeling of revulsion. You know that the purpose of the Shrine is to hide the house from view of those that lurk in the woods and to protect the family from any evil that they might do."
    "But you have never seen anything evil in the woods, and so you don’t understand why such ugly things are necessary. Every time you watch your mother sacrifice a Dove you feel sick. Why should those cute doves need to pay for your family’s superstitions?"
    "Trying to give yourself courage, you take a deep breath. You cannot help but notice how old the Shrine is. As a child you never questioned it, but it looks like it has stood there far longer than the house itself."
    "Worn down by countless years of wind and rain you can barely make out the depiction of three faces carved into the stone. Below them, the depiction of an old crone is less weathered. Her face deeply wrinkled, her head cowled."
    "You let out a deep sigh and berate yourself for procrastinating. If you hope to ever see your mother again, you must leave now."
    player "Lo to the Watcher, with power to see"
    player "Lo to the Warrior, who endeth the line"
    player "Lo to the Crone, who darkens the path"

    ##Ritual

    menu:
        "1. You offer water":
            $ water_point = 1
            $ user_point = user_point + 1

        "2. You offer blood":
            $ blood_point = 1
            $ user_point = user_point - 1

        "3. You offer neither":
            $ neither_point = 1

    label result_ritual:
        if water_point == 1:
            player "Lo to the Three, that we may pass free"
            "You sprinkle a few drops of water from your flask onto the shrine. The droplets seem to fall in slow motion onto the surface and like always, appear to veer towards the three faces."
            "No water spills onto the ground or pools in the base of the shrine. You know it is impossible, but it is like the stone absorbs the water."
            "With the end of the ceremony you are free to start your journey. You look back at your home one last time and start out."
        elif blood_point == 1:
            player "Lo to the Three, that we may pass free"
            "You open the door of a nearby aviary. The doves, as if knowing what is to come, shy away from your hand. You quickly capture the closest and cradle it to your chest in one hand. You carefully close and fasten the door before taking the dove to the shrine."
            player "I'm sorry."
            "You whisper and stroke the dove for a moment. Then, you take out your skinning knife and quickly end the Dove’s life, ensuring that the spilled blood lands on the shrine so that this horrible act is, at least, not wasted."
            "The blood trickles down the surface of the Shrine, seeming to flow toward the depiction of the old woman. Somehow spreading across the relief, making it appear particularly horrific."
            "With the end of the ceremony you are free to start your journey. You look back at your home one last time and start out."
        elif neither_point == 1:
            player "Lo to the Three, that we may pass free"
            "No.  You will not do it.  This entire ritual is useless and outdated.  You see no point in watering a statue and those poor doves have done nothing to deserve such a fate."
            "With the end of the ceremony you are free to start your journey. You look back at your home one last time and start out."

    #Sound outsideHome.mp3 Stop
    stop outsideHome fadeout 2.0

    #play crossroads.mp3 sound
    play crossroads "sound/crossroads.mp3" fadein 2.0

    #CROSSROAD
    scene bg Crossroads with dissolve
    centered "{size=50}{color=#f4e842}CROSSROAD{/size}{/color}"
    "You walk down a well travelled path toward the woods. The bright morning sun filters down through the groves of pine and oak all around you and the air is filled with birdsong leaving you feeling warm and tranquil."
    "Soon, you pass by the furthest point that you have ever travelled. You pause momentarily at the boundary of everything that you have known. Nerves making it difficult for you to make the next step. You take a deep breath and pray that you will make it back in time to see your mother again."
    "You notice that it is not long before the forest begins to change. The trees that are straight and sturdy around your home are thin, gnarled and misshapen, their tendrils seeming to reach out for you as you pass."
    "The branches sway in the breeze, further enhancing the image of grasping hands. The formless shadows seem to move and dance, almost as if free to move about on their own."
    "You reach a fork in the path. A signpost marks the two directions. It is clearly old but the directions are still legible and indicate a bridge to the left and a swamp to the right."
    "Click the sgin where you want to go"

    #Sound crossroads.mp3 Stop
    stop crossroads fadeout 2.0

    #image button to choose bridge or swamp
    call screen imagemap


    #(2)-1. Bridge
    label bridge:

    scene bg Bridge with dissolve

    #play bridge.mp3 sound
    play bridge "sound/bridge.mp3" fadein 2.0

    centered "{size=50}{color=#f4e842}BRIDGE{/size}{/color}"
    "You come to a clearing in the forest and can see a well-kept bridge that crosses over a river."
    "The bank on either side is bright and green, almost like a perfectly manicured garden."
    "You breathe a sigh of relief. This was the right choice. It looks so much less scary than the swamp."
    player "I'm so glad I didn't go that way, I would've ended up lost in some bog for sure"
    "As you come closer to the bridge, you see that the water swirls fiercely beneath the stone arches of the bridge and tears at the banks, taking chunks of earth with it as it rushes downstream."
    "There isn't a living thing in sight.\nNo birds.\nNo butterflies.\nOnly the hiss of water.\n"
    "You no longer feel quite so confident about your choice."
    player "This feels....wrong"
    player "What was mother always singing about bridges?"
    player "Oh that's it, I remember now"
    player "Beware houses made of candy ♪\nAnd you'll be good and dandy\nBeware tunnels and bridges\nAnd life will be your riches♪"
    player "But visit a witch or step on a bridge♪\nAnd your life will end in a ditch♪"
    player "hmmmm\nThe bridge looks safe\nI’m sure the water is moving far too fast for anything to be hiding underneath."
    player "........"
    player "I don't want to go back\nThe bog looked more dangerous than this silly bridge"
    "The moment you set foot on the bridge, a Troll springs out of the water, blocking your way forward."
    player "AHHHHHHHHH"
    troll "What's a silly billy goat like you doing on my bridge all by yourself?"
    player "I'm...I'm...I'm not alone"
    troll "You're RIGHT! Because I'm here!"
    player "I'm with a...hunter"
    troll "No you're not my tasty treat, Ha Ha Ha!!"
    "You start to cry"
    player "I am! I am! there's a hunter! You ugly Troll!"
    troll "Then why are you crying my little goat?"
    "Crying intensifies"
    troll "That's okay, cry.  Your tears will marinate the meat"
    player "I'm going to my uncles home!"
    troll "The only place your going is in my belly"

    if blood_point == 1:
        jump troll

    if water_point == 1:
        jump hecate

    #Saved from Troll by Witch in Huntress
    player "AHHHHHHHHH"
    troll "Raaaaggh - Uck!"
    "The troll’s terrifying roar is abruptly cut short with a single thunk.\nWith a look of surprise, the Troll falls forward, dead."
    "From his back sprouts an arrow, buried deep within its thick skin.\nBehind him stands a Huntress."
    player "What?.."
    huntress "It's your lucky day, Sweetheart."
    huntress "Trolls like to play with their food.\nToday he choked on it."
    player "What..what happend?"
    huntress "LAUGHS\nSuch strength in these beasts, easily toppled if you know just where to strike."
    player "Why did he attack me?"
    huntress "Maybe you should ask him?"
    player "Uh... I'm good."
    huntress "Are you good? You look lost…"
    player "I'm heading to the north part of the woods, to see my uncle."
    huntress "How serendipitous!  It so happens that I'm going north as well, I can help you find your uncle’s house."
    huntress "There are worse things in these woods than Trolls, after all."
    player "THANK YOU! You're so kind.\nI was so scared that I might meet a witch."
    huntress "LAUGHS\nWe wouldn't want that now would we."
     #Sound bridge.mp3 Stop
    stop bridge fadeout 2.0
    jump labyrinth_entrance_with_huntress





#Saved from Troll by Hectate
############   With Hectate      ###############################################################################
    label hecate:

    #Sound bridge.mp3 Stop
    stop bridge fadeout 2.0

    "Suddenly the entire world freezes, as if time itself has stopped.\nNot a sound is heard, the trees no longer sway in the breeze.\nEven a passing bird hangs stationary mid-flight whilst overhead.\nThe troll’s charge, stopped completely, it’s arm still frozen overhead."
    "You look around, wide eyed at the impossibility of it all when at your side you spy a most unexpected sight."
    "Immediately beside you stands a woman in a diaphanous robe of flowing red silk, cinched at the waist with a belt of the same material."
    "In her right hand she holds a lit torch, though its flame provides no light.\nIn her left she holds a dagger, not in a threatening manner but pointed upward."
    "Her stance and posture reminds you of a statue, though this may be because but for her robe, slowly billowing in the complete absence of any breeze, she has been completely immobile, as if inanimate."
    "Despite this all, her most striking feature is her face, or more accurately, ‘faces’ as there is not one but three of them."
    "The one facing you, set below a pair of glowing golden eyes is a mouth curved slightly upward in a knowing smile."
    "What looks almost as if built into the side of her head is another face, seemingly identical in every way but for her scowling expression, her upper lip slightly curled to showing teeth underneath."
    "To her right, yet another face, this one laughing hysterically, though no sound escapes her."
    "At what she is laughing, you can only guess."

    player "Who are you?  What’s happening?"
    hectate_calm "Do you not already know us child?"
    hectate_calm "Have you not before prayed for our notice, our protection?"
    "Sudden realisation hits you.\nThis is the figure from your shrine!\nWater.\nWith an offering of water you have summoned this being?\nBut how is that possible?"
    player "Lo to the watcher, with power to see"
    "You manage to stammer, your mind feeling sluggish at the shock of it all."
    hectate_calm "Indeed, that is are name given to us by some, though like us, it is one amongst many"
    "The faces turn so that the scowling expression is turned toward you."
    hectate_angry "Though you can hardly keep calling us Watcher throughout this whole mess, do not believe for a second that you can!"
    player "Then...then what should I call you?"
    "Just as quickly, the head spins so that the smiling face is once again turned towards you."
    hectate_calm "We have gone by many names child. The Watcher is but one. Night-mother by some, The Fates by others."
    hectate_calm "The Wheel-weaver or Webspinner, the Taker of Light or Daughter of Moon. Endonia, Artemis, Selene or Hera. All are part true, all are part lies.  All are we.  You, child, will call us…"
    hectate_insane "Frank!"
    "The head spins to show you the laughing face, having finally deigned to pay some attention."
    hectate_insane "You should call us Frank!"
    "The head spins back to the first, and with a sigh and a roll of her eyes"
    hectate_angry "No!"
    hectate_calm "Hecate...call us Hecate"
    player "But, how did I summon you? Surely a little water could not do this?"
    "Hearing laughter from the oddly jovial face, you fear you may have said something foolish."
    hectate_calm "You did not summon us child. We come and go of our own volition. Though you offering was appreciated, it was inconsequential."
    hectate_calm "Though we appear now, it is but for our own interest, our interest in you. Your offering was not the catalyst."
    player "You’re interested in me?  Why?"
    "Shivering at the thought, even if you have no idea what a census taker or Chianti is"
    player "Test me with what?"
    "The first face towards you again, it's knowing smile now back.\nIt says nothing further, instead the torch in Hecate’s hand flashes and you both disappear."
    "Time resumes in the surrounding scene. The troll, now free to move but alone stops short in its charge.\nConfused that you appear to have simply vanished it scratches its head and mutters "
    troll "Huh?"
    hectate_calm "Trolls are nasty beasts"
    player "Wow!"


    #jump labyrinth_entrance_with_hectate
    scene bg Labyrinth with dissolve
    #play entrance.mp3 sound
    play entrance "sound/entrance.mp3" fadein 2.0
    centered "{size=50}{color=#f4e842}Labyrinth Entrance With Hectate{/size}{/color}"

    jump junction_with_hectate

    #JUNCTION
    label junction_with_hectate:
    scene bg Junction with dissolve
    centered "{size=50}{color=#f4e842}Junction with Hectate{/size}{/color}"
    player "Hmm, two paths."
    hectate_angry "Hmm you have- Two eye balls apparently!\nGods! We can see what you see."
    hectate_angry "Why do you say everything out loud\nIt's like you're trying to provide exposition for someone.\n "
    hectate_insane "[e_name] stared at the three faces feeling a sense of sadness."
    hectate_insane "Uncertainty was in the air."
    hectate_angry "What am I doing."
    hectate_insane "Providing exposition."
    hectate_angry "Well its annoying."
    hectate_insane "Well its fun."
    hectate_insane "Hecate feels annoyed yet amused at the SAME time."
    player "Which way should I go Hecate?"
    hectate_calm "Which path do you wish to take."
    player "The one that lets me leave this maze."
    hectate_calm "That path lies within."
    hectate_insane "I'm not actually a goddess."
    hectate_insane "My true form is a fortune cookie."
    hectate_insane "Ambiguous and delicious."
    player "I demand to hear a suggested path from all three of your faces."
    hectate_angry "Watch it [e_name]!"
    hectate_angry "Do not demand to ask anything from me.\nYou're lucky I can be kind\nYou don't want to see my fury."
    hectate_insane "Remember Atlantis oh oh and Pompeii"
    hectate_calm "We pave the paths but you choose which of them to walk."
    player "Sorry my Goddess I don't wish to disrespect you."
    hectate_calm "Be mindful little one.\nTo disrespect me is to disregard your life\n"
    hectate_calm "Now choose your path wisely"
    $ company_with_hectate = 1

    #Sound entrance.mp3 Stop
    stop entrance fadeout 2.0

    #(4)Branch: Chimera or Sirens
    menu:
        "1. Left to Chimera":
            $ junction_option = 1
        "2. Right to Sirens":
            $ junction_option = 2

    label junction_result_with_hectate:
        if junction_option == 1:
            jump chimera_with_hectate

        elif junction_option == 2:
            jump sirens_with_hectate

    label chimera_with_hectate:
        scene bg Chimera with dissolve

        #play Fire.mp3 sound
        play Fire "sound/Fire.mp3" fadein 2.0

        "Upon entering the room, the first thing that registers on your mind is the smell. The second thing that registers is your attempt not to gag, due primarily to the first thing."
        "Your nostrils are assaulted by the stench of what must be a combination of rotting flesh and rancid food. The ratios between them varying with each breath to make new and noxious combinations."
        player "Eugh...! What is that?!"
        "Looking around you spy a large room, the corners and walls are largely in shadow as the room is primarily lit via a flame from a sconce at the centre of the room."
        "You feel the shadows may be something of a blessing however."
        "You peer into the darkness trying to determine what the smell is emanating from, which is when you notice the corners of the room are piled with mounds of humanoid bodies and detritus in various states of decay."
        "The majority are now antiquated, their leavings now almost nothing but dust and bone. There are still many that are much more “fresh”, and you suspect that it is from these the smell comes."
        "Disconcertingly, almost all of these appear to be missing parts, an arm here, a leg there. Almost as if they are being eaten."
        player "Bad...Very bad...Very bad room"
        "As if alerted by the sound of your voice, you begin to hear a low growl emanating from the surrounding shadows."
        "An instinctual fear grips your heart as you see, stepping into the light, the face of a lion gradually emerge into view. It’s growl now not just heard but felt and you can’t help but back away."
        "As the lion continues stepping forward you notice not not all is as it seems. The lion’s tail, as it emerges from the darkness does not seem ordinary."
        "Suddenly, your entire field of vision is encompassed by a large pair of fangs. The lion’s tail, you now realise, is not a tail at all but large snake!"
        "Its jaws snap shut, right in front of your face having reached the limit of its length, and withdraws with a hiss, staring watchful as it hovers over the lion’s head."
        "You realise this is no lion at all. You remember your mother telling you stories of these monstrosities before."
        "Unfortunately in the stories they were simply background with no indication of how to deal with them. You only remember them being called “Chimera”."
        chimera "So it seems yet another little morsel enters our lair"
        player "Morsel? Uh oh"
        "The beasts voice best described as a rumble. In addition to the fear, you are surprised at how eloquently it appears to be able to speak."
        chimera "Yes, we hear that a lot"
        player "You can call me [e_name], I’d prefer not to be called a ‘morsel'"
        chimera "But it shall soon be the truth"
        $ chimera_visit = 1
        jump chimera_puzzle

    label chimera_with_hectate_result:
        if chimera_hectate_option == 1:
            jump DoNotEatMe

        elif chimera_hectate_option == 2:
            jump Assistance_hectate

        elif chimera_hectate_option == 3:
            jump Argument

    label Assistance_hectate:
        "Fearing your life is soon to be at an end, you bow your head and pray with all your heart for help."
        player "Lo to the watcher, with.."
        hectate_angry "Yes yes.  Power to see, we get it"
        "The figure of Hecate is immediately right beside you though at no point had you noticed any intervening movement."
        hectate_angry "You know the thing about being a watcher?!"
        hectate_angry "The idea is to ‘watch’.  In other words, not to have to intervene any time you get in trouble!"
        player "But, I think I’m about to die?"
        hectate_calm "Very much in keeping with the idea behind a ‘test’ child.  To see how ‘you’ handle adversity"
        hectate_insane "And even if you die, why not just resurrect?"
        player "I can’t, I’m mortal"
        hectate_insane "“Oh, that’s what that means?  That’s stupid.  You should be immortal, it’s lots more fun!"
        player "“I’ll think about it.  In the meantime, can you do something about this Chimera?"
        hectate_insane "“Hmm?  Oh fine, if you insist"
        "In fits of giggles, Hecate stares at the Chimera and it appears to you that the the entire world is suddenly bathed in the purest white light."
        "Blinded, you raise your hands in an attempt to shield your eyes but to no avail."
        "After what seems like an eternity, the light subsides and you vision slowly returns. Looking around you find Hecate has disappeared but more importantly, so is the Chimera!"
        "Finally, alone you proceed forth through the opposite door."





############   With Hectate      ##################################################







########################### With Huntress -> Hectate ##################################################

    #LABYRINTH ENTRANCE with Huntress -> Hectate
    label labyrinth_entrance_with_huntress:
    scene bg Labyrinth with dissolve
    #play entrance.mp3 sound
    play entrance "sound/entrance.mp3" fadein 2.0

    centered "{size=50}{color=#f4e842}Labyrinth Entrance with Huntress{/size}{/color}"
    "You've been walking for so long that you feel like you should've already arrived at your uncle’s house."
    "While being with the huntress, Elaheh, you've passed many strange things. Glowing eyes follow your every move. You finally come to a stop at a giant stone archway topped with the sigil of Ouroburos."
    "The snake eating its own tail."
    player "I don't understand"
    huntress "What's that my dear?"
    player "We should've arrived at my uncles or at least.."
    player "The end of the woods"
    player "Do you know where we are?"
    huntress "Oh quite well\nWe're in my home"
    player "Where I can't see it"
    "You look around to try spot a cottage but can't see anything."
    player "Is it"
    "Elaheh has disappeared."
    player "Elaheh! Elaheh!\nElaheh! Elaheh!"
    "You can't spot Elaheh but you can hear faintly laughter being carried by the breeze."
    player "Elaheh!"
    "You're beginning to grow fearful as you realize you are by yourself."

    "The mysterious huntress has abandoned you in a strange maze setting and you're becoming uneasy."
    "You're starting to assume that the huntress has lead you somewhere dangerous and that things out of sight might be watching."
    player "I've been lost for hours"
    player "I was saved from a Troll only to get lost"
    player "Just my luck!"

    "You spin around and see a woman standing just a few feet away. She wears a thin, translucent gown of red silk, cinched at the waist with a belt made of the same material."
    "In her right hand she holds a lit torch, though its flame seems to give off no light. In her left hand she holds a dagger pointed upward."
    "If not for her robe billowing softly, despite the complete absence of breeze, you might have believed she was a statue."
    "But you cannot tear your eyes away from her face. Or rather her faces. She has three of them."
    "The one facing you is beautiful, with golden eyes that seem to glow and a mouth curved into a small, knowing smile."
    "Where her left ear might normally be is another face."
    "Seemingly identical in every way to the first, but its expression fierce and scowling. On the right side, the third face laughed hysterically, though no sound could be heard."
    player "Wow!"
    player "What are you?"
    hectate_insane "I have wings, so I must be a chicken"
    hectate_angry "I have many faces I must be a demon"
    hectate_calm "No! I'm the god of your religion"
    player "The Nightmother"
    player "The Wheel Spinner"
    player "Hecate you've answered my prayers"
    hectate_calm "The gods provide no answers child"
    hectate_calm "We only pave paths"
    hectate_calm "You alone decide where to walk"
    player "Will you help me out of this place?"
    hectate_calm "That depends on the path you walk"
    hectate_angry "Some paths go off cliffs"
    hectate_insane "Some paths have cracks....bum cracks!"
    hectate_calm "Only one path will provide you what you want"
    player "I want the path that shows me the exit"
    hectate_angry "Well you won't find that path standing still!"
    hectate_calm "Come child we shall guide you"
    hectate_calm "You will find your path"
    hectate_insane "We're off to see the WIZARD the wonderful wizard of...wherever we are"
    hectate_angry "We're not off to find a wizard fool"
    hectate_calm "No...not a wizard\nWitch"
    jump junction_with_hectate
############################# With Huntress -> Hectate ##################################################






####################################Puzzle-Start#######################################################
    label chimera_puzzle:
        scene bg Chimera with dissolve

        #play Fire.mp3 sound
        play Fire "sound/Fire.mp3" fadein 2.0

        # Puzzle start time put into now1
        $ start_time = time.time()


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
    jump chimera_success

label giveup:

    $ k.set_sensitive(False)

    menu:
        "Are you sure you want to give up?"

        "Yes":
            python:
                k.hide()
            jump DoNotEatMe

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
            jump DoNotEatMe

    "Okay, here we go!"

    scene bg table

    python:
        k = Puzzle()
        k.sensitive = False
        k.show()

    jump continue
####################################Puzzle-End##########################






    #Chimera_success
    label chimera_success:
        scene bg Chimera with dissolve

        #Puzzle finish time put into now2
        $ elapsed_time = time.time() - start_time
        stop Fire fadeout 2.0

        if elapsed_time <= 60 and company_with_skull == 1 :
            $ user_point = user_point - 1
            $ chimera_skull_option = 3
            "You took [elapsed_time] seconds"
            "That was very quick!  However Bones had no opportunity to help, you lose 1 point"
            jump chimera_with_skull_result

        elif company_with_skull == 1:
            $ user_point = user_point + 1
            $ chimera_skull_option = 2
            "You took [elapsed_time] seconds"
            "You are too slow!  However Bones now has the opportunity to help, you gain 1 point"
            jump chimera_with_skull_result

        elif elapsed_time <= 60 and company_with_hectate == 1 :
            $ user_point = user_point + 1
            $ chimera_hectate_option = 3
            "You took [elapsed_time] seconds"
            "That was very quick! Hecate is impressed, you gain 1 point"
            jump chimera_with_hectate_result

        elif company_with_hectate == 1:
            $ user_point = user_point - 1
            $ chimera_hectate_option = 2
            "You took [elapsed_time] seconds"
            "You are too slow, As Hecate must now help you, you lose 1 point"
            jump chimera_with_hectate_result


    #(5)-1. Minotaur
    label minotaur:

        scene bg Minotaur with dissolve

        #play Bull.mp3 sound
        play Bull "sound/Bull.mp3" fadein 2.0

        centered "{size=50}{color=#f4e842}MINOTAUR{/size}{/color}"
        "This room, unlike almost all that has preceded it, is spectacular in its opulence."
        "Closing the door behind you, you begin to feel nervous."
        "Due to its lavishness you feel as if you are not actually permitted to enter, as if it is off-limits."
        "Countless draperies adorn the walls, hiding the cold grey stone behind."
        "The floor is littered with innumerable throw pillows, rugs and all manner of softness."
        "Torches mounted on walls bathing the grandiose display in warm and soothing light."
        "All manner of colours are represented in the scene, from gold framed seats to green and blue rugs...all but the colour red you cannot help but notice and are unsure as to why."
        "You contemplate the risks involved with laying down in what appears to be a particularly comfortable bed."
        player "Maybe this is just for me to have a rest? Maybe there’s no horrible monster in this room?"
        "Stomp"
        "The entire room seems to shake."
        player "Why did I say it? Why did I have to say it?"
        "Stomp"
        "A booming thud echoes through your skull, and whatever it is, it is getting closer"
        "Stomp"
        "Stomp"
        "Stomp"
        "From the room beyond, you spy an enormous beast emerging from a tunnel opposite you. Despite the large size of the tunnel, the creature still needs to bend down so that it may fit through."
        "With the head of a particularly large bull, the creatures torso resembles that of an extremely muscular man."
        "This ends however with its, also muscular, legs jointed in the reverse of that seen in a human, ending in a pair of cloven hoofs."
        "In its powerful arms it carries the biggest battleaxe you have ever seen, one side looking incredibly sharp and the other ending in a particularly vicious looking spike."
        player "Uh oh"
        "The creature, focusing its gaze upon you, appears to be sizing you up. You suspect, from the sight of its oversized biceps that you would not last long in any form of combat."
        "The creature, having now cleared the tunnel simply stands passively. Appearing to wait to see what you will do"
        player "Uh, hello there, giant...cow?"
        "It snorts angrily, apparently unhappy with being called a cow."
        minotaur "You ‘ere for the apple then?"
        player "Is there an answer that won’t make you hit me with that axe?"
        minotaur "Eh? Uh...not really. I like hittin’ things with axes"
        player "So, is that all you like?"
        minotaur "Nope, protectin’ the apple too"
        player "By hitting things with axes.."
        minotaur "By hittin’ things with axes"
        player "Well, it’s always good to see someone with their priorities in order. Do you have a name?"
        "The beast concentrates, quite obviously using any and all mental capacity available to it. Finally, as if finally hitting on an idea worthy of shouting “Eureka”, the creature proudly exclaims;"
        minotaur "Minnow-Tore!"
        player "Did you mean Minotaur?"
        "Clearly quite pleased with itself having come up with the answer, it ignores you and takes a test swing with his axe. Cleaving the air with practiced efficiency, it appears satisfied with the axe’s weight and balance."
        player "So how long have you guarded the apple?"
        minotaur "Eh?"
        player "How long have you been hitting things with axes?"
        minotaur "Oh, long as this place has been around, and always will"
        player "Always will? So, you’ll never die?"
        minotaur "Nope, Witch says so!"
        player "That must be nice. You get to live forever, doing what you love"
        minotaur "It’s a livin"
        "And with that, the Minotaur seems to decide it has exhausted any further need for conversation, having determined that you are an obvious threat to the apple. It begins to advance on you, a murderous gleam in it’s terrifying, if slightly dull, eyes."

        #Sound Bull.mp3 Stop
        stop Bull fadeout 2.0

    #(6)Branch: 'Reason With it' or 'I am only here for a rest'
    menu:
        "1. Try to reason with it":
            $ minotaur_option = 1
            $ user_point = user_point + 1

        "2. I'm only here for a rest!":
            $ minotaur_option = 2
            $ user_point = user_point - 1


    label minotaur_result:
        if minotaur_option == 1:
            jump minotaur_reason_with

        elif minotaur_option == 2:
            jump minotaur_attack

    label minotaur_reason_with:
        player "Wait a second!"
        minotaur "What?"
        player "I’m not a threat to the apple!"
        minotaur "Yeah yeah, you all say that"
        "Scrambling frantically backward, you search your mind for any argument that would convince this monster that it did not have to kill you."
        "Thinking back, you sift through as much information as you are able, making as many logical conclusions as possible though you have relatively little to go on."
        "The Minotaur is more than a little slow on the uptake. Check."
        "It has determined you are a threat to the apple based on very little. Check."
        "It’s axe looks incredibly sharp. Check, if slightly less helpful."
        "It will seemingly live forever, well at the least it thinks so. Check."
        "And with that, you think you may have an idea, but this will be a long shot."
        player "But it’s true! I’m actually trying to save the apple...from you!"
        "That immediately halt’s the Minotaur’s advance, clearly confused."
        minotaur "Eh, what? What you talkin’ about?"
        player "You live here, right nearby the apple right?"
        minotaur "Yeah"
        player "And you live forever right?"
        minotaur "Yup"
        player "Well by that token, you pose the biggest threat!"
        minotaur "Uh..."
        player "Well think about it. If you stretch out the arrow of time to that of the infinite, anything that is possible, however remote the possibility, will certainly happen eventually"
        player "Given that you live in such close proximity to the artifact, it seems the most likely that you, and not I, even if only accidentally, will be the one that somehow damages the apple!"
        "Even as you finish speaking you realise that this would be a stretch."
        minotaur "...Huh?"
        player "You live long and hurt apple"
        minotaur "Ah! Why didn’t you just say so?!"
        "And with that the Minotaur begins to spin his axe, effortlessly twirling the end with his wrist in an ever faster circle."
        "Now introducing figure eights and cross cut patterns, so fast that you have difficulty following, you begin to back away fearing that ‘Minnow-Tore’ has decided to kill you anyway."
        "Before you can blink you suddenly hear a sickening squelch and the Minotaur’s head cleanly separates from its body."
        "While the body falls to its knees and slumps forward, the head, falling nearby, lands with an almost self satisfied expression, as if proud of a job well done."
        "You are dumbstruck at such blind adherence and devotion to such singular purpose."
        "Having ended its own life based purely on the idea that it could possibly pose a threat to that which it has been set to guard leaves you shaking your head as you skirt around the body and head for the tunnel."
        player "I...did not see that coming"
        jump witch

    #(6)-1. Minotaur Attack
    label minotaur_attack:
        player "Wait a second!"
        minotaur "What?"
        player "Just, can you stop? I’m only here to rest, this all looks amazingly comfortable."
        minotaur "Not for you!"
        "The Minotaur advances and begins to swing its axe."
        "Now no longer mere test swings, you feel the breeze from displaced air as the razored edge passes mere millimeters from your head."
        "You jump backwards in an attempt to gain some distance but the beast keeps up the pressure, forcing you to dive to the side as the axe head crashes down right where you were standing just a second earlier."
        "Now enraged, the Minotaur’s attacks become more erratic. The axe head smashing chairs and creating deep gouges on the previously pristine furniture."
        "With a roar, the creature bow drops it’s head and drops down on all fours, his back leg scraping backward in an effort to gain purchase."
        player "I think I know what comes next..."


    #(7)Branch: Dodge or 'Remain Still'
    menu:
        "1. Dodge":
            $ minotaur_attack_option = 1

        "2. Remain Still":
            $ minotaur_attack_option = 2
            $ user_point = user_point + 1


    label minotaur_attack_result:
        if minotaur_attack_option == 1:
            "With an idea of what is about to happen, you get ready to jump to the side in an effort to dodge."
            "As expected, the beast charges more quickly than a creature of this size has any right to. It however, appears to have expected your dodging attempt and adjusts its path accordingly."
            "Unfortunately, having committed to dodging you cannot help but jump right into its path and the Minotaur barrels directly into you."
            "Your only saving grace is that the impact was too fast for you to be able to feel your demise."
            "END"
            scene bg credits with dissolve
            centered "{size=50}{color=#f4e842}END{/size}{/color}"
            return

        elif minotaur_attack_option == 2:
            "With an idea of what is about to happen, you have an idea that the Minotaur would most likely be used to having its targets try to jump aside."
            "Summoning all your bravery, you make yourself appear to get ready to jump."
            "As expected, the beast charges more quickly than a creature of this size has any right to, you are however resolved to follow through with your plan."
            "Falling for your feint, the Minotaur adjusts its charge towards where it believes you will soon be."
            "You however simply stand your ground and close your eyes, hoping against hope."
            "You soon hear an almighty crash, feeling the vibrations through the floor and fearing the entire room has come down around you, you open your eyes."
            "Behind you the stone wall appears cracked and broken as if hit with tremendous force."
            "Lodged within appears the Minotaurs body slumped against the rubble, head still wedged within the stone."
            "Breathing a sigh of relief at having bested the creature as if by pure luck."
            player "It didn’t have to end this way..."
            "You shake you head and head off towards the tunnel at the opposite end of the room"
            jump witch


    label witch:
        scene bg Witch with dissolve

        #play thunder.mp3 sound
        play thunder "sound/thunder.mp3" fadein 2.0

        centered "{size=50}{color=#f4e842}WITCH{/size}{/color}"
        "After contesting with the mermaids, chimera and minotaur you fear that the worst is still not behind you."
        "You've entered into a dark valley. Everything in this area has a rotten appearance, the flowers and vines have thorns and the sky is black with clouds."
        "In the centre of the valley stands a tree with a twisted monster in its centre."



        #Sound thunder.mp3 Stop
        stop thunder fadeout 2.0

    label final_dicision:
        if (company_with_hectate == 1 and user_point >= 4):
            jump good_ending_with_hectate

        elif (company_with_hectate == 1 and user_point <= 3 and user_point >=0):
            jump neutral_ending_with_hectate

        elif (company_with_hectate == 1 and user_point < 0):
            jump bad_ending_with_hectate

        elif (company_with_skull == 1 and user_point >= 4):
            jump good_ending_with_skull

        elif (company_with_skull == 1 and user_point <= 3 and user_point >=0):
            jump neutral_ending_with_skull

        elif (company_with_hectate == 1 and user_point < 0):
            jump bad_ending_with_skull

        else:
            scene bg credits with dissolve
            centered "{size=50}{color=#f4e842}END{/size}{/color}"
            return


    label good_ending_with_hectate:
        centered "{size=50}{color=#f4e842}GOOD ENDING with Hectate{/size}{/color}"
        treewitch "GIRL"
        treewitch "[e_name]"
        treewitch "You dare approach ME?!"
        player "Bones, what is this thing"
        "A beautiful huntress appears, walking towards you from behind the tree."
        huntress "That THING is MY essence"
        huntress "That THING is more powerful than any GOD"
        huntress "This form, MY huntress form, is merely a shade"
        huntress "A shade of THIS"
        huntress "I've watched you through the trees\nFelt you with my roots\nYou're NOTHING but FOOD for my spirit"
        hectate_angry "Your magic has become foul\nGuard your tongue Elaheh"
        hectate_calm "You may be powerful, but don't presume to compare yourself to me"
        hectate_calm "To me, you are as an insect and I shall not suffer the insult that you would delude yourself otherwise"
        hectate_calm "Had I wished you to die; your shade, your life tree, all that you are would burn"
        hectate_angry "And you shall"
        treewitch " -demonic screech-"
        huntress "LIAR! You yet require a disciple. And only I have the power required."
        hectate_calm "And I have one, [e_name]"
        player "Me?"
        hectate_calm "Indeed, throughout this ordeal you have shown the required spirit and intellect which would serve you well as my disciple"
        "You look over at the witch and huntress, stunned expressions on their faces."
        player "Will I end up like them?"
        hectate_calm "No child, you shall become what you wish. Their likeness is but only a corruption of my power"
        "And with that, Hecate glares at the witch and huntress. Immediately, the pair begin to burn, as if immolated from within. With screams of agony, the huntress and the entire tree, including the apple are reduced to nothing but piles of ash."
        player "But...my mother?"
        hectate_calm "Again, shall be as you wish. Your power will be enough that you may save her"
        player "I thought I needed the apple for that?"
        hectate_calm "The apple is only the physical representation of my power. Should you agree, the apple will be remade"
        player "Then I agree! Please take me on as your disciple!"
        hectate_calm "As it shall be, so it now is"
        "And with that you feel your body filling with power incalculable. You feel as if you have the ability to do anything, and further the innate knowledge with which to do so."
        "You reach out with your mind and can feel the surrounding countryside, as if it is only an extension of your own body. You can feel the sickness within your mother and know that you have within you the power to heal her at a whim."
        "You know, finally, that everything is going to be okay."
        scene bg credits with dissolve
        centered "{size=50}{color=#f4e842}END{/size}{/color}"

        return

    label neutral_ending_with_hectate:
        centered "{size=50}{color=#f4e842}MEDIOCRE ENDING with Hectate{/size}{/color}"
        treewitch "GIRL"
        treewitch "[e_name]"
        treewitch "You dare approach ME?!"
        player "Bones, what is this thing"
        "A beautiful huntress appears, walking towards you from behind the tree."
        huntress "That THING is MY essence"
        huntress "That THING is more powerful than any GOD"
        huntress "This form, MY huntress form, is merely a shade"
        huntress "A shade of THIS"
        huntress "I've watched you through the trees\nFelt you with my roots\nYou're NOTHING but FOOD for my spirit"
        hectate_angry "Your magic has become foul\nGuard your tongue Elaheh"
        hectate_calm "You may be powerful, but don't presume to compare yourself to me"
        hectate_calm "To me, you are as an insect and I shall not suffer the insult that you would delude yourself otherwise"
        hectate_calm "Had I wished you to die; your shade, your life tree, all that you are would burn"
        hectate_angry "And you shall"
        treewitch "-demonic screech-"
        huntress "LIAR! You yet require a disciple. And only I have the power required."
        hectate_calm "And one day I may have one, though not today"
        "And with that, Hecate glares at the witch and huntress. Immediately, the pair begin to burn, as if immolated from within. With screams of agony, the huntress and the entire tree, including the apple are reduced to nothing but piles of ash."
        player "But...my mother?"
        hectate_calm "What will happen, will happen"
        player "You know, for a minute there I thought you would make me your new disciple"
        hectate_calm "Not quite, you’re actions though commendable still leave something to be desired"
        hectate_calm "As such, I have disposed of Elaheh for you, and will assist you in escaping this labyrinth, however that is where my assistance will end."
        "And with that, Hecate waves her hand and you are immediately teleported outside of the labyrinth. Hecate is no longer with you and you find that you have been ported to the outskirts of your uncle’s farm."
        "As there is nothing else for it, you set off to see your uncle."
        scene bg credits with dissolve
        centered "{size=50}{color=#f4e842}END{/size}{/color}"
        return

    label bad_ending_with_hectate:
        centered "{size=50}{color=#f4e842}BAD ENDING with Hectate{/size}{/color}"
        treewitch "GIRL"
        treewitch "[e_name]"
        treewitch "You dare approach ME?!"
        player "Bones, what is this thing"
        "A beautiful huntress appears, walking towards you from behind the tree."
        huntress "That THING is MY essence"
        huntress "That THING is more powerful than any GOD"
        huntress "This form, MY huntress form, is merely a shade"
        huntress "A shade of THIS"
        huntress "I've watched you through the trees\nFelt you with my roots\nYou're NOTHING but FOOD for my spirit"
        hectate_angry "Your magic has become foul"
        hectate_angry "Guard your tongue Elaheh"
        hectate_calm "You may be powerful, but don't presume to compare yourself to me"
        hectate_calm "To me, you are as an insect and I shall not suffer the insult that you would delude yourself otherwise"
        hectate_calm "Had I wished you to die; your shade, your life tree, all that you are would burn, and one day shall"
        treewitch "-demonic screech-"
        huntress "LIAR!"
        hectate_calm "I lead [e_name] to you"
        hectate_calm "Had she been worthy, you would die today"
        huntress "She couldn't slay me"
        hectate_calm "You are correct"
        hectate_calm "Her spirit is corrupted, her intellect weak"
        hectate_calm "I shall leave her for you, to do with as you wish"
        player "NO PLEASE HECATE!"
        hectate_calm "The gods only pave the path"
        hectate_calm "But you must decide where to walk"
        player "Please! Lo to the wat-"
        hectate_angry "Do not pray to me child!\nThe girl deserves this fate\nOne day Elaheh you will meet yours"
        "Hecate fades away."
        huntress "You’re quite young\nYou'll fuel my essence for decades"
        player "No!"
        "The huntress fades away as does the twisted tree."
        player "Where are you!\nI'll find my way out"
        "You start to cry."
        player "You can't keep me here forever!"
        centered "{size=40}{color=#f4e842}60 years later{/size}{/color}"
        "Sixty years has gone by and your skin and muscles have deteriorated but you've found the exit. Your skeletal frame collapses in a bog and the huntress appears before you."
        player "Hey please help\nI've been stuck in this labyrinth since I was a girl"
        huntress "Now you're just bones"
        huntress "How can I help a pile of bones"
        player "Please just turn me into dust"
        huntress "Okay..but first I want you to help me"
        scene bg credits with dissolve
        centered "{size=50}{color=#f4e842}END{/size}{/color}"

        return


    label good_ending_with_skull:
        centered "{size=50}{color=#f4e842}GOOD ENDING with Bones{/size}{/color}"
        treewitch "GIRL"
        treewitch "[e_name]"
        treewitch "You dare approach ME?!"
        player "Bones, what is this thing"
        "A beautiful huntress appears, walking towards you from behind the tree."
        huntress "That THING is MY essence"
        huntress "That THING is more powerful than any GOD"
        huntress "This form, MY huntress form, is merely a shade"
        huntress "A shade of THIS"
        huntress "I've watched you through the trees\nFelt you with my roots\nYou're NOTHING but FOOD for my spirit"
        bones "Wait!"
        huntress "Why? Is this not what you wanted?"
        player "Wait, what?"
        bones "Yeah, well kinda. You know how I’ve always wanted to die?"
        player "Oh that’s just great..."
        bones "Yeah....sorry. I hadn’t really intended for you to be part of that deal..."
        player "Hardly helps me now does it?"
        "Bones seems to think for a brief minute."
        bones "I have an idea, when I say the word, go for the apple!"
        huntress "Well? It’s not often people visit just to talk amongst themselves"
        bones "I’ve been thinking, I’d like to renegotiate the terms of our deal"
        huntress "To what? And why? I hold all the cards"
        "Bones proceeds to talk with the huntress in a largely nonsensical manner. You realise Bones is simply trying to distract the witch to take her attention from you."
        "Slowly approaching the tree and the hanging apple you occasionally tune in to the conversation;"
        bones "And that’s why mice are actually the true rulers of the Earth, not to mention that dolphins..."
        "You shake your head, wondering how the conversation got to that, you notice that you have managed to sneak close to the apple"
        huntress "Enough talk!"
        "The huntress has noticed that you have been edging closer to the source of her power and begins to raise her bow"
        huntress "Wait!"
        "Time seems to slow as adrenaline courses through your body. You immediately begin to run at full speed towards your goal."
        "As the huntress released an arrow, you jump. Leaping with all your might you just manage to grasp your fingers around the golden orb."
        "As you pull the apple from the tree the loosed arrow vanishes in mid air"
        huntress "Noooo!"
        bones "YES!"
        "It seems evident that the huntress’s powers were intrinsically linked to the apple. Having gained possession you immediately feel your body filling with power incalculable."
        "You feel as if you have the ability to do anything, and further the innate knowledge with which to do so."
        "And with that, you glare at the witch and huntress. Immediately, the pair begin to burn, as if immolated from within."
        "With screams of agony, the huntress and the entire tree are reduced to nothing but piles of ash."
        "You turn to Bones"
        player "Thank you for your help Bones, I owe you...despite your ‘agreement’. Do you still wish to die?"
        bones "Eventually yes, but I kind of want to see how this all plays out for the moment"
        player "As you wish. But why do I seem to have all this power? Didn’t you once get the apple?"
        bones "I only took a small bite, it must work differently if you actually possess the apple. Weird"
        "You reach out with your mind and can feel the surrounding countryside, as if it is only an extension of your own body."
        "You can feel the sickness within your mother and know that you have within you the power to heal her at a whim."
        "You know, finally, that everything is going to be okay."
        scene bg credits with dissolve
        centered "{size=50}{color=#f4e842}END{/size}{/color}"

        return

    label neutral_ending_with_skull:
        centered "{size=50}{color=#f4e842}MEDIOCRE ENDING with Bones{/size}{/color}"
        treewitch "GIRL"
        treewitch "[e_name]"
        treewitch "You dare approach ME?!"
        player "Bones, what is this thing"
        "A beautiful huntress appears, walking towards you from behind the tree."
        huntress "That THING is MY essence"
        huntress "That THING is more powerful than any GOD"
        huntress "This form, MY huntress form, is merely a shade"
        huntress "A shade of THIS"
        huntress "I've watched you through the trees\nFelt you with my roots\nYou're NOTHING but FOOD for my spirit"
        bones "Wait!"
        huntress "Why? Is this not what you wanted?"
        player "Wait, what?"
        bones "Yeah, well kinda. You know how I’ve always wanted to die?"
        player "Oh that’s just great..."
        bones "Yeah....sorry. I hadn’t really intended for you to be part of that deal..."
        player "Hardly helps me now does it?"
        "Bones seems to think for a brief minute."
        bones "I have an idea, when I say the word, go for the apple!"
        huntress "Well? It’s not often people visit just to talk amongst themselves"
        bones "I’ve been thinking, I’d like to renegotiate the terms of our deal"
        huntress "To what? And why? I hold all the cards"
        "Bones proceeds to talk with the huntress in a largely nonsensical manner. You realise Bones is simply trying to distract the witch to take her attention from you."
        "Slowly approaching the tree and the hanging apple you occasionally tune in to the conversation;"
        bones "And that’s why mice are actually the true rulers of the Earth, not to mention that dolphins..."
        "You shake your head, wondering how the conversation got to that, you notice that you have managed to sneak close to the apple"
        huntress "Enough talk!"
        "The huntress has noticed that you have been edging closer to the source of her power and begins to raise her bow"
        huntress "Wait!"
        "Time seems to slow as adrenaline courses through your body. You immediately begin to run at full speed towards your goal."
        "As the huntress released an arrow, you jump. Leaping with all your might you reach out for the golden orb however it is at this moment the arrow hits its mark."
        "The arrow, filled with a magical energy, strikes Bones right between the eyes and disintegrates him instantaneously."
        "You simultaneously grasp your hands around the apple and immediately feel your body filling with power incalculable."
        "You feel as if you have the ability to do anything, and further the innate knowledge with which to do so."
        "However due to the speed and suddenness of events, all you can think to do is to teleport yourself outside of the labyrinth."
        "The very next second you land back on the ground, but are no longer where you once were. Looking around you see that you are actually on the outskirts of your uncle’s farm."
        "While you are sad that Bones’ ‘life’ has ended, there is nothing else for it, you set off to see your uncle."
        scene bg credits with dissolve
        centered "{size=50}{color=#f4e842}END{/size}{/color}"
        return

    label bad_ending_with_skull:
        centered "{size=50}{color=#f4e842}BAD ENDING with Bones{/size}{/color}"
        treewitch "GIRL"
        treewitch "[e_name]"
        treewitch "You dare approach ME?!"
        player "Bones, what is this thing"
        "A beautiful huntress appears, walking towards you from behind the tree."
        huntress "That THING is MY essence"
        huntress "That THING is more powerful than any GOD"
        huntress "This form, MY huntress form, is merely a shade"
        huntress "A shade of THIS"
        huntress "I've watched you through the trees\nFelt you with my roots\nYou're NOTHING but FOOD for my spirit"
        bones "What about our deal?"
        player "WHAT?!"
        huntress "Ah yes, you wish to die"
        bones "Please, Yes"
        bones "This place has taken my essence, taken my flesh\nThere's nothing left of me to take\nAnd given you a new morsel to feed upon\n"
        bones "Now please...let me die"
        huntress "Your wish shall be granted"
        player "You trapped me!\nYou lied to me!"
        bones "I'm sorry [e_name] but I can't keep going on like this"
        player "Was there even an apple?"
        bones "That part was true, I ate it from-"
        "Huntress uses her magic and disintegrates Bones"
        huntress "You’re quite young"
        huntress "You will fuel my essence for decades"
        huntress "Until you too are like that silly skull"
        player "No!"
        "The huntress fades away as does the twisted tree."
        player "Where are you!\nI'll find my way out"
        "You start to cry."
        player "You can't keep me here forever!"
        centered "{size=40}{color=#f4e842}60 years later{/size}{/color}"
        "Sixty years has gone by and your skin and muscles have deteriorated but you've found the exit."
        "Your skeletal frame collapses in a bog and the huntress appears before you."
        player "Hey please help"
        player "I've been stuck in this labyrinth since I was a girl"
        huntress "Now you're just bones"
        huntress "How can I help a pile of bones"
        player "Please just turn me into dust"
        huntress "Okay..but first I want you to help me"
        scene bg credits with dissolve
        centered "{size=50}{color=#f4e842}END{/size}{/color}"
        return




    #(4)-2.Sirens
    label sirens_with_hectate:
        scene bg Sirens with dissolve

        #play waves.mp3 sound
        play waves "sound/waves.mp3" fadein 2.0

        centered "{size=50}{color=#f4e842}SIRENS with Hectate{/size}{/color}"
        "After twisting through various channels and paths you can hear faintly a song lightly carrying in the breeze. The music is lulling you towards an opening which reveals a large body of water. Three mermaids sit on rocks."
        mermaid "Sailors washed up on the shore​♪\nGuided by her sweet lure ​♫\nShe calls you from your safe ships​♪Nice face but mean tricks​♫"
        mermaid "The ocean licks its blue lips​♪\nHearing splashes and kicks​♫\nThe sailors song sings no more​♪\nWashed up on the shore​♫"
        player "You sang that beautifully"
        mermaid "Thank you gorgeous"
        hectate_calm "Sounds like that song came from personal experience"
        mermaid "The song was created by our mother ​Melpomene"
        hectate_calm "The siren of the eastern sea"
        mermaid "Yes, the very same"
        mermaid "Does the dear girl wish to cross our lake?"
        player "Yes I do..Miss?"
        mermaid "Molpe\nIs the girl your friend Hecate?"
        hectate_calm "No"
        mermaid "Is the girl your enemy?"
        hectate_calm "No"
        mermaid "Can we swim with her?"
        hectate_calm "That is the girls choosing"
        player "I can't swim"
        mermaid "That's okay we can show you"
        player "Maybe another time"
        player "I can see a boat in the middle of the lake\nCould you get it for us?"
        mermaid "Hop in the water and come get it"

        menu:
            "1. You decide to swim":
                $ sirens_option_with_hectate = 1

            "2. You are not going to swim":
                $ sirens_option_with_hectate = 2

        label sirens_result_with_hectate:
            if sirens_option_with_hectate == 1:
                hectate_calm "Foolish girl"
                hectate_calm "I thought you had more sense than swimming with mermaids"
                "Once in the water the mermaids were pleasant until you couldn't touch the ground. Then they drowned you and ate your flesh."
                scene bg credits with dissolve
                centered "{size=50}{color=#f4e842}END{/size}{/color}"
                return

            elif sirens_option_with_hectate == 2:
                player "I'm sorry but as I said I can't swim"
                player "Is there anything else I can do"
                mermaid "You liked our singing?"
                player "Very much"
                mermaid "I'll sing the notes and solve the quiz."


        #Background music temporarily stop
        stop music fadeout 1.5

        #Sound waves.mp3 Stop
        stop waves fadeout 2.0

        #Mermaid Song Quizz Start#############################################################
        "Listen and watch carefully Mermaid song video"

        play movie "Mermaid song.ogv" noloop
        show movie with dissolve
        "Listen and watch carefully Mermaid song video"
        stop movie
        hide movie with dissolve
        "Quiz: Which is the correct order of musical notes?"
        #Mermaid Song Quizz Finish#############################################################

        #Play background music again
        play music "sound/BackgroundMusic.mp3" fadein 1.5

        #play waves.mp3 sound
        play waves "sound/waves.mp3" fadein 2.0

        #Call Options for Mermaid Song Quizz
        call screen imagemap_with_hectate

        #When user has right answer
        label sirens_with_hectate2:
        $ user_point = user_point + 1
        mermaid "That was beautiful!"
        mermaid "I'll get you the boat"
        player "Thanks"
        mermaid "Just to stop you singing"
        hectate_calm "With a voice like yours you would make a poor witch"
        hectate_calm "I guess singing isn't everything\nIt's character that really matters\nBeing a good witch requires some things"
        hectate_calm "You need a clear tone and powerful spirit\nThe witch of these woods can sing beautifully\nI mentored her for awhile.."
        hectate_calm "Until she decided to defy my laws\nShe made this place\nThis abdominal place\nDark magic..spells of corruption"
        hectate_angry "When you break the laws of man you may evade capture or death"
        hectate_angry "When you break the laws of gods not even in death will you evade judgment"
        hectate_angry "SHE WILL BE JUDGED"
        player "........"
        hectate_calm "Excuse me"
        hectate_calm "I lost control for a second"
        hectate_insane "Just breath we don't want another Atlantis incident"
        player "Maybe we should keep going"
        hectate_calm "I agree child"

        #Sound waves.mp3 Stop
        stop waves fadeout 2.0

        jump monster_visit_check




    #(2)-2.swamp
    label swamp:

    scene bg Swamp with dissolve

    #play swamp.mp3 sound
    play swamp "sound/swamp.mp3" fadein 2.0

    centered "{size=50}{color=#f4e842}SWAMP{/size}{/color}"
    "The path you've followed has become little more than a slushy muck. Every step you take sucks yous feet down into the mud and it takes enormous effort pull a foot free to take a step forward."
    "You are filled with a sense of dread. Menacing eyes look out at you from between the rotting branches and from beneath the stagnant green water that seems to grab at your legs as you move."
    player "I knew I should've gone the other way!"
    player "I'm turning into a mosquito smorgasboard"
    player "By the looks of this swamp, hopefully that's the worst that happens"
    bones "Try living here sweetheart! It's a dry biscuit I can assure you."
    "The skeleton laying half-submerged in the bog turns it’s head and you swear, though it has no eyelids, that it just winked at you."

    player "AHHHHHHHHH"
    bones "AHHHHHHHHH"
    player "AHHHHHHHHH"
    bones "AHHHHHHHHH Screaming is fun!"

    "You turn to run."

    bones "Wait little lass, I'm not bad to the bone, trust me."
    player "I've lost my mind! it's this swamp! I don't know where I'm going."
    bones "I've lost my mind, my muscles, most recently my arm to a cheeky mutt! Stupid dogs..."
    player "This isn't possible!"
    bones "Ohhh I wish it wasn't, I had a bite of a golden apple.  ONE.MEASLY. BITE, if only I had eaten the whole thing"
    bones "Maybe then I would have some skin. The magic has preserved me when clearly I should be dead."
    bones "Gods I wish I was dead. Imagine all the things I could do, like not exist."
    bones "Gods I wish I didn't exist."
    player "That's what you wish for?"
    player "That's silly, why not wish you had the entire apple."
    bones "HEY! you watch mosquitoes eat your flesh and a mangy dog run away with your arm and see what YOU wish for."
    bones "Geez."
    player "Uh, sorry, I guess, Mr...pile of.. Bones"
    bones "Quite okay lassie"
    player "Whelp, I’d best be on my way"
    bones "no, no, no, no, no, no Oh gods no. Please don't leave me here like this."
    player "I'm sorry but I'm on my way to see my uncle, my mother is sick and I need to tell him"
    player "Plus mother told me not to talk to strangers AND I don't think I can help you"
    bones "Firstly, I'm not a stranger, I like to think we're friends, best friends, I'm your best friend Bones. What you see is what you get, no skeletons in my closet!"
    "Bones tries to smile. Unsuccessfully."
    player "I'm truly"
    bones "Secondly, please there is a part two"
    player "I have to see my"
    bones "I CAN HELP YOUR MOTHER"
    player "How could YOU, a skeleton, a pile of bones incapable of anything help my mother"
    bones "THE APPLE..THE GOLDEN APPLE, please sweet girl, please, look at me I should be dead but thanks to a single bite, TA-DUH, here lies old bones"
    player "Yeah, here lies 'wishes he was dead' apparently my best friend, old bones"
    bones "Yes I know I don't look good for a skull in his forties but I only had a SINGLE bite"
    bones "That bite has saved me from the clutches of death. Imagine what an entire apple could do for your mother"
    player "How do I know you're not lying?"
    bones "When was the last time you talked to a skull?"
    player "Well-"
    bones "Never!...well at least I hope you haven't"
    bones "Makes you sound crazy if you have"
    player "If I do want to get this apple, what do you want in return?"
    bones "Your company"
    bones "Exciting conversations"
    bones "Maybe you could figure out a way to kill me, when you've got a free minute?"

    #Sound swamp.mp3 Stop
    stop swamp fadeout 2.0

    #(9)Branch: 'Partner with Skull' or 'Decline Skull'
    menu:
        "1. Partner with Skull":
            $ swamp_option = 1

        "2. Decline Skull":
            $ swamp_option = 2

    label swamp_result:
        if swamp_option == 1:
            jump partner_with_bones

        elif swamp_option == 2:
            jump decline_skull

    label partner_with_bones:
    player "Deal"
    bones "I knew you were a smart girl, from the first moment I laid my eye sockets on you"
    player "Sigh"
    bones "...."
    bones "Okay so if we're going to get this Golden Apple I'm going to need you to take me somewhere"
    player "Where?"
    bones "A labyrinth, deary\nOh and what was your name littlein?"
    player "[e_name]"
    bones "Funny... I think I know somebody by that name"
    player "What's your name?"
    bones "M-m-Myers, no that's not it, maybe Mark, uhhh"
    player "You can't remember your name"
    bones "Well the dog ate my brain too, OKAY! I'm as empty as a fools bottle, half simple, donkey kicked! Alright!"
    player "Sorry, uhm, Bones"
    bones "Geez.. no I'm sorry uh"
    player "[e_name]"
    bones "YES, [e_name], I was getting there"


     #LABYRINTH ENTRANCE
    label labyrinth_entrance_with_skull:
    scene bg Labyrinth with dissolve
    #play entrance.mp3 sound
    play entrance "sound/entrance.mp3" fadein 2.0
    centered "{size=50}{color=#f4e842}Labyrinth Entrance with Bones{/size}{/color}"
    "You've been walking for what feels like forever. The forest feels like it’s crowding in around you on all sides, funneling you always forward."
    "Suddenly, the forest opens out into an eerie clearing. A giant open archway with high walls stands before you."
    player "Finally we made it! I was afraid I'd look like you when we found the entrance"
    bones "This isn't the entrance"
    player "WHAT!"
    player "WE'VE BEEN WALKING FOR AGES"
    player "YOU SAID WE WERE CLOSE"
    bones "We are close"
    player "YOU'VE BEING SAYING THAT FOR AGES TOO"
    player "Now we come to a GIANT entrance and were still not there"
    player "STUPID SKULL I SHOULD THROW YOU INTO THE JAWS OF-"
    bones "We are close, because we're actually here"
    bones "I just wanted to rattle your bones"
    bones "Tickle your funny bone"
    player "One more bone joke- and I swear to the gods"
    bones "Oh lighten up ​[e_name]"
    bones "You'd think a girl with a name like yours would have a sense of humour, hmph"
    player "Grrr"
    "You look up and see a snake sigil. The snake is eating its own tail."
    player "The Ouroboros"
    bones "Yes the snake that eats its own tail. The symbol of the infinite"
    bones "This maze is like that snake. Twisting, turning."
    bones "And for some, treacherous"
    player "Well you've been inside and found the apple"
    player "How hard can it be?"
    bones "Yes I found the apple"
    bones "I bit that apple"
    bones "That one bite sustained me. Sustained me for years while I withered away..."
    bones "All while searching for the exit"
    "You're creeped out"
    bones "Don't worry! You found me on the outside didn't ya"
    player "Yeah.... as a pile of bones"


    #JUNCTION WITH BONES
    scene bg Junction with dissolve
    centered "{size=50}{color=#f4e842}Junction with Bones{/size}{/color}"
    "You travel the twisting and turning path for what must be hours. It’s impossible to know, you can’t see the sun through the dense canopy."
    "Finally, you come to a junction. It is unique only because it is the only time you have had to think about which way to go in what feels like forever."

    bones "Then I said to her I don't know how I got the warts."
    bones "She said that I had been...uhhh"
    bones "Wait..how old are you?"
    player "I'm twelve"
    bones "Oh right...um she said I had been"
    bones ".............."
    bones "Holding..hands..YES!"
    bones "Holding hands with the maiden next door"
    player "Bones please shut up"
    bones "Sorry I'm over sharing again. I've been so lonely"
    player "Where should we go"
    bones "Do I look like a magic 8 ball?"
    player "You look like a useless skull I'll throw away in a minute"
    bones "That way"
    player "What way?"
    bones "If I had hands I would be pointing that way, down the middle"
    bones "When in doubt, chose the straight route"
    player "These is no straight route!"
    player "Left or Right"
    bones "Sorry, I don't have eyes either"
    player "Wait...You do know where we're going?"
    bones "Well...kinda"
    player "WHAT!? KINDA!"
    bones " I have a gut feeling, wink, wink"
    bones "Get it because-"
    player "You don't have guts"
    bones "Also I don't have a clue"
    player "Ugh why do I keep you around!"
    bones "The antics, I’m a loveable scamp!"
    player "Whelp we're lost"
    bones "Well if we need to eat someone just remember that I'm all bones"
    player "Left or Right"
    $ company_with_skull = 1


    #Sound entrance.mp3 Stop
    stop entrance fadeout 2.0

    #(4)Branch: Chimera or Sirens
    menu:
        "1. Left to Chimera":
            $ junction_option_with_skull = 1
        "2. Right to Sirens":
            $ junction_option_with_skull = 2

    label junction_option_with_skull:
        if junction_option_with_skull == 1:
            jump chimera_with_skull

        elif junction_option_with_skull == 2:
            jump sirens_with_skull

    label chimera_with_skull:
        scene bg Chimera with dissolve
        centered "{size=50}{color=#f4e842}Chimera with Bones{/size}{/color}"

        #play Fire.mp3 sound
        play Fire "sound/Fire.mp3" fadein 2.0
        "Upon entering the room, the first thing that registers on your mind is the smell. The second thing that registers is your attempt not to gag, due primarily to the first thing."
        "Your nostrils are assaulted by the stench of what must be a combination of rotting flesh and rancid food. The ratios between them varying with each breath to make new and noxious combinations."
        player "Eugh...! What is that?!"
        "Looking around you spy a large room, the corners and walls are largely in shadow as the room is primarily lit via a flame from a sconce at the centre of the room."
        "You feel the shadows may be something of a blessing however."
        "You peer into the darkness trying to determine what the smell is emanating from, which is when you notice the corners of the room are piled with mounds of humanoid bodies and detritus in various states of decay."
        "The majority are now antiquated, their leavings now almost nothing but dust and bone. There are still many that are much more “fresh”, and you suspect that it is from these the smell comes."
        "Disconcertingly, almost all of these appear to be missing parts, an arm here, a leg there. Almost as if they are being eaten."
        player "Bad...Very bad...Very bad room"
        player "Hey, recognise any of these guys?"
        bones "Oh ha ha, yeah. Because all us bones look alike to you right?"
        player "Well yeah...kinda"
        "As if alerted by the sound of your voice, you begin to hear a low growl emanating from the surrounding shadows."
        "An instinctual fear grips your heart as you see, stepping into the light, the face of a lion gradually emerge into view. It’s growl now not just heard but felt and you can’t help but back away."
        "As the lion continues stepping forward you notice not not all is as it seems. The lion’s tail, as it emerges from the darkness does not seem ordinary."
        "Suddenly, your entire field of vision is encompassed by a large pair of fangs. The lion’s tail, you now realise, is not a tail at all but large snake!"
        "Its jaws snap shut, right in front of your face having reached the limit of its length, and withdraws with a hiss, staring watchful as it hovers over the lion’s head."
        "You realise this is no lion at all. You remember your mother telling you stories of these monstrosities before."
        "Unfortunately in the stories they were simply background with no indication of how to deal with them. You only remember them being called “Chimera”."
        chimera "So it seems yet another little morsel enters our lair"
        player "Morsel? Uh oh"
        "The beasts voice best described as a rumble. In addition to the fear, you are surprised at how eloquently it appears to be able to speak."
        chimera "Yes, we hear that a lot"
        player "You can call me [e_name], I’d prefer not to be called a ‘morsel'"
        chimera "But it shall soon be the truth"
        $ chimera_visit = 1

    label chimera_with_skull_result:
        if chimera_skull_option == 1:
            jump DoNotEatMe

        elif chimera_skull_option == 2:
            jump Assistance

        elif chimera_skull_option == 3:
            jump Argument

        label DoNotEatMe:
            player "Please don’t eat me!  I can probably be of help to you!"
            chimera "Yes, we hear that a lot too. Often accompanied by attempts at bribery or even with the promise to bring us more food."
            player "Um...Is that still an option?"
            chimera "It is..."
            "The snake again strikes forward with blinding speed.  You have barely registered any movement when you feel the fangs enter your flesh."
            chimera "However it will likely do as little good as it did the others"
            "The snake again retreats, but you can pay little attention. The snake's venom has already begun working it’s way through your body."
            "You realise you can no longer move a muscle and almost immediately fall to the ground."
            "You are glad you cannot feel anything as the lion’s jaws close around your neck."
            scene bg credits with dissolve
            centered "{size=50}{color=#f4e842}END{/size}{/color}"
            return

        label Assistance:
            player "“Uh...little help Bones?!"
            bones "Yeah yeah\nHelp me Old Bones Kenobi, you’re my only hope"
            player "What?"
            bones "You wouldn’t understand."
            "Turning to address the Chimera, Bones addresses him in a manner to which you suspect he is unaccustomed."
            bones "Hey, Snake-Butt!  Settle down there a second.  What’s the whole idea behind this?  What’s going on here?"
            chimera "Snake-Butt?"
            "The Chimera’s lion aspect raises a quizzical eyebrow. Seemingly intrigued."
            bones "How did you get here?  From the looks of you, I doubt you were born in that state.  I kind of doubt a lion and a snake once loved each other very much."
            chimera "Indeed not, little skull. I was created by the witch many, many years ago.  My purpose is to exist, feed and grow stronger.  Here, in this room is my world from which I may not leave."
            bones "Uh huh, and that’s it is it?  No greater purpose but to sit here and eat then?"
            bones "Have you even seen the witch since you were created?  Has she not given you any direction?"
            chimera "...."
            "The lion and snake aspects of the creature give each other looks of uncertainty.  Sensing the skull is succeeding in its goal, you feel it best to stay out of the way."
            bones "When we first came in, you said that ‘you had heard that before’.  What else have you heard before?  How many years have you sat here, hearing the same old thing time and again, never changing."
            bones "The same cycle over and over.  Person walks in, begs for their life.  You eat them and repeat ad nauseam.  How long have you been doing this?"
            bones "Do you not want anything more?  Why not simply leave, live your own life and make of it what you will?"
            chimera "My purpose…"
            bones "Is whatever you wish"
            bones "How about this, think about how long you have been here already.  Now, think about how long you will be here still if you choose to continue the cycle."
            "This seems to finally get through to the Chimera.  The thought of continuing this existence in perpetuity too much for it to bear."
            chimera "...Whatever I wish"
            "The Chimera paces around you and, turning to leave through the door you had entered, pauses."
            chimera "You have my thanks, little skull."
            "And with that, the beast leaves.  The last you see as it slips through the door is the snake, winking before departing."
            player "How did you come up with that so quickly?"
            bones "Trust me, I was in that swamp for a long time. I know a little about boredom and aimlessness"
            jump monster_visit_check

        label Argument:
            player "But why?"
            chimera "Why will I eat you?  Why else but to sate my hunger"
            "The Chimera begins to advance on you, the lion’s growl and the snakes hiss growing louder."
            "Looking quickly around the room in a desperate attempt to find any reason to extend the conversation, you hit upon the multitude of bodies piled up in the corners of the room."
            "Suddenly, you think you may be on to something.  As grotesque as it is, many of the bodies appear largely intact.  Only certain pieces missing, apparently at random."
            player "I don’t think that’s true"
            "The Chimera raises an eyebrow quizzically."
            player "You aren’t eating all these others based on hunger. Otherwise there would likely be almost nothing left of these poor souls."
            player "It’s apparent that you have little need of food.  So why really?"
            "Your question stops the Chimera short, though still disturbingly close.  It appears nobody has asked this before, which you can only take as a good sign."
            chimera "If you must know, it is simply because that is what I do, and always have done"
            player "It’s hardly a good reason though, is it?"
            chimera "What of it?"
            player "Well for one, where’s the dignity in that?"
            chimera "You would question my dignity?"
            "Anger creeps in to the Chimera’s voice as it takes yet another step towards you."
            player "Of course!  Look around!"
            player "It looks to me like you spend all of your time sitting in this room, waiting on the off chance that some poor explorer, who has no real hope of fighting you, happens to wander in."
            player "After which, you just kill them and...nibble at them."
            chimera "“Again, I ask what of it?"
            player "Well look at yourself! From the looks of you, I doubt you were born the way you are now. I kind of doubt a lion and a snake once loved each other very much and along you came!"
            player "Meaning, something has made you this way.  But I bet you still remember what it was like before you were joined"
            chimera "Of course, we remember that time rather fondly"
            player "Well, how about you lion.  When were you last able to hunt your prey in the wilds?  When did you last take down and animal for the benefit of the pack?"
            player "And you snake.When did you last stalk game, hidden from view in the long grass where you could finally strike at your target, basking in the knowledge that inevitably your venom would spell it’s doom?"
            "The lion and snake heads look at each other, uncertain"
            player "Are you both truly satisfied with your current existence?  Not seeking out prey, but having in trickle down to you from the outside. An existence devoid of any skill, any challenge or any meaning"
            player "Surely you cannot possibly be"
            chimera "What would you have us do?"
            player "Leave!  Go forth and seek out your own meaning in life, your own reason to exist!"
            "Pausing, for what seems to you an infinitely long time, the Chimera ponders your words."
            "A bead of sweat forms on your brown and begins to trail down, so fearful you are that you will end up sharing your fate with those surrounding you."
            "Finally, the lion’s head glances up at the snake, who nods and they are finally in agreement."
            chimera "[e_name]you are indeed wise for your years.  We will take on board your words and do this thing.  We will go forth and see what awaits outside in the larger world"
            "You smile and nod at the creature, not wanting to say anything further for fear you will inadvertently change its mind."
            "As the Chimera begins to leave from the same door you emerged, it pauses."
            chimera "Thank you [e_name] for helping us see that there is more to life than this"
            "And with that, it is gone and you breathe a gigantic sigh of relief.  You have no doubt that this encounter could have gone very differently."
            "Looking around, you have no further wish to stay with the dead, and leave via the opposite door wondering what else you could possibly meet."
            jump monster_visit_check


    ###############################With SKull######################



    label decline_skull:
        centered "{size=50}{color=#f4e842}DECLINE SKULL{/size}{/color}"
        player "This is not real"
        bones "No you silly girl, it is!"
        player "I've just go to focus and take a breath"
        bones "Listen to me."
        player "Breath in"
        "Breath in"
        bones "No listen you stu-"
        player "And out"
        bones "Would you like me to make sounds of the ocean too, wake up you little foo-"
        "Breath out"
        bones "No please, please help me, I can help you"
        player "Goodbye not real skeleton. Goodbye crazy horrible swamp"
        "You start to walk away laughing. In the distance you can hear the skeleton."
        bones "You silly fool! I hope the witch finds you, I hope she takes everything from you like she did me"
        bones "I didn't mean it! Please I don't want the dog to come back and bury me."


    #(10)Branch: 'Exit Woods' or 'Continue On'
    menu:
        "1. Exit Woods":
            $ decline_skull_option = 1

        "2. Continue On":
            $ decline_skull_option = 2

    label decline_skull_result:
        if decline_skull_option == 1:
            "You've come to the edge of the woods and can spy your uncles home. You've made the blood sacrifice and the witch can't see you. You leave the woods. ​game ends"
            player "Wow I almost lost my mind in there"
            player "Glad I found my way out"
            scene bg credits with dissolve
            centered "{size=50}{color=#f4e842}END{/size}{/color}"
            return

        elif decline_skull_option == 2:
            "Meet Witch"
            jump meet_witch

    label meet_witch:

        centered "{size=50}{color=#f4e842}MEET HUNTRESS{/size}{/color}"
        "You've progressed further into the bog and are growing further fearful that you may never leave; suddenly you hear a bush shaking."
        player "Please don't be a witch, please don't be a witch, Please don't be a witch, please don't be a witch"
        "A Huntress springs forth."
        player "*Screams*"
        huntress "Shh the witch might hear, haha"
        "The huntress looks elegant, she holds a dagger in her hand. Girl starts crying."
        player "I'm so scared, I ran into a talking skeleton and -"
        huntress "poor girl, lost in the woods"
        "Girl sobs."
        huntress "Imagine my surprise, I was just hunting for some lunch when I spy you through the trees."
        huntress "You're a lucky girl, follow me and I'll help you find your way"
        player "I'm going to my uncles house on the other side of the woods"
        huntress "Is that the north side?"
        player "Yes"
        huntress "That just so happens to be where I'm going"
        player "Thank you miss?"
        huntress "Elaheh"
        player "Thank you Elaheh"
        huntress "Oh it's my pleasure"

        jump labyrinth_entrance_with_huntress

    #(4)-2.Sirens
    label sirens_with_skull:
        scene bg Sirens with dissolve
        #play waves.mp3 sound
        play waves "sound/waves.mp3" fadein 2.0
        centered "{size=50}{color=#f4e842}SIRENS with Bones{/size}{/color}"
        "You choose the right path, you aren’t sure exactly why, maybe the path seems a little less claustrophobic and you’re ready for a little space to breathe."
        "You also think you can hear a song on the breeze in that direction."
        "You follow the winding path for some time, the song getting slowly louder and louder as you go. Finally, the path opens out to reveal a large body of water"
        "Three mermaids sit on rocks."
        "They are the ones singing the song you’ve been hearing, luring you always closer and closer."
        mermaid "Sailing on an anchor ​♫\nTrapped beneath the tides ​♪\nCurse the drowning sailor​♫\n And the wave he rides♪"
        player "Such a beautiful song"
        bones "That song was dark song"
        bones "I have a song"
        bones "Under the sea ♪\nUnder the sea ♫\nDarling it's better♪"
        player "Shhh"
        bones "Geez okay Ursula"
        player "Who's Ursula?"
        bones "Don't worry.."
        mermaid "Thank you sweet girl"
        mermaid "You should come and swim with us\nYou should come and sing with us\nSwim and sing all day"
        bones "Oh I bet you would love that evil Aerial!"
        player "Who's Aerial?- you know what stop talking"
        player "I think we need to cross this lake"
        player "I can see a boat in the middle"
        player "Could you swim across and get it for me"
        mermaid "Why don't you swim across?"
        player "Well- I can't swim"
        mermaid "We can teach you"
        bones "If you get in the water you'll be swimming with the fishes"
        bones "Literally and figuratively"
        player "It doesn't look that far out"
        bones "It is for someone who can't swim"
        mermaid "It's not deep"
        mermaid "You can almost stand at the deepest point"
        bones "Don't listen to these sardine brains"
        $ sirens_visit = 1

        menu:
            "1. You decide to swim":
                $ sirens_option_with_skull = 1

            "2. You are not going to swim":
                $ sirens_option_with_skull = 2

        label sirens_result:
            if sirens_option_with_skull == 1:
                bones "I'm not a flotation device or fish food."
                bones "I'm sorry but this is a bad idea"
                bones "Leave me here"
                "Once in the water the mermaids were pleasant until you couldn't touch the ground. Then they drowned you and ate your flesh."
                scene bg credits with dissolve
                centered "{size=50}{color=#f4e842}END{/size}{/color}"
                return

            elif sirens_option_with_skull == 2:
                player "I'm sorry but as I said I can't swim"
                player "Is there anything else I can do"
                mermaid "You liked our singing before?"
                player "Very much"
                mermaid "I'll sing the notes and solve the quiz."

        #Background music temporarily stop
        stop music fadeout 1.5

        #Sound waves.mp3 Stop
        stop waves fadeout 2.0

        #Mermaid Song Quizz Start#############################################################
        "Listen and watch carefully Mermaid song video"

        play movie "Mermaid song.ogv" noloop
        show movie with dissolve
        "Listen and watch carefully Mermaid song video"
        stop movie
        hide movie with dissolve
        "Quiz: Which is the correct order of musical notes?"
        #Mermaid Song Quizz Finish#############################################################

        #Play background music again
        play music "sound/BackgroundMusic.mp3" fadein 1.5

        #play waves.mp3 sound
        play waves "sound/waves.mp3" fadein 2.0

        #Call Options for Mermaid Song Quizz
        call screen imagemap_with_skull

        #When user has right answer
    label sirens_with_skull2:
        $ user_point = user_point + 1
        mermaid "That was beautiful!"
        mermaid "Here is your boat and take this too"
        mermaid "To think I was going to eat you"
        player "You we're going to eat me?!"
        bones "I told you"
        bones "Swim with scales and tell no tells"
        player "Well- thanks for not eating me"
        "You get on the boat with Bones and sail across the lake safely."

        #Sound waves.mp3 Stop
        stop waves fadeout 2.0

        jump monster_visit_check

    # Checks to see if other monster has been visited yet
    label monster_visit_check:
        if chimera_visit == 0 and company_with_hectate == 1:
            jump chimera_with_hectate
        elif chimera_visit == 0 and company_with_skull == 1:
            jump chimera_with_skull
        elif sirens_visit == 0 and company_with_hectate == 1:
            jump sirens_with_hectate
        elif sirens_visit == 0 and company_with_skull == 1:
            jump sirens_with_skull
        else:
            jump minotaur

    #(3)-1. Troll
    label troll:
        "Selecting the blood offering has successfully hidden you from the witch's sight, however as a result nobody has come to help you."
        "The Troll eats you."
        scene bg credits with dissolve
        centered "{size=50}{color=#f4e842}END{/size}{/color}"
        return

    label sirnes_dead:
        "Your answer is wrong."
        "You are drowned"
        scene bg credits with dissolve
        centered "{size=50}{color=#f4e842}END{/size}{/color}"
        return


return
