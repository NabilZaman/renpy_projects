
init python:
    def retrigger_external_event(screen_name, displayable_id, event_name):
        renpy.notify("Hello!")
        screen_displayable = renpy.get_displayable(screen_name, displayable_id)
        if screen_displayable is not None:
            screen_displayable.set_transform_event(event_name)

transform zoom_on_hover:
    on hover:
        linear 0.1 zoom 2.0
    on idle:
        zoom 1.0


transform fit_center(displayable):
    displayable
    align (0.5, 0.5)
    fit "contain"

transform zoomer(factor, displayable):
    displayable
    zoom factor

transform outer_card_default:
    # zoom 0.33
    pass

define card_text = (
        "Attack : 50\n"
        "Defense : 100\n"
        "Foo : 10000\n"
        )

image foo = zoomer(.5, "icons/green_card.png")

define card_img = fit_center(Image("icons/green_card.png"))

define compound_img = zoomer(0.33, Fixed(
    Fixed(
        fit_center(Image("icons/green_card.png")),
        Fixed(Frame("icons/time_of_day_cycle.png"), pos=(21, 79), xysize=(396, 238)),
        Text("Card Name", pos=(23, 33), yanchor=0.5, bold=True, color="#000"),
        Text(card_text, pos=(31, 362), color="#000"),
        Text("3", pos=(391, 596), anchor=(0.5, 0.5), bold=True, size=36, outlines=[(3, "#000", 2, 1)])
    ),
    xysize=(437, 642)
))

screen test_card_placement():
    fixed:
        at outer_card_default
        align (0.5, 0.5)
        xysize (437, 642)
        fixed:
            add "icons/green_card.png": # card border
                align (0.5, 0.5)
                fit "contain"
            fixed:
                pos (21, 79)
                xysize (396, 238)
                add Frame("icons/time_of_day_cycle.png")
            text "Card Name":
                pos (23, 33)
                yanchor 0.5
                color "#000"
                bold True
            text card_text:
                pos (31, 362)
                color "#000"
            text "3":
                pos (391, 596)
                anchor (0.5, 0.5)
                bold True
                size 36
                outlines [(3, "#000", 2, 1)]

screen test_card_obj():
    imagebutton:
        align (0.5, 0.5)
        at zoom_on_hover
        idle compound_img
        action Return()



label testing:

    "before animation"

    call screen test_card_obj

    "after animation"

    return


# The game starts here.

label start:
    # The setup label contains all the logic to set up the various game systems.
    call setup

    # This sets off the state machine that will drive the main game. We should not return from this operation until the game has ended.
    $ state.advance_state()

    # call testing

    "The end."

    return


# init python:
#     def retrigger_external_event(screen_name, displayable_id, event_name):
#         screen_displayable = renpy.get_displayable(screen_name, displayable_id)
#         if screen_displayable is not None:
#             screen_displayable.set_transform_event(event_name)

# screen my_screen:
#   button:
#     action Function(retrigger_external_event, "my_screen", "my_screen_displayable", "show")

#   text "Hello, World!" id "my_screen_displayable" at "my_repeatable_transform"

# transform my_repeatable_transform:
#   on show:
#     linear 0.5 zoom 2.0
