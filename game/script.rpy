init:

    #define player "e-name" and will input from user
    define player = Character("[e_name]", color="#f44242")
    define Mother = Character("Mother", color="#f4ee42")
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
    centered "{color=#024eff}Input your name before the story start{/color}"
    call screen test 
    $ e_name = _return
   
    #HOME
    centered "{size=50}{color=#f4e842}HOME START{/size}{/color}"
    "Mother is on death bed fearing she will soon breathe her last.\nShe requests you, her daughter, to visit your uncle on the far side of the wood.\nShe asks that you make an offering to the woods for safe passage."
    centered "{color=#024eff}What's your decision?{/color}"
    
    #(1)Branch: Leave or stay?
    menu:
        "1. You decide to stay with your mother":
            jump stay
        "2. You decide to leave":  
            jump leave

    #(1)-1.Stay - Story End
    label stay:
        player "I can’t leave you mother"
        player "I love you, mother"
        return

    #(1)-2.Leave - journey start
    label leave:
    "Your mother instructs you to;\nSpill earth (ashes from urn)\nSpill water (fresh drinking water)\nSpill blood (sacrifice a dove)"
    Mother "I know of your dislike, but do not forget the dove!"

    #SHRINE
    centered "{size=50}{color=#f4e842}SHRINE{/size}{/color}"
    "Outside your house, you are given options to complete / not-complete the three parts of the ceremony for safe passage"
    player "Lo to the Watcher, with power to see"
    menu:
        "1. You offer water":
            $ water_point = 1
            
        "2. You chose not to offer water":  
            $ water_point = 2

    label result_water:
        if water_point == 1:
            centered "{color=#e50b0b}You reach down and unfasten your flask of water,\nsprinkling a small amount over the shrine. {/color}"
            
        elif water_point == 2:
            centered "{color=#e50b0b}You are not certain how long you will need to travel to reach your uncles home\n
            And may need all the water you can carry.\n
            You chose not to spill any of your precious water\n
            as you are sure that the words themselves are more than enough.{/color}"
    
    player "Lo to the Watcher, with power to see"

    menu:
        "1. You offer earth":
            $ earth_point = 1
            
        "2. You chose not to offer earth":  
            $ earth_point = 2

    label result_earth:
        if earth_point == 1:
            centered "{color=#e50b0b}Bending down, you scoop a handful of loose soil and scatter it across the shrine.{/color}"
            
        elif earth_point == 2:
            centered "{color=#e50b0b}You feel as if this is a waste of time, much better spent if you were already on your way.
            \nForgoing the offering of earth, you hurriedly continue with the ceremony.{/color}"

    player "Lo to the Crone, who darkens the path"   

    menu:
        "1. You offer the blood":
            $ blood_point = 1
            
        "2. You chose not to offer the blood":  
            $ blood_point = 2

    label result_blood:
        if blood_point == 1:
            centered "{color=#e50b0b}You walk to the nearby hutch, unfasten and carefully open the door.{/color}"
            
        elif blood_point == 2:
            centered "{color=#e50b0b}No, you will not do it.  Those poor doves have suffered enough, and you will have no further part in it. You continue with the ceremony, inwardly smiling at the sound of the doves cooing as if in gratitude{/color}"

    player "Lo to the Three, that we may pass free"  

    #CORSSROAD
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
    centered "{size=50}{color=#f4e842}Labyrinth Entrance{/size}{/color}"
    "You arrive at the Labyrinth entrance with either the Skull, Goddess or Witch (Huntress) companion.\nWitch (Huntress) dissappears leaving the player to find their own way.\nGoddess dissappears but can appear later.\nSkull stays with the player"

    #JUNCTION
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
            jump chimera

        elif junction_option == 2:
            jump sirens    

    #(4)-1. Chimera
    label chimera:
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
