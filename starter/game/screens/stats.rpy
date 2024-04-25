
screen stats_menu():

    tag menu

    add HBox(Transform("#292835", xsize=350), "#21212db2") # The background; can be whatever

    use game_menu('Stats')

    fixed:
        xsize 1500 xalign 1.0

        hbox:
            yoffset 200
            vbox:
                xsize 300
                label "Stats"

                text "punchin': 5"

                text "runnin': 10"

                text "shootin': 25"

                text "karma: [state.karma]"

                text "money: [state.money]"

            vbox:
                xsize 300
                label "Affection"

                text "Jim: 1"

                text "Johanna: 2"




