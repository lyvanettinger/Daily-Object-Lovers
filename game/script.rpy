# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mc = Character("MC-Chan")

define drmt = Character("Doormat")
define door = Character("Door")
define toaster = Character("Toaster")


define c = Character("Connor")

transform half_size: 
    zoom 0.5 #adjust as required

transform double_size:
    zoom 2.0
    
transform left_center:
    xalign 0.15
    yalign 0.5

# The game starts here.

label start:

    scene bg hall

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

    mc "!!!"

    show doormat sad

    drmt "You are standing on my face!"


    mc "OH"

    mc "SORRY!!!"

    
    mc "I'll be out of here quickly!"

    hide doormat
    show alice embarrassed

    mc "I try to open the door, but as I grab the handle"



    show door default at left_center

    # Show door
    door "...Miss"

    show alice worried

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
    show alice doubt at half_size, right

    mc "After some 'struggles', I finally have made it into the kitchen"

    show alice happy

    mc "I get some bread and gently stuff it in the toaster"

    mc "..."

    show toaster happy small at left_center

    toaster "MC-SAMA!!!"

    show alice worried

    mc "..."

    mc "Oh not AGAIN!"

    show toaster expectant small

    toaster "MC-sama! Why do you keep stuffing me with bread??"
    
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

    # End the game here
    return

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg kitchen

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    play music "wake_up.mp3"

    # These display lines of dialogue.

    show toaster happy small at truecenter

    t "MC-chan!"

    show toaster sad small at truecenter

    t "You've finally come to play the game~ You took way too long T~T"

    show toaster expectant small at truecenter

    t "When would you want to take a bath together? Pwease pweasee"

    hide toaster expectant small

    play music "connor_theme.mp3"

    show connor scary at truecenter

    c "IT WAS ME CONNOR, ALL ALONG"

    # This ends the game.

    return
