



#####

##################################################################################

label unscheduled_morning_encounter(callback):
    play sound "effects/explosion.wav"

    "The next morning, I wake to the sound of an explosion."

    show bg dorm hallway morning with dissolve

    "I rush out into the hall, still dressed in my traveling clothes from last night."

    show expression wg.image

    wg.says "Shit!"

    $ wg.meet()

    "I find another student standing in a door frame, the door itself dangling on a single hinge."

    mc.says "What happened? Are you alright?"

    wg.says "Yeah, it's... none of your business. You better not tell anyone about this, OK?"

    "By this point I've made my way in front of the room with the broken door and I'm
    trying to peek around her to get a better look inside the room."

    mc.says "Sure, but do you need any help?"

    "I don't see any flames or major signs of destruction,
    but a lot of things are strewn across the floor along with a some shattered glass."

    wg.says "It's fine, I don't need help."

    menu:
        "What do I do?"

        "Leave her alone.":
            "She really didn't look like she wanted anyone bothering her."

            mc.says "Ok, well I'll see you around I guess."

            "I leave her looking troubled but a little releived and head out onto campus."

            call .exploring_campus_morning1

        "Insist on helping.":
            "She doesn't look like she really wants anyone bothering her, but
            I'm driven more by curiosity at this point than anything else."

            mc.says "Look, just let me help you, it'll be faster with two people."

            call .helping_wind_girl

    $ callback()

label .exploring_campus_morning1:
    ""


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
