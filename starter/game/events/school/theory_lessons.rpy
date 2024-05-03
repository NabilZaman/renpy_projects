# events/plot/theory_lessons.rpy
#
# Put events in this file that should run when the player attends magic theory class
#
# See the README.md for details on how you should define events.
#

### Event Container Definitions

define magic_theory_events = []

###

label generic_theory_class(callback):
    "The professor opens up the class to questions while we're free to independently practice
    chanelling."

    $ state.stats.magic_theory.gain(3)

    $ callback()

label theory_lesson1(callback):

    show expression ti.image

    $ ti.meet()

    $ ti.introduce()

    ti.says """
    Welcome, prospects, to Arcane {i}FUN{/i}damentals! I'm so excited to have you with me on this
    journey through the foundations of magic and spiritual channeling.

    Some of you join us with prior study into these matters, however there's a good chance such
    experience has left you with bad habits and misconceptions.

    My goal here is to smooth the rough and imbalanced backgrounds you all come to me with. We
    will be comprehensive, so you may find some of this redundant. It's up to you whether to
    take this seriously.

    On the other hand, for those of you who find yourself struggling to keep up, I cannot cater
    the lessons to you either. I have exactly one week to cover the sum total of humanity's
    understanding on magic theory so I don't have the luxury of slowing down.

    Now we'd best get into the lecture then. We have no time to dilly, let alone dally.
    """

    "I've been so preocupied by all the expectations on me that I had forgotten why I was so
    excited to come here in the first place. I'm fascinated by magic and no one could tell me
    anything about it back home."

    ti.says """
    Today we'll begin by covering the spiritual energies. These are the forces we tap into when we
    channel our spells and manipulate the world around us.

    Classically there have been many attempts to organize and understand these energies, however
    it's a remarkably difficult endeavor - inconsistencies and exceptions have a way of creeping in.

    The most common classical taxonomies identify six main types which will comprise the curriculum
    you'll study in your basic level classes here. Those students with the aptitude that find
    themselves joining one of the research groups here will learn there are many more types of
    energy that defy this system of classification that are the subject of active research.

    These six classical elements are: water, wind, fire, light, life, and kinesis.

    Why these six? What do these have in common?

    Dynamism. Movement. Change. This is the heart of magic. It is why we can make rain on a
    sunny day, give light to a moonless night. We can mend a broken limb but we cannot impede
    an oncoming blade. Magic is harnessing the essence of change itself.

    Now, the headmaster would have {i}my{/i} head if I spent all day lecturing on theory alone,
    so how about we put this to practice?
    """

    """
    The professor puts down his notes and across the room I hear chairs creek as we all lean
    forward, anticipating something is coming.

    He steps clear of his desk, and makes a sweeping motion with his arm as a slight chill falls
    on the room. I can't quite make out what he did until some other students gesture up
    and I notice the air is sparkling. Is that ice?

    He then lifts his finger to his mouth as if urging quiet. Moving his hand a few inches from
    his face and a small flame {i}poofs/{i} into place, floating above his finger.

    He opens his mouth, inhales loudly, and blows the flame into a massive fireball that seems
    to reach the vaulted ceiling. A loud hiss erupts as the suspended ice rapidly turns to
    steam that permeates the room.

    I'm so focused on the effect that I miss what he does next, but everything suddenly grows dark
    as the curtains are pulled over the windows all across the room. A few students scream as they
    can't contain their surpsise.

    We sit in darkness and silence for several long moments before a focused beam of light shines
    onto the front of the room where the professor is standing. Then another, and another,
    three lights in all shining on him from the corners of the room.

    I wait for his next move but he just looks up. I follow his gaze and am greeted by a dozen
    small rainbows flickering in the mist.

    After a few more moments of quiet, the curtains open wide and the effect fades.

    The professor is still standing in the front of the room, breathing heavily with a massive
    grin on his face, clearly having enjoyed his own performance.

    He then takes a bow and I join the rest of the class in applause.
    """

    ti.says "Hahaha, damn. That always takes it out of me but it's worth it to impress you lot."

    "He laughs while he works to catch his breath."

    ti.says """
    My little show there only made use of five of the six elements; I haven't managed to work in
    a compelling demonstration of life energy yet.

    So what have we learned besides that I am an incorrigable show-off?

    Well any of you who are already a bit practiced will know that it's actually quite difficult to
    switch quickly between the different elements, but you may not understand why. Let's get
    into the details and see if we can work it out.

    The process of channeling can be summarized in three steps:

    First, Attunement. You must attune yourself to the spiritual energy in question. This is hardest
    when you first attune yourself to a specific element, but it becomes easier and easier through
    repitiion until it is second nature.

    Second, Recall. You must recall the effect you are trying to create. This is key and where
    most students misstep. It is not enough to understand what the effect is, or how it looks, but
    you must evoke the experience of it to be able to materialize it again.

    To those of you who are newer to this, yes this means you can only channel phenomena with magic
    that you have experienced firsthand.

    In your other classes you will practice with simple, easily reproduceable experiences to reinfoce
    this process.

    Lastly, you must feed that experience with the mana from within you. The spiritual energies
    provide us with a template to follow, a mold to fill, but the material to fuel it comes from your
    own mana.

    These steps each get easier through practice, but it is particularly challanging to switch
    from attuning one element to another. The mental dexterity it requires to perform this transition
    smoothly is a skill all of its own.

    Which is to say, I am very impressive. You may now applaud again.
    """

    ti.says """
    Thank you for your attention. That concludes our lecture for this morning.

    After noon you will find each of the subject matter instructors will be hosting
    introductory lessons on their respective spiritual element of study.

    These will be hosted each day this week so feel free to attend them in any order you like.
    These lessons are not mandatory so feel free to self-study or take a walk about town if you
    prefer, it is a lovely day after all, but don't neglect preparing for your exams.
    """

    $ state.stats.magic_theory.gain(10)

    $ callback()

