
##### Day 0 #####

label day0(callback):
    show bg black

    "Driver" "So, m'lord, you're a new student at the Academy, huh?"

    "M'lord?" # Rethink form of address to be dynamic or non-gendered

    show bg carriage night with dissolve

    mc.says "Hmm? Yeah I suppose I will be."

    "Driver" "Pretty unusual, having a pick-up like this.
    Not that it's my first time carrying a student up there or anything."

    mc.says "Oh really?"

    """
    It was hard focusing on what the driver was saying when so much is happening all
    around the carriage.

    It had been three days since I left home with a caravan heading to the magical city of
    Ardenvale.

    The trip had been a pleasant one. The caravan was mostly full of merchants heading to ply their
    trade in the city and other settlements across the north. We were guarded by a family friend,
    which was how I got my place there.

    The weather was still agreeable and we'd camped under the stars each night while some of
    the more well traveled members of our group filled my head with stories of the wonders I could
    expect when we arrived in Ardenvale.

    I had been sure they were exaggerating for effect, but seeing it all for myself now,
    if anything they were too reserved in their depictions.

    There was so much life, so much motion. It was like... well, magic.
    """

    "Driver" "It's just, you know, odd for one of you to be arriving on your own like this.
    Usually students will have their own retinue. And... more bags, you know?"

    mc.says "Mmhmm, yeah."

    "A child running right by us is carrying a stick rapidly changing in color with a stream of
    sparks flying off the end."

    "Driver" "So... you must be one them uh, 'special cases', huh?"

    mc.says "Sure?"

    """
    Special what?

    I didn't have time to give it much thought as just then a stone disk we were passing by
    erupted with water all about its circumference. The water formed a wall taller than the carriage
    that sputtered and splashed as children gleafully ran around it, running their hands through
    the circular geyser.
    """

    "Driver" "Too right, well, none of my business, that."

    """
    Whatever the driver was thinking, they didn't say more, leaving me to gaze flabbergasted
    at each wonder we passed by.

    It's not that I hadn't seen magic before. The local spirit temple would perform rituals during
    holidays which were impressive demontrations in their own right.

    But the tone was always of stoic reverence, giving thanks and showing devotion to the spirits.

    It was nothing like this.
    """

    "Driver" "It always gets lively right before the start of a new term. Plenty to see in town."

    """
    The driver seemed to notice me gaping out the windows with a grin.

    I continue staring, nearly hanging out the window at one point to try to read the writing
    on a shop sign that was revolving on its own, and I could swear it had changed its text
    since its last revolution.
    """

    "Driver" "Well, I'm sure you'll be learning a lot up there. And we're not too far now."

    show bg school approach night with dissolve

    "As we round the bend on the street I finally get a proper view at our destination:
    The Magical Institute of Ardenvale

    Home to the most advanced magical research in the world.

    No one could see that castle bearing down on them and hang onto any shread of misplaced confidence.
    Visitors were at the mercy of the powers that reside here.
    """

    call .welcome

    $ callback()

label .welcome:

    show bg admin night with dissolve

    "We finally make it to the entrance where the driver drops me off along with
    the lone bag that comprises all my wordly posessions."

    "I can hardly take a step inside the grand doors before I'm ambushed by an administrator."

    "Administrator" "Welcome to the institute! We hope your journey was a pleasant one?"

    mc.says "Oh, it \u2014"

    "Administrator" "May I see your invitation?"

    "They deftly swipe the invitation from my hands just as I'm producing it from my pocket."

    "Administrator" """Oh, very interesting. Yes, we've certainly been expecting you.

    Well I'd love to give you a tour of the grounds you'll be calling home, but it's dreadfully
    late already and you must be exhausted.

    Let me lead you to where you'll be staying."""

    "They grabbed my arm with too much strength for someone with their frame and dragged me out
    the door I just came in."

    "Administrator" """Most of the students have already arrived and are resting in their rooms.
    Do try not to make any undue ruckus in the dormitories.

    As you should already be aware, tomorrow is the opening ceremony for the new term.
    That will be the first day of your new life here.

    For now here are the keys to your room. There is a strict curfew once classes begin but it
    would be wise for you to begin practicing it now.
    """

    "The dragging didn't stop until we got to the doorstep of my room."

    "Administrator" "Oh, how exciting! We expect great things from you, so be sure to get some rest."

    show bg dorm room night with dissolve

    """Practically dumping me there, they finally let me go, and briskly walk away without
    ever letting me get a word in.

    Which is well enough. They were right that I was exhausted.

    Entering my new room, I drop my bag to the floor, not bothering to unpack,
    and let myself drop into the bed.

    Between the excitement of everything I saw in town on the ride in and my nerves confronting the
    reality of actually being a student here, I'm worried that I won't be able to get any rest at all.

    On the other hand, the journey here had been long and it all seemed to be catching up with
    me now as I let out a yawn.

    What had they said? They "expect great things?"

    I stifle another yawn as my eyelids grow heavy and I let sleep take me.
    """

    show bg black with dissolve

    return


init python:
    plot_schedule.schedule_event((0, TOD.NIGHT), Event("day0"))