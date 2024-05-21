
##### Day 1 #####

label day1_morning(callback):

    show bg black with dissolve

    "
    I wake up the next morning just before sunrise, the still sore from travel.
    "

    show bg dorm room night with dissolve

    """
    I didn't have a chance to appreciate it last night but the bed in my room may be the
    nicest I've ever used. I slept like a rock.

    I stretch and look outside. The sky is still dark but growing red with the coming sun.
    I can't see any activity from my window and I take a moment to just appreciate the quiet.
    """

    call .windgirl_encounter

    scene bg dorm room morning with dissolve

    """
    Trying to put that out of mind, I return to my room.

    The opening ceremony will be today, but I've got a little time before it'll start,
    so I decide to tidy up a bit.

    After unpacking my two sets of clothes into a wardrobe large enough to make my collection
    feel inadequate, I turned to set up my personal effects on my desk:

    A worn dagger that used to belong to my father, and a sharpening stone to maintain it.

    A clear crystal with a streak running through it strung on a cord -
    a protective charm from a merchant who had visited our home town years ago.

    I don't wear it much anymore but it felt appropriate to bring whatever protection
    I could muster when leaving home to come here.

    Lastly I pulled out a tattered leatherbound notebook. Somewhere between a diary and a sketchbook
    I use it regularly and it's showing its age. I'll need to pick up some more parchment for it in
    town.
    """

    show bg dorm hallway morning

    """
    I pull out the last of my travel rations from my sack and munch on it as I join the
    throng of students heading their way to the auditorium.
    """

    call .opening_ceremony

    $ callback()

label .windgirl_encounter():
    play sound "effects/explosion.wav" volume 0.3

    "Which is promptly dirupted by the sound of an explosion."

    show bg dorm hallway morning with dissolve

    "I rush out into the hall, still dressed in my traveling clothes from last night."

    show expression wg.image

    wg.says "Shit!"

    $ wg.meet()

    "I find another student standing in a door frame, the door itself dangling on a single hinge."

    mc.says "What happened? Are you alright?"

    wg.says "Yeah, it's... none of your business. You better not tell anyone about this, OK?"

    "By this point I had made my way in front of the room she was guarding, trying to peek
    around her to get a better look."

    mc.says "I won't, but do you need any help?"

    "I don't see any major signs of destruction,
    but a lot of things are strewn across the floor along with some shattered glass."

    wg.says "It's fine, I don't need help."

    menu:
        "What do I do?"

        "Leave her alone.":
            "She really didn't look like she wanted anyone bothering her."

            mc.says "Ok, well I'll see you around I guess."

            "I leave her looking troubled but a little releived and head out onto campus."

        "Insist on helping.":
            $ state.flags.Set('wg_bad_intro')

            "She doesn't look like she really wants anyone bothering her, but
            I'm driven more by curiosity at this point than anything else."

            mc.says "Look, just let me help you, it'll be easier with two people."

            "I start to step around her, but she deftly moves to stand in my way."

            wg.says "I said, I don't need your help!"

            $ wg.aff_change(-3)

            """
            She gives me a shove, and at the same time a strong gust blows in through her
            open window.

            The window swings loudly and I notice that some of the panes have broken off,
            which accounts for the glass I saw in the room.
            """

            mc.says "Sorry, I'll leave you alone then."

            "I can't help but be a little alarmed, and she looks embarassed but releived to see me go.
            I guess I didn't make the best first impression."

    return


