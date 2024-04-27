
# Define Screens
screen location_tooltip(location, display_pos):
    frame:
        anchor (0.5, 1.0)
        pos display_pos
        background "color_black"
        vbox:
            text location.name size 18

screen calendar_display():
    vbox:
        xalign 1.0
        yalign 0.0
        offset(-10, 10)
        imagebutton:
            idle "icons/time_icon_[TOD.TIME_NAMES[state.cal.time_of_day]].jpg"
            xalign 0.5
            action state.freeze
        text "[TOD.TIME_NAMES[state.cal.time_of_day]]":
            size 28
            xalign 0.5
            outlines [(1, "#000", 0, 0)]
            if state.is_frozen():
                color "#66b"
            else:
                color "#fff"
        text "Day: [state.cal.day]":
            outlines [(1, "#000", 0, 0)]
            size 28
            xalign 0.5

screen powers_display():
    hbox:
        xalign 0.0
        yalign 0.0
        offset (10, 10)
        spacing 6
        text "Time Freezes Left:":
            size 24
            outlines [(1, "#000", 0, 0)]
        for i in range(state.freezes_available):
            frame:
                background "color_black"
                xysize(21, 21)
                yalign 0.5
                frame:
                    background "color_mauve"
                    xysize(15, 15)
                    xalign 0.5
                    yalign 0.5


screen money_display():
    hbox:
        xalign 1.0
        yalign 1.0
        offset(-10, -10)
        add "icons/gem.jpg":
            yalign 0.5
        text "[state.money]":
            outlines [(1, "#000", 0, 0)]
            yalign 0.5

screen location_display():
    fixed:
        text "[state.cur_map.name]":
            size 72
            outlines [(2, "#000", 0, 0)]
            xalign 0.5

screen hud_screen():
    use calendar_display
    use money_display
    use location_display
    use powers_display

screen town_map_select(time_slot_map):
    imagemap:
        auto time_slot_map.background

        for rect, loc in time_slot_map.locations.items():
            hotspot rect:
                action state.setup_map_interaction(loc)
                hovered loc.on_hover
                unhovered loc.off_hover
                sensitive loc.available()

    use hud_screen

screen school_map_select(time_slot_map):
    imagemap:
        auto time_slot_map.background

        for rect, loc in time_slot_map.locations.items():
            hotspot rect:
                action state.setup_map_interaction(loc)
                hovered loc.on_hover
                unhovered loc.off_hover
                sensitive loc.available()

        use hud_screen

