
label day6(callback):
    scene bg dorm room morning with dissolve

    """
    I'm so worked up I'm awake before the sun's fully risen.

    Today's the day.

    Today I take the exam that decides my future at this academy. Or more accurately, whether
    I have any future at all here.

    I... don't know what I would do if I went home now. I don't really have any other prospects.
    My life was pretty aimless before. I know mom will be disappointed.

    I don't know if I'm ready, given how behind I was at the start of the week I'm honestly
    pretty worried.

    I've learned a lot and I'm sure I can demonstrate that. I just have to hope that that's
    enough.

    But the anxiety of it all is still getting to me. No matter how much I pep myself up I can't
    shake this sinking feeling in my gut.

    The exam won't start for a little while but longer I'm too antsy to stay in my room.
    """

    scene bg school courtyard morning with dissolve

    """
    I step out into the courtyard and the smell hits me first.

    Smoke.

    Off in the distance towards town, I can see a faint plume of gray.
    I have a terrible feeling about this.

    There's no way for a fire to make it all the way up to the campus, but something
    is bothering me.

    The smoke, it's coming from the northeastern corner. I think back to my experiences
    exploring the town.

    There's a residential area there and... the shrine?

    My memories of my dreams come to me. The shrine caught fire? But that was just a dream.

    I need to go check, but the exam will begin soon, there's no time.
    """

    call .exam_or_save

    $ callback()

default exam_save_menuset = set()

label .exam_or_save:

    menu:
        set exam_save_menuset

        "What should I do?"

        "Go to the exam, I don't have time to make it all they way to town.":
            """That's right. I have been preparing for this exam all week. If I went into town now
            I'd surely miss it and risk my attendance here.

            I start to head to the hall where the exam will be held but I hesitate.

            I can't do it. I need to know.
            """
            #TODO: maybe replace this with a real bad end.
            jump .exam_or_save

        "Check the shrine in town, I need to make sure it's OK.":
            """
            I can't shake this feeling that I need to go, I need to be there.

            But I can't risk missing the exam. And so what if the shrine burns? No one even uses it.

            Except... the Shrinekeeper. In my dream she was still in there.

            It doesn't make any sense, even if there was a fire, and even if it happened to be at
            that old temple, she would have made it out by now. Dreams aren't real.

            I turn to head to the hall where the exam will be held.

            "Save them."

            I can't do it. If there's any chance they're in danger, I have to go.
            """

    call .race
    return

label .race:
    scene bg town street afternoon with dissolve

    """
    I sprint into town, rehersing the route to the temple in my head.

    I'm ready to feel like an idiot. There's probably no fire at all, some idiot just had a
    tragic grilling blunder and the shrine will be there just as before: an island kept afloat
    by a sole keeper in a sea of that rundown temple.

    Even if there is a fire, what are the odds it's made its way to the temple?

    Anything to keep my mind off of the fact that by running this far into town already, I have
    no hope of making it back in time for the start of the exam.
    """

    scene bg shrine evening with dissolve

    """
    By the time I get to the temple, it's too late. The whole thing is ablaze, the western
    wing is already collapsed and smouldering.

    I just have to hope the Shrinekeeper made it out OK. She must have, right?

    Besides I'm powerless, here. There's nothing I could do even if I wanted to.
    """

    """
    I feel it again. The thrumming.

    I'm not powerless. I've been working my ass off all week.

    Forget the exam. Here and now. This is my test.
    """

    menu:
        "Without consciously meaning to I've already attuned myself to"

        "Water":
            """
            Water, what else?

            I recall the feeling of jumping in the fountain. Being soaked all the way through.
            Water dripping from my clothes, down my hair, covering my whole body, and I will the
            spirits, please.

            And thank them, they respond.

            In a rush I'm drenched, water falls to the ground around me and push on.
            """
            call .rescue('water')

        "Kinesis":
            "
            Kinesis. I don't know where I'll find the Shrinekeeper but the temple is falling
            apart and I can't get close enough to the burning structures to move them myself so
            I'll need to rely on the spirits for help.
            "
            call .rescue('kinesis')

    return

