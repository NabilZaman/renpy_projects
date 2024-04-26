

##

label prologue0(callback):
    show bg black

    "Driver" "So, m'lord, you're a new student at the institute, huh?"

    "M'lord?"

    show bg carriage night with dissolve

    "MC" "Hmm? Oh, yeah I suppose I will be."

    "Driver" "Pretty unusual, having a pick-up like this.
    Not that it's my first time carrying a student up there or anything."

    "MC" "Really?"

    "It was hard focusing on what the driver was saying when so much is happening all around the carriage."

    "There was so much life, so much motion. It was like... well, magic."

    "Driver" "It's just, you know, odd for one of you to be arriving on your own like this.
    Usually students will have their own retinue. And... more bags, you know?"

    "MC" "Mmhmm, yeah."

    "A child running right by us is carrying a stick rapidly changing in color with a stream of sparks flying off the end."

    "Driver" "So... you must be one them uh, 'special cases', huh?"

    "MC" "Might be."

    "Special what?"

    "There were so many wonders lining the streets. A shop has a sign that spins on its own
    and reads a different slogan with each revolution."

    "And there! A woman has her baby in a carriage that seems to be pushing itself."

    "Driver" "It always gets lively right before the start of a new term. Plenty to see in town."

    "The driver seemed to notice me gaping out the windows with a grin."

    "Driver" "Well, I'm sure you'll be learning a lot up there. And we're not too far now."

    show bg school approach night with dissolve

    "And as we round the bend on the street I finally get a proper view at our destination:
    The Magical Institute of Qyburn"

    "Home to the most advanced magical research in the world."

    "No one could see that castle bearing down on them and hang onto any shread of misplaced confidence.
    Visitors were at the mercy of the powers that reside here."

    call .welcome

    $ callback()

label .welcome:

    show bg admin night with dissolve

    "We finally make it to the entrance where the driver drops me off along with
    the lone bag that comprises all my wordly posessions."

    "I can hardly take a step inside the grand doors before I'm ambushed by an administrator."

    "Administrator" "Welcome to the institute! We hope your journey was a pleasant one?"

    "MC" "Oh, it \u2014"

    "Administrator" "May I see your invitation?"

    "They deftly swipe the invitation from my hands just as I'm producing it from my pocket."

    "Administrator" """Oh, very interesting. Yes, we've certainly been expecting you.

    Well I'd love to give you a tour of the grounds you'll be calling home, but it's dreadfully
    late already and you must be exhausted.

    Let me lead you to where you'll be staying."""

    "They grabbed my arm with too much strength for someone with their frame and dragged me out the door
    I just came in."

    "Administrator" """Tomorrow you'll be free to acquaint yourself with the grounds and the town.
    You'll surely meet other students and prospects flitting about.

    Then Monday, of course, is the opening ceremony for the new term. That will be the first day
    of your new life here.

    For now here are the keys to your room. There is a strict curfew once classes begin but it
    would be wise for you to begin practicing it now.
    """

    "The dragging didn't stop until we got to the doorstep of my room."

    "Administrator" "Oh, how exciting! We expect great things from you, so be sure to get some rest."

    show bg dorm room night with dissolve

    """Practically dumping me there, they finally let me go, and briskly walk away without
    ever letting me get a word in.

    Which was well enough. They were right that I was exhausted.

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
    plot_schedule.schedule_event((0, TOD.NIGHT), Event("prologue0"))

##

label prologue1(callback):

    show bg black with dissolve

    "The next morning, I wake to the sound of an explosion."

    # play sound effect

    show bg dorm hallway morning with dissolve

    "I rush out of my room and into the hall"

    "MC" "What happened?!"

    show wind_girl with easeinright

    "???" "Nothing happened. You never saw me."

    hide wind_girl with easeoutleft

    "What is even going on here?"

    show wind_girl with easeinleft

    "???" "And just so we're abundantly clear, you're not a snitch, are you?"

    "MC" "No, ma'am."

    "???" "Good."

    hide wind_girl with easeoutleft

    "..."

    $ callback()

init python:
    plot_schedule.schedule_event((1, TOD.MORNING), Event("prologue1"))

##
