

##################################################################################
# Unused Prologue Scenes
##################################################################################

label .unused_sink_encounter:
    show bg black
    show sink at truecenter
    with moveinbottom

    """
    Each basin has has a metal tube protruding from the wall above it and a hole at it's base
    which seems like it would hurt the basin's ability to hold any water for long.

    I approach with curiosity and just as I'm leaning in to get a closer look at the aparatus
    it springs to life with water running out the tube into the basin and down the hole.

    I can't help but release a yelp in surprise and rush out the room the way I came in.
    """

    scene bg dorm hallway morning
    with pushleft

    "
    I'm crouching in the hall, peeking back into the room, fearing that I've triggered some
    magical alarm system, when I notice I'm no longer alone.
    "

    show expression tg.image

    $ tg.meet()

    tg.says "Are you ok there? {i}*snicker*{/i}"

    "She seems to be trying, not very successfully, to stifle laughter after catching me...
    well I'm not sure what I've done wrong yet but I'd prefer to not get in trouble for it."

    menu:
        "What do I do?"

        "Play it cool.":
            mc.says "Ok? Me? I'm great. Why wouldn't I be ok?"

            tg.says "Pardon me, you just seemed a bit alarmed, is all."

        "Come up with an excuse":
            mc.says "Oh, I'm fine, yep. I was just, uh, making sure no one snuck in there."

            tg.says "Snuck in? I imagine anyone on campus is welcome to use the facilities."

    "Her smile fades and she looks a little puzzled before asking,"

    tg.says "Have you never used a washroom before?"

    "A washroom? So this room is for washing things, probably powered by some magic?"

    "Swallowing my pride as it doesn't seem like maintaining a bluff will get me anywhere,"

    mc.says "Honestly, no, I've never heard of one before now."

    "A look of shock quickly passes over her face before being replaced by a twinkle of excitement in her eyes."

    tg.says "That's surprsing; they're such marvelous conveniences!"

    "She grabs my arm and pulls me back into the room and shows me how getting near the basin
    causes the device above it to start emitting a fountain of water."

    tg.says """The basis is a fairly standard water artifice hidden behind the wall with some clever
    engineering to funnel the watter the right way without causing a mess. The real genius, however,
    is how newer installations use adjoining artifice to react to your presence to begin dispensing
    when you approach.

    I thought you might have never used an automatic one before, which was alarming the first time
    I tried one as a child... but to think you've never used a washroom before.

    I know the technology's only a few decades old, but I've grown up with them my whole life
    so it's such hardship when I have do without while traveling.

    What house are you from that doesn't have washrooms in their estate?
    """

    "What house? My confusion seems to show as she interjects:"

    $ tg.introduce()

    tg.says "Oh where are my manners? I'm [tg.first_name], of house [tg.family_name]."

    "It finally clicks. She's nobility. I have no idea what the etiquette is around introductions
    but she doesn't look like she'll take any transgression personally."

    mc.says "I'm [mc.name()] of Alderwood. I'm afraid I don't belong to any of the noble houses."

    tg.says "Oh, wow. I'm sorry for jumping to conclusions. Are you employed by the academy?"

    mc.says "I'm actually a student, or will be once the term start."

    tg.says "Really? I didn't realize the school admitted commoners. Well I've made a fool of myself."

    mc.says "True, the only way you could look more foolish is if I had caught you panicking over
    being caught tresspassing by an automatic washbasin,"

    "I reply with a grin and we both laugh off the awkward circumstances of our meeting."

    "I was apprehensive about how to interact with other students here, but I'm totally disarmed by
    how friendly [tg.name()] has been."

    tg.says "Ok, in that case, I {i}have{/i} to show you the toilets.
    This is going to change your life."

    """
    She drags me back into the washroom to show me several other wonders and we spend
    a while together, her excitedly describing the workings of the artifice mechanisms involved,
    and me mostly just trying to keep up.

    Apparently the school also has indoor bath houses, though they're in detached buildings
    due to the complexity of drawing and draining that much water.

    By the time we're through, the sun has fully risen and there's plenty of motion around the hall
    as students prepare for the day.
    """

    tg.says "Shoot, I need to get ready if I'm going to be in time for the opening ceremony.
    It was a pleasure meeting you, [mc.name()]."