label .rescue(element):
    """
        I rush through the threshold of the temple gate, the flames haven't quite reached it yet but
        I can feel the heat from here.
    """
    if element == 'water':
        "The water rapidly evaporating off of me keeps me from feeling the brundt of
        the heat."
    else:
        "The heat and smoke is so intense, I begin to cough."
        $ state.status.change_health(-20)

    """
    Where is she? I think back to my dream. The east wing, her room was there.

    I don't have time to find the entrance to the building proper; for all I know it's already
    collapsed or engulfed by flames.

    But I remember the window. I rush along the outside of the building to where I saw the
    light in my dreams.

    There!
    """

    if element == 'kinesis':
        """
        I recall the feeling of setting [wg.name()]'s window into place.
        The heft of the pane against the frame, the joints where it snapped into place.

        I don't doubt the window's construction in this temple differs wildly from those back
        in our dorm room, but surely the spirits can cut me some slack on this?

        And thank them, they respond.

        I watch as the window flexes, and shatters, and a rush of hot air rushes out.
        """
    else:
        """
        I approach the window. It's hot to the touch and I don't see a handle. I don't think
        I can't get it open from the outside.

        But I don't have any time, I wrap my hand in my sleeve and ram my fist into the
        glass pane.

        It shatters and several shard scratch my arm, but I can barely feel it.
        """
        $ state.status.change_health(-20)

    """
    The room is thankfully not itself burning, but it's filled with smoke.

    I leap through, covering my mouth and face with my shirt, looking frantically around.
    I don't see the shrinekeeper anyway, but notice the door is open.

    I rush out into the hall and see her. The old woman looks so frail lying in the hall,
    I can't tell if she's breathing.

    I lift her in my arms and carry her back to the window.

    I have to push out the remaining sharp edges of the shattered glass before I can
    push her out the window and follow after.

    I rush to carry her away from the burning remains of the temple and towards fresh air.

    ...

    I make it our of the temple entrance and onto the street which by now is filled with onlookers.

    I put the Shrinekeeper onto the ground, my strength finally failing me, and inspect her.

    The wasn't burned but... I don't think she's breathing either.
    """

    mc.says "Help! Can anyone help her?"

    """
    An older gentleman pushes through the crowd and comes up to us.
    """

    "Old man" "Give her here"

    "He nudges me out of the way as he lays his hands on her chest and throat."

    "Old man" "She'll have inhaled too much smoke in there. Her throat and lungs will have suffered
    serious injuries."

    mc.says "Do something!"

    "Old man" "I am."

    """
    I finally notice the telltale glow of channeling from him and shortly afterwords
    the Shrinekeeper jerks to her side and begins a fit of coughing.
    """

    "Old healer" "I've done about as much as I can. Healing scalds and superficial burns is a
    far cry from healing internal ones, but I've done what I could. It's up to the spirits now."

    return

label day6_afternoon(callback):

    scene bg dorm hallway morning with dissolve

    """
    Everything after that was a blur.

    There was no saving the temple after that but people worked together to ensure that the fire
    was largely contained. There should be no risk to the rest of the district.

    Some older residents from nearby took in the Shrinekeepr assuring me they'd take care of her
    while she recovered.

    I guess even though the temple was largely neglected there were some people who still cared
    about her. I'm glad.

    Some people wanted to ask me questions, others were praising my heroism.
    But I don't feel heroic, just dead tired.
    """

    scene bg dorm room morning with dissolve

    """
    I don't quite remember how I made it back to my room.
    The last vestiges of adrenaline keeping me going are long gone and I just feel empty.

    I collapse in my bed and try to make sense of what's happened.

    The dreams I've been having, they were real, weren't they? How?

    And the exam... well, I missed it. I don't even feel bad about it; it all feels so small now.

    I'm just glad I was able to act in time.

    It's still midday but I'm just so tired that I'm ready to sleep again.
    """

    show bg black with dissolve

    "
    Funny, the thrumming that's visited me each night has been my constant companion, but I can't
    hear it now. I almost miss it.
    "

    $ callback()

