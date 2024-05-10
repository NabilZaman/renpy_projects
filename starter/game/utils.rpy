
init -900 python:
    def always_true(x):
        return True

    def get_size(d):
        d = renpy.easy.displayable(d)
        w, h = renpy.render(d, 0, 0, 0, 0).get_size()
        w, h = int(round(w)), int(round(h))
        return w, h

    # @deprecated
    # def proportional_scale(img, maxwidth, maxheight):
    #     currentwidth, currentheight = get_size(img)
    #     xscale = float(maxwidth) / float(currentwidth)
    #     yscale = float(maxheight) / float(currentheight)

    #     if xscale < yscale:
    #         minscale = xscale
    #     else:
    #         minscale = yscale

    #     return im.FactorScale(img,minscale,minscale)

    def show_stat_gain(value: int, name: str):
        sign = '+' if value > 0 else '-'
        color = '#0f0' if value > 0 else '#f00'
        msg = f'{sign}{value} {name}'
        show_fading_msg(msg, color)

    def show_fading_msg(msg: str, text_color="#fff"):
        msg_display = Text(msg, color=text_color, outlines=[(1, "#000", 0, 0)])
        renpy.show('message', what=msg_display, at_list=[rise_and_fade])
        renpy.restart_interaction()
