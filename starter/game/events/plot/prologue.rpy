
label prologue0(callback):

    "This is how our story begins."

    $ callback()

define plot_events = EventSchedule()

init python:
    plot_events.schedule_event((0, TOD.NIGHT), Event("prologue0"))



