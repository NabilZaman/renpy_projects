
##### Day 2 #####

# - Have a pop-up modal.
# - it will reiterate the narrative deal (qualifying exam) and how it will play out in
#   game mechanics
# - Make sure the locations are set up so that it is technically possible, but difficult, to fail
#   by just ignoring the classes and fucking about in town or whatever.

label day2(callback):

    scene bg school infirmary morning with dissolve

    show expression sn.image

    sn.says """
    Good morning sleepy head.

    You were brought in last night by a sweet old thing who was quite shook up with you collapsing
    on her.

    I looked you over and couldn't find a thing wrong with you, so I just let you sleep it off here.

    Classes haven't even started yet and you kids are already working yourselves to death.

    Speaking of, you're a first year, right? So you'll be needing to get ready if you want to
    catch your first class.
    """

    """
    I thank the nurse, embarrassed and rush back to my room to get ready.
    """

    $ callback()

label day2_night(callback):
    scene bg dorm room night with dissolve

    """
    I collapse into my bed at the end of the day, my mind still whirling with everything I've been
    learning.

    Between classes where I'm already way behind the other students and having to report to the
    guild, I'm worried I won't last long here.

    But for now it's late and I'm plenty tired so I should try to quell my doubts and get to bed.
    I can already feel a headache coming on.

    I close my eyes and begin to drift.
    """

    call .dream

    $ callback()

label .dream:
    """
    ...

    I feel... heat. And pain. My head throbs insistently.
    And there's a persistent thrumming in my ears.

    The thoughts are hard to pin down.

    The sensations fade as I finally settle into sleep.
    """

    return


init python:
    plot_schedule.schedule_event((2, TOD.MORNING), Event("day2", takes_time=False))
    plot_schedule.schedule_event((2, TOD.NIGHT), Event("day2_night"))
