
label day4_night(callback):
    scene bg dorm room night with dissolve

    """
    I finally did it today. I channeled for the first time in my life. At least, the first time
    on purpose.

    I'm still riding that high as I return to my room.

    A part of me was convinced I didn't actually have what it takes to channel. But now it feels like
    I might have a shot to make it through this.

    I'm not even surprised when the thrumming starts in my ears as I settle in to rest for the night.
    """

    call .dream

    $ callback()

label .dream:
    """
    ...

    Tonight my dreams take a different turn than usual.

    My head hurts and my ears are still buzzing, but I'm a kid again.

    I got up early and snuck out before sunrise with my friends.

    We're going to go check out the old abandoned temple. It's a test of courage.

    Some of them believe there's an old which who lives here. One of them even believes they saw
    a ghost here once.

    But I'm not afraid. I told them they were stupid for believing in such childish things.

    Plus I've got a secret weapon in case any ghosts do try to sneak up on us.

    We met up outside my house and are now moving quietly through the empty streets.

    The moon is so bright that it's not hard to see, and we all know our way around the
    neighborhood. It doesn't take long before we make it to the old temple.

    I lead the way with 3 other kids huddling close behind, but I've never really been this close
    to the temple before so I'm starting to lose my nerve a little.

    The stonework on the ground is uneven and I stumble. I catch myself, but not before yelling
    a bit more loudly than I had intended.

    A light comes on in a nearby room, and we see her: it's the witch!

    I jolt awake to find that it's already morning.
    """

    return

init python:
    plot_schedule.schedule_event((4, TOD.NIGHT), Event("day4_night"))
