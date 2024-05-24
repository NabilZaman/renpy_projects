
label theory_lesson5(callback):
    scene bg lecture hall morning

    show expression ti.image

    ti.says """
    Today is the last day of our series on Arcane Fundamentals.

    Rather than focusing the lecture on any specific subject, today will be student guided. If you
    have any questions or areas you want elaboration on now is your chance to ask them before
    your exams tomorrow.
    """

    """
    We spend most of class reviewing a number of concepts and clarifying channeling techniques.

    After which some of the students began asking questions outside the scope of what would
    be covered on the exam.
    """

    "Student" "Professor, we've only covered the lesser elements so far, what about the greater
    elements?"

    ti.says """
    Good question, though perhaps beginning on a bit of a false premise.

    As we mentioned in our first class, the six elements that we've covered, and that will be the
    focus of your basic level studies at the academy, are what I called "The Six Classical Elements."

    Now, what I glossed over is that their full name might more precisely be called
    "The Six Classical Lesser Elements." This, of course, implies the existence of some set of
    "Greater Elements" to be their counterpart.

    Well, while the lesser elements make up a convenient basis for teaching and training due
    their ease of use and the existence of long traditions of practice, the greater elements are
    anything but convenient.

    As I've mentioned before, spiritual taxonomy tends to be a losing battle, and there is no
    wide agreement on what members make up the class of "Greater Elements." Even the number of such
    elements varies widely on the source, with some claiming four, some six, some 12, one source even
    counting 43 in an exercise in the author's imagination.

    Some of these elements such as Earth and Lightning are the subject of active research,
    thought to be regarded as "Greater" due to just how rare and destructive the effects of
    channeling them these elements can be.

    Others such as Death and Time are simply nonsense used to liven up children's tales.

    I'd encourage any students with an inquisitive enough disposition to join a research
    group on campus in your later years here and take a hand at uncovering the truth
    behind some of these so-called "Greater Elements."
    """

    ti.says "Any last quesitons?"

    """
    Many of the other students around me look bored or half-asleep, but for me the novelty hasn't
    worn off. My mind is reeling from how much we've learned in just one week. This puts many of my
    experiences into perspective, but something about this explanation feels off.

    When it finally clicks and I shoot my hand into the air.
    """

    ti.says "Yes, a question in the back?"

    mc.says "Professor, you've covered a lot on spiritural energy, but what about the spirits
    themselves?"

    ti.says """Ah, an interesting line of inquiry. One that many have devoted their lives to
    researching with... inconsistent results.

    This is a subject I've glossed over in the interest of time but I'm glad you've asked and
    you deserve an answer.

    To cut to the heart of your question, you seek to personify the energies we call upon in
    our practice of magic. Many traditional belief systems teach of these beings we call
    "the spirits", give them will, give them agency.

    But our way here is of empiricism. We conclude only what we can see, what we can touch, what
    we can measure.

    It's not that magi have disproven the existence of spirits, per se. It's just that the
    question is ill formed. We cannot know whether the the spirits have will anymore than we
    can know whether the earth or the sky or the chairs upon which you rest have will. Do they
    mind your rear end pressed upon them? Perhaps they fancy some more than others?

    Of course the spirits are where we get the modifier "spiritual" that we ascribe to this energy
    and how we channel it. Whether you interpret this as a linguistic holdover or literally is a
    matter of personal belief and not in the domain of these lectures.
    """

    "I shouldn't be but I'm still surprised by how differently people here
    consider the spirits than back home."

    menu:
        "I guess he's right":
            $ state.stats.spiritual_affinity.gain(5)
            "I'm not surprised to hear this perspective, and there is a logic to what he's saying.
            Maybe the spirits are just a superstitious interpretation of these energies."

        "That doesn't feel right to me":
            $ state.stats.spiritual_affinity.gain(-5)
            "I can see what he's saying, but I've always been able to feel the spirits.
            It doesn't makes sense to deny that now."


    ti.says "I believe that's all the time we have. I wish you all the best of luck
    on your exams tomorrow. If you apply yourself as you've done in my class, I have no doubts you'll
    come out victorious."

    $ state.stats.magic_theory.gain(10)

    $ callback()

label day6_night(callback):
    scene bg dorm room night with dissolve

    """
    I return to my room at the end of the day. I'm tired but it's still not too late and
    I'm not ready to sleep.

    Tomorrow will be the the exam. I don't really feel ready yet, so I pull out my notes
    from this class and decide to review what we've learned.

    I hadn't spent more than 10 minutes going through my notes before I hear the sounds of
    rapid footsteps down the hall accompanied by what sounded like banging on doors.
    """

    "???" "Get up! Get out! Aspirants out of your rooms!"

    """I open my door to get a look at what's going on.

    I see several older students running down the halls, banging on doors.

    Other students are opening their room doors, looking as confused as I am, many of them
    in their nightwear.
    """

    "Older Student" "Everyone get out! Come on let's go, let's go. Get a move on."

    "One of the upperclassmen catch sight of me peeking out from my room."

    "Older Student" "You there, stop dawdling and get out of there. Everyone out into the couryard!"

    call .initiation

    scene bg dorm room night with dissolve

    call .dream

    """
    Tonight the thrumming begins earlier than before.

    I realize it's the same sensation I get when I push myself too hard to attune to the spirits.
    Except, different.

    It's deeper, and somehow... more insistent.

    It must be some sort of after-effect of working myself so hard in clases.

    Perhaps everyone feels this when they first start studying magic, but all the other students
    began study with private instructors when they were much younger.

    In any case it's been such a consistent companion to me these last few nights that it's
    almost comforting.

    I'm able to ignore it well enough that it doens't take long to fall asleep.
    """

    $ callback()

