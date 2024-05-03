
##### Event Container Definitions

define administration_events = []
define dorm_room_events = []
define cafeteria_events = []
define water_lesson_events = []
define wind_lesson_events = []
define fire_lesson_events = []
define life_lesson_events = []
define light_lesson_events = []
define kinesis_lesson_events = []

##### Sleep Events #####

label generic_sleep_event(callback):

    "I return to my room exhausted and promptly fall asleep.."

    python:
        state.status.hp
        callback()


init python:
    create_contained_event(dorm_room_events, "generic_sleep_event", reuse=True, priority=-10)

#####
##### Elemental Lessons #####

label generic_water_lesson(callback):

    "I attend the water elemental lecture. I feel like I'm starting to get it."

    python:
        state.stats.water.gain(5)
        callback()

label generic_wind_lesson(callback):

    "I attend the wind elemental lecture. I feel like I'm starting to get it."

    python:
        state.stats.wind.gain(5)
        callback()

label generic_fire_lesson(callback):

    "I attend the fire elemental lecture. I feel like I'm starting to get it."

    python:
        state.stats.fire.gain(5)
        callback()

label generic_light_lesson(callback):

    "I attend the light elemental lecture. I feel like I'm starting to get it."

    python:
        state.stats.light.gain(5)
        callback()

label generic_life_lesson(callback):

    "I attend the life elemental lecture. I feel like I'm starting to get it."

    python:
        state.stats.life.gain(5)
        callback()

label generic_kinesis_lesson(callback):

    "I attend the kinesis elemental lecture. I feel like I'm starting to get it."

    python:
        state.stats.kinesis.gain(5)
        callback()


init python:
    create_contained_event(dorm_room_events, "generic_sleep_event", reuse=True, priority=-10)
    create_contained_event(water_lesson_events, "generic_water_lesson", reuse=True, priority=-10)
    create_contained_event(wind_lesson_events, "generic_wind_lesson", reuse=True, priority=-10)
    create_contained_event(fire_lesson_events, "generic_fire_lesson", reuse=True, priority=-10)
    create_contained_event(light_lesson_events, "generic_light_lesson", reuse=True, priority=-10)
    create_contained_event(life_lesson_events, "generic_life_lesson", reuse=True, priority=-10)
    create_contained_event(kinesis_lesson_events, "generic_kinesis_lesson", reuse=True, priority=-10)

#####


