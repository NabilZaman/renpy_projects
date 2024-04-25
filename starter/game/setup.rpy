
# Setup Town map
default town_map = Map("Town", "town_map_select")
default town_map_morning = TimeSlotMap("background_concepts/city_overview3_%s.PNG")
default town_map_afternoon = TimeSlotMap("background_concepts/city_overview3_%s.PNG")
default town_map_night = TimeSlotMap("background_concepts/city_overview3_%s.PNG")

# Setup School map
default school_map = Map("Campus", "school_map_select")
default school_map_morning = TimeSlotMap("background_concepts/school_campus_%s.jpg")
default school_map_afternoon = TimeSlotMap("background_concepts/school_campus_%s.jpg")
default school_map_night = TimeSlotMap("background_concepts/school_campus_%s.jpg")

# Setup locations and events
default market_morning = Location("Market", "market_background", events=market_events)
default campus_entrance = Location("School Gates", "color_black")
default campus_exit = Location("Path to Town", "color_black")


default state = StateManager()

label setup:
    python:
        # Setup Locations
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

        state.set_map(school_map) # The first map will be the school map.


    return