label day6_night(callback):
    """
    ...

    I stir slightly, my senses returning to me.
    """

    mc.says "I must have slept straight through to evening."

    ts.says "It's been precisely 3 hours, 23 minutes and 19 seconds."

    scene bg dorm room night

    "I sit up in bed."

    mc.says "Is someone there?"

    ts.says "I've been here for some time now but I didn't wake you as it appeared that
    you needed rest."

    show expression ts.image

    $ ts.meet()

    """
    I look around to find someone... floating(?) in the middle of my room.
    """

    ts.says "Would you like to know how long I've been here?"

    mc.says "Who are you?"

    ts.says """
    Ah, I suppose we've not been introduced yet from your perspective.

    I'm... what humans might call a 'Time Spirit'.
    """

    $ ts.introduce()

    mc.says "A what? Wait you're a spirit??"

    "So spirits are real? And she's a spirit of time? Is that even possible?"

    ts.says "Yes. You should ask your questions so that I may answer them."

    mc.says "I don't even know where to begin. How is this possible? What are you doing here?"

    ts.says """
    'This' is possible because you've attuned to me, and I to you, in a sense.
    To put it lightly, it's not usual, what we've done.

    As for my purpose now, well, that's a more delicate subject. One that you're not ready to hear
    fully. But the most pertinant aspect of my purpose now is to offer you my assistance.
    """

    "Of all the impossible things that have happened to me this week, this one really takes the cake."

    mc.says "Ok... thank you, I guess? I don't know what help you're offering,
    or what help you think I need, but I have about a million more questions if that's alright."

    ts.says """
    Questions that I'm sure you'll find the answers to soon, but not right now.

    You've had a long day but it's not through yet.
    There's some important business left unfinished.

    I'll meet you again at the same time, right outside your door.
    But until then, you've got an exam to take.
    """

    python:
        state.change_time(6, TOD.MORNING) # here we go again
        callback()

label day6_morning_take2(callback):

    scene bg black with dissolve

    """
    It begins in my ears like usual, the thrumming loud and angry.
    But it continues now, not just in my head, but my whole body vibrates urgently.

    The feeling crashes into me so suddenly my vision swims and I worry I might vomit.
    I'm glad I'm sitting in my bed as I feel I might collapse again.

    But then it subsides, as quickly as it comes, and my senses start to recover.

    I need to take a few moments to catch my breath. I'm thankful I didn't manage to
    eat anything today as I don't think I'd be able to keep it down.

    The spirit must have done something to me, but if that was their idea of helping they
    must have a warped sense of what humans find helpful. I'm definitely not feeling any better.
    """

    # maybe use a more dramatic effect due to the time travel
    scene bg dorm room morning with dissolve

    """
    I look around the room, still sitting in my bed and it takes me a moment to realize that
    it's not evening anymore.

    Outside the window the sun has just risen. Did I somehow pass out all night without
    realizing?

    I suppose so. Then it's time to face the reality of the situation. Though I
    may have helped save the Shrinekeeper I missed the qualification exam and so my admission
    at the academy will be rescinded.

    I start to gather my things to pack and then think better of it. I'll need time to make
    arrangements to travel home. I wonder if I can petition the school to let me use this
    room while I wait?
    """

    scene bg school courtyard morning with dissolve

    scene bg school admin morning with dissolve

    "I make my way to the administration office and manage to find a familiar face
    who greets me with a smile."

    "Administrator" "Good morning, prospect. I do hope you're ready?"

    """Ready? To leave? I suppose it's obvious they will have noted my absense and have just assumed
    I chickened out. So they've already begun the expulsion process.

    I hope they'll still be receptive to my request.
    """

    mc.says "Good morning, administrator. I'm afraid that's what I've come to talk to you about.
    I don't believe I'm quite ready yet."

    "The administrators smile quickly turns into a frown."

    "Administrator" "Not ready? Well that won't do. We cannot and will not make exceptions."

    mc.says "I understand, I was just hoping you could accomodate me a few more nights while I
    make arrangements."

    "Administrator" """
    A few more nights? Arrangements? I don't know what's gotten into you but we'll do no such thing.

    I'm shocked, to be quite honest. Your fundamentals professor spoke highly of your efforts. He
    said you'd made respectable progress given your limited background.

    I don't know if you've just gotten cold feet or we've just been a bit too successful in
    scaring you kids into taking this exam seriously, but you're going to march out into the exam
    hall and steel yourself to give it your all.
    """

    "The administrator ushers me out the door of the building."

    scene bg school courtyard morning with dissolve

    "Administrator" "We've taken a keen interest in you,  you know.
    You better shape up and act with a little more confidence."

    """As usual they don't give me a chance to get a word in, but it's just as well given I have
    no idea what to say.

    Did I make a mistake? Was the exam not yesterday? No, I'm sure it was, but...

    What had the time spirit told me? They said I had an exam to take. That didn't make sense to
    me before, I thought they were speaking metaphorically.

    But no, this is what they meant by helping me. They somehow sent me back in time.
    """

    scene bg lecture hall morning with dissolve

    """
    I make my way to the exam hall. Though I'm still a little early, students are already trickling in.

    After everything I've been through, it seems silly to be nervous about this now.

    The time spiri gave me another chance. All that's left is to focus and not let it go to waste.
    """

    call .exam_intro

    # "No, don't disturb them. The student in there has had a hard day and needs their rest."
    # ...
    # "I'm sorry, what should I call you? Lady Time Spirit?"
    # "You shall call me..."
    # She gets a distant look as an exagerated smile creeps onto her face
    # "Needle."

    $ callback()

