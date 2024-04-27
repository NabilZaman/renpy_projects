
init -100 python:
    from enum import Enum

    class Significance(Enum):
        MAIN = 0
        MAJOR = 1
        MINOR = 2

    major_characters = []
    minor_characters = []

    class CustomCharacter:
        def __init__(self, name: str, significance: Significance, color: str = "#c44",
                        dark_outline=True, image=None):
            self._name = name
            self.met = False
            self.introduced = False
            self.color = color
            self.significance = significance
            self.image = image

            if dark_outline:
                outline_color = "#000"
            else:
                outline_color = "#fff"
            name_outline = [(3, outline_color, 0, 0)]
            text_outline = [(2, outline_color, 0, 0)]
            self.char = DynamicCharacter(self.name, who_color=color, what_color=color,
                                            who_outlines=name_outline, what_outlines=text_outline)
            self.affection = 0

            global major_characters
            global minor_characters
            if significance == Significance.MAJOR:
                major_characters.append(self)
            elif significance == Significance.MINOR:
                minor_characters.appear(self)

        def name(self):
            return self._name if self.introduced else '???'

        @property
        def says(self):
            return self.char


define wg_color = "#3ae766"
define wg = CustomCharacter("Rae", Significance.MAJOR, wg_color, image="character_concepts/wind_girl_transparent.png")

define mc_color = "#c8d1d2ff"
define mc = CustomCharacter("MC", Significance.MAIN, mc_color)

