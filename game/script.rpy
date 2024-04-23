# Game script

# -- Characters --
define mc = Character("[mcname] [mclastname]")
# Love interests
define drmt = Character("Doormat")
define door = Character("Door")
define toaster = Character("Toaster")
# Side characters
define connor = Character("Connor")


# Custom transforms
transform half_size: 
    zoom 0.5 # adjust as required

transform double_size:
    zoom 2.0
    
transform left_center:
    xalign 0.15
    yalign 0.5


# Custom transitions
define moveinoutdissolve = ComposeTransition(dissolve, before=moveoutleft, after=moveinright)


# The game starts here.
label start:
    stop music fadeout 1.0
    # Get player's first and last name
    python:
        mcname = renpy.input("Hey hey, not so fast. What's your first name?", length=16)
        mcname = mcname.strip()
        mclastname = renpy.input("And.... your last name?", length=16)
        mclastname = mclastname.strip()

        if not mcname:
            mcname = "Joe"
        if not mclastname:
            mclastname = "Shro"

    mc "{i}Yawning, I stretched and got out of bed. \"What a wonderful day\" I thought to myself. Surely, nothing will go wrong...{/i}"

    scene bg hall
    with fade

    play music "wake_up.mp3"

    show alice default at half_size, right

    mc "It took a while, but I've finally managed to get downstairs"

    show alice worried

    mc "I'll never forget those bloody screams of the stairs..."

    show alice default

    mc "I am a bit hungry though, might aswell head into the kitchen"
    mc "I think it was behind that door..."

    show doormat worried at left_center 

    drmt "...Miss"
    
    show alice worried

    mc "!!!" with vpunch

    show doormat sad

    drmt "You are standing on my face!"
    mc "OH"
    mc "SORRY!!!"
    mc "I'll be out of here quickly!"

    hide doormat
    show alice embarrassed

    mc "I try to open the door, but as I grab the handle"

    show door default at left_center

    door "...Miss"

    show alice worried
    with hpunch

    mc "Oh no, what now"
    door "Could you perhaps..."

    show alice default

    mc "What is it?"
    
    show door angry

    door "Not touch my..."
    mc "Your what?"

    show door pout

    door "..."

    show alice embarrassed

    mc "..."

    show alice worried

    mc "OH"
    mc "I'M SORRY"

    show door blush

    door "As long as you're gentle..."
    mc "NO, I'M GETTING OUT OF HERE"

    hide door

    scene bg kitchen
    with dissolve
    show alice doubt at half_size, right 
    with moveinoutdissolve

    mc "After some 'struggles', I finally have made it into the kitchen"

    show alice happy

    # Show choice menu
    menu:
        mc "I decide to..."

        "Talk to the toaster":
            call connor

        "Stuff bread in the toaster":
            call toaster

    show alice embarrassed
    mc "That scared the shit out of me...."

    # End the game here
    return

label toaster:
    # decide to stuff bread

    mc "I get some bread and gently stuff it in the toaster"
    mc "..."

    show toaster happy small at left_center

    toaster "[mcname]-SAMA!!!"

    show alice worried

    mc "..."
    mc "Oh not AGAIN!"

    show toaster expectant small

    toaster "[mcname]-sama! Why do you keep stuffing me with bread??"
    
    show alice doubt

    mc "Well, because I'm hu-"

    show toaster happy small

    toaster "when we could be having a bath together instead? 0w0"
    mc "..."

    show toaster sad small

    toaster "Not funny? TwT"

    show alice worried

    mc "..."
    toaster "Please don't hate me senpai!! TwT"

    show alice doubt

    mc "You're not making it easy..."

    show toaster happy small

    toaster "Please! UwU"
    toaster "Have some toast!! Maybe you will change your mind! TwT"

    show alice worried

    mc "You know what, I wasn't hungry anyways"

    show alice doubt
    hide toaster

    mc "I slowly walk away from the toaster, hearing it cry softer and softer"
    toaster "Sob sob, uuuuuu"

    # return to original label
    return


label connor:
    # decide to talk to toaster (delulu)

    mc "{i}What if everything in my house can talk?? I'll try it on my toaster...{/i}"
    mc "Toaster-kun?"

    show toaster happy small at truecenter

    toaster "[mcname]-chan!"

    show toaster sad small at truecenter

    toaster "You've finally come to say hi to me~ You took way too long T~T"

    show toaster expectant small at truecenter

    toaster "When would you want to take a bath together? Pwease pweasee"

    hide toaster expectant small

    play music "connor_theme.mp3"

    show connor scary at truecenter

    connor "IT WAS ME CONNOR, ALL ALONG"

    hide connor scary
    with moveouttop

    # return to original label
    return