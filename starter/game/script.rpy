# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# Define displayables

init python:      
    from typing import Callable

    class Event:
        def __init__(self, background, label, takes_time=True):
            self.background = background
            self.label = label
            self.takes_time = takes_time

        def trigger():
            # show background
            # jump to label... call label?
            # have some side effect? maybe that will be in the label
            pass
    
    
    class Location:
        def __init__(self, name: str):
            self.name = name
            self.events = []
        
        def pop_next_event(self) -> Event:
            if self.available:
                return self.events.pop()

        def available(self):
            return bool(self.events)

    class TOD:
        time_type = int
        MORNING = 0
        AFTERNOON = 1
        NIGHT = 2
        LATE_NIGHT = 3

        TIME_SLOTS = 1
        
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
            self.locations = {}

        def add_location(self, rectangle: tuple[int, int, int, int], location: Location):
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
            def interact():
                # If the locations is somehow unavailable, don't do anything, user needs to pick another location
                if location.available():
                    event = location.pop_next_event()
                    event.trigger()
                    if event.takes_time:
                        self.cal.advance()
                        self.display_map()

        
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


        # Setup Town Map
        town_map = Map()
        town_map_morning = TimeSlotMap("town_map_select", "background_concepts/city_overview3_%s.PNG")
        town_map_afternoon = TimeSlotMap("town_map_select", "background_concepts/city_overview3_%s.PNG")
        town_map_night = TimeSlotMap("town_map_select", "background_concepts/city_overview3_%s.PNG")
        town_map.add_time_slot(TOD.MORNING, town_map_morning)
        town_map.add_time_slot(TOD.AFTERNOON, town_map_afternoon)
        town_map.add_time_slot(TOD.NIGHT, town_map_night)
        # Setup School Map
        school_map = Map()
        school_map_morning = TimeSlotMap("school_map_select", "background_concepts/school_campus_%s.PNG")
        school_map_afternoon = TimeSlotMap("school_map_select", "background_concepts/school_campus_%s.PNG")
        school_map_night = TimeSlotMap("school_map_select", "background_concepts/school_campus_%s.PNG")
        school_map.add_time_slot(TOD.MORNING, school_map_morning)
        school_map.add_time_slot(TOD.AFTERNOON, school_map_afternoon)
        school_map.add_time_slot(TOD.NIGHT, school_map_night)


# Define Screens
screen town_map_select(time_slot_map):
    imagemap:
        # auto "background_concepts/city_overview3_%s.PNG"
        auto time_slot_map.background

        hotspot (1048, 160, 82, 85) action setup(1)
        hotspot (530, 473, 85, 96) action setup(2)
        hotspot (812, 712, 86, 92) action setup(3)

screen school_map_select(time_slot_map):
    imagemap:
        # auto "background_concepts/school_campus_%s.jpg"
        auto time_slot_map.background

        hotspot (933, 431, 70, 74) action setup(4)
        hotspot (494, 230, 70, 67) action setup(5)
        hotspot (328, 644, 73, 74) action setup(6)





# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    "Here's the first statement"

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