label .exam_intro:
    scene bg black with dissolve

    scene bg lecture hall morning with dissolve

    show expression ti.image

    ti.says """
    Welcome prospects, after today I hope to welcome many of you as full students of
    the Academy. But first we'll see if you have what it takes.

    The exam will be conducted in two phases. You'll find this is the norm for the rest
    of your time here at Qyburn.

    First, the written portion will be conducted in this room. It will mostly cover what
    we've discussed in the lectures in class, however some additional material from the
    assigned reading may also appear for the overachievers among you who'd like to prove
    your knowledge of the material.

    Second, there will of course be a practical portion. You will be broken up into groups
    and each group assigned to a professor at the academy to proctor your exam.

    Your proctor will ask you to demonstrate your ability to channel basic elemental spells.
    They may also present scenarios which you must respond to by channeling an appropriate
    spell, however agin this is an opportunity for those of you who've developed your skills
    further to prove that.

    The bar to pass and earn status as a full student is only high enough that we can be
    confident you have the potential to succeed here. We do not demand perfection.

    However your performance on this exam will determine your class placements as well as determine
    your initial ranking amongs your peers. You will find that your ranking may earn you
    other priveleges during your time here.

    And now I tire of the sound of my own voice so as I hand out the written exams I will
    leave you with these final words:

    Potentia utendem est.
    """

    call .written_exam

    return

label .written_exam:

    # TODO: show exam UI?

    hide expression ti.image

    "I take the writen exam. A UI window should appear now to summarize my progress."

    # """
    # I open the exam booklet and turn to the first page.

    # "Name the six spiritual elements and give an example of a valid spell that one
    # could channel by attuning that element."

    # I know this. In fact, as I flip through the pages, I know each of these.
    # """

    # # TODO: do skill checks to see if you get bonus points.

    # """
    # It isn't until I get to the final two questions that I'm stumped.

    # Something about Snell's Law of light refraction and it's application in casting light across
    # disprate media... the question goes well over my head.

    # But despite that, I feel good about this. I feel like I answered enough questions on the
    # written portion to clear the bar for passing the exam.

    # I make a feeble guess at the last two questions, because hey why not, and turn in my completed
    # booklet.
    # """

    show expression ti.image

    ti.says "And that concludes the written portion of the exam."

    "The fundamentals instructor reenters the room with a entourage of a dozen other
    professors in tow."

    ti.says "We will now assign you to groups proctored by my colleagues here.
    Please report to your proctor and follow them outside as your name is called."

    # """
    # The proctors go through the roster of examinees one by one and file out of the hall.

    # A handful of names receive no response, I guess there were some genuine no shows after all.

    # I can't help but wonder if that's what happened earlier when I was in town and not here.
    # Except, wait, I'm currently also in town, so I was always here taking the exam all along?
    # It hurts my head to think about - I'll have to ask the Time Spirit when I next get the chance.

    # Finally my name is called and I go to join my proctor on the field where we'll take our
    # practical exam.
    # """

    call .practical_exam

    return

label .practical_exam:

    "I take the practical exam. A UI window should appear now to present the spellcasting
    challanges."

    call .after_exam

    return