label .initiation:
    scene bg school fountain night

    """
    I join the crowd of first year students shuffling out the dormitory doors.
    A general murmur of confusion and annoyance covers up the underlying quiet
    unease we all felt. What was going on?

    There was a chill in the air that I shivered against; the nights had started to grow colder
    and I didn't think to grab a cloak on the way out of my room.

    Some other upperclassmen seemed to be stationed out in the couryard and were directing the
    crowd further.
    """

    "Older Student" "To the fountain, move along now, pick up the pace."

    """
    As the train of first years arrived near the rather impressive fountain at the center of the
    courtyard, other upperclassmen were already organizing us into a ring around the structure.

    I had learned the fountain itself was powered by water artifice, not dissimilar from the
    self-filling wash basins in the restrooms in the dorms, and would erupt with
    water at regular intervals puting on a show that less than a week ago would have left me stunned.

    It was still plenty impressive while we mingled into a circle around the fountain while
    the last stragglers funneled in and we all awaited further instruction.

    A the upperclassmen we forming a group themselves as they were released from their
    duties ushering the first year students. Several were stepping onto what seemed to be an
    improvised wooden podium while the rest were positioned on the ground at the
    opposite end of the circle.

    One of them upperclassmen on the podium stepped forward carrying a large gnarled staff.
    She cleared her throat to speak.
    """

    wc.says "Aspirants! Brothers and sisters to be. Heed me."

    """
    The effect was similar to when the headmaster addressed us in the opening ceremony, though
    not quite as pronounced.

    As if on cue the fountain quieted down as it completed its latest cycle of eruptions and
    became motionless more quickly than could be natural.
    The whispering stopped and the crowd was as still as the water.
    """

    wc.says "{size=40}You come seeking power.{/size}"

    """
    {size=40}*BAM*{/size}

    She slams her staff on the podium and ripple moves across the water in the fountain.
    """

    wc.says "{size=20}You will have it.{/size}"

    wc.says "{size=40}You come thirsting for knowledge.{/size}"

    "{size=40}*BAM*{/size}"

    wc.says "{size=20}You will have it.{/size}"

    wc.says "{size=40}You come wanting a home.{/size}"

    "{size=40}*BAM*{/size}"

    wc.says "{size=20}You will find one here.{/size}"

    "With each successive slam of her staff the water is aggitated more strongly. It's roiling now,
    sloshing against the sides of the fountain."

    wc.says "But these gifts must be earned."

    wc.says "You will work, and you will struggle, and you will grow. But this will not be enough."

    "{size=40}*BAM*{/size}"

    """
    Her strike of the staff seems to cause the water of the fountain to erupt again.
    But not in a graceful spectacle as it does on its regular schedule.
    It forms a torrential wall of water 11 or 12 feet high around the fountain.
    """

    wc.says "{size=20}The obstacles in your path are too great to face alone.{/size}"

    """Her voice sounds almost solemn but it's hard to take notice as
    the water starts to swirl, frothing and growing angrier.

    Several students inch away reflexively but the crowd is packed enough that most have
    no room to move.
    """

    wc.says "Tomorrow you will take your exams and some of you will earn your places here
    at the Academy. The rest will return from whence they came. But tonight I bind you as one."

    """And the swirling water, barely contained by the magic fueling it, is set free as a deluge
    washes over the crowd of first years and we erupt in shrieks of alarm.

    The force of the water isn't actually so bad. No one I could see fell over, though several
    were bracing themselves on each other.
    But the force of the impact wasn't the real effect.

    It wasn't anywhere near freezing tonight, but the wind was persistent enough that
    being abruptly soaked through had suddenly made everyone very uncomfortably cold.

    The upperlassman leading the event had to raise her voice beyond its already magically
    aplified levels to speak over our alarmed reactions.
    """

    wc.says "You will pledge your strength to each other!"

    "{size=40}*BAM*{/size}"

    "The exclamations quieted down and while I stood there shivering it took me a while to notice
    the wind had completely stopped."

    wc.says "You will pledge your strength to the school!"

    "{size=40}*BAM*{/size}"

    """
    On the other end of the fountain where the other group of upperclassmen had gathered, roughly
    half of them had channeled large flames suspended in front of them. I couldn't feel the heat from
    where I stood but the light was almost blinding against the dark night.
    """

    wc.says "You will pledge your strength to the realm!"

    "{size=40}*BAM*{/size}"

    "And a force of heated wind blew over the crowd of shivering students, easing our "

    # wc.says "One __, one ___, one family of magi united across the realm."


    """You have come here yearning. You have come here wanting."""

    "You will be bound."

    "You will be united."

    "You will pledge your strengths to the school and each other."

    ""



    return

label .dream:
    """
    ...

    Through the now-familar buzzing that joins me in my dreams each night, I notice another
    sound layered on top of it. A crackling.

    The lights I've seen before are clearer. Reds and yellows and oranges.

    I can smell smoke again.

    When the witch caught us I panicked and ran.

    I was holding the little artifice my parents use in their tavern.

    The building isn't so big, and there's not a lot of room for tables inside. So half of them are
    set up outside.

    But nights here can get real cold. So we've got a few of these artficial flames set up in cages
    all around the tables so folks can enjoy some warmth while they're eating.

    But when we got caught I was so surprised I lost it. I must have dropped it while we were running.

    Now I'm back at the abandoned temple. The artifice must have activated and the long dead and
    untreated wood of the structure eagerly took to the flame.

    The conflagration grows and hungers. It consumes everything.

    I feel it coming to get me and I brace myself to meet it.
    """

    return

init python:
    plot_schedule.schedule_event((6, TOD.MORNING), Event("theory_lesson5"))
    plot_schedule.schedule_event((6, TOD.NIGHT), Event("day6_night"))
