
##### Day 2 #####

# - Have a pop-up modal.
# - it will reiterate the narrative deal (qualifying exam) and how it will play out in
#   game mechanics
# - Make sure the locations are set up so that it is technically possible, but difficult, to fail
#   by just ignoring the classes and fucking about in town or whatever.

label day2(callback):

    scene bg school infirmary morning with dissolve

    """
    I wake up the next morning in a room I don't recognize with a throbbing headache.

    The bed is firm and not as comfortable as the one in my room, and everythign is so bright -
    the sheets, the floor, the curtains half-shuttered around my bed are all a stark white.

    The sun shining through the tall windows seems to be determined to target me in particular
    and aggrevates the throbbing in my head.

    I hear footsteps against the shining stone floor as my stirring gets the attention of
    whoeever is attending here.
    """

    show expression sn.image

    sn.says """
    Good morning sleepy-head.

    I don't know what you think you're doing working yourself half-to-death before classes
    have even begun.

    There's always a few of you each year who don't know your own limits and wind up in here
    the first week, but I have to say you've really jumped the gun.
    """

    "I'm not really sure what she's talking about, and my confusion must be showing on my face
    as she looks concerned and cuts her lecture short."

    sn.says """
    I looked you over last night and you had the classic signs of channeling sickness.
    Not uncommon among students who get a bit overzealous in their studies or while trying to show
    off.

    Generally nothing you need but to get some rest and let your body take care of itself.
    You do know where you are, don't you?
    """

    mc.says "Qyburn Academy?"

    $ sn.introduce()

    sn.says """
    That's right, you're in the infirmary at the Academy, hun.

    You were brought in last night by a sweet old thing who was quite shook up with you collapsing
    on her. I didn't catch the full story but you really shouldn't be channeling so heavily,
    especially off campus.

    Now, the school doesn't have any explicit rules against it, but if you're fool enough to
    wind up in here again I won't let you off with such a polite warning, you hear me?
    """

    "I'm still plenty confused, what channeling?"

    mc.says "Yes, ma'am... Though I really wasn't pushing myself."

    sn.says """
    You may have thought so, but the fact that you're lying here in one of my beds is evidence
    to the contrary.

    Judging by how your confused face has first-year written all over it, you'll
    probably be interested to know that your first class will be starting soon. If you've
    got the energy to argue you're probably right enough to get to class.
    """

    """
    That's right, classes start today! I jump out of bed pushing through the dizziness.

    Still a little confused and more than a little embarassed to realize I'm in a patient's gown
    and not the clothes I wore last night, I thank the nurse and quickly get changed before
    rushing to class.
    """

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


label day2_night(callback):
    scene bg dorm hallway morning with dissolve

    """
    I'm heading back to my room at the end of the day when I spot the student from the
    explosion yesterday working on something in front of her room.

    I stop for a moment to observe. Somehow it seems like she's managed to remount her door which
    is remarkable given the state it was in yesterday.
    """

    call .reintroduce_windgirl

    scene bg dorm room night with dissolve

    """
    I return to my room and collapse into my bed.

    Today was our first day of classes and while I feel like I'm learning a lot also feel way
    behind the other students. Plus a part of me is still worried about what the guild duties
    will turn out to be. Not to mention I woke up this morning in the infirmary after collapsing
    last night for reasons I still don't understand.

    But for now it's late and I'm plenty tired so I try to quell my doubts and get to bed.
    I can already feel a headache coming on.

    I close my eyes and begin to drift.
    """

    call .dream

    $ callback()

