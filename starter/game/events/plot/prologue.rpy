

##### Day 0 #####

label prologue0(callback):
    show bg black

    "Driver" "So, m'lord, you're a new student at the institute, huh?"

    "M'lord?"

    show bg carriage night with dissolve

    mc.says "Hmm? Oh, yeah I suppose I will be."

    "Driver" "Pretty unusual, having a pick-up like this.
    Not that it's my first time carrying a student up there or anything."

    mc.says "Really?"

    "It was hard focusing on what the driver was saying when so much is happening all around the carriage."

    "There was so much life, so much motion. It was like... well, magic."

    "Driver" "It's just, you know, odd for one of you to be arriving on your own like this.
    Usually students will have their own retinue. And... more bags, you know?"

    mc.says "Mmhmm, yeah."

    "A child running right by us is carrying a stick rapidly changing in color with a stream of sparks flying off the end."

    "Driver" "So... you must be one them uh, 'special cases', huh?"

    mc.says "Might be."

    "Special what?"

    "Driver" "Too right, well, none of my business, that."

    "Whatever the driver was thinking, they got quiet after that, which let me focus on everything around us."

    "There were so many wonders on the street. A shop has a sign that spins on its own
    and reads a different slogan with each revolution."

    "And there! A woman has her baby in a carriage that seems to be pushing itself."

    "Driver" "It always gets lively right before the start of a new term. Plenty to see in town."

    "The driver seemed to notice me gaping out the windows with a grin."

    "I continue staring, nearly hanging out the window at one point to watch a fountain erupting with
    what appear to be flower petals that went off jus as we rode past."

    "Driver" "Well, I'm sure you'll be learning a lot up there. And we're not too far now."

    show bg school approach night with dissolve

    "As we round the bend on the street I finally get a proper view at our destination:
    The Magical Institute of Qyburn"

    "Home to the most advanced magical research in the world."

    "No one could see that castle bearing down on them and hang onto any shread of misplaced confidence.
    Visitors were at the mercy of the powers that reside here."

    call .welcome

    $ callback()

label .welcome:

    show bg admin night with dissolve

    "We finally make it to the entrance where the driver drops me off along with
    the lone bag that comprises all my wordly posessions."

    "I can hardly take a step inside the grand doors before I'm ambushed by an administrator."

    "Administrator" "Welcome to the institute! We hope your journey was a pleasant one?"

    mc.says "Oh, it \u2014"

    "Administrator" "May I see your invitation?"

    "They deftly swipe the invitation from my hands just as I'm producing it from my pocket."

    "Administrator" """Oh, very interesting. Yes, we've certainly been expecting you.

    Well I'd love to give you a tour of the grounds you'll be calling home, but it's dreadfully
    late already and you must be exhausted.

    Let me lead you to where you'll be staying."""

    "They grabbed my arm with too much strength for someone with their frame and dragged me out
    the door I just came in."

    "Administrator" """Most of the students have already arrived and are resting in their rooms.
    Do try not to make any undue ruckus in the dormitories.

    As you should already be aware, tomorrow is the opening ceremony for the new term.
    That will be the first day of your new life here.

    For now here are the keys to your room. There is a strict curfew once classes begin but it
    would be wise for you to begin practicing it now.
    """

    "The dragging didn't stop until we got to the doorstep of my room."

    "Administrator" "Oh, how exciting! We expect great things from you, so be sure to get some rest."

    show bg dorm room night with dissolve

    """Practically dumping me there, they finally let me go, and briskly walk away without
    ever letting me get a word in.

    Which is well enough. They were right that I was exhausted.

    Entering my new room, I drop my bag to the floor, not bothering to unpack,
    and let myself drop into the bed.

    Between the excitement of everything I saw in town on the ride in and my nerves confronting the
    reality of actually being a student here, I'm worried that I won't be able to get any rest at all.

    On the other hand, the journey here had been long and it all seemed to be catching up with
    me now as I let out a yawn.

    What had they said? They "expect great things?"

    I stifle another yawn as my eyelids grow heavy and I let sleep take me.
    """

    show bg black with dissolve

    return


init python:
    plot_schedule.schedule_event((0, TOD.NIGHT), Event("prologue0"))

##### Day 1 #####

