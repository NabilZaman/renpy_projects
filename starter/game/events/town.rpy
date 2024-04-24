
label market_event(callback):
    "It's a beautiful day in the market."
    $ state.money += 10
    $ callback()
    return