label .after_exam:

    scene bg lecture hall morning with dissolve

    ti.says """
    And that concludes the qualification exam.

    You should each already have your results and know whether you've passed or failed the exam.
    The rankings will be posted tomorrow on my door.

    It's been a plessure teaching you all, now go out there and enjoy a well deserved rest of your
    day off.
    """

    # Show interface of ranking you against your peers.


    # "After the exam, I'm tired and I come back to my room."

    # "Oh hey, it's time spirit. Hi time spirit!"

    # ts.says "Hey."

    # "The end."

    return


label day6_afternoon_take2(callback):

    scene bg dorm hallway morning with dissolve

    """
    I make it back to the dorm and I feel like I'm walking on air.

    I did it.

    I'm a full student at the academy now.

    Not only that but... well, I guess I've met a time spirit and saved the shrinekeeper from the
    burning temple, so all in all it's been a pretty successful day.

    Wait.
    """

    ms.says "The Shrinekeeper!"

    """
    As the realization dawns on me, my mood darkens.

    The fire at the temple. If I went to take the exam then no one went to the temple to save her.

    I'm almost back to my room now and think to turn back but what could I possibly do now?

    I have to at least go check.
    """

    show expression ts.image

    ts.says "You needn't worry about the shrine keepr. They were saved them this morning while you
    took the exam."

    """
    I see the time spirit floating in front of my room as I approach and her words lift the mood
    again.
    """

    mc.says "Really? I'm glad. I'm honestly still pretty turned around by all this."

    """
    I reach for the handle to my door when the spirit stops me.
    """

    ts.says "You shouldn't go in there. Not yet, at least. There's a hero taking a well deserved
    rest inside."

    mc.says "What do you mean? Who would be in my room... no."

    "This can't be possible."

    mc.says "Am I inside there right now?"

    ts.says """
    You were inside, yes, as of 1 hour 43 minutes 8 seconds ago.
    You then left to return to this morning in another 57 minutes and 11 seconds.

    It would be a both rude and catastrophic if you were to disturb your own slumber.
    So let's take our conversation outside; I understand you have more questions for me.
    """

    """
    I can't make sense of this right now but I obediently follow the spirit as she floats to
    the front of the dorm.
    """

    call .talk_with_timespirit

    $ callback()

