

label day3_night(callback):
    scene bg dorm room night with dissolve

    """
    I make it back to my room at the end of the day, exhausted.

    I'm surprised by how physically taxing channeling has proven, and my head still hasn't
    forgiven me for pushing myself so hard in class today.

    The moon is bright enough to light up my room and I'm tempted to stay up a little bit longer.

    I had vague intentions of doing some attuning practice tonight, but I don't think my head can
    I can take much more today so I just pull the curtains shut.

    I slide into bed, thankful the academy designed the accomodations to satisfy its primarily
    noble student body, and drop into sleep so quickly I hardly notice the thrumming that's begun
    in my ears.
    """

    call .dream

    $ callback()

label .dream:
    """
    ...

    My ears ring loudly now, and my head's throbbing so hard I wince at the pain.

    No. Not at the pain, at the light.

    The flickering is so bright. I thought I had closed my curtains?

    And the heat is so intense. I can't sleep like this.

    Or am I already sleeping? I must be dreaming...

    The sensations are already fading as my thoughts work to catch up,
    and the darkness of sleep reclaims me.
    """

    return

init python:
    plot_schedule.schedule_event((3, TOD.NIGHT), Event("day3_night"))
