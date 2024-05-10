
init -100 python:
    from typing import Callable, Iterable
    from enum import Enum
    from dataclasses import dataclass, asdict as data_as_dict

    Rectangle = tuple[int, int, int, int]
    Day = int
    TimeOfDay = int
    EventDT = tuple[Day, TimeOfDay]

    class Chapter(Enum):
        PROLOGUE = 0
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5

    @dataclass
    class StateCondition():
        # required state parameters
        allowed_chapters: list = None
        disallowed_chapters: list = None
        allowed_times: list = None
        disallowed_times: list = None
        allowed_days: list = None
        disallowed_days: list = None
        required_flags: list = None
        banned_flags: list = None
        custom: Callable = None

        def __call__(self, state):
            """ Determine if this condition is met based on the configured requirements. """
            success = True
            if allowed_chapters is not None:
                success = success and (state.chapter in allowed_chapters)
            if disallowed_chapters is not None:
                success = success and (state.chapter not in disallowed_chapters)
            if allowed_times is not None:
                success = success and (state.cal.time_of_day in allowed_times)
            if disallowed_times is not None:
                success = success and (state.cal.time_of_day not in disallowed_times)
            if allowed_days is not None:
                success = success and (state.cal.day in allowed_days)
            if disallowed_days is not None:
                success = success and (state.cal.day not in disallowed_days)
            if required_flags is not None:
                success = success and (all(state.flags.get(f) for f in required_flags))
            if banned_flags is not None:
                success = success and not (any(state.flags.get(f) for f in banned_flags))
            if custom is not None:
                success = success and custom(state)

            return success


    class Event:
        def __init__(self, label: str, takes_time=True, reuse=False, priority=0,
                        condition: Callable = None):
            self.label = label
            self.takes_time = takes_time
            self.reuse = reuse
            # The priority determines in what order events will occur.
            # Events with higher numeric priorities come before lower ones.
            # Ties broken arbitrarily (not random)
            self.priority = priority
            self.condition = condition
            if self.condition is None:
                self.condition = always_true

        def allowed(self, state: "StateManager") -> bool:
            return self.condition(state)

        def trigger(self):
            context = EventContext(self)
            store.quick_menu = True
            renpy.transition(dissolve)
            renpy.call(self.label, context)
            # All custom logic and side-effects take place in label


    class EventContext():
        def __init__(self, event: Event):
            self.event = event

        def __call__(self):
            renpy.call("post_event", self)


    class Location:
        def __init__(self, name: str, background: str, events: list[Event] = None,
                        warning_msg='', enabled=True):
            self.name = name
            self.background = background
            self.events = [] if events is None else events
            self.warning_msg = warning_msg
            self.enabled = enabled
            self.sort_events()

        def enable(self) -> None:
            self.enabled = True

        def sort_events(self) -> None:
            self.events.sort(key=lambda e: e.priority)

        def add_event(self, event: Event) -> None:
            self.events.append(event)
            self.sort_events()

        def available_events(self) -> list[Event]:
            global state
            return [e for e in self.events if e.allowed(state)]

        def find_next_event_index(self) -> int:
            global state
            # loop "backwards" as that is our priority order
            for i in range(len(self.events)-1, -1, -1):
                if self.events[i].allowed(state):
                    return i # return the first index we find
            return None

        def pop_next_event(self) -> Event:
            if self.available:
                index = self.find_next_event_index()
                next_event = self.events.pop(index)
                if next_event.reuse:
                    self.add_event(next_event)
                return next_event

        def available(self):
            return self.enabled and bool(self.available_events())

        def has_warning(self):
            return bool(self.warning_msg)

        def selectable(self):
            return self.available() or self.has_warning()

        def on_hover(self):
            renpy.show_screen("location_tooltip", self, renpy.get_mouse_pos())
            renpy.restart_interaction()

        def off_hover(self):
            renpy.hide_screen("location_tooltip")
            renpy.restart_interaction()


    class TOD:
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
            self.day = 0
            self.time_of_day = TOD.NIGHT
            self.frozen = False

        def advance(self) -> None:
            if self.frozen:
                # play frozen animation
                self.frozen = False
            else:
                next_time = TOD.next(self.time_of_day)
                if next_time <= self.time_of_day: #We've wrapped around so it's a new day!
                    self.day += 1
                prev_time = self.time_of_day
                self.time_of_day = next_time
                renpy.scene()
                renpy.transition(dissolve)
                renpy.show("bg black")
                renpy.call_screen("time_of_day_transition", prev_time)

        @property
        def current(self) -> EventDT:
            return (self.day, self.time_of_day)


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
            self._time_slots: dict[TimeOfDay, TimeSlotMap] = {}

        def add_time_slot(self, tod: TimeOfDay, timeSlotMap: TimeSlotMap) -> None:
            self._time_slots[tod] = timeSlotMap

        def get_map_for_time(self, tod: TimeOfDay) -> TimeSlotMap:
            return self._time_slots.get(tod)

        def add_location_for_times(self, rect: Rectangle, location: Location, times: Iterable[TimeOfDay]):
            for tod in times:
                self.get_map_for_time(tod).add_location(rect, location)


    class EventSchedule:
        def __init__(self):
            self._events: dict[EventDT, list[Event]] = defaultdict(list)

        def schedule_event(self, when: EventDT, event: Event):
            self._events[when].insert(0, event)

        def fetch_next_event(self, when: EventDT) -> Event:
            cur_events = self._events[when]
            if not cur_events:
                return

            next_event = cur_events.pop() # we always get the right-most event
            if next_event.reuse: # push it to the back of the queue
                self.schedule_event(when, next_event)

            return next_event

    class Skill:
        def __init__(self, name, learned=False):
            self.name = name
            self.learned = learned
            self.exp = 0

        def learn(self):
            self.learned = True

        @property
        def level(self):
            # TODO: Come up with a better level-curve
            return self.exp // 10

        def gain(self, value):
            show_stat_gain(value, f'{self.name} xp')
            self.exp += value

    class MagicSkill(Skill):
        pass

    class MundaneSkill(Skill):
        pass

    @dataclass
    class Status:
        max_hp: int = 100
        max_mp: int = 100
        hp: int = 100
        mp: int = 100

        def change_max_health(self, delta: int):
            show_stat_gain(delta, f'max health')
            self.max_hp += delta
            self.change_health(delta)

        def change_max_mana(self, delta: int):
            show_stat_gain(delta, f'max mana')
            self.max_mp += delta
            self.change_mana(delta)

        def change_health(self, delta: int):
            show_stat_gain(delta, f'health')
            self.hp = min(self.hp + delta, self.max_hp)

        def change_mana(self, delta: int):
            show_stat_gain(delta, f'mana')
            self.mp = min(self.mp + delta, self.max_mp)


    @dataclass
    class Stats:
        # Magical Skills
        magic_theory: MagicSkill = MagicSkill('Magic Theory')
        spiritual_affinity: MagicSkill = MagicSkill('Spiritual Affinity')
        water: MagicSkill = MagicSkill('Water')
        wind: MagicSkill = MagicSkill('Wind')
        fire: MagicSkill = MagicSkill('Fire')
        life: MagicSkill = MagicSkill('Life')
        light: MagicSkill = MagicSkill('Light')
        kinesis: MagicSkill = MagicSkill('Kinesis')
        time: MagicSkill = MagicSkill('Time')

        # Mundane Skills
        strength: MundaneSkill = MundaneSkill('Strength')
        agility: MundaneSkill = MundaneSkill('Agility')
        charisma: MundaneSkill = MundaneSkill('Charisma')
        creativity: MundaneSkill = MundaneSkill('Creativity')

        def magic_skills(self) -> list[MagicSkill]:
            result = []
            for skill in data_as_dict(self).values():
                if isinstance(skill, MagicSkill):
                    result.append(skill)
            return result

        def mundane_skills(self) -> list[MundaneSkill]:
            result = []
            for skill in data_as_dict(self).values():
                if isinstance(skill, MundaneSkill):
                    result.append(skill)
            return result

        def get_skill_by_name(self, name: str) -> Skill:
            return data_as_dict(self).get(name)


    class Flags:
        """ Used to manage /boolean/ flags in the game. """
        def __init__(self):
            self._flags: dict[str, bool] = defaultdict(bool)

        def get(self, name: str):
            return self._flags[name]

        def set(self, name: str, value: bool) -> None:
            self._flags[name] = value


    class StateManager:
        def __init__(self):
            self.cal = Calendar()
            self.cur_map: Map = None
            self.event_schedule = EventSchedule()
            self.stats = Stats()
            self.status = Status()
            self.money = 100
            self.freeze_capacity = 0
            self.freezes_consumed = 0
            self.karma = 0
            self.flags = Flags()
            self.chapter = Chapter.PROLOGUE

        def advance_state(self) -> None:
            next_event = self.event_schedule.fetch_next_event(self.cal.current)
            if next_event:
                next_event.trigger()
            else:
                self.display_map()

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
            renpy.transition(dissolve)
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
                if location.available():
                    event = location.pop_next_event()
                    renpy.scene()
                    renpy.show(location.background)
                    location.off_hover()
                    event.trigger()
                else: # display the warning
                    renpy.show_screen('warning_dialog', location.warning_msg)
                    renpy.restart_interaction()

            return interact

        def freeze(self) -> None:
            renpy.restart_interaction()
            if self.is_frozen():
                self.do_unfreeze()
            elif self.can_freeze():
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

        def change_money(self, delta: int) -> None:
            show_stat_gain(delta, 'money')
            self.money += delta

        def change_karma(slef, delta: int) -> None:
            self.karma += delta

        def change_time(self, day: Day, tod: TimeOfDay):
            self.cal.day = day
            self.cal.time_of_day = tod

    def create_contained_event(event_container: list, label: str, takes_time=True, reuse=False, priority=0,
                                condition: Callable[[StateManager], bool] = None):
        event = Event(label, takes_time, reuse, priority, condition)
        event_container.append(event)

define plot_schedule = EventSchedule()

label post_event(context):
    if context.event.takes_time:
        $ state.cal.advance()

    $ state.advance_state()

    return

