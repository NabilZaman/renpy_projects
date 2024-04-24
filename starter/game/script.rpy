# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


# Define displayables

init python:      
    from typing import Callable, Iterable

    Rectangle = tuple[int, int, int, int]

    class Event:
        def __init__(self, label: str, takes_time=True, reuse=False):
            self.label = label
            self.takes_time = takes_time
            self.reuse = reuse

        def trigger(self):
            context = EventContext(self)
            store.quick_menu = True
            renpy.call(self.label, context)
            # All custom logic and side-effects take place in label
    

    class EventContext:
        def __init__(self, event: Event):
            self.event = event

        def __call__(self):
            global state
            state.post_event(self)
    
    class Location:
        def __init__(self, name: str, background: str):
            self.name = name
            self.background = background
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
        
        def on_hover(self):
            renpy.show_screen("location_tooltip", self, renpy.get_mouse_pos())
            renpy.restart_interaction()
        
        def off_hover(self):
            renpy.hide_screen("location_tooltip")
            renpy.restart_interaction()


    class TOD:
        time_type = int
        MORNING = 0
        AFTERNOON = 1
        NIGHT = 2
        LATE_NIGHT = 3

        TIME_SLOTS = 3
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
        def __init__(self, background: str):
            self.background = background
            self.locations: dict[Rectangle, Location] = {}

        def add_location(self, rectangle: Rectangle, location: Location):
            self.locations[rectangle] = location


    class Map:
        """An (interactable) game map that evolves with time."""
        def __init__(self, name: str, screen_name: str):
            self.name = name
            self.screen = screen_name
            self._time_slots: dict[TOD.time_type, TimeSlotMap] = {}
        
        def add_time_slot(self, tod: TOD.time_type, timeSlotMap: TimeSlotMap) -> None:
            self._time_slots[tod] = timeSlotMap
        
        def get_map_for_time(self, tod: TOD.time_type) -> TimeSlotMap:
            return self._time_slots.get(tod)

        def add_location_for_times(self, rect: Rectangle, location: Location, times: Iterable[TOD.time_type]):
            for tod in times:
                self.get_map_for_time(tod).add_location(rect, location)


    class StateManager:
        def __init__(self):
            self.cal = Calendar()
            self.cur_map: Map = None
            self.stats = {}
            self.money = 100
            self.freeze_capacity = 0
            self.freezes_consumed = 0
        
        def get_cur_time_map(self) -> TimeSlotMap:
            if self.cur_map is None:
                renpy.notify("No map!")
                return None
            return self.cur_map.get_map_for_time(self.cal.time_of_day)

        def display_map(self) -> None:
            if self.cur_map is None:
                return
            cur_time_map = self.get_cur_time_map()
            store.quick_menu = False
            renpy.call_screen(self.cur_map.screen, self.get_cur_time_map())
        
        def set_map(self, map: Map):
            self.cur_map = map
        
        @property
        def freezes_available(self) -> int:
            return self.freeze_capacity - self.freezes_consumed

        def refresh_freezes(self) -> None:
            self.freezes_consumed = 0

        def setup_map_interaction(self, location: Location) -> Callable[[], bool]:
            def interact():
                # If the locations is somehow unavailable, don't do anything, user needs to pick another location
                if location.available():
                    event = location.pop_next_event()
                    renpy.show(location.background)
                    location.off_hover()
                    event.trigger()
                    if event.takes_time:
                        self.cal.advance()
                    self.display_map()
            return interact

        def post_event(self, context):
                if context.event.takes_time:
                    self.cal.advance()
                self.display_map()

        
        def freeze(self) -> None:
            # renpy.notify(f"Freezing!! {self.freeze_capacity - self.freezes_consumed}")
            renpy.restart_interaction()
            # If already frozen, unfreeze
            if self.is_frozen():
                self.do_unfreeze()
            elif self.can_freeze(): # otherwise, if we can freeze, do
                self.do_freeze()
            else: # else, we can't freeze right now
                # display some warning saying no freezes available, or just deactivate the freeze button
                pass
        
        def do_freeze(self) -> None:
            self.cal.frozen = True
            self.freezes_consumed += 1
            renpy.sound.play("effects/freeze.wav")
        
        def do_unfreeze(self) -> None:
            self.cal.frozen = False
            self.freezes_consumed -= 1
            renpy.sound.play("effects/freeze_rev.wav")

        def is_frozen(self) -> bool:
            return self.cal.frozen

        def can_freeze(self) -> bool:
            return self.freezes_consumed < self.freeze_capacity

        def setup_time_freeze_interaction(self) -> Callable[[], None]:
            return self.freeze