label prologue1_morning(callback):

    show bg black with dissolve

    "
    I wake up the next morning just before sunrise, the still sore from travel.
    "

    show bg dorm room night with dissolve

    """
    I didn't have a chance to appreciate it last night but the bed in my room may be the
    nicest I've ever been in. I slept like a rock.

    I stretch and look outside. The sky is still dark but growing red with the coming sun.
    I can't see any activity from my window and I take a moment to just appreciate the quiet.
    """

    """
    Today will be the opening ceremony but not for at least an hour more, so I decide to tidy up a bit.

    After unpacking my two sets of clothes into a wardrobe large enough to make my collection
    feel inadequate, I turn to set up my personal effects on my desk:

    A worn dagger that used to belong to my father, and a sharpening stone to maintain it.

    A clear crystal with a streak running through it strung on a cord -
    a protective charm from a merchant who had visited our home town years ago.

    I don't wear it much anymore but it felt appropriate to bring whatever protection
    I could muster when leaving home to come here.

    Lastly I pull out a tattered leatherbound notebook. Somewhere between a diary and a sketchbook
    I use it regularly and it's showing its age. I'll need to pick up some more parchment for it in
    town.
    """

    show bg dorm hallway morning

    """
    I pull out the last of my traveling rations from my sack and munch on it as I look back outside.

    The sun has stubbornly refused to budge in the sixty seconds it took me to unpack so I decide
    to explore the dormitory.

    I hear signs of life from other rooms as others are starting to wake.
    I don't feel like I have the courage needed to endure a run-in with my neighbors yet,
    so I move with haste to a quieter section of the building.

    A door standing ajar catches my attention and I peek through to find not another bedroom
    but what appears to be a series of raised washbasins mounted to the wall.
    """

    show bg sink at truecenter
    with moveinbottom

    """
    I approach with curiosity and just as I'm leaning in to get a closer look at the aparatus
    it springs to life with water running down into the basin, and down a hole in the base.

    I can't help but release a yelp in surprise and rush out the room the way I came in.
    """

    show bg dorm hallway morning
    with pushleft

    "
    I'm crouching in the hall, peaking back into the room, fearing that I've triggered some
    magical alarm system, when I notice I'm no longer alone.
    "

    show expression ag.image

    $ ag.meet()

    ag.says "Are you ok there? {i}*snicker*{/i}"

    "She seems to be trying, not very successfully, to stifle laughter after catching me...
    well I'm not sure what I've done wrong yet but I'd prefer to not get in trouble for it."

    menu:
        "What do I do?"

        "Play it cool.":
            mc.says "Ok? Me? I'm great. Why wouldn't I be ok?"

            ag.says "Oh, pardon me, you just seemed a bit alarmed, is all."

        "Come up with an excuse":
            mc.says "Oh, I'm fine, yep. I was just, uh, making sure no one snuck in there."

            ag.says "Snuck in? I imagine anyone who's made it on campus is welcome to use the facilities."

    "Her smile fades and she looks a little puzzled before asking,"

    ag.says "Have you never used a washroom before?"

    "A washroom? So this room is for washing things, probably powered by some magic?"

    "Swallowing my pride as it doesn't seem like maintaining a bluff will get me anywhere,"

    mc.says "Honestly, no, I've never heard of one before now."

    "A look of shock quickly passes over her face before being replaced by a twinkle of excitement in her eyes."

    ag.says "That's surprsing; they're such marvelous conveniences!"

    "She grabs my arm and pulls me back into the room and shows me how getting near the basin
    causes the device above it to start emitting a fountain of water."

    ag.says """The basis is a fairly standard water artifice hidden behind the wall with some clever
    engineering to funnel the watter the right way without causing a mess. The real genius, however,
    is how newer installations react to your mana to immediately begin dispensing when you approach.

    I thought you might have never used an automatic one before, which was alarming the first time
    I tried one as a child... but to think you've never used a washroom before.

    I know the technology's only a few decades old, but I've grown up with them my whole life
    so it's such hardship when I have do without while traveling.

    What house are you from that doesn't have washrooms in their estate?
    """

    "What house? My confusion seems to show as she interjects:"

    $ ag.introduce()

    ag.says "Oh where are my manners? I'm [ag.name()], of house [ag.family_name]."

    "It finally clicks. She's nobility. I have no idea what the etiquette is around introductions
    but she doesn't look like she'll take any transgression personally."

    mc.says "I'm [mc.name()] of Karnsley. I'm afraid I don't belong to any of the noble houses."

    ag.says "Oh, wow. I'm sorry for jumping to conclusions. Are you employed by the academy?"

    mc.says "I'm actually a student, or will be once the term start."

    ag.says "Really? I didn't realize the school admitted commoners. Well I've made a fool of myself."

    mc.says "True, the only way you could look more foolish is if I had caught you panicking over being
    caught tresspassing by an automatic washbasin,"

    "I reply with a grin and we both laugh off the awkward circumstances of our meeting."

    "I was apprehensive about how to interact with other students here, but I'm totally disarmed by
    how friendly [ag.name()] has been."

    ag.says "Ok, in that case, I {i}have{/i} to show you the toilets.
    This is going to change your life."

    """
    She drags me back into the washroom to show me several other wonders and we spend
    a while together, her excitedly describing the workings of the artifice mechanisms involved,
    and me mostly just trying to keep up.

    Apparently the school also has indoor bath houses, though they're in detached buildings
    due to the complexity of drawing and draining that much water.

    By the time we're through, the sun has fully risen and there's plenty of motion around the door
    as students prepare for the day.
    """

    ag.says "Shoot, I need to get ready if I'm going to be in time for the opening ceremony.
    It was a pleasure meeting you, [mc.name()]."

    "So we part ways and I join the throng of students heading their way to the auditorium."

    call .opening_ceremony

    $ callback()

