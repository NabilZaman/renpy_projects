
init -100 python:
    from enum import Enum

    class Significance(Enum):
        MAIN = 0
        MAJOR = 1
        MINOR = 2

    class CustomCharacter:
        def __init__(self, name: str, significance: Significance, color: str = "#fff",
                        dark_outline=True, image=None, met=False, introduced=False,
                        default_name='???', familiar_name=None):
            self.family_name = ' '.join(name.split()[1:])
            self.first_name = name.split()[0]
            self.full_name = name
            self.default_name = default_name
            self.familiar_name = self.first_name if familiar_name is None else familiar_name
            self.met = met
            self.introduced = introduced
            self.color = color
            self.significance = significance
            self.image = Image(image) if image is not None else None

            if dark_outline:
                outline_color = "#000"
            else:
                outline_color = "#fff"
            name_outline = [(2, outline_color, 0, 0)]
            text_outline = [(1, outline_color, 0, 0)]
            self.char = DynamicCharacter(self.name, who_color=color, what_color=color,
                                            who_outlines=name_outline, what_outlines=text_outline)
            self.affection = 0

            global major_characters
            global minor_characters
            if significance == Significance.MAJOR:
                major_characters.append(self)
            elif significance == Significance.MINOR:
                minor_characters.append(self)

        def name(self) -> str:
            return self.familiar_name if self.introduced else self.default_name

        def full_name(self):
            return self.full_name

        def meet(self) -> None:
            # this can display some popup or achievement or something eventually
            self.met = True

        def introduce(self) -> str:
            # this can display some popup or achievement or something eventually
            self.introduced = True
            return self.name()

        def aff_change(self, value=1) -> None:
            self.affection += value

        @property
        def says(self):
            return self.char

    def met_characters(significance: Significance):
        full_list = None
        if significance is Significance.MAJOR:
            full_list = major_characters
        elif significance is Significance.MINOR:
            full_list = minor_characters
        return [c for c in full_list if c.met]


default major_characters = []
default minor_characters = []

define char_folder = 'character_concepts/'

define generic_male = 'character_concepts/generic_male_silhouette.png'
define generic_female = 'character_concepts/generic_female_silhouette.png'

### Main Character ###

define mc_color = "#c8d1d2ff"
default mc = CustomCharacter("MC", Significance.MAIN, mc_color, met=True, introduced=True)

### Major Characters ###

define wg_color = "#3ae766"
default wg = CustomCharacter("Rae", Significance.MAJOR, wg_color, image=char_folder+"wind_girl_transparent.png")

define tg_color = "#4cd1f6"
default tg = CustomCharacter("Elena Rozen", Significance.MAJOR, tg_color, image=char_folder+"white_hair_girl_transparent.png")

define tb_color = "#fff"
default tb = CustomCharacter("TwinBoy", Significance.MAJOR, tb_color, image=char_folder+"white_hair_boy_transparent.png")

define ag_color = "#f3d513"
default ag = CustomCharacter("ArtistGirl", Significance.MAJOR, ag_color, image=char_folder+"green_hair_girl_transparent.png")

define sc_color = "#ff4a4a"
default sc = CustomCharacter("SportsCharacter", Significance.MAJOR, sc_color, image=generic_male)

define jc_color = "#ff954a"
default jc = CustomCharacter("JerkCharacter", Significance.MAJOR, jc_color, image=generic_male)

define ts_color = "#fff"
default ts = CustomCharacter("TimeSpirit", Significance.MAJOR, ts_color, image=char_folder+"time_spirit_transparent.png")

### Minor Characters ###
default minor_character_color = "#fff"
default hm = CustomCharacter("Headmaster", Significance.MINOR, minor_character_color, image=char_folder+"dean_transparent.png", introduced=True)
default gr = CustomCharacter("Receptionist", Significance.MINOR, minor_character_color, image=char_folder+"guild_receptionist_transparent.png", met=True, introduced=True)
default gm = CustomCharacter("Guildmaster", Significance.MINOR, minor_character_color, image=char_folder+"guildmaster_transparent.png", introduced=True)
default sk = CustomCharacter("ShrineKeeper", Significance.MINOR, minor_character_color, image=char_folder+"shrine_keeper_transparent.png", introduced=True)
default sn = CustomCharacter("SchoolNurse", Significance.MINOR, minor_character_color, image=char_folder+"hot_nurse_transparent.png", introduced=True)
default ti = CustomCharacter("TheoryInstructor", Significance.MINOR, minor_character_color, image=char_folder+"theory_professor_transparent.png", introduced=True)