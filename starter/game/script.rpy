# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# Define displayables

init python:      
    from typing import Callable

    Rectangle = tuple[int, int, int, int]

    class Event:
        def __init__(self, background: str, label: str, takes_time=True, reuse=False):
            self.background = background
            self.label = label
            self.takes_time = takes_time
            self.reuse = reuse

        def trigger(self):
            renpy.show(self.background)
            renpy.call(self.label)
            # have some side effect? maybe that will be in the label
            pass
    
    
    class Location:
        def __init__(self, name: str):
            self.name = name
            self.events = []

        def add_event(self, event: Event) -> None:
            self.events.append(event)
        
        def pop_next_event(self) -> Event:
            if self.available:
                next_event = self.events.pop()
                if next_event.reuse:
                    self.add_event(next_event)
                return next_event

        def available(self):
            return bool(self.events)

    class TOD:
        time_type = int
        MORNING = 0
        AFTERNOON = 1
        NIGHT = 2
        LATE_NIGHT = 3

        TIME_SLOTS = 1
        TIME_NAMES = ['morning', 'afternoon', 'night', 'late_night']
        
        @classmethod
        def next(cls, cur_time) -> int:
            return (cur_time + 1) % cls.TIME_SLOTS


    class Calendar:
        def __init__(self):
            self.day = 1
            self.time_of_day = TOD.MORNING
            self.frozen = False
        
        def advance(self) -> None:
            if self.frozen:
                self.frozen = False
            else:
                next_time = TOD.next(self.time_of_day)
                if next_time <= self.time_of_day: #We've wrapped around so it's a new day!
                    self.day += 1
                self.time_of_day = next_time


    class TimeSlotMap:
        """An instance of a map at a particular time slot"""
        def __init__(self, name: str, background: str):
            self.name = name
            self.background = background
            self.locations: dict[Rectangle, Location] = {}

        def add_location(self, rectangle: Rectangle, location: Location):
            self.locations[rectangle] = location


    class Map:
        """An (interactable) game map that evolves with time."""
        def __init__(self):
            self._time_slots: dict[TOD.time_type, TimeSlotMap] = {}
        
        def add_time_slot(self, tod: TOD.time_type, timeSlotMap: TimeSlotMap) -> None:
            self._time_slots[tod] = timeSlotMap
        
        def get_map_for_time(self, tod: TOD.time_type) -> TimeSlotMap:
            return self._time_slots.get(tod)


    class StateManager:
        def __init__(self):
            self.cal = Calendar()
            self.cur_map: Map = None
            self.stats = {}
            self.freeze_capacity = 0
            self.freezes_consumed = 0
        
        def display_map(self):
            if self.cur_map is None:
                return
            instance_map = self.cur_map.get_map_for_time(self.cal.time_of_day)
            # call the appropriate map screen using call screen expression?
        
        def set_map(self, map: Map):
            self.cur_map = map
        
        def setup_map_interaction(self, location: Location) -> Callable[[], bool]:
            print("Putting a hotspot at location: " + str(location.name))
            def interact():
                renpy.notify("Help!")
                # If the locations is somehow unavailable, don't do anything, user needs to pick another location
                if location.available():
                    event = location.pop_next_event()
                    event.trigger()
                    if event.takes_time:
                        self.cal.advance()
                        self.display_map()
            return interact

        
        def freeze() -> None:
            # If already frozen, unfreeze
            if self.cal.frozen:
                self.cal.frozen = False
                self.freezes_consumed -= 1
            elif self.can_freeze(): # otehrwise, if we can freeze, do
                self.cal.frozen = True
                self.freezes_consumed += 1
            else: # else, we can't freeze right now
                # display some warning saying no freezes available, or just deactivate the freeze button
                pass

        def can_freeze(self) -> bool:
            return self.freezes_consumed < self.freeze_capacity

        def setup_time_freeze_interaction(self) -> Callable[[], None]:
            return self.freeze

define town_map = Map()
define town_map_morning = TimeSlotMap("town_map_select", "background_concepts/city_overview3_%s.PNG")
define town_map_afternoon = TimeSlotMap("town_map_select", "background_concepts/city_overview3_%s.PNG")
define town_map_night = TimeSlotMap("town_map_select", "background_concepts/city_overview3_%s.PNG")

define school_map = Map()
define school_map_morning = TimeSlotMap("school_map_select", "background_concepts/school_campus_%s.jpg")
define school_map_afternoon = TimeSlotMap("school_map_select", "background_concepts/school_campus_%s.jpg")
define school_map_night = TimeSlotMap("school_map_select", "background_concepts/school_campus_%s.jpg")

default market_morning = Location("Market")
image market_background = Frame("background_concepts/city_overview2.webp")
default general_market_event = Event("market_background", "market_event", reuse=True)

default state = StateManager()




# Define Screens
screen town_map_select(time_slot_map):
    imagemap:
        # auto "background_concepts/city_overview3_%s.PNG"
        auto time_slot_map.background

        for rect, loc in time_slot_map.locations.items():
            hotspot rect action state.setup_map_interaction(loc)
        # hotspot (1048, 160, 82, 85) action setup(1)
        # hotspot (530, 473, 85, 96) action setup(2)
        # hotspot (812, 712, 86, 92) action setup(3)

screen school_map_select(time_slot_map):
    imagemap:
        # auto "background_concepts/school_campus_%s.jpg"
        auto time_slot_map.background

        for rect, loc in time_slot_map.locations.items():
            hotspot rect action state.setup_map_interaction(loc)
        # hotspot (933, 431, 70, 74) action setup(4)
        # hotspot (494, 230, 70, 67) action setup(5)
        # hotspot (328, 644, 73, 74) action setup(6)


image time_icon = "time_icon_[TOD.TIME_NAMES[state.cal.time_of_day]]"


label market_event:
    "It's a beautiful day in the market."
    return

# The game starts here.

label start:

    python:
        # Setup Town Map        
        town_map.add_time_slot(TOD.MORNING, town_map_morning)
        town_map.add_time_slot(TOD.AFTERNOON, town_map_afternoon)
        town_map.add_time_slot(TOD.NIGHT, town_map_night)
        market_morning.add_event(general_market_event)
        town_map_morning.add_location((1048, 160, 82, 85), market_morning)
        school_map_morning.add_location((933, 431, 70, 74), market_morning)

        # Setup School Map
        school_map.add_time_slot(TOD.MORNING, school_map_morning)
        school_map.add_time_slot(TOD.AFTERNOON, school_map_afternoon)
        school_map.add_time_slot(TOD.NIGHT, school_map_night)

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    show time_icon

    "Here's the first statement"

    $ state.cal.time_of_day += 1

    "After this there will be an interactive town map"  

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    call screen town_map_select(town_map_morning)

    "Now there will be an interactive school map"

    call screen school_map_select(school_map_morning)

    "That concludes the interactive portion of the game."

    "The end."

    # This ends the game.

    return
