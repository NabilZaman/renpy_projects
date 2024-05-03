
define character_menu_portrait_width = 400
define character_menu_portrait_height = 600

init python:
    def set_active_bio(index: int):
        def do_action():
            global character_menu_index
            character_menu_index = index
            renpy.restart_interaction()
        return do_action

default character_menu_index = 0

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
        ypos 10
        xsize 1500 xalign 1.0

        python:
            characters = met_characters(Significance.MAJOR)

        vbox:
            spacing 50
            # character select up top
            hbox:
                spacing 10
                for i, char in enumerate(characters):
                    fixed:
                        yfit True
                        xfit True
                        frame:
                            textbutton char.name():
                                action set_active_bio(i)

            # If we've met any major characters yet, show the first one by default
            if characters:
                use char_bio_screen(characters[character_menu_index])
            else: # Otherwise tell the player off for being a loser
                text "You haven't met anyone important yet, get out there and start making friends!":
                    xalign 0.5
                    yalign 0.5
                    outlines [(1, "#000", 0, 0)]


            # below it is the character panel
            # Each of these should probably be a screen? And then the button actions above should
            # swap out the screen. I'm just not sure how to show one the screens by default


screen char_bio_screen(char):
    frame:
        xfill True
        hbox:
            frame:
                background "color_white"
                xysize (character_menu_portrait_width, character_menu_portrait_height)
                frame:
                    xalign 0.5
                    yalign 0.5
                    background proportional_scale(char.image, character_menu_portrait_width, character_menu_portrait_height)
            #Then the character stats
            frame:
                has vbox
                spacing 10
                text "Height: 100"
                text "Weight: 100"
                text "Smile: Priceless"
                frame:
                    has vbox
                    # Then the mysteries collection.
                    label "Mysteries"
                    text "Who did the cookie jar theft? Was it this one?!"
