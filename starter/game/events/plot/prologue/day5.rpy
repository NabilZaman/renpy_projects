
label theory_lesson4(callback):
    scene bg lecture hall morning

    show expression ti.image

    ti.says "Welcome back to arcane fundamentals class. Today will be the final day of our
    exploration of the mechanics of channeling as we discuss Coherence."

    ti.says """
    Coherence is the process of merging your recalled experience into the physical world.

    This is an act of will. You use your strength of will to impose the effect of your spell
    over the neutral state of the world.

    The process itself is quite simple. Many of you will have accidentally begun doing this
    yesterday as you practiced recall.

    That is, those of you who weren't busy doing so on purpose to show off.
    """

    "He says, as he sternly eyes some of the students channeling flashier spells yesterday."

    ti.says """
    That being said, simple does not mean easy.

    This is the most draining step. Novice wizards may only
    be able to channel once or twice in a day until they build up the strength.

    Addtionally specific techniques for Coherence are very element-specific,
    and you'll learn more about them in your other coursework.

    Today we'll be going going over one of the most generally applicable techniques, by applying
    the Principle of Distinction.

    For now we'll begin again as usual. Attune to your chosen element, then begin to recall
    the experience you are aiming to evoke.

    However this time your aim is to go a step further. Not simply evoking a known experience
    but taking that experience and making it whole within the world.

    While the goal is ultimately to use spiritual energy to recreate your experience,
    it's easy to get stuck simply replaying the experience over and over again internally.

    To make it external, it helps to fixate on a detail about your current situation
    that differs from your experience and include that in your channeling.

    Perhaps a stream you're Recalling must travel down a slightly different path than it did
    in your experience, or an object you're pushing is beginning from on the ground instead
    of on a table. This is the Principle of Distinction.

    There is a natural tension between the ease with which you can Recall an experience in an
    environment that matches it closely, and using Distinction to force it to manifest as more than
    a mere memory.

    Now that's enough talk, let's see you put this into practice.
    I see that some of you have already gotten started.
    """

    """
    I'm trying again by attuning to kinesis and moving my pencil around.
    """

    ti.says """
    We've broken these channeling lessons into three parts, but once you've gotten used to it,
    there's really not much that separates Recall and Coherence in practice.

    If you're able to successfully Recall an experience, you'll find you only fail to bind your
    experience to the world if you've either already exhausted yourself, or if you're unable to
    move beyond the bounds of your experience.

    The latter is where the Principle of Distinction will help you but you'll find this is largely
    a novice trap and you'll hardly have to consider it over time.

    The real reason to study the difference is that these are two skills you can train and improve
    on independently that will net you disparate benefits.

    Becoming more proficient in Recall will let you channel more varied and unique experiences,
    especially those that differ wildly from the situation you find yourself in at the moment.

    While training in techniques to improve your spells' Coherence will let you channel more
    impressive and difficult experiences with less strain.
    """

    """
    While the professor lectured, I've managed to lift the pencil a second time.
    This it just kept rising, clearing my head and soaring high towards the ceiling.

    I feel like the spell has lifted me just as high; I'm elated. I know this is an insignificant
    nothing of a spell, but... it's mine.

    It feels as if everything is different now, it feels as if I can do anything.

    I'm still watching the pencil intently, but distracted by my thoughts I'm surprised when I
    feel with a jolt the pencil can't rise anymore, it must have hit the ceiling. It shakes my
    concentration and the pencil comes plummeting down.

    It lands with *snap* on my desk, though only the tip seems to have taken any real damage.
    I pet it gently. It's a hero now. The first pencil to fly by my magic.
    """

    $ state.stats.magic_theory.gain(10)

    ti.says "And this is where we'll wrap things up for today. Be sure to attend tomorrow's
    final lesson. We'll be going over in more detail what you'll need to prepare for your exams
    and answering any lingering questions you may have as you refine your channeling techniques."

    $ callback()

label day5_night(callback):
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

    My head hurts and my ears are still buzzing, but tonight I'm a kid again.

    I got up early and snuck out before sunrise with my friends.

    We're going to go check out the old abandoned temple. It's a test of courage.

    Some of them believe there's an old which who lives here. One of them even believes they saw
    a ghost there once.

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
    plot_schedule.schedule_event((5, TOD.MORNING), Event("theory_lesson4"))
    plot_schedule.schedule_event((5, TOD.NIGHT), Event("day5_night"))