default intro_chosen_element = None
default effort_cost = 10

label theory_lesson2(callback):

    show expression ti.image

    ti.says "Welcome back to arcane fundamentals class! Last time we discussed the spiritual
    elements and the process of channeling them in the abstract. Today we'll begin our study
    on channeling by focusing on the first step: Attunement."

    "Some of the class emits an audible groan."

    ti.says "Yes, some of you will already be familiar with these drills. We will not be
    chanelling any complete spells today, feel free to practice at your own pace outside of my class."

    "Understanding catching up to me, I'm a little disappointed as well, but I suspect I could
    benefit from these drills more than anyone else in class so I shouldn't be ungrateful."

    ti.says "Because Attunement is a skill that more than any other improves through repitition,
    our exercises today will practice attuning to a single element repeatedly to develop that
    familiarity."

    menu:
        "Which element will I choose?"

        "Water":
            $ intro_chosen_element = 'water'
        "Wind":
            $ intro_chosen_element = 'wind'
        "Fire":
            $ intro_chosen_element = 'fire'
        "Life":
            $ intro_chosen_element = 'life'
        "Light":
            $ intro_chosen_element = 'light'
        "Kinesis":
            $ intro_chosen_element = 'kinesis'

    """
    I focus on the spiritual energies of [intro_chosen_element]. When I start off,
    the sensation is surprisingly familiar, a slight humming throughout my body.

    I have never intentionally channeled before, but I have once or twice done so on accident
    when I was particularly emotionally charged.
    I'm pleasently surprised that it feels natural already.

    After a while the effort starts to give me a headache.
    """

    menu:
        "What should I do?"

        "Push through it":
            "My headach gets much more intense, but I keep performing the drills."
            python:
                state.stats.magic_theory.gain(1)
                state.status.change_health(-effort_cost)
                state.status.change_mana(-effort_cost)
                effort_cost = 25

        "Take a break":
            "I take a short break and feel my headache subside.
            I continue the drills."

    ti.says """
    Most students by the time they're in their second year specialize in one of the
    elements. This is in large part due to how potent it is to dedicate your studies to
    attuning to a single element quickly and efficiently.

    You don't need to make such a decision immediately, it will probably do you good to have
    a more generalized grounding so you don't limit your options. But for now,
    as you're getting started, do stick to any one element as you continue to practice.
    """

    "There isn't that much time left in class and my effort has begun to tire me out."

    if effort_cost == 10:
        "The headache comes back, more intensely than before."
    else:
        "My persistent headache, which I've managed to ignore so far, grows near unbearable."

    menu:
        "What should I do?"

        "Push through it":
            "I push to continue my drills despite the throbbing and buzzing in my ears."
            python:
                state.stats.magic_theory.gain(1)
                state.status.change_health(-effort_cost)
                state.status.change_mana(-effort_cost)
            "I can only manage it for a little while before I collapse exhausted until class ends."

        "End my drills early and rest.":
            "I release my concentration and relief hits me immediately, though my headache doesn't
            go away completely by the time class ends."

    python:
        effort_cost = 10 # reset the cost, if this is something we do more, we should come up with a better system for this
        state.stats.magic_theory.gain(10)
        state.stats.get_skill_by_name(intro_chosen_element).gain(2)
        callback()

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

    "We keep the drills up throughout class, the professor offering more helpful hints."

    python:
        state.stats.magic_theory.gain(10)
        callback()

label theory_lesson4(callback):

    show expression ti.image

    # TODO: This lesson needs reworking more than most, revisit when we have a better idea around mana

    ti.says "Welcome back to arcane fundamentals class! Today will be the final day of our
    exploration of the mechanics of channeling as we discuss infusing our spell with Mana."

    "This is probably the subject I'm most familiar with so far."

    ti.says """Man I'm so uncofident about this mana thing.

    Mana is another concept with some traditional understanding that we've discovered to be
    incomplete with more research into the field.

    It is a energy of living things. You can use it to magic. You can also use it to not magic.
    """

    $ state.stats.magic_theory.gain(10)

    $ callback()

label theory_lesson5(callback):

    show expression ti.image

    ti.says """
    Today is the last day of our series on Arcane Fundamentals.

    Rather than focusing the lecture on any specific subject, today will be student guided. If you
    have any questions or areas you want elaboration on now is your chance to ask them before
    your exams tomorrow.
    """

    """
    We spend the class reviewing a number of concepts and clarifying channeling techniques.
    """

    ti.says "Before we conclude, does anyone have any final questions?"

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

init python:
    create_contained_event(magic_theory_events, 'generic_theory_class', reuse=True, priority=-10)
    create_contained_event(magic_theory_events, 'theory_lesson1', priority=100)
    create_contained_event(magic_theory_events, 'theory_lesson2', priority=99)
    create_contained_event(magic_theory_events, 'theory_lesson3', priority=98)
    create_contained_event(magic_theory_events, 'theory_lesson4', priority=97)
    create_contained_event(magic_theory_events, 'theory_lesson5', priority=96)


