
screen characters_menu():

    tag menu

    add HBox(Transform("#292835", xsize=350), menu_main_panel_color) # The background; can be whatever

    use game_menu('Characters')

    # Here I'd like a selection of major characters at the top of the screen,
    # Then as you click on each one, the old character info panel slides off screen and the new
    # panel slides onto the screen
    # Then each character panel should have their image, key facts,
    # and maybe even a place to write notes? That may be overkill.
    fixed:
        xsize 1500 xalign 1.0

        vbox:
            # character select up top
            hbox:
                spacing 10
                for c in major_characters:
                    textbutton c.name():
                        xysize (100, 30)
                        action NullAction()
            # below it is the character panel
            # Each of these should probably be a screen? And then the button actions above should
            # swap out the screen. I'm just not sure how to show one the screens by default
            hbox:
                #first is a character portrait
                frame:
                    background "color_white"
                    xysize (280, 400)
                    frame:
                        background proportional_scale(c.image, 280, 400)
                #Then the character stats
                frame:
                    has vbox
                    text "Height: 100"
                    text "Weight: 100"
                    text "Smile: Priceless"
                    frame:
                        has vbox
                        # Then the mysteries collection.
                        label "Mysteries"
                        text "Who did the cookie jar theft? Was it this one?!"