label .reintroduce_windgirl:

    """
    She seems to notice me watching her, which is alarming given how our meeting went yesterday.

    Yet, I somehow manage to resist the urge to promptly dash into my room and instead walk over
    to hers.
    """

    show expression wg.image

    mc.says "Hey, that's a really impressive job you've done on your door there."

    wg.says "Thanks, I'm used to fixing stuff up back home..."

    "She looks a bit uncomfortable, still."

    if state.flags.get('wg_bad_intro'):

        mc.says "I wanted to appologize about yesterday. I was wrong to push so hard."

        "She actually seems to brighten a little at this."

        wg.says "Yeah, well, you were wrong. But you're also fogiven.
        I was a bit pricklier than I intended to be."

        wg.aff_change(3)
    else:
        wg.says "I'm sorry about yesterday. I was a bit pricklier than I intended to be."

        mc.says "No need, I get it."

        """
        I say, not being entirely honest. I don't really get what the big deal
        was but I don't need to be making enemies of my hallmates on my first week.
        """

    mc.says "Well I can get out of your way then."

    wg.says "Look, just let me explain, will you?"

    "She blurts this out looking like she's had more to say but has been struggling to get it out."

    wg.says """
    I'm not used to any of this. The big castle, the elaborate furnishings, even just... being
    indoors so much.

    So the day of the oppening ceremony what do I do but blow up my big fancy room with furniture
    worth more than my family makes in a year. I was sure I was going to get kicked out if
    anyone found out.

    Then of course you show up.

    I'm not looking to go biting the heads off of everyone I meet, but I value my privacy to begin
    with and I just wasn't ready for any of this.

    So can we just start over?
    """

    mc.says "I'd love to."

    $ wg.introduce()

    wg.says "Great. I'm [wg.name()]. No house, just [wg.name()]."

    "House? Oh she means noble family."

    mc.says "I'm [mc.name()], I don't come from any noble house either."

    wg.says "Really? How'd you end up in here?"

    mc.says "I'm sponsored by the Adventurer's Guild."

    wg.says "No shit, I'm backed by the Navigator's Guild! I thought I was the only one."

    mc.says """
    Haha, yeah I think I've been a bit more clueless than you, to be honest.
    I didn't realize that most of the students here would be from noble families.

    All the accomodations and furniture are well beyond me too. The beds are the nicest I've ever
    slept on.
    """

    wg.says "Man, I'm the opposite. They're so soft I just can't get comfortable in them."

    "We've been talking this whole time in front of her room and it's in much better shape
    than it was yesterday, but her window doesn't look like it's been repaired yet."

    mc.says "So... I know you just said you valued your privacy, but I couldn't help noticing
    your window. You probably have it under control but it's a bit chilly tonight and I
    just want you to know I'm happy to help if you want it."

    "She looks back and shifts a little uncomfortably."

    wg.says "I found a replacement part, but the way it's mounted is pretty annoying. I guess
    I could use the help since you're offering."

    """
    I only let the shock show on my face briefly before she beckons me in to show me what needs
    doing. Apparently the new pane needs to be mounted from outside but there's a latch that needs
    to be depressed from inside so it's clearly meant to be a two person operation.

    I head outside with the replacement pane and locate the exterior of her room. She instructs me
    on how to put the pane into place. It takes a bit of force but eventually everything snaps into
    place.

    I return to her room to admire the product of our labor.
    """

    $ wg.aff_change(5)

    wg.says "Thanks for the help."

    mc.says "It's no trouble. Can't even tell this place was a disaster area just yesterday."

    "She gives me a light punch."

    wg.says "Alright that's enough help from you,"

    mc.says "But wait I've been dying to ask you how you blew up your room."

    wg.says "Ugh, that story can wait until {i}I've{/i} stopped dying from embarrasment at the whole
    ordeal. Good night."

    """
    She says this as she pushes me out of her room and closes her miraculously functioning door
    for emphasis.

    I was pretty worried after our first encounter but my heart feels a bit lighter riding
    on the hope that I may have made my first friend here.
    """

    return

label .dream:
    """
    ...

    I feel... heat. And pain. My head throbs insistently.
    And there's a persistent thrumming in my ears.

    The heat is coming.

    No, it's here. It's all around me.

    The thoughts are hard to pin down.

    The sensations fade as I finally settle into sleep.
    """

    return


init python:
    plot_schedule.schedule_event((2, TOD.MORNING), Event("day2", takes_time=False))
    plot_schedule.schedule_event((2, TOD.MORNING), Event("theory_lesson1"))
    plot_schedule.schedule_event((2, TOD.NIGHT), Event("day2_night"))
