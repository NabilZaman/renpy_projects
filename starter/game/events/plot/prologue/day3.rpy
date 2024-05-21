
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

label day3_afternoon(callback):

    """
    After class I decided to tour the campus a bit; it would be good to know my way around.

    I knew from the signage around the administration that the school had a number
    of facilities outside of the lecture halls.

    There was a garden, music rooms, and a sports field as well as a man-made lake somewhere
    off-campus.

    The campus itself was pretty empty, most of the students from class had made their way back
    to the dorms or into town, with only a few loitering on campus.

    My wanderings take me near the sports field and I decide to check it out.

    The field itself is wide and fairly well maintained without any tall grass that would
    get in the way of activities.

    But circumscribing the field was a dirt path with chalk drawn lines at regular intervals.
    I spot someone running along this track.
    """

    call .sports_character_encounter

    $ callback()

label .sports_character_encounter:
    "They seem to notice me and slow to a stop as they come around. They're breathing is
    heavy but their run doesn't seem to have phased them as they cheefully greet me."

    show expression sc.image

    sc.meet()

    sc.says "Hey! Fancy seeing a new face around here. Are you a new student?"

    mc.says "That's right, I'm [mc.name()]."

    sc.introduce()

    sc.says """Just [mc.name()], huh? Well in that case I'm [sc.name()]. It's a pleassure to
    make your acquaintence.

    How are you liking your time at Ardenvale so far? The first week for aspirants can be a bit
    of a doozy.
    """

    menu:
        "What do I say?"

        "It's been great!":
            mc.says "I've been incredible! I didn't really have a chance to study magic
            before so it's amazing how much I'm learning in just a couple classes."

            sc.says "That's great to hear. I know my first week was grueling but you definitely
            learn a lot of really important foundational skills."

        "It's been pretty rough.":
            mc.says "It's been pretty rough. I didn't really have a chance to study magic
            before so I feel pretty behind after just a couple of classes."

            sc.says "Oh that's too bad. But don't get discouraged, the fundamentals class is
            designed to give you a solid foundation. If you stick with it you'll pick up a load
            of useful skills that will serve you the rest of your time here."

    mc.says "Are you also a student here? I haven't seen you in the intro class."

    sc.says """
    Haha no, I am a student, but I've already done my time in that class, thank you very much.

    I'm a third year. Most of the upperclassmen won't start trickling in till the end of this week
    as classes for us don't start until next week.

    I just so happen to have arrived early to take care of a few things for one of my research
    advisors. And you've caught me working off some pent up energy out on the track here.
    """

    "That's right, upperclassmen. Somehow it didn't occur to me that there would be older students
    here, I guess because I hadn't run across any yet."

    mc.says "Oh, wow. I somehow didn't picture magic students would be getting much exercise."

    sc.says """
    Hah, yeah it doesn't really fit the stereotype, does it? Just goes to show how poorly magic
    is understood in the general population, really.

    There's a lot to be gained by building the up your physical as well as you mental capacities.
    From building strength to simply improve your channeling endurance to the more ephemeral
    goal of broadening your horizons to be able to pull from more varied expereinces in your
    channeling.

    The school doesn't have instructors on-staff for non-magical disciplines but there are plenty
    of student-led clubs for all sorts of interests. From music to sports or even mundane academic
    subjects like mathematics and poetry.

    The school understands these all have their applications in furthering the abilities of
    the mages who invest in them, but it's left to students to pursue them at their own behest.

    And I just so happen to get antsy if I don't have a physical outlet so I'm in pretty much all
    the sports clubs.
    """

    mc.says "I had no idea. I hope I have a chance to try some of these out."

    "Though I worry I won't have much of a chance between my guild duties and trying
    to keep up with school."

    sc.says """You definitely should try them out! But not yet. You first years need to focus on
    getting through Quals before you can start worrying about anything else.

    Anyway, I've gonna squeeze in a few more laps before lunch. I'll see you around!
    """

    "I leave the track and get on with my afternoon."

    return

label day3_night(callback):
    scene bg dorm room night with dissolve

    """
    I make it back to my room at the end of the day, exhausted.

    I'm surprised by how physically taxing channeling has proven, and my head still hasn't
    forgiven me for pushing myself so hard in class today.

    The moon is bright enough to light up my room and I'm tempted to stay up a little bit longer.

    I had vague intentions of doing some attuning practice tonight, but I don't think my head can
    I can take much more today so I just pull the curtains shut.

    I slide into bed, thankful the academy designed the accomodations to satisfy its primarily
    noble student body, and drop into sleep so quickly I hardly notice the thrumming that's begun
    in my ears.
    """

    call .dream

    $ callback()

label .dream:
    """
    ...

    My ears ring loudly now, and my head's throbbing so hard I wince at the pain.

    No. Not at the pain, at the light.

    The flickering is so bright. I thought I had closed my curtains?

    And there's a heat. It's so intense. I can't sleep like this.

    Or am I already sleeping? I must be dreaming...

    The sensations are already fading as my thoughts work to catch up,
    and the stillness of sleep reclaims me.
    """

    return


init python:
    plot_schedule.schedule_event((3, TOD.MORNING), Event("theory_lesson2"))
    plot_schedule.schedule_event((3, TOD.AFTERNOON), Event("day_3_afternoon", takes_time=False))
    plot_schedule.schedule_event((3, TOD.NIGHT), Event("day3_night"))
