

##

label prologue0(callback):
    show color_black
    """
    I had been preparing for this journey for a long time.

    Weeks spent practicing what to say, how to act, how I'd make a first impression.
    How I'd definitely not make a fool of myself.
    """

    show bg carriage night

    """
    All such resolutions were totally forgotten as I hung halfway out the window of
    my carriage gaping at the sights we passed.

    The cariage rolled down cobbled streets lined with market stalls and filled with lights.
    One could hardly tell the sun had set more than an hour ago, for all the bustle going about.

    <Here there should be more description of the magical technologies at play>

    The driver would turn back to eye me every so often but his judgement was the least of my concerns.
    """

    """
    The caravan I had been traveling with had setup camp just outside the city walls and
    I was more than a little surprised to find the cariage waiting for me.

    It was my first time riding in one and the novelty wasn't helping my nerves.

    I unconsciously grip the invitation in my pocket, already damp with moisture from my palms.

    And then as we turn a turn a bend I can finally get a clear look at our destination:
    The Qyburn Magical Institute.
    """

    show bg school approach night

    """
    Yep, no one could see that castle bearing down on them and have any shread of misplaced confidence.
    Visitors were at the mercy of the powers that reside here.
    """

    call .welcome

    $ callback()

label .welcome:

    show bg admin night

    "administrator" "Welcome to the institute! We hope your journey was a pleasant one?"

    "MC" "Oh, it --"

    "administrator" "May I see your invitation?"

    "They deftly swipe the invitation from my hands just as I'm producing it from my pocket."

    "administrator" """Oh, very interesting. Yes, we've been expecting you.

    Well I'd love to give you a tour of the grounds you'll be calling home, but it's dreadfully
    late already and you must be exhausted.

    Let me lead you to where you'll be staying.

    Tomorrow you'll be free to acquaint yourself with the grounds and the town.
    You'll surely meet other students and prospects flitting about.

    Then Monday, of course, is the opening ceremony for the new term. That will be the first day
    of your new life here.

    For now here are the keys to your room. There is a strict curfew once classes begin but it
    would be wise for you to begin practicing it now.

    Oh how exciting!
    """

    show bg dorm night

    """The school administrator, whose name I never caught, had been tightly gripping my arm the
    whole walk from the office to my room.

    Practically dumping me on the doorstep as they finally let me go, they briskly walk away without
    ever letting me get a word in.

    Which was well enough. They were right that I was exhausted.

    Entering my new room, I drop my bag to the floor, not bothering to unpack,
    and drop myself into the bed.
    """

    return


init python:
    plot_schedule.schedule_event((0, TOD.NIGHT), Event("prologue0"))

##

label prologue1(callback):

    "The next morning, everything was fine. The end."

    $ callback()

init python:
    plot_schedule.schedule_event((1, TOD.MORNING), Event("prologue1"))

##
