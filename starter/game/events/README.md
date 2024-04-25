
All events should go in files in this folder.

## What does an event look like?

An event is made up of two things:

1. a label that holds the content of what happens (who says what
plus any gameplay-affecting side effects like skill increases or money)
2. an Event object that references that label


## Where do events go

An event should be stored in a simple list that contains it at all events that
can be encountered at the same location.

Generally this list can be defined at the top of a file like

```
define my_events_list = []
```

## What should go in my event label

The core of the event logic and narrative all go within this label.

However there are two requirements for a label representing an event:
1. It must take a single argument. This argument will be a callback function to execute to return the control back to the context which called the event label to begin with.
2. It should execute the provided callback function at the end of the label in a python statement.

Otherwise the label should contain the text and images needed to communicate the narrative of the event you're writing.

Your label should also apply any side effects like setting flags and updating the game state as necessary.


## How should I create an event object

The setup of creating and registering an event can be done manually, however
it's reccomended to use the provided convenience function `create_contained_event`.

This funciton takes the container defined above and then the rest of the parameters match the
`Event` constructor.

For example:
```
label my_event(callback):
  ...

init python:
  create_contained_event(my_events_list, "my_event", takes_time=True, reuse=False)
```

One last thing to note that while creating the event you may want to add a condition funciton to the event.

A condition funciton determines whether the event should be available to play. Some events may only unlock later in the game or if the player's stats meet certain requirements.
This funciton take a single argument that is the game state and returns a boolean.

You can define this in the same `init python` block as the event. For example

```
init python:
  def condition(state: StateManager) -> bool:
    return state.money > 20
  create_contained_event(my_events_list, "my_event", takes_time=True, reuse=False, priority=0, condition=condition)
```

