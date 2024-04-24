
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