label .helping_wind_girl:
    "She looks troubled but relents, stepping aside to let me in."

    "Getting a clear look for the first time, the room isn't in that bad of a shape.
    A few things are strewn about but the only real trouble are the shards of glass."

    mc.says "I'm [mc.name()], by the way. I'm an incoming first-year."

    $ wg.introduce()

    wg.says "[wg.name()]. I'm also a first-year."

    "Finding the trash bin, I start carefully collecting the glass as I find it and disposing of it."

    "The silence grows awkward and I can't hold my curiosity back any longer."

    mc.says "So what happened in here?"

    wg.says "I messed up, OK?"

    mc.says "You did this? How?"

    wg.says """I was just... breathing.
    I do breathing exercises in the morning.

    It's just me and my breath. Flowing into my lungs, then back out again.

    It helps me... work through my anxieties, center myself.

    And sometimes, it feels like the wind joins me. Usually it's empowering. But today...

    I'm just not used to spending a lot of time inside. It's so stiffling.

    I don't really know what I did, and the next thing I knew the window and door had both burst open.
    """

    mc.says "Wow, that's incredible."

    wg.says "Sure, incredible. I've trashed my room and damaged school property and it's not even the
    first day of classes yet."

    mc.says "Yeah, but you can control the wind! You did something effortlessly
    that I wouldn't even know where to begin with."

    "She doesn't respond immediately, considering her words."

    wg.says "I don't really think about it. Not usually, at least. But then things like this can happen."

    mc.says "Well I guess that's why we're here. I definitely hope I can learn to do anything as cool as this."

    "She cracks a smile, for the first time since we've met, and seems to eye me up and down."

    wg.says "I doubt it. You don't look all that impressive."

    "We laugh at her joke and I feel some of the anxieties of being alone in an unfamiliar city melt.
    [wg.name()] also looks like she's been able to relax a little too."

    "We spend the rest of the morning cleaning up her room in relative silence but in brighter spirits."

    return


label .administrators_discussing_special_cases:
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

    "Admin2" "They were the child involved in the Karnsley incident."

    "Admin1" "Oh. I see. Then that is curious. And they haven't demonstrated any innate...
    talents? Tendencies? Anything that would shed some light on the matter?"

    "Admin2" "As I said, unremarkable. Which is not to say they are an idiot.
    Just they scored in 52% percentile in the qualifying exam."

    "Admin1" "How disappointing. But still, some mysteries run deeper than others.
    And this one especially has the potential to change everything."

    return

default entrance_exam_chosen_element = None
default entrance_exam_element_set = set()

label .exam_element_choice:
    menu:
        set entrance_exam_element_set

        "Which element will I choose?"

        "Water":
            $ entrance_exam_chosen_element = 'water'
        "Wind":
            $ entrance_exam_chosen_element = 'wind'
        "Fire":
            "Fire? No. Not fire. I pick another."
            jump .exam_element_choice
        "Life":
            $ entrance_exam_chosen_element = 'life'
        "Light":
            $ entrance_exam_chosen_element = 'light'
        "Kinesis":
            $ entrance_exam_chosen_element = 'kinesis'

    return

