
init -900 python:
    def always_true(x):
        return True

    def get_size(d):
        d = renpy.easy.displayable(d)
        w, h = renpy.render(d, 0, 0, 0, 0).get_size()
        w, h = int(round(w)), int(round(h))
        return w, h

    def proportional_scale(img, maxwidth, maxheight):
        currentwidth, currentheight = get_size(img)
        xscale = float(maxwidth) / float(currentwidth)
        yscale = float(maxheight) / float(currentheight)

        if xscale < yscale:
            minscale = xscale
        else:
            minscale = yscale

        return im.FactorScale(img,minscale,minscale)

    def show_stat_gain(value: int, name: str):
        sign = '+' if value > 0 else '-'
        msg = f'{sign}{value} {name}'
        show_fading_msg(msg)

    def show_fading_msg(msg: str):
        pass # TODO: Learn how to do this
