
default top_button = (0, 0)

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

    def set_top_button(col, row):
        global top_button
        top_button = (col, row)


screen spells_menu():

    python:
        learned_spellbooks = [s for s in spellbooks if s.learned]
        x_interval = 175
        y_interval = 275
        top_book = learned_spellbooks[top_button[1]] if top_button[1] < len(learned_spellbooks) else None
        top_spell = top_book.spells[top_button[0]] if top_button[0] < len(top_book.spells) else None


    tag menu

    add HBox(Transform(menu_nav_panel_color, xsize=350), menu_main_panel_color) # The background; can be whatever

    use game_menu('Spells')

    # This should present the list of spells the player has access to.
    # It should also allow them to register their spell slots.

    fixed:
        ypos 0
        xsize 1550 xalign 1.0

        viewport:
            scrollbars "vertical"
            mousewheel True
            fixed:
                yfit True
                for row, spellbook in enumerate(learned_spellbooks):
                    for col, spell in enumerate(spellbook.spells):
                        if (col, row) != top_button or (top_book is None or top_spell is None):
                            imagebutton:
                                pos (int(x_interval * (col + 1)), int(y_interval * (row + 0.75)))
                                anchor (0.5, 0.5)
                                at zoom_on_hover
                                idle build_card_image(spellbook.card_frame, spell)
                                action NullAction()
                                hovered Function(set_top_button, col, row)
                if top_book and top_spell:
                    imagebutton: # top
                        pos (int(x_interval * (top_button[0] + 1)), int(y_interval * (top_button[1] + 0.75)))
                        anchor (0.5, 0.5)
                        at zoom_on_hover
                        idle build_card_image(top_book.card_frame, top_spell)
                        action NullAction()
                fixed: # this leaves an extra row of space for padding
                    pos(700, (len(learned_spellbooks) + 1) * y_interval)
                    xysize (0, 0)


