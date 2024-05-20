# events/town.rpy
#
# Put events in this file that should be encountered in town locations
#
# See the README.md for details on how you should define events.
#

### Event Container Definitions

define shrine_events = []
define market_events = []
define explore_town_events = []
define dojo_events = []
define blacksmith_events = []
define fountain_events = []
define back_alley_events = []
define inn_events = []
define guild_events = []

###

##### Market Events #####
##
label generic_market_event(callback):

    "It's a beautiful day in the market."

    "While walking down the street you happen across 10... money. How lucky!"
    $ state.money += 10
    $ callback()

init python:
    create_contained_event(market_events, "generic_market_event", reuse=True, priority=-10)
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
#####
##### Explore Events #####

# These are a bunch of placeholders to just reserve ideas, not adding all of these yet

label discover_dojo(callback):
    "Here I have discovered the dojo"

    python:
        dojo.enable()
        callback()

label discover_blacksmith(callback):
    "Here I have discovered the blacksmith"

    python:
        blacksmith.enable()
        callback()

label discover_orphanage(callback):
    "Here I have discovered the orphanage"

    python:
        # not a real location yet
        callback()

label discover_fountain(callback):
    "Here I have discovered the fountain"

    python:
        fountain.enable()
        callback()

label discover_back_alley(callback):
    "Here I have discovered the back alley"

    python:
        back_alley.enable()
        callback()

label discover_printer(callback):
    "Here I have discovered the printer"

    python:
        # not a real locations yet
        callback()

label discover_inn(callback):
    "Here I have discovered the inn"

    python:
        # not a real location yet
        callback()

label discover_carpenter(callback):
    "Here I have discovered the carpenter"

    python:
        # not a real locations yet
        callback()

init python:
    create_contained_event(explore_town_events, 'discover_dojo')
    create_contained_event(explore_town_events, 'discover_blacksmith')
    create_contained_event(explore_town_events, 'discover_fountain')
    create_contained_event(explore_town_events, 'discover_back_alley')

#####

# dojo_events
# blacksmith_events
# fountain_events
# back_alley_events
# inn_events

##### Dojo Events #####
label generic_dojo_event(callback):

    "I visit the dojo. There's nothing to do here today."

    $ callback()

init python:
    create_contained_event(dojo_events, 'generic_dojo_event', takes_time=False, reuse=True, priority=-10)
#####

##### Blacksmith Events #####
label generic_blacksmith_event(callback):

    "I visit the blacksmith. There's nothing to do here today."

    $ callback()
init python:
    create_contained_event(blacksmith_events, 'generic_blacksmith_event', takes_time=False, reuse=True, priority=-10)
#####

##### Fountain Events #####
label generic_fountain_event(callback):
    "I visit the fountain. There's nothing to do here today."

    $ callback()

init python:
    create_contained_event(fountain_events, 'generic_fountain_event', takes_time=False, reuse=True, priority=-10)
#####

##### Back Alley Events #####
label generic_back_alley_event(callback):
    "I visit the back alleys. There's nothing to do here today."

    $ callback()

init python:
    create_contained_event(back_alley_events, 'generic_back_alley_event', takes_time=False, reuse=True, priority=-10)
#####

##### Inn Events #####
label generic_inn_event(callback):
    "I visit the inn. There's nothing to do here today."

    $ callback()

init python:
    create_contained_event(inn_events, 'generic_inn_event', takes_time=False, reuse=True, priority=-10)
#####

##### Guild Events #####
label generic_guild_event(callback):
    "I visit the guild. There's nothing to do here today."

    $ callback()

init python:
    create_contained_event(guild_events, 'generic_guild_event', takes_time=False, reuse=True, priority=-10)
#####

##### Shrine Events #####
label generic_shrine_event(callback):
    "I visit the shrine. There's a lot of work to do but it feels good to help out."

    python:
        state.stats.spiritual_affinity.gain(5)
        callback()

init python:
    create_contained_event(shrine_events, 'generic_shrine_event', takes_time=False, reuse=True, priority=-10)
#####
