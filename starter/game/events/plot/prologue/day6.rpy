
label theory_lesson5(callback):

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

    call .dream

    $ callback()

label .dream:
    """
    ...

    Through the now-familar buzzing that joins me in my dreams each night, I notice another
    sound layered on top of it. A crackling.

    The lights I've seen before are clearer. Reds and yellows and oranges.

    And a new sensation strikes me. I can smell Smoke.

    When the witch caught us I panicked and ran.

    I was holding the little artifice my parents use in their tavern.

    The building isn't so big, and there's not a lot of room for tables inside. So half of them are
    set up outside.

    But nights here can get real cold. So we've got a few of these artficial flames set up in cages
    all around the tables so folks can enjoy some warmth while they're eating.

    But when we got caught I was so surprised I lost it. I must have dropped it while we were running.

    Now I'm back at the abandoned temple. The artifice must have triggered and the long dead and
    untreated wood of the structure eagerly took to the flame.

    The flame grows and grows and consumes everything. I feel it coming to get me and I'm ready
    to accept it.
    """

    return

init python:
    plot_schedule.schedule_event((6, TOD.MORNING), Event("theory_lesson5"))
    plot_schedule.schedule_event((6, TOD.NIGHT), Event("day6_night"))
