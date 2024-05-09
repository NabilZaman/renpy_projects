
label day5_night(callback):
    scene bg dorm room night with dissolve

    """
    Tonight the thrumming begins earlier than before.

    I realize it's the same sensation I get when I push myself too hard to attune to the spirits.
    Except, different.

    It's deeper, and somehow... more insistent.

    It must be some sort of after-effect of working myself so hard in clases.

    Perhaps everyone feels this when they first start studying magic, but all the other students
    began study with private instructors when they were much younger.

    In any case it's been such a consistent companion to me these last few nights that it's
    almost comforting.

    I'm able to ignore it well enough that it doens't take long to fall asleep.
    """

    call .dream

    $ callback()

label .dream:
    """
    ...

    Through the now-familar buzzing that joins me in my dreams each night, I notice another
    sound layered on top of it. A crackling.

    The lights I've seen before are clearer. Reds and yellows and oranges.

    And a new sensation strikes me. I can smell Smoke.

    When the witch caught us I panicked and ran.

    I was holding the little artifice my parents use in their tavern.

    The building isn't so big, and there's not a lot of room for tables inside. So half of them are
    set up outside.

    But nights here can get real cold. So we've got a few of these artficial flames set up in cages
    all around the tables so folks can enjoy some warmth while they're eating.

    But when I was so surprised I lost it. I must have dropped it while we were running.

    Now I'm back at the abandoned temple. The artifice must have triggered and the long dead and
    untreated wood of the structure eagerly took to the flame.

    The flame grows and grows and consumes everything. I feel it coming to get me and I'm ready
    to accept it.
    """

    return

init python:
    plot_schedule.schedule_event((5, TOD.NIGHT), Event("day5_night"))
