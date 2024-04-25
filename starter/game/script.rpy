
# The game starts here.

label start:

    call setup

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # show screen calendar_display()

    $ state.advance_state()

    "That concludes the interactive portion of the game."

    "The end."

    # This ends the game.

    return