label .opening_ceremony:

    scene bg school auditorium with dissolve

    """I've taken my seat in the auditorium amongst what seem to be over a hundred other students.

    A few stragglers are still trickling in but it seems like the ceremony is getting ready to begin.
    """

    $ hm.meet()

    show expression hm.image

    """An elderly man makes his way slowly onto the central podium on stage.
    He's clearly quite frail but somehow manages to exude power at the same time.

    All the chatter dies down.
    """

    hm.says "{size=72}{cps=20}POTENTIA UTENDEM EST!{/cps}{/size}"

    "The old man roars, far louder than should be possible, and no hint of frailty
    remains in his frame."

    hm.says """These are the words of our institution. These are the words we will instill in you.
    And if you expect to survive here, these are the words you must live by.

    First, you will know who we are.

    We are not spiritual philosophers like you will find in the east.

    We are not diviners and supplicants to the spirits as you will find in the temples
    to the south.

    Who are we? We are the Magi. The practitioners of magic. We do not fear our own power for we
    understand how to use it. How to bend and reshape the world into a better one.

    Starting from this day, you too will be magi.

    Oh, aspirants of the spiritual arts, stray souls seeking to drink from the font of knowledge,
    be welcome here. But know that this knowledge you seek comes at a price.

    You will work and you will grow, for we will work you and we will grow you.
    We will mold you into the magi of tomorrow and you will be greater than anything
    that has come before.

    But as you grow in power so too will you grow in your duty to that power.
    There is no greater sin than the inaction of the powerful.

    Once your time is done here you will take what we teach you back to your homes,
    to your lands, to the far corners of the world and you will put it to use.
    """

    "And then there is a long pause. The old man appears to almost shrink he no longer
    imposes the same aura as before, but everone is still a bit shaken by that performance."

    hm.says "And with that let's call the ceremony bit of this pageant done eh? Hoh oh oh oh oh."

    $ hm.introduce()

    hm.says """
    For those who don't yet know me, I am the Headmaster at the Ardenvale Institute of Magic.

    Now for a few logistical matters. You are all the 238th class at this hallowed institution.
    Or rather you will be.

    While you're all gathered here to study at the academy, ultimately, not all of you will be
    joining as students.

    How do I mean? Well as of today you are all prospects. For one week our esteemed faculty
    will be conducting lessons in the fundamentals we expect all our students to master.

    Some of you may have arrived with prior study such that you already feel you have no need
    for such lessons. I caution that you act on your hubris at your own peril.

    At the end of the this week we will be holding a qualifying exam, and as is fitting our words,
    there will be a practical component that will demand you to apply what you learn.

    If you pass this qualifying exam, or "Quals" as your peers have taken to calling it, you will
    be inducted as full students of the academy.

    If we find you lack the aptitude necessary to succeed here, we will ask you to leave.
    """

    "My heart sinks into my stomach. There's a exam in one week? I don't know the first thing
    about magic and it seems like more than half the students here have had some private instruction
    before coming here."

    hm.says """Oh, and one last thing.

    I want to take this moment to call attention to a program we run at this institute.
    In keeping with our words, every year we partner with the esteemed guilds in the city
    to admit a handful of guild-sponsored students.

    These students will be expected to immeidately put into practice what they learn here
    at the academy by reporting to their guild patrons for duties. They will of course
    have to balance this against their other coursework.

    I for one look forward to such promising talent joining us for the schoolyear.

    And that's it! Enjoy the rest of your day off as classes begin tomorrow.
    """

    hide expression hm.image

    """
    I join the crowd emptying out of the building, trying to process what I've signed up for.

    I'm one of those students sponsored by a guild that the headmaster mentioned at the end of
    his address. That part doesn't surprise me, I knew roughly what the deal was.

    I've always been interested in magic and the spirits, I feel like I can see them from time
    to time, like after a rainfall or being carried by a particularly powerful squall.

    But I've never had any particular talent for it. I've never managed to cast any spells, I
    wouldn't know where to begin.

    The only reason I'm here is that a friend of my mother had apparently made arrangements
    for me to attend this school through the Adventurer's guild.

    I knew it was prestigious but I figured I had already been admitted so the hard part was over.
    """

    "I make it as far as the stairs in front of the building, lost in my self-pity, before a staff
    member stops me to hand me a note. Apparently I'm to report to the Adventurer's guild today for
    orientation."

    return

label day1_afternoon(callback):
    call .adventurers_guild_intro

    $ callback()

