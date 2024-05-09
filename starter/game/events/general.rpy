# events/general.rpy
#
# Put events in this file that are more general events that don't fit in other locations.
#
# See the README.md for details on how you should define events.
#


# Maybe these should just be put in town/school.rpy... especially if we could have a chance of an
# event occuring at the gates.
label to_town(callback):
    python:
        state.set_map(town_map)
        if callback is not None:
            callback()
        else:
            state.display_map()
    return

define town_transition = Event("to_town", takes_time=False, reuse=True)

label to_campus(callback):
    python:
        state.set_map(school_map)
        if callback is not None:
            callback()
        else:
            state.display_map()
    return

define school_transition = Event("to_campus", takes_time=False, reuse=True)

