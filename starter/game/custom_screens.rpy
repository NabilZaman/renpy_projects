
# Define Screens
screen location_tooltip(location, display_pos):
    frame:
        anchor (0.5, 1.0)
        pos display_pos
        background "color_black"
        vbox:
            text location.name size 18

screen calendar_display(interactable=True):
    vbox:
        xalign 1.0
        yalign 0.0
        offset(-10, 10)
        imagebutton:
            idle "icons/time_icon_[TOD.TIME_NAMES[state.cal.time_of_day]].jpg"
            xalign 0.5
            action (state.freeze if interactable else NullAction())
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
    vbox:
        offset(10, 10)
        text f"HP: {state.status.hp}":
            outlines [(1, "#000", 0, 0)]
        text f"MP: {state.status.mp}":
            outlines [(1, "#000", 0, 0)]
        hbox:
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

screen slim_hud_screen():
    use calendar_display
    use money_display

screen map_select(time_slot_map):
    imagemap:
        auto time_slot_map.background

        for rect, loc in time_slot_map.locations.items():
            hotspot rect:
                action state.setup_map_interaction(loc)
                sensitive loc.selectable()
            if loc.selectable():
                # if the rect is too low, draw the text on top
                if (rect[1] + rect[3]) > (config.screen_height - 100):
                    text loc.name:
                        yanchor 1.0
                        xanchor 0.5
                        ypos rect[1]
                        xpos int(rect[0] + rect[2] / 2)
                        outlines [(1, "#000", 0, 0)]
                else:
                    text loc.name:
                        yanchor 0.0
                        xanchor 0.5
                        ypos rect[1] + rect[3]
                        xpos int(rect[0] + rect[2] / 2)
                        outlines [(1, "#000", 0, 0)]
    use hud_screen

screen warning_dialog(message):
    modal True
    fixed:
        xalign 0.5
        yalign 0.5
        xmaximum 500
        yfit True
        xfit True
        frame:
            padding (20, 10)
            vbox:
                spacing 15
                text message:
                    xalign 0.5
                textbutton "OK":
                    xalign 1.0
                    action Hide('warning_dialog') # This should hide the screen

define time_of_day_angles = {
    TOD.MORNING: 0,
    TOD.AFTERNOON: 240,
    TOD.NIGHT: 120,
}

define time_of_day_audio = {
    TOD.MORNING: "effects/morning_sound.wav",
    TOD.AFTERNOON: "effects/afternoon_sound.wav",
    TOD.NIGHT: "effects/evening_sound.wav",
}

screen time_of_day_transition(initial_time):
    python:
        target_time = (initial_time + 1) % TOD.TIME_SLOTS
        initial_angle = time_of_day_angles[initial_time]
        final_angle = initial_angle - 120
        sound_effect = time_of_day_audio[target_time]
    on "show" action Play("sound", sound_effect)
    fixed:
        frame:
            xfill True
            yfill True
            background "color_black"
            fixed:
                xalign 0.5
                yalign 0.5
                xysize (300, 300)
                add "time_of_day_cycle" at time_of_day_spin(2.0, start_angle=initial_angle, end_angle=final_angle):
                    fit "contain"
                    xalign 0.5
                    yalign 0.5

    timer 3.0 action Return(True)
