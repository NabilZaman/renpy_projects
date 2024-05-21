
label theory_lesson3(callback):
    scene bg lecture hall morning

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

    $ state.stats.magic_theory.gain(10)

    "We keep the drills up throughout class, the professor offering more helpful hints."

    ti.says "That marks the end of today's lesson. You all displayed a good effort. Those of you
    you had trouble with this step, don't lose heart. You'll have more opportunities to refine your
    technique during tomorrow's lesson."

    "With that he dismisses us for our free afternoon period."

    $ callback()

label day4_afternoon(callback):
    scene bg school courtyard morning with dissolve

    """
    We filter out after class each going our separate ways. I'm fatigued from the effort of
    practicing Recall today. While I could tell I was getting somewhere it never felt like
    it fully clicked.

    I want to find a quiet place to keep practicing, but I think back to waking up in the
    infirmary earlier this week and think better of pushing myself any harder today.

    Instead I remember reading that there was a library on campus. If I can't practice more today,
    maybe I can find some useful reference material there.
    """

    call .library_encounter

    $ callback()

label .library_encounter:

    scene bg school library with dissolve

    """
    It doesn't take me long to find the library and when I enter I'm struck first by how dark it is.
    It was an aggressively sunny day outside but despite having a vaulted ceiling with large windows,
    the sunlight seems to shy away from the interior of the library building.

    It's takes a moment for my eyes to adjust before I notice the second thing to strike me about
    the place: the massive staircase leading down below the floor.

    The library itself seems to be a single story structure from the outside, though with
    tall enough ceilings to grant the building the prestige it deserves. But from inside it becomes
    clear that it extends for many floors down, from the angle of the railing it's not clear how many
    floors the spiral staircase descends.

    The staircase itself is maybe 40ft across and each quarter turn descends another floor deeper
    into the bowels of the facility.

    I'm so entranced by the architecture that it takes me a while to notice the third thing that
    strikes me: I'm not alone.

    Well, to be clear, the first thing I took note of was that I was alone, or so I thought. But
    that wasn't too surprising as my experience so far has been there are so few of us
    on campus yet that nearly anywhere you go you're more likely than not to have the whole place
    to yourself.

    But in fact, there was someone already here. Another student was settled into corner with
    half a dozen cushions surrounding them.

    They were poring over a large tome nearly half their own height, but the most
    bizarre feature of the scene was that while the student was nestled snug in their cocoon
    of pillows, the tome was completely unsupported, suspeded in space in front of them.

    I'm so intrigued I don't think twice about stepping up to them and interrupting their
    study.
    """

    mc.says "Hi, uh, what are you reading?"

    """
    My interjection seems to startle them completely as the next moment the tome ceases to ignore
    gravity and lands with a loud {b}*THUMP*{/b} on the ground.

    I move to apologize for intrusion but the student has retreated deeper into their cocoon \u2014
    there must have been more cushions than my initial estimate \u2014 and the next thing I know
    one of the pillows is flying straight at me.

    I don't have much experience reacting to these sorts of attacks so I take the full force of it
    to the face. It's actually quite pleasant.
    """

    mc.says "Mmph. I'm sorry, look I didn't mean to startle you, I'm a new student and I was just
    looking around the library. Can you please stop attacking me?"

    "The pillow gremlin peeks her head out of her fort and looks a bit appologetic."

    show expression mg.image

    $ mg.meet()

    mg.says "Sorry."

    mc.says "It's alright. My name's [mc.name()]. Are you also a student here?"

    "Still halfway enclosed in pillows, they nod."

    $ mg.introduce()

    mg.says "[mg.full_name]."

    "She looks really young to be a student, but I don't really know the school's
    admissions policies."

    mc.says "Nice to meet you. I haven't seen you in class, are you an upperclassmen?"

    "She shakes her head vigorously."

    mg.says "No. I'm joining this year. Maybe."

    "Maybe? The combative tension has let up enough that I finally spare a glance at the tome she
    was reading. \"insert_something_complicated_sounding_here\""

    mc.says "Okay... well to be honest I didn't have any good reason to intrude.
    I'm sorry to have bothered you."

    "I move to leave when she erupts from her chrysalis."

    mg.says "Wait!"

    "I stop and get a good look at her for the first time. She's a good foot shorter
    than me, at least, and can't be more than 13 or 14 years old."

    mg.says "What do you know about mysteries?"

    mc.says "Mysteries?"

    "She nods her head aggressively, and I swear I can see her eyes twinkle."

    mg.says "The wandering closet. The invisible club. The fountain of blood."

    "I didn't think she could baffle me further. But here I am, baffleder than before."

    mg.says "The school hides mysteries. I want to know. I need to."

    mc.says "I'm sorry, I'm not familiar with any of those... mysteries."

    "She looks dejected, then determined."

    mg.says "Will you look?"

    "She wants me to uncover mysteries in the school?"

    mc.says "I mean, yeah, sure? If I come across anything about those mysteries I'll let you know."

    mg.says "Not just these. There are lots. Tell me what you learn."

    mc.says "Ok, I promise."

    """
    She looks at me critically for a moment then, seemingly satisfied with the outcome of our
    conversation, *Thwumps* back into her pile of cusions.

    She gives me one last appraising eye before the massive tome that has been resting on the
    floor since she dropped it lifts back into its place in front of her, flipping to where it
    left off.

    I've completely lost track of what I was doing in the library to begin with, so I make my
    retreat to somewhere that I desperately hope makes a little more sense.
    """

    return

label day4_night(callback):
    scene bg dorm room night with dissolve

    """
    I don't have a chance to stop and consider it outside of times like this, but my dreams
    have been more vivid than usual. The stresses of my new life here must be getting to me.
    """

    call .dream

    $ callback()

label .dream:
    """
    ...

    Reality melts away to make room for the land of dreams. I'm lucid enough for it to
    occur to me that I've been dreaming more than usual recently.

    This one is familiar.

    The heat, the lights, they're the same as last time. But another sense
    assaults me tonight. The smell.

    Smoke.

    It's not just pungeant, as I drift deeper into the dream, it's suffocating.

    I gasp for air as the panick rises within me.

    I need air.

    I need to get out.

    I try to scream but taking in enough air to do even that burns my throat.

    I can't speak; I can't think anything except how I can't breathe and I'm going to die.

    Until suddenly it's over.

    Relief washes over me as the last remnants of my consciousness slips away into sleep.
    """

    return

init python:
    plot_schedule.schedule_event((4, TOD.MORNING), Event("theory_lesson3"))
    plot_schedule.schedule_event((4, TOD.AFTERNOON), Event("day4_afternoon", takes_time=False))
    plot_schedule.schedule_event((4, TOD.NIGHT), Event("day4_night"))
