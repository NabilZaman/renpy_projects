
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