label .adventurers_guild_intro:

    scene bg guild hall with dissolve

    "It doesn't take me too long to find the guild. Most of the guild halls in
    town seem to be situated on the same street and this one is pretty prominent."

    show expression gr.image

    gr.says "Welcome to the Adventurer's guild! Have you come to petition the guild with a request?"

    mc.says "Hi. No I don't think so, I'm a student up at the academy and was told to report here."

    gr.says "A student? I'm afraid I don't know \u2014"

    gr.says "Oh, that's right! Let me go fetch the guildmaster."

    """The receptionist leaves and I take a look around. It's early afternoon and the hall is mostly
    empty. I guess people don't linger for too long after they've finished their business here.

    The Adventurer's guild is a pretty well regarded institution, we even had a small
    branch back home.

    I've thought more than a few times about joining up with them as it always felt like an easy
    solution to the otherwise directionless life I've lead. But my mom wouldn't hear it.

    Come to think of it I'm surprised she was convinced to let me come to this school on a
    guild sponsorship at all.
    """

    hide expression gr.image

    show expression gm.image

    gm.says "Ah here you are. Damien's kid, right? I knew your father back in the day."

    """
    I'm shocked to hear this. My dad died when I was pretty young and I honeslty don't know much
    about him.

    I remember him telling me stories of his adventures before bed that would fill my sleep with
    dreams of gallantry and heroism.

    But after he died, no one would ever tell me how it happened. My mother wouldn't tolerate
    talk of him. All I know is that he had been on a particularly dangerous contract for the guild
    and didn't make it back.
    """

    gm.says """
    You probably already have a decent idea of how the guild works but your situation is a bit special
    so let's just start from the beginning and clear up any misconceptions you might be carrying.

    First of all you are a student - not an adventurer. The guild isn't in the business of hiring
    minors and during your time acting on behalf of the guild you must understand that you do not
    have the rank and privileges of a full member of the guild.

    That being said, your position is not without its perks.

    You will be a provisional member of the Adventurer's Guild, and will be
    granted a provisional license.

    This process isn't all too dissimilar to what any prospective adventurer might go through
    if they walked into our halls and applied for membership. The difference is that your path
    from here to full membership is much more clearly prescribed:

    During your time in our care you'll perform contracts on behalf of the guild. Once you
    graduate, should you still be in good standing with us, you'll not only be inducted
    as a full fledged member of the Adventurer's guild, but you'll begin your career as a
    {b}class C{/b} adventurer.

    This is a significant merit - most adventurers don't make it to class C without at least
    10 years of experience under their belt, and very few ever find themselves promoted past
    this classification.

    As a sponsored graduate from Qyburn you will find yourself quickly advancing through the
    guild ranks.
    """

    "She pauses to take a breath and steps over to grab a drink from a small bar tucked around
    the corner from the reception that I hadn't noticed until now."

    gm.says """
    You're making me talk today. Don't worry, we're almost through.

    So where was I? Right, so all of that is contingent on your fullfillment of duties to the guild
    and remaining in good academic standing back at the adademy.

    A kid like you from a Podunk-backwater like Alderwood couldn't fathom the sums of money the guild
    is fronting to sponsor your tution up there.

    Part of that is paid for from the revenue you'll earn doing contracts, but you can't
    hope to earn enough to pay back that debt in full - and we don't expect you to.

    Instead the guild is making an investment in you as a promising young candidate for a future
    master adventurer. If we find you're not living up to that promise, we'll have no choice
    but to divest our investment in you.
    """

    "She pauses to take another long drink and I can't make out what's in that dark red-brown
    liquid she has in her mug."

    call .adventuers_guild_questions

    gm.says """
    Great. So having said all that, put it out of mind for now.

    There will be plenty of time for that once you're a full student at the academy,
    but you're no use to us if you don't pass your Quals.

    So report back here in a weeks time after you've {i}passed{/i} your exams, and we'll get you set
    up with a physical license and let you start taking on contracts.
    """

    call .post_guild

    return

default guild_menu_set1 = set()

