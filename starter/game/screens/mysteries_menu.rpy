
screen mysteries_menu():

    tag menu

    add HBox(Transform(menu_nav_panel_color, xsize=350), menu_main_panel_color) # The background; can be whatever

    use game_menu('Mysteries')

    # This menu should track all the ongoing mysteries.
    # This should be a left panel of mysteries and a right panel with bulleted
    # descriptions of each discovery the player has made along the way to solving it.
    # The left panel should differential ongoing and completed mysteries.
    # Maybe with different sections. Or maybe with just a big check mark.
    #
    # One idea is for one of the characters to be very mystery-focused and solving mysteries
    # makes them grow linearly in affection for you. There's like no other way to befriend them.

    text ""
