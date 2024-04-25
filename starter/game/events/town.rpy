# events/town.rpy
#
# Put events in this file that should be encountered in town locations
#
# See the README.md for details on how you should define events.
#

### Event Container Definitions

define market_events = []

###

### Market Events
##
label generic_market_event(callback):

    "It's a beautiful day in the market."

    "While walking down the street you happen across 10... money. How lucky!"
    $ state.money += 10
    $ callback()

init python:
    create_contained_event(market_events, "generic_market_event", reuse=True)
##

label special_market_event(callback):

    "It's a beautiful day in the market."

    "While walking down the street you happen across 100... money. How incredibly lucky!"
    $ state.money += 100
    $ callback()

init python:
    def special_market_event_requirements(state: StateManager) -> bool:
        if state.karma > 100:
            renpy.notify("Your karma is more than 100!")
        return state.karma > 100

    create_contained_event(market_events, "special_market_event", condition=special_market_event_requirements)
##
###