label .adventuers_guild_questions:
    menu:
        # use a menu set so you can go through all the options
        set guild_menu_set1

        gm.says "Alright that's my whole spiel. Do you have any questions before we kick you out?"

        "You knew my father?":
            gm.says """
            I did.

            Damien was equal parts a good man and a scoundrel, but he had a big heart and he
            loved you with all of it.

            He would go to unreasonable lengths to help those in front of him.

            He had all these grand plans of making it big as an adventurer. Bringing back wealth
            and glory. He figured this was how he'd do right by you all.

            But he didn't understand where his wife and kids needed him most was back home with them.
            And then he went and got himself killed.

            But there's no point in reminiscing on the past. Maybe if you can establish yourself
            more around here, I'll have more stories to tell about him.
            """
            jump .adventuers_guild_questions
        "Do I get paid?":
            gm.says """
            Hah! Well you've got the right attitude, believe it or not. We're not a charity, and the
            guild collects payment for the contracts we fulfill.

            Based on your rank we have standard rate splits. For example a full Class E adventurer
            would generally expect to get a 60\% split of the payout, which isn't bad considering
            it's costing us more to organize these contracts, facilitate the payments, and offer
            support to adventurers than we're making on that 40\% cut.

            But we need you all to make enough to feed yourselves and stay off the streets while you
            hopefully get good enough to take on more difficult contracts.

            Those contracts in turn are more lucrative so the guild needs to take less of a cut
            to cover our overheads. So at the higher ranks, the job pays pretty well.

            Of course, we won't be anywhere near as generous with you. We're already paying
            for your cushy room as well as all the food you eat up there at the academy,
            not to mention the outrageous sums they charge for tuition.

            So we'll be taking most of what you bring in from contracts so you can start paying
            back what we've invested in you.

            Still we'll leave you with some pocket change so you can afford to buy some candy after
            class.
            """
            jump .adventuers_guild_questions
        "Not really":
            pass
            # skip the rest of the questions
    return

label .post_guild:

    scene bg town street afternoon with dissolve

    """
    After leaving the guild hall I note that it's well past midday now.
    This far north, it won't be long now until sunset.

    I feel my stomach grumbling as I realize I haven't had anything to eat since early morning.
    """

    call .market_lunch

    scene bg town street afternoon with dissolve

    mc.says "Excuse me, can you point me to the nearest shrine to the spirits?"

    "Stranger1" "Sorry, I'm not sure..."

    "Stranger2" "A shrine? I don't think I've ever seen one around here."

    "Stranger3" "Sorry there aren't too many superstitious folks around here kid."

    "It takes several more tries before I find someone who can point me in the right direction"

    "Stranger17" "A shrine... yeah I swear I've seen one around somewhere. I think down that
    district there, a little ways past the residential blocks. There should be one over there."

    "And by the time I track it down it's been nearly two hours since I started and the sun is
    hanging low in the sky."

    return

label .market_lunch:
    scene bg market with dissolve

    """
    I make my way to the market and follow my nose to the prepared food stalls.

    There I'm met with a cavalcade of sights and sounds and smells of so many dishes being prepared.

    I spend a while deliberating before settling on some dumplings and a fresh peach for dessert.
    """

    $ state.change_money(-3)

    """
    I find a quiet bench overlooking the river to enjoy my meal.

    I feel like a lot's happened already and I should take this opportunity to take stock.

    I'm here to study at the Qyburn academy. I'm not having to pay for any of it myself because
    the guild is somehow convinced I'm worth sponsoring. But why?

    When my mom told me a year ago that this had been decided I didn't really question it.
    My parents were both adventurers back in the day so I figured it was as a favor to my mom, but
    I didn't appreciate how much of a big deal it would turn out to be.

    I've always been facinated by magic, but I've never cast anything before on purpose.
    I guess sometimes when I got really emotional I might accidentally stir up some wind or
    knock something over. But those kinds of stories weren't uncommon.

    Our local shrine cleric didn't have much of a talent for it. Thile they would perform
    traditonal rituals during holidays using the spirits there was nothing they could teach me.
    There would also be traveilng magi from time to time who would stay at our village while
    passing through. But they never had much patience for me.

    So here I am attending a renowned magical academy when I don't really know the first thing about
    magic.

    Whatever the reason, classes begin tomorrow and I'm genuinely excited about that, but that
    excitement is deadened by the prospect of an exam at the end of the week. I don't know if I can
    prepare for it in time.

    Then starting next week I guess I'll have duties for the Adventurer's guild.
    And the guildmaster said they knew my father. This could be my chance to find out what happened
    to him and what kind of man he was.

    It's a lot to handle but somewhere between the full stomach and laying out my concerns
    I feel a lot more in control.

    I also recall that there was one more thing I had been meaning to do in town today. I return
    to the market and pick up a few more peaches before starting on my last mission for the day.
    """

    $ state.change_money(-2)

    return

label day1_night(callback):

    call .shrine_intro

    $ callback()