label .unused_practical_exam_scene:

    "There are 6 of us lined up on the grass. We're not that far from the next group over
    being proctored by another professor."

    "Proctor" "
    Alright, listen up. I'll first go through and make sure you each even know what
    channeling is. Take a moment to attune to your element of choice.
    "

    call .exam_element_choice

    """
    I attune myself to [entrance_exam_chosen_element] and await the instructors instructions.

    I'm a little surprised I'm totally calm.

    Rushing into a burning building, channeling the only thing between you and death, has a
    way of really making regular old channeling a lot less stressful.
    """

    "Proctor" "Good, now, one at a time, I need you to each channel any simple spell you can, then
    release your element. Starting from you at the far end, go."

    """
    One by one we each make a simple demonstration of our ability.

    The first student must have attuned to wind as a gust picks up too suddenly and too strongly
    to be natural. It carries with it the sent of smoke.

    After the proctor gives their assent, the wind stops.

    The second student seems to falter for a second, and I can't see the effect they're supposed
    to be creating at first, but then notice a faint glow just in front of their nose, casting their
    face slightly brighter than before. It's a clear day and the sun is bright so it's hard to tell.

    The proctor doesn't seem to be concerned and grunts for the student to stop.

    I'm fifth in line and the student just before me attunes to fire.

    I state transfixes at the small flame they create in their cupped hands, sheltering it from the
    wind.

    I don't hear what the instructor says and can't look away from the dancing flame. Even when the
    student dismisses it, I still see the afterimage. I can feel the intensity of the heat.
    I can hear the cracking of wood collapsing onto the inferno.
    """

    "Proctor" "Hey! You! I can tell you're attuning [entrance_exam_chosen_element], don't you
    know how to channel it?"

    "I snap back to reality. I can't slip up now."

    # TODO: write element-specific effect descriptions. Kill any choices I can't write a spell description for
    if entrance_exam_chosen_element == 'water':
        "I channel some water."
    elif entrance_exam_chosen_element == 'wind':
        "I channel some wind."
    elif entrance_exam_chosen_element == 'light':
        "I channel some light."
    elif entrance_exam_chosen_element == 'life':
        "I channel some life."
    elif entrance_exam_chosen_element == 'kinesis':
        "I channel some kinesis."

    "The proctor seems satisfied and I try to shake off the feeling from before."

    "Proctor" """
    Good. You all can at least can channel something. Next I'll be testing your endurance.

    One by one I'll be calling on you again to channel your chosen spells. This time, however,
    I need you to maintain the effect for as long as you can. I'll be timing you.

    You'll need to last at least 20 seconds to get a passing mark.
    If you can somehow reach 5 minutes I'll call you there, don't need you passing out on me.

    Don't attune early as you'll just tire yourself out. I'll give you a moment to reattune when
    I get to you.

    Again starting from the far end, go.
    """

    """
    Once more we each attune and sustain our channeling while the proctor times us and notes
    our times on their board.

    Each of us just repeats what we had done before just holding the effect for longer.

    I don't risk looking at the 4th student's flames this time, instead counting the seconds
    before they had to stop. I'm not sure if my count was fast, but they seemed to last nearly
    a minute.

    I repeat my performance again as well, and try to maintain the effect as long as I can.

    I feel the time passing but I can't really tell how long it's been.
    I'm honestly not even that tired when I finally hear the proctor call out.
    """

    "Proctor" "That's enough, that's 300 seconds. Next!"

    "300 seconds? I made it the full 5 minutes then. I let myself be a little impressed at
    my own performance."

    "Proctor" """
    Alright that will conclude the basic practical examination.

    As will already have been explained to you, we'll be going through a few scenario exercises
    as well. Feel free to sit this out if you don't think you can keep channeling from here.

    This time you'll all be channeling at once. Make sure you release all spiritual elements,
    don't attune to anything until I finish giving you the scenario and tell you to go.

    Then you'll all as quickly as you can respond by attuning to whatever element you'd like
    and channeling any spell you feel would be an appropriate response to that scenario.

    I'll be grading you on your reaction time and the hypothetical efficacy of your responses.

    Now we'd better hop to it, most other exam groups have already finished because you lot decided
    to show off during the endurance portion.
    """

    #TODO: 1. put this in the UI
    # 2. make each scenaio a multiple (maybe just 2 option) choice of response
    # 3. implement scoring based on the skill level and choice combiations
    # 4. (we could make this timed?? I mean it could work. But doesn't seem worth it.)

    "Proctor" "Scenario 1: "

    "I do the magic."

    "I wasn't very tired before but I'm starting to feel it catch up to me now."

    "Proctor" "Scenario 2: "

    "I do the magic."

    "Proctor" "Alright now, last one. Scenario 3: You're walking through the woods alone at night when
    all of a sudden, Shia Le Bouf!"

    "I do the magic."

    return
