
default top_button = (0, 0)

default spell_slots = 6

define spellbook_x_interval = 175
define spellbook_y_interval = 275

init python:
    def build_card_image(frame: str, spell: Spell):
        card_text = '\n'.join(f'{attr.name}: {val}' for attr, val in spell.effect.items())
        return zoomer(0.33, Fixed(
                Fixed(
                    fit_center(Image(frame)),
                    Fixed(Frame(spell.image), pos=(21, 79), xysize=(396, 238)),
                    Text(spell.name, pos=(23, 33), yanchor=0.5, bold=True, color="#000"),
                    Text(card_text, pos=(31, 362), color="#000"),
                    Text(str(spell.cost), pos=(391, 596), anchor=(0.5, 0.5), bold=True, size=36, outlines=[(3, "#000", 2, 1)])
                ),
                xysize=(437, 642)
            ))

    def set_top_button(col, row) -> None:
        global top_button
        top_button = (col, row)

    def is_unhovered(col, row, top_book, top_spell) -> bool:
        return (col, row) != top_button# or (top_book is None or top_spell is None)

    def get_card_pos(col, row) -> tuple[int, int]:
        return (int(spellbook_x_interval * (col + 1)), int(spellbook_y_interval * (row + 0.75)))

    def toggle_spell_registry(spell: Spell, spellbook: Spellbook):
        if spell_registry.is_registered(spell):
            spell_registry.unregister(spell)
        else:
            spell_registry.register(spell, spellbook)

    def build_spell_button(spellbook, spell, do_zoom=True, hover_action=None, pos=None):
        if hover_action is None:
            hover_action = NullAction()
        kwargs = {
            'anchor': (0.5, 0.5),
            'idle_image': build_card_image(spellbook.card_frame, spell),
            'action': Function(toggle_spell_registry, spell, spellbook),
            'hovered': hover_action
        }
        if pos is not None:
            kwargs['pos'] = pos

        button = ImageButton(**kwargs)
        if do_zoom:
            button = compose(button, zoom_on_hover)
        return button

    def unregistered_spells(spellbook: Spellbook) -> list[Spell]:
        return [s for s in spellbook.spells if not spell_registry.is_registered(s)]


screen spells_menu():

    python:
        learned_spellbooks = [s for s in spellbooks if s.learned]
        top_book = None
        if top_button[1] < len(learned_spellbooks):
            top_book = learned_spellbooks[top_button[1]]
        top_spell = None
        if top_book is not None and top_button[0] < len(unregistered_spells(top_book)):
            top_spell = unregistered_spells(top_book)[top_button[0]]

    tag menu

    add HBox(Transform(menu_nav_panel_color, xsize=350), Frame("bg_menu")) # The background; can be whatever

    use game_menu('Spells')

    # This should present the list of spells the player has access to.
    # It should also allow them to register their spell slots.

    fixed:
        ypos 0
        xsize 1550 xalign 1.0

        frame:
            background Frame("bg_menu_content")
            ypos 10
            xysize (1530, 800)
            # text f"{top_button}: ({top_book}, {top_spell.name} {top_spell.cost})"
            vbox:
                spacing 30
                viewport:
                    xysize (1530, 800)
                    scrollbars "vertical"
                    vscrollbar_unscrollable "hide"
                    mousewheel True
                    fixed:
                        # xysize (1200, 1200)
                        yfit True
                        for row, spellbook in enumerate(learned_spellbooks):
                            for col, spell in enumerate(unregistered_spells(spellbook)):
                                if is_unhovered(col, row, top_book, top_spell):
                                    add build_spell_button(spellbook, spell,
                                        hover_action=Function(set_top_button, col, row),
                                        pos=get_card_pos(col, row))
                        if top_book and top_spell and not spell_registry.is_registered(top_spell):
                            add build_spell_button(top_book, top_spell,
                                pos=get_card_pos(*top_button)
                            )
                        fixed: # this leaves an extra row of space for padding
                            pos(700, (len(learned_spellbooks) + 1) * spellbook_y_interval)
                            xysize (0, 0)
                frame:
                    background Frame("bg_spell_registry")
                    xysize (1520, 230)
                    has hbox
                    xoffset 10
                    spacing 25
                    for slot in range(spell_slots):
                        if slot < len(spell_registry):
                            add build_spell_button(
                                spell_registry[slot][1], spell_registry[slot][0],
                                do_zoom=False):
                                align (0.5, 0.5)
                        else:
                            add "card_slot":
                                xysize (144, 212)
                                alpha 0.65

