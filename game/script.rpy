# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character("Toaster")
define c = Character("Connor")

# The game starts here.

label start:

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
