
##### Event Container Definitions

define administration_events = []
define dorm_room_events = []
define cafeteria_events = []
define fundamentals_class_events = []

#####

label generic_sleep_event(callback):

    "I return to my room exhausted and promptly fall asleep.."

    $ callback()

init python:
    create_contained_event(dorm_room_events, "generic_sleep_event", reuse=True)

#####

label generic_fundamentals_class(callback):

    "We go through some study materials and then are left to self-study for the rest of class."

    $ callback()

init python:
    create_contained_event(fundamentals_class_events, "generic_fundamentals_class", reuse=True)

#####