label .shrine_intro:

    scene bg shrine evening with dissolve

    """
    Back home it's pretty normal for people to show reverence to the spirits, and the shrine is
    a pretty prominent feature of the town.

    I was never especially devout, but I was taught that whenever traveling you should pay respects
    to the local spirits and ask for their protection while visiting their domain.

    It seems the people here have a different perspective towards the spirits, which feels odd
    because this city and everything that's made it so successful is built entirely on the power
    of the spirits.

    Now that I approach the shrine, my offering of fresh peaches in tow,
    I take notice of how run-down the temple around it is.

    The main offering altar is well maintained but there are side buildings that look abandoned and
    unkempt.

    It's so quiet that I feel like I'm intruding, but I gather up my courage and move to make my
    offering.
    """

    show expression sk.image

    sk.says "Well now isn't this a surprise. What are you doing here young one?"

    mc.says "Good evening ma'am. I'm new to town and I'm here to pay my respects to the
    local spirits."

    sk.says "Have you now? And what have your brought the spirits this evening?"

    mc.says "Just some peaches from the market."

    "I put my 3 peaches on the altar step back down from the steps."

    sk.says "Peaches, you say?"

    "The old woman saunters over to the offering altar picks up a peach and inspects it."

    sk.says "Mmm, you've got a good eye for produce."

    "And with a loud crunch, she takes a bite of my offering."

    sk.says "How did you know peaches were my favorite?"

    "I'm at a loss for words. This woman can't be an official here, she must be some vagrant who
    swipes offerings people leave here!"

    sk.says "Hehehehe oh you must see the look on your face.
    Oh don't get your knickers in a knot, I'm just having some fun with you.
    "

    mc.says "By stealing offerings from the shrine! Does noone in this city
    respect the spirits anymore?!"

    "I don't know why this has me so heated. Somehow this moment was important to me. Some connection
    to home through similar ritual."

    sk.says """
    You should be old enough to know by now the spirits aren't sneaking in at night to
    whisk your offering away. At a more distinguished temple in the south the attendants might
    leave this offering out for a few days until the spoiling fruit threatens to injure
    the dignity of the shrine.

    At which point they'll throw it on a rubbish heap. Or perhaps at some of the more progressive
    sites they might collect the eddible offerings to donate to an orphanage.

    But don't you think to question my devotion to the spirits just beacuse I won't tolerate letting
    a prime peach go to waste!

    Why else would I carry on with such a thankless job as maintaining this temple?
    """

    "I'm a embarrased by being called out this way, but I still can't help glancing at the poor
    state of the rest of the temple."

    "The old woman seems to catch my gaze and grows a bit more solemn."

    sk.says """
    Not that this place hasn't seen better days. But what am I to do? You can't
    fix up a temple with peaches alone, not that the locals bother offering even that much.

    Look, I know you're not a bad kid. I didn't need to leap don't your throat like that.
    In my advanced age I've learned to be less concerned about dignity; much better
    to say what's on your mind and have fun with what time I've got left.

    So you've come all the way out here, let me offer you a blessing:

    As I've borne witness, the sprits accept and appreciate your offering, child.
    May they show you their favor, offer you their protection, and guide you with
    their wisdom during your stay here.
    """

    mc.says "Thank you, shrine keeper."

    """I offer her a bow, but as I straighten again I feel a dizziness come over me, along with a
    thrumming in my ears.

    I have to support myself on a pillar to stop from falling as the thrumming grows, louder and
    more insistent.

    I can hear someone calling out to me, at the edges of my perception... the shrine keeper?

    Then as quickly as it came, the sensation fades again. I'm sweating and shivering slightly but
    am already feeling much better, though I see the shrine keeper looking very concerned.

    Finding my balance again, I straighten up.
    """

    mc.says "I'm sorry, I don't know what just came over me. I should be fine now that it's passed."

    "Then all at once it hits me again, like a tsunami, and I lose consciousness."

    return

init python:
    plot_schedule.schedule_event((1, TOD.MORNING), Event("day1_morning"))
    plot_schedule.schedule_event((1, TOD.AFTERNOON), Event("day1_afternoon"))
    plot_schedule.schedule_event((1, TOD.NIGHT), Event("day1_night"))