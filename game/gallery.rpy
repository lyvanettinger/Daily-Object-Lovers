transform alice_transform:
    zoom 0.5    
    xalign 0.5
    yalign 1.0

transform gallery_button:
    fit "contain"
    xsize 312
    ysize 312

style button:
    background "#888"
    insensitive_background "#444"
    hover_background "#aaa"

style button_text:
    color "#fff"
    selected_color "#ff0"

init python:

    # Create gallery
    g = Gallery()

    # Create button with an unlocked image
    g.button("hall")
    g.image("bg hall")

    # Create button with 4 images
    g.button("alice")
    # unlock_image makes it so seeing the image unlocks it
    # passing 2 displayables to this image
    g.unlock_image("bg hall", "alice default")
    # 2 transforms one for each displayable
    g.transform(None ,alice_transform)
    g.unlock_image("alice blush")
    g.transform(alice_transform)
    g.unlock_image("alice doubt")
    g.transform(alice_transform)
    g.unlock_image("alice happy")
    g.transform(alice_transform)

    g.button("doormat")
    g.unlock_image("bg hall", "doormat happy")
    g.unlock_image("bg hall", "doormat worried")
    g.unlock_image("bg hall", "doormat angry")
    g.unlock_image("bg hall", "doormat sad")

    g.button("door")
    g.unlock_image("bg hall", "door default")
    g.unlock_image("bg hall", "door angry")
    g.unlock_image("bg hall", "door blush")
    g.unlock_image("bg hall", "door pout")
    g.unlock_image("bg hall", "door happy")
        
    g.button("toaster")
    g.unlock_image("bg kitchen", "toaster expectant small")
    g.unlock_image("bg kitchen", "toaster happy small")
    g.unlock_image("bg kitchen", "toaster sad small")

    g.button("fork")
    g.unlock_image("bg kitchen", "fork default")
    g.unlock_image("bg kitchen", "fork blush")
    g.unlock_image("bg kitchen", "fork shocked")
    g.unlock_image("bg kitchen", "fork angry")

    # Transition between images
    g.transition = dissolve

screen gallery:

    tag menu

    add "gal/gal-bg.png"

    hbox:
        xalign 0.5
        yalign 0.5

        spacing 30

        grid 3 2:
            spacing 20

            add g.make_button(name="alice", unlocked="alice default", locked="gal/gal-lock.png", xalign=0.5, yalign=0.5) at gallery_button
            add g.make_button(name="doormat", unlocked="doormat happy", locked="gal/gal-lock.png", xalign=0.5, yalign=0.5) at gallery_button
            add g.make_button(name="door", unlocked="door default", locked="gal/gal-lock.png", xalign=0.5, yalign=0.5) at gallery_button
            add g.make_button(name="toaster", unlocked="toaster happy small", locked="gal/gal-lock.png", xalign=0.5, yalign=0.5) at gallery_button
            add g.make_button(name="fork", unlocked="fork default", locked="gal/gal-lock.png", xalign=0.5, yalign=0.5) at gallery_button
            add g.make_button(name="hall", unlocked="bg hall", locked="gal/gal-lock.png", xalign=0.5, yalign=0.5) at gallery_button

        # The screen is responsible for returning to the main menu. It could also
        # navigate to other gallery screens.
        textbutton "Return" action Return() style "button", "button_text" xalign 1.0 yalign 0.5