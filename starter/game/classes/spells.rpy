
init -99 python:
    class Element(Enum):
        Water = 0
        Wind = 1
        Fire = 2
        Kinesis = 3
        Light = 4
        Life = 5

    class SpellAttribute(Enum):
        Force = 0
        Cool = 1
        Heat = 2
        Recovery = 3
        Soothe = 4

    @dataclass
    class Spell:
        name: str
        element: Element
        lvl_req: int
        image: str
        effect: dict[SpellAttribute, int]
        cost: int
        registered: bool = False


    class Spellbook:
        def __init__(self, card_frame: str):
            self.card_frame = card_frame
            self.spells = []
            self.learned = False

            global spellbooks
            spellbooks.append(self)

        def learn(self):
            self.learned = True

        def add_spell(self, spell: Spell):
            self.spells.append(spell)


    class SpellRegistry:
        def __init__(self):
            self.spells: list[tuple[Spell, Spellbook]] = []

        def register(self, spell: Spell, spellbook: Spellbook):
            self.spells.append((spell, spellbook))

        def unregister(self, spell: Spell):
            for entry in self.spells:
                if entry[0] == spell:
                    self.spells.remove(entry)

        def is_registered(self, spell: Spell):
            for entry in self.spells:
                if entry[0] == spell:
                    return True
            return False

        def __iter__(self):
            for spell, book in self.spells:
                yield spell, book

        def __len__(self):
            return len(self.spells)

        def __getitem__(self, key):
            return self.spells[key]


    def create_spell(name: str, element: Element, level_req: int, image: str,
                        effect: dict[SpellAttribute, int], cost: int, spellbook: Spellbook):
        spellbook.add_spell(Spell(name, element, level_req, image, effect, cost))

define icon_folder = 'icons/'

define water_card_frame = icon_folder + "blue_card.png"
define wind_card_frame = icon_folder + "green_card.png"
define fire_card_frame = icon_folder + "red_card.png"
define kinesis_card_frame = icon_folder + "metallic_card.png"
define light_card_frame = icon_folder + "rainbow_card.png"
define life_card_frame = icon_folder + "green_card.png"

default spellbooks = []
default spell_registry = SpellRegistry()


default water_spells = Spellbook(water_card_frame)
default wind_spells = Spellbook(wind_card_frame)
default fire_spells = Spellbook(fire_card_frame)
default kinesis_spells = Spellbook(kinesis_card_frame)
default light_spells = Spellbook(light_card_frame)
default life_spells = Spellbook(life_card_frame)

init python:
    def setup_spells():
        create_spell(
            name="Drench",
            element=Element.Water,
            level_req=1,
            image="icons/time_of_day_cycle.png",
            effect={SpellAttribute.Cool: 5, SpellAttribute.Force: 2},
            cost=1,
            spellbook=water_spells
        )
        create_spell(
            name="Drench",
            element=Element.Water,
            level_req=2,
            image="icons/time_of_day_cycle.png",
            effect={SpellAttribute.Cool: 5, SpellAttribute.Force: 2},
            cost=2,
            spellbook=water_spells
        )
        create_spell(
            name="Drench",
            element=Element.Water,
            level_req=3,
            image="icons/time_of_day_cycle.png",
            effect={SpellAttribute.Cool: 5, SpellAttribute.Force: 2},
            cost=3,
            spellbook=water_spells
        )
        create_spell(
            name="Gust",
            element=Element.Wind,
            level_req=1,
            image="icons/time_of_day_cycle.png",
            effect={SpellAttribute.Force: 5},
            cost=1,
            spellbook=wind_spells
        )
        create_spell(
            name="Gust",
            element=Element.Wind,
            level_req=2,
            image="icons/time_of_day_cycle.png",
            effect={SpellAttribute.Force: 5},
            cost=2,
            spellbook=wind_spells
        )
        create_spell(
            name="Gust",
            element=Element.Wind,
            level_req=3,
            image="icons/time_of_day_cycle.png",
            effect={SpellAttribute.Force: 5},
            cost=3,
            spellbook=wind_spells
        )
        spellbooks.extend([water_spells, water_spells, water_spells, water_spells, water_spells])
        water_spells.learn()
        wind_spells.learn()

