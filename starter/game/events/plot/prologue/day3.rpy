
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
    plot_schedule.schedule_event((3, TOD.NIGHT), Event("day3_night"))
