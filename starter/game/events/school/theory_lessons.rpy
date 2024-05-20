# events/plot/theory_lessons.rpy
#
# Put events in this file that should run when the player attends magic theory class
#
# See the README.md for details on how you should define events.
#

### Event Container Definitions

define magic_theory_events = []

###

label generic_theory_class(callback):
    "The professor opens up the class to questions while we're free to independently practice
    chanelling."

    $ state.stats.magic_theory.gain(3)

    $ callback()

init python:
    create_contained_event(magic_theory_events, 'generic_theory_class', reuse=True, priority=-10)