label .talk_with_timespirit:

    scene bg school courtyard morning with dissolve

    """
    As we step (float?) outside I lose track of the spirit. My frayed mind isn't tolerant of
    another surprise today and I start to look around in a panic.

    I'm more than ready to accept the explanation that many of the impossible happenings were
    the delusions of an overly taxed mind, when I hear her voice.
    """

    ts.says "Don't worry I'm still with you, just... less than before. In the interest of
    diescretion."

    mc.says "Discetion? What do you mean?"

    ts.says "It wouldn't be wise for me to be seen by others."

    mc.says "So anyone could see you? I worried you were in my head."

    ts.says """
    I'm certainly not in your head. And yes, if I am projecting myself so strongly,
    then at times, perhaps others could see me. In glimpses.

    No other human will have attuned to me so they won't see me as you do, but it's still best
    if I stay concealed when we aren't alone.
    """

    """
    I look around and there are many other students mingling in the courtyard, celebrating the
    end of the first hard week of school.

    We walk around for a bit longer in silence, I don't want to be heard talking to myeslf,
    and I need some time to collect my thoughts.

    So I have a spirit following me around, a time spirit at that. I didn't know that time
    spirits existed. I guess I didn't really know any spirits even existed.

    And she turned back time. Or sent me back in time. Why? How? My million questions start
    to rush back to me and I don't know where to begin.

    I guess I should start with the question that is eating at me the most right now.
    """

    mc.says "Why me?"

    "She doesn't respond for several seconds, and I wonder if she left. I'd have no way of knowing."

    ts.says "I saw you at the srine. You paid respects that humans don't often do anymore."

    mc.says "So... because I was devout? I'm sorry but I didn't really believe in spirits until
    I met you. Not fully."

    ts.says """No, human devotion to causes and religion is for self satisfaction. It's of no interst
    to the spirits.

    No I saw you and you were... receptive to me, even if you didn't mean to be.
    I could reach out to you and I needed your help.
    """

    "They needed my help?"

    mc.says "With the temple today, you wanted me to save it?"

    ts.says "No, you could not save the temple. But you could save its resident."

    "I try to process this. The time spirit met me when I visited the temple
    for the first time the day after I arrived."

    mc.says "That's when I started having those dreams."

    ts.says "Human cognition is... malleable when dreaming. I granted you prescience so that you
    might see what I did. Of what would happen today."

    mc.says "Why? Why did you need me to save the shrine keeper?"

    ts.says "I've observed the keeper of that shrine for many years. I've developed... a fondness
    for her. And as I've already said, you were receptive to me. If I could have warned her directly
    I would have."

    """
    I guess that makes sense. She needed someone to prevent the worst of the disaster today and
    I was all she could find.
    """

    mc.says "So then... you came to find me after the fire to repay me? That's why you sent me
    back in time?"

    ts.says "In a manner of speaking... But, it will be important that you are enrolled at the
    academy in the days to come.
    I shifted your path to allow you to accomplish everything you needed."

    "I wait for her to elaborate but when she doesn't I feel the weight of the silence. There
    are things the spirit isn't willing to tell me about what she wants from me."

    mc.says "Then, after you sent me back, there were two me weren't there? There still are?"

    ts.says """A spirit's perception of time is very different from a human's, a time spirit's
    especially.

    From my perspective there is but one of you, but your path through time is... more complicated
    than many others. Much of that is due to my influence.

    So you may find that if you visit your room in the next 3 minutes and 39 seonds, you
    will perceive yourself from a different angle than usual. It's not something humans are
    well equipped to handle so I'd discourage you trying.
    """

    "In my random walk around campus I've found myself back in front of the dormitory."

    mc.says "Was I always here? If I woke up early and stepped outside, would I find myself
    standing here? Or am I only here now and... not before?"

    """My head hurts trying to organize the logic of the situation and I feel foolish trying
    to express concepts beyond my understanding in words.

    It doesn't help that in response I hear the spirit laugh at me."""

    ts.says """Hahahaha, oh I've missed conversing with humans. Hypotheticals are concept
    I struggled to grasp for ages. They still amuse me.

    For all intents and purposes, yes, you were always standing outside these doors
    while inside you slept.
    """

    ts.says "You're about to wake up now so I have to leave to greet you. Wait no less than 10
    minutes before returning to your room."

    "And with that I'm alone again."

    return

label day6_night_take2(callback):

    scene bg black with dissolve

    "I decide to continue my stroll around campus to clear my thoughts before returning to my
    dorm room."

    "When I make it back I hesitantly open the door, not sure what I'd do if I encountered myself."

    scene bg dorm room night with dissolve

    show expression ts.image

    ts.says "Welcome back. I only just shifted you 4 minutes ago."

    "She looks a little too comfortable in here, absently inspecting the posessions on my desk."

    mc.says "Thanks. So... what now?"

    ts.says "Excellent question. Now you ought to rest, there will be time for more questions
    later."

    mc.says "That's the thing, though. How much later? What are you still doing here if I've
    managed to rescue the shrine keeper and taken the exam?"

    ts.says """As I've just finished telling you, my purpose here is a delicate matter, but you're
    right, now that you've finished your qualifying exam, that purpose has shifted.

    Suffice to say I'll be needing your assistance again, and you'll be needing mine.
    So from now, I'll be joining you."""

    "I don't have the energy to press the absurdity of the circumstances anymore today,
    so just like that, I have my own guardian spirit."

    mc.says "In that case we should at least make introductions. I'm [mc.first_name].
    What should I call you?"

    "In response, the spirit appears pensive for a moment."

    ts.says "You will call me [ts.name()]."

    # Now play credits

    $ callback()


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


init python:
    plot_schedule.schedule_event((6, TOD.MORNING), Event("day6"))
    plot_schedule.schedule_event((6, TOD.AFTERNOON), Event("day6_afternoon"))
    plot_schedule.schedule_event((6, TOD.NIGHT), Event("day6_night", takes_time=False))
    plot_schedule.schedule_event((6, TOD.MORNING), Event("day6_morning_take2"))
    plot_schedule.schedule_event((6, TOD.AFTERNOON), Event("day6_afternoon_take2"))
