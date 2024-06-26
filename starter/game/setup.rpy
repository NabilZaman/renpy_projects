
# Setup Town map
default prologue_town_map = Map("Town", "map_select")
default prologue_town_map_afternoon = TimeSlotMap(bg_folder+"city_overview1_%s.PNG")
default prologue_town_map_evening = TimeSlotMap(bg_folder+"city_overview1_%s.PNG")

# Setup School map
default prologue_school_map = Map("Campus", "map_select")
default prologue_school_map_morning = TimeSlotMap(bg_folder+"school_campus2_%s.png")
default prologue_school_map_afternoon = TimeSlotMap(bg_folder+"school_campus2_%s.png")
default prologue_school_map_evening = TimeSlotMap(bg_folder+"school_campus2_%s.png")

#### Declare Locations ####

## School Locations ##
default dorm_room = Location("Dorm Room", "bg dorm room night", events=dorm_room_events)
default theory_class = Location("Intro Class", "bg lecture hall morning", events=magic_theory_events)
default water_class = Location("Water Class", "bg lecture hall morning", events=water_lesson_events)
default wind_class = Location("Wind Class", "bg lecture hall morning", events=wind_lesson_events)
default fire_class = Location("Fire Class", "bg lecture hall morning", events=fire_lesson_events)
default light_class = Location("Light Class", "bg lecture hall morning", events=light_lesson_events)
default life_class = Location("Life Class", "bg lecture hall morning", events=life_lesson_events)
default kinesis_class = Location("Kinesis Class", "bg lecture hall morning", events=kinesis_lesson_events)
default administration = Location("Administration", "bg admin night", events=administration_events)
default cafeteria = Location("Dining Hall", "bg black", events=cafeteria_events)
default campus_exit_morning = Location("Path to Town", "bg black",
    warning_msg="You can't go into town right now; you've got to get to class!")
default campus_exit_afternoon = Location("Path to Town", "bg black")

## Town Locations ##
default shrine = Location("Shrine", "bg shrine evening", events=shrine_events)
default adventurer_guild = Location("Adventurer's Guild", "bg guild hall", events=guild_events)
default market = Location("Market", "bg market", events=market_events)
default campus_entrance = Location("School Gates", "bg black")
default explore_town = Location("Explore Town", "bg town street afternoon", events=explore_town_events)
default dojo = Location("Dojo", "bg black", events=dojo_events, enabled=False)
default blacksmith = Location("Blacksmith", "bg black", events=blacksmith_events, enabled=False)
default fountain = Location("Fountain", "bg black", events=fountain_events, enabled=False)
default back_alley = Location("Back Alley", "bg black", events=back_alley_events, enabled=False)
default inn = Location("Inn", "bg black", events=inn_events, enabled=False)


# setup generic map handles
default town_map = prologue_town_map
default school_map = prologue_school_map

default state = StateManager()

label setup:
    python:
        # Setup Locations
        campus_entrance.add_event(school_transition)
        campus_exit_afternoon.add_event(town_transition)

        # Setup Town Map
        # can't go into town in the morning during the prologue
        prologue_town_map.add_time_slot(TOD.AFTERNOON, prologue_town_map_afternoon)
        prologue_town_map.add_time_slot(TOD.NIGHT, prologue_town_map_evening)
        prologue_town_map.add_location_for_times((1373, 46, 55, 54), campus_entrance, (TOD.AFTERNOON, TOD.NIGHT))
        prologue_town_map.add_location_for_times((618, 376, 46, 52), adventurer_guild, (TOD.AFTERNOON,))
        prologue_town_map.add_location_for_times((1431, 714, 44, 48), market, (TOD.AFTERNOON,))
        prologue_town_map.add_location_for_times((912, 649, 51, 49), explore_town, (TOD.AFTERNOON,))
        prologue_town_map.add_location_for_times((833, 783, 37, 45), dojo, (TOD.AFTERNOON,))
        prologue_town_map.add_location_for_times((165, 313, 42, 40), blacksmith, (TOD.AFTERNOON,))
        prologue_town_map.add_location_for_times((99, 773, 44, 46), fountain, (TOD.AFTERNOON,))
        prologue_town_map.add_location_for_times((1607, 302, 38, 39), back_alley, (TOD.AFTERNOON,))
        prologue_town_map.add_location_for_times((329, 634, 48, 45), inn, (TOD.AFTERNOON,))
        prologue_town_map.add_location_for_times((1711, 594, 42, 45), shrine, (TOD.AFTERNOON,))

        # Setup School Map
        prologue_school_map.add_time_slot(TOD.MORNING, prologue_school_map_morning)
        prologue_school_map.add_time_slot(TOD.AFTERNOON, prologue_school_map_afternoon)
        prologue_school_map.add_time_slot(TOD.NIGHT, prologue_school_map_evening)
        prologue_school_map.add_location_for_times((621, 307, 56, 47), theory_class, (TOD.MORNING,))
        prologue_school_map.add_location_for_times((407, 520, 68, 55), water_class, (TOD.AFTERNOON,))
        prologue_school_map.add_location_for_times((257, 709, 53, 48), wind_class, (TOD.AFTERNOON,))
        prologue_school_map.add_location_for_times((339, 919, 66, 63), fire_class, (TOD.AFTERNOON,))
        prologue_school_map.add_location_for_times((633, 972, 63, 61), light_class, (TOD.AFTERNOON,))
        prologue_school_map.add_location_for_times((1609, 683, 54, 58), life_class, (TOD.AFTERNOON,))
        prologue_school_map.add_location_for_times((675, 694, 55, 63), kinesis_class, (TOD.AFTERNOON,))
        prologue_school_map.add_location_for_times((944, 493, 54, 54), administration, (TOD.MORNING, TOD.AFTERNOON))
        prologue_school_map.add_location_for_times((1381, 703, 45, 43), cafeteria, (TOD.MORNING, TOD.AFTERNOON))
        prologue_school_map.add_location_for_times((940, 1014, 74, 63), campus_exit_morning, (TOD.MORNING,))
        prologue_school_map.add_location_for_times((940, 1014, 74, 63), campus_exit_afternoon, (TOD.AFTERNOON,))
        prologue_school_map.add_location_for_times((1572, 918, 65, 63), dorm_room, (TOD.NIGHT,))

        state.freeze_capacity = 2

        state.set_map(prologue_school_map) # The first map will be the prologue school map.
        state.event_schedule = plot_schedule

        setup_spells()


    return
