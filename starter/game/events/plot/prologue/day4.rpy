
label theory_lesson3(callback):

    show expression ti.image

    ti.says "Welcome back to arcane fundamentals class! Last time we covered attunement in more detail.
    Today we'll be focusing on the second phase of channeling: Recall."

    "I'm a little hesitant after pushing myself so hard last time, but I can't help but be excited."

    ti.says "The recall step in channeling imposes a limitation on your abilities that no amount
    of study or practice can overcome. Great Magi improve their repetoire through a long and varied
    life experiences. In a way, true masters of the art are avid students of life itself."

    "The professor looks pensive for a moment."

    ti.says """
    That was awfully deep, wasn't it? Well don't go getting any bright ideas about rushing
    out of here to go living life to the fullest. If I'm stuck inside here, you are too.

    The fact is that while life experiences are a necessary component, they are by no means sufficient.
    Which means more drills!

    Today we'll again limit our attention and improve through repetition. Focus on a memory of a
    simple physical phenomenon that aligns to one of the spiritual elements.

    If you don't already have an experience in mind, I suggest you try lifting your pencil and
    dropping it several times. Then focus on the experience of the pencils motion before attuning
    yourself to the energies of Kinesis.
    """

    """
    Not having any better ideas, and feeling a bit foolish, I begin repeatedly dropping my pencil.

    I try to focus on the imagery of watching it fall. The rate at which it falls, the sounds of it
    clattering, the way it bounces chaotically on my desk.

    Then I attune to Kinesis and try recalling that experience.

    Nothing happens at first, which isn't too surprising, but I soon grow frustrated with my lack
    of progress and start fiddling with the pencil again.
    """

    ti.says "Remember, if you're trying to explore Kinesis, focus both on the pencil rising and falling.
    In particular you're the one lifting the pencil so you'll have a more intimate connection to
    that experience."

    """
    I try again with the Professor's advice in mind and it doesn't take too long before I start to
    feel something.

    I've been attuning this whole time so the familiar humming is back, but now I feel like I can
    see the motion of the pencil in space, rising gently above my desk then tumbling again.
    """

    $ state.stats.magic_theory.gain(10)

    "We keep the drills up throughout class, the professor offering more helpful hints."

    ti.says "That marks the end of today's lesson. You all displayed a good effort. Those of you
    you had trouble with this step, don't lose heart. You'll have more opportunities to refine your
    technique durin tomorrow's lesson."

    "With that he dismisses us for our free afternoon period."

    $ callback()

label day4_night(callback):
    scene bg dorm room night with dissolve

    """
    I don't have a chance to stop and consider it outside of times like this, but my dreams
    have been more vivid than usual. The stresses of my new life here must be getting to me.
    """

    call .dream

    $ callback()

label .dream:
    """
    ...

    Reality melts away to make room for the land of dreams. I'm lucid enough for it to
    occur to me that I've been dreaming more than usual recently.

    This one is familiar.

    The heat, the lights, they're the same as last time. But another sense
    assaults me tonight. The smell.

    Smoke.

    It's not just pungeant, as I drift deeper into the dream, it's suffocating.

    I gasp for air as the panick rises within me.

    I need air.

    I need to get out.

    I try to scream but taking in enough air to do even that burns my throat.

    And suddenly it's over.
    """

    return

init python:
    plot_schedule.schedule_event((4, TOD.MORNING), Event("theory_lesson3"))
    plot_schedule.schedule_event((4, TOD.NIGHT), Event("day4_night"))
