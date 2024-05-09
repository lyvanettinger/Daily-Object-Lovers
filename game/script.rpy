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
define fadehold = Fade(0.5, 1.0, 0.5)


init python:
    # choose random splash image on startup. splash images need to be names "splash[id]", with the following function adjusted accordingly:
    rand = renpy.random.randint(0, 2)
    renpy.image('splash', 'splashes/splash%d.jpg' % rand)


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

    call prologue from _prologue

    return


# Show random splash art on startup
label splashscreen:
    scene black
    with Pause(1)

    play sound "arrr.wav"

    $ renpy.show('splash')
    with dissolve
    with Pause(2)

    scene black with dissolve
    with Pause(1)

    return