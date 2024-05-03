
screen stats_menu():

    tag menu

    add HBox(Transform(menu_nav_panel_color, xsize=350), menu_main_panel_color) # The background; can be whatever

    use game_menu('Stats')

    fixed:
        xsize 1500 xalign 1.0

        hbox:
            yoffset 200
            vbox:
                xsize 500
                label "Magical Skills"
                for skill in state.stats.magic_skills():
                    text f"{{b}}{skill.name}{{/b}}: {skill.level} ({skill.exp}xp)"


            vbox:
                xsize 500
                label "Mundane Skills"
                for skill in state.stats.mundane_skills():
                    text f"{{b}}{skill.name}{{/b}}: {skill.level} ({skill.exp}xp)"


            vbox:
                xsize 500
                label "Affection"

                text "Jim: 1"

                text "Johanna: 2"

# We can also put things like money and symbols of major points of progression here.
# This should be a overall summary of your character's progress.



