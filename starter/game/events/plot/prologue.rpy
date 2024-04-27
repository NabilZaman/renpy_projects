

##

label prologue0(callback):
    show bg black

    "Driver" "So, m'lord, you're a new student at the institute, huh?"

    "M'lord?"

    show bg carriage night with dissolve

    mc.says "Hmm? Oh, yeah I suppose I will be."

    "Driver" "Pretty unusual, having a pick-up like this.
    Not that it's my first time carrying a student up there or anything."

    mc.says "Really?"

    "It was hard focusing on what the driver was saying when so much is happening all around the carriage."

    "There was so much life, so much motion. It was like... well, magic."

    "Driver" "It's just, you know, odd for one of you to be arriving on your own like this.
    Usually students will have their own retinue. And... more bags, you know?"

    mc.says "Mmhmm, yeah."

    "A child running right by us is carrying a stick rapidly changing in color with a stream of sparks flying off the end."

    "Driver" "So... you must be one them uh, 'special cases', huh?"

    mc.says "Might be."

    "Special what?"

    "Driver" "Too right, well, none of my business, that."

    "Whatever the driver was thinking, they got quiet after that, which let me focus on everything around us."

    "There were so many wonders on the street. A shop has a sign that spins on its own
    and reads a different slogan with each revolution."

    "And there! A woman has her baby in a carriage that seems to be pushing itself."

    "Driver" "It always gets lively right before the start of a new term. Plenty to see in town."

    "The driver seemed to notice me gaping out the windows with a grin."

    "I continue staring, nearly hanging out the window at one point to watch a fountain erupting with
    what appear to be flower petals that went off jus as we rode past."

    "Driver" "Well, I'm sure you'll be learning a lot up there. And we're not too far now."

    show bg school approach night with dissolve

    "As we round the bend on the street I finally get a proper view at our destination:
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

    mc.says "Oh, it \u2014"

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
    plot_schedule.schedule_event((0, TOD.NIGHT), Event("prologue0"))

##

label prologue1(callback):

    show bg black with dissolve

    play sound "effects/explosion.wav"

    "The next morning, I wake to the sound of an explosion."

    show bg dorm hallway morning with dissolve

    "I rush out of my room and into the hall, still dressed in my traveling clothes from last night."

    show wind_girl

    wg.says "Shit!"

    "I find another student standing in a doorway with the door dangling on a single hinge."

    mc.says "What happened? Are you alright?"

    wg.says "Yeah, it's... none of your business. You better not tell anyone about this, OK?"

    mc.says "Sure, I guess? Are you sure you don't need any help?"

    """By this point I've made my way in front of the room with the broken door.

    I try to peek around her to get a better look inside the room.

    I don't see any flames or major signs of destruction,
    but a lot of things are strewn across the floor along with a lot of shattered glass.
    """

    wg.says ""

    hide wind_girl with easeoutleft

    # "What is even going on here?"

    # show wind_girl with easeinleft

    # "???" "And just so we're abundantly clear, you're not a snitch, are you?"

    # "MC" "No, ma'am."

    # "???" "Good."

    # hide wind_girl with easeoutleft

    "..."

    call .follow_wind_girl


    $ callback()

label .wind_girl_reveal:
    mc.says "So what happened in here?"

    wg.says "I messed up, OK?"

    mc.says "You did this? How?"

    wg.says """I was just... breathing.
    I do breathing exercises in the morning.

    Just in.

    And out.

    It's just me and my breath. Flowing into my lungs, then back out again.
    It helps me... work through my anxieties, center myself.

    And sometimes, it feels like the wind joins me. Usually it's empowering. But today...

    I'm just not used to spending a lot of time inside. It's so stiffling.

    I don't really know what I did, but the next thing I knew the window burst open.
    """

    mc.says "Wow, that's amazing."

    wg.says "Sure, amazing. I've trashed my room and damaged school property and it's not even the
    first day of classes yet. "

label .follow_wind_girl:
    "I do my best to follow the mysterious student, but I don't really know my way around
    the dorm yet."

    "I turn the corner and notice that a door leading out is swinging shut."

    "As I step outside, she's ready for me and has me pushed against the wall, her fists around my collar."

    wg.says "Who are you and why are you following me?"

    $ wg.affection -= 1

    "Ruh roh!"

    return

label .administrators_discssing_special_cases:
    "Admin1" "We have many prospects this year that show a lot of promise."

    "Admin2" "Indeed. And 4 chosen by the guilds, twice as many as last year."

    "Admin1" "How are the guild prospects getting on?"

    "Admin2" "Excellent. The one chosen by the navigator's guild is especially powerful.
    She nearly evacuated her dorm room of air without lifting a finger. Caused quite the stir."

    "Admin1" "Hah! Wonderful. I have heard the artificers guild's chosen are both brilliant
    young minds."

    "Admin2" "An understatement. They have no understanding of basic artifabrication theory,
    and so they have no common sense to hold them back. They don't hesitate to achieve the impossible."

    "Admin2" "Give them a few years and they'll shake the world."

    "Admin1" "I'm sure their time here will be elightening for everyone involved.
    And what of the last one, the adventurers guild's chosen? I'm not sure I've heard much of them."

    "Admin2" "Ah yes, well that one is a bit of a curiosity."

    "Admin1" "Oh? How so?"

    "Admin2" "It's just to say... they so far seem completely unremarkable."

    "Admin1 frowns, as if they just saw someone urinating on their couch."

    "Admin1" "Well that can't be right. What did the guild include in their profile? What was the
    rationale for admission?"

    "Admin2" "They were the child involved in the Durindale incident."

    "Admin1" "Oh. I see. Then that is curious. And they haven't demonstrated any innate...
    talents? Tendencies? Anything that would shed some light on the matter?"

    "Admin2" "As I said, unremarkable. Which is not to say they are an idiot.
    Just they scored in 52% percentile in the qualifying exam."

    "Admin1" "How disappointing. But still, some mysteries run deeper than others.
    And this one especially has the potential to change everything."



init python:
    plot_schedule.schedule_event((1, TOD.MORNING), Event("prologue1"))

##