default preferences.show_empty_window = False
default town_map = Map("Town", "town_map_select")
default town_map_morning = TimeSlotMap("background_concepts/city_overview3_%s.PNG")
default town_map_afternoon = TimeSlotMap("background_concepts/city_overview3_%s.PNG")
default town_map_night = TimeSlotMap("background_concepts/city_overview3_%s.PNG")

default school_map = Map("Campus", "school_map_select")
default school_map_morning = TimeSlotMap("background_concepts/school_campus_%s.jpg")
default school_map_afternoon = TimeSlotMap("background_concepts/school_campus_%s.jpg")
default school_map_night = TimeSlotMap("background_concepts/school_campus_%s.jpg")

default market_morning = Location("Market", "market_background")
default general_market_event = Event("market_event", reuse=True)
default campus_entrance = Location("School Gates", "color_black")
default school_transition = Event("to_campus", takes_time=False,    reuse=True)
default campus_exit = Location("School Gates", "color_black")
default town_transition = Event("to_town", takes_time=False, reuse=True)

default state = StateManager()

define gui.dialogue_text_outlines = [(1, "#000", 0, 0)]

image market_background = Frame("background_concepts/city_overview2.webp")
image color_mauve = "#88f"
image color_black = "#000"
image time_icon = "time_icon_[TOD.TIME_NAMES[state.cal.time_of_day]]"
# image tod_label = text "foo" #Text("[TOD.TIME_NAMES[state.cal.time_of_day]]", substitute=True)

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
        text "Time Freezes Left: ":
            size 24
            outlines [(1, "#000", 0, 0)]
        for i in range(state.freezes_available):
            frame:
                background "color_black"
                xysize(25, 25)
                margin (3,3)
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


label setup:
    python:
        # Setup Locations
        market_morning.add_event(general_market_event)
        campus_entrance.add_event(school_transition)
        campus_exit.add_event(town_transition)

        # Setup Town Map
        town_map.add_time_slot(TOD.MORNING, town_map_morning)
        town_map.add_time_slot(TOD.AFTERNOON, town_map_afternoon)
        town_map.add_time_slot(TOD.NIGHT, town_map_night)
        town_map.add_location_for_times((1048, 160, 82, 85), market_morning, (TOD.MORNING, TOD.AFTERNOON, TOD.NIGHT))
        town_map.add_location_for_times((1285, 90, 65, 95), campus_entrance, (TOD.MORNING, TOD.AFTERNOON, TOD.NIGHT))

        # Setup School Map
        school_map.add_time_slot(TOD.MORNING, school_map_morning)
        school_map.add_time_slot(TOD.AFTERNOON, school_map_afternoon)
        school_map.add_time_slot(TOD.NIGHT, school_map_night)
        school_map.add_location_for_times((933, 431, 70, 74), market_morning, (TOD.MORNING, TOD.AFTERNOON, TOD.NIGHT))
        school_map.add_location_for_times((469, 818, 67, 77), campus_exit, (TOD.MORNING, TOD.AFTERNOON, TOD.NIGHT))
        
        state.freeze_capacity = 2

    return



label market_event(callback):
    "It's a beautiful day in the market."
    $ state.money += 10
    $ callback()
    return

label to_town(callback):
    python:
        state.set_map(town_map)
        if callback is not None:
            callback()
        else:
            state.display_map()
    return

label to_campus(callback):
    python:
        state.set_map(school_map)
        if callback is not None:
            callback()
        else:
            state.display_map()
    return

# The game starts here.

label start:

    call setup

    "Here's the first statement"

    "After this there will be an interactive town map"  

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # show screen calendar_display()

    call to_town(None)

    "That concludes the interactive portion of the game."

    "The end."

    # This ends the game.

    return
