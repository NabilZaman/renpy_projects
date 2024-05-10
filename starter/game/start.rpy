
label testing:

    "before animation"

    $ show_stat_gain(3, 'coolness')

    "after animation"

    return


# The game starts here.

label start:
    # The setup label contains all the logic to set up the various game systems.
    call setup

    # This sets off the state machine that will drive the main game. We should not return from this operation until the game has ended.
    $ state.advance_state()

    call testing

    "The end."

    return
