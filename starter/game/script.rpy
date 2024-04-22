# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# Define displayables

image button_idle = Solid("#abc", xysize=(50, 50))
image button_hover = Solid("#385675", xysize=(50, 50))

init python:
    
    screen_width = 100
    screen_height = 100
    # Define displayables

    # bg_town = Frame("background_concepts/city_overview.webp")
    bg_town = Frame("background_concepts/city_overview3.PNG")

    # Define persistent values

    stats = {k : 0 for k in range(9)}

    # Define operations

    def setup(i):
        def activate():
            stats[i] += 1
            renpy.notify(f"Your {i} stat is {stats[i]}!")
            if stats[i] > 10:
                return True
        return activate


screen action_select():
    imagemap:
        idle "background_concepts/city_overview3.PNG"
        hover "background_concepts/city_overview3_hover.PNG"
        ground "background_concepts/city_overview3.PNG"
        # (934, 172, 74, 74)

        hotspot (1048, 160, 82, 85) action setup(1)
        hotspot (530, 473, 85, 96) action setup(2)
        hotspot (812, 712, 86, 92) action setup(3)





# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    image foo = "#fff"
    scene foo

    "Here's the first statement"

    "After this there will be an interactive segment"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    call screen action_select

    "That concludes the interactive portion of the game."

    "The end."

    # This ends the game.

    return