label .opening_ceremony:

    scene bg school auditorium with dissolve

    """I've taken my seat in the auditorium amongst what seem to be over a hundred other students.

    A few stragglers are still trickling in but it seems like the ceremony is getting ready to begin.
    """

    $ hm.meet()

    show expression hm.image

    """An elderly man makes his way onto the central podium on the stage. He's clearly quite frail but
    somehow manages to exude power at the same time.

    All the chatter dies down.
    """

    hm.says "{size=72}{cps=20}POTENTIA UTENDEM EST!{/cps}{/size}"

    "The old man roars, far louder than should be possible, and no hint of frailty remains in his frame."

    hm.says """These are the words of our institution. These are the words we will instill in you.
    And if you expect to survive here, these are the words you must live by.

    First, you must know who we are.

    We are not spiritual theoreticians like you will find in the institutions of the east.

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

    But as you grow in power so too will you grow in your duty to put that power to use.
    There is no greater sin than the inaction of the powerful.

    And once your time is done here you will take what we teach you back to your homes,
    to your lands, to the far corners of the world and you will put it to use.
    """

    "And then there is a long pause. The old man appears to almost shrink he no longer
    imposes the same aura as before, but everone is still a bit shaken by that performance."

    hm.says "And with that let's call the ceremony bit of this pageant done eh? Hoh oh oh oh oh."

    $ hm.introduce()

    hm.says """
    In case you haven't gathered it yet, I am the Headmaster at the Qyburn Institute of Magic.

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

    Each year we tend to have either one or two such students, but this year we have an
    unprecedented five. I for one look forward to such promising talent joining us for the
    schoolyear.

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

    "I make it as far as the stairs in front of the building, lost my my self-pity, before a staff
    member stops me to hand me a note. Apparently I'm to report to the Adventurer's guild today for orientation."

    return

label prologue1_afternoon(callback):
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

    I've thought more than a few times about joining up with them as it always felt like a easy
    solution to the otherwise directionless life I've lead. But my mom wouldn't hear it.

    Come to think of it I'm surprised she was convinced to let me come to this school on a
    guild sponsorship.
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
    and didn't make it.
    """

    gm.says """
    You probably already have a decent idea of how the guild works but your situation is a bit special
    so let's just start from the beginning and clear up any misconceptions you might be carrying.

    First of all you are a student - not an adventurer. The guild isn't in the business of hiring
    minors and during your time acting on behalf of the guild you must understand that you do not
    have the rank and privileges of a full member of the guild.

    That being said, your position is not without its perks.

    You are from this day forward, provisional members of the Adventurer's Guild, and will be
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
    Damn, you're making me talk today. Don't worry, we're almost through.

    So where was I? Right, so all of that is contingent on your fullfillment of duties to the guild
    and remaining in good academic standing back at the adademy.

    A kid like you from a Podunk-backwater like Karnsley couldn't fathom the sums of money the guild
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

            He had all these grand plans of making it big as an adventurer. Bringing back wealth and glory.
            He figured this was how he'd do right by you all.

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

    Classes begin tomorrow but more importantly there's an exam at the end of the week that
    I need to make sure I'm prepared for.

    I have duties to the Adventurer's Guild, but that can wait until next week.

    And the guildmaster said they knew my father. This could be my chance to find out what happened
    to him and what kind of man he was.

    Somewhere between the full stomach and laying out my concerns I feel a lot more in control.

    I also recall that there was one more thing I had been meaning to do in town today. I return
    to the market and pick up a few more peaches before starting on my last mission for the day.
    """

    $ state.change_money(-2)

    return

label prologue1_night(callback):

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
    plot_schedule.schedule_event((1, TOD.MORNING), Event("prologue1_morning"))
    plot_schedule.schedule_event((1, TOD.AFTERNOON), Event("prologue1_afternoon"))
    plot_schedule.schedule_event((1, TOD.NIGHT), Event("prologue1_night"))

##### Day 3 #####

# - Have a pop-up modal.
# - it will reiterate the narrative deal (qualifying exam) and how it will play out in
#   game mechanics
# - Make sure the locations are set up so that it is technically possible, but difficult, to fail
#   by just ignoring the classes and fucking about in town or whatever.

label prologue2(callback):

    scene bg school infirmary morning with dissolve

    show expression sn.image

    "Hello!"

    "This is infirmary scene"

    "Is this scene a good idea or just a distraction?"

    "Eh. I dunno. Feels like more filler is better at this point."

    # do the first lesson
    # first lesson should cover basic concepts in spiritual magic, colored by limited human understanding
    # add some points to magic fundamentals

    $ callback()

init python:
    plot_schedule.schedule_event((2, TOD.MORNING), Event("prologue2", takes_time=False))

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
