
init python:
    import time
    class Animation:
        def __init__(self, duration=1.0, loop=False):
            self.duration = duration
            self.loop = loop

        def execute(self, trns, progress):
            pass  # Override this

        def __call__(self, trns, t, _):
            progress = (t % self.duration) / self.duration
            self.execute(trns, progress)
            if self.loop or t < self.duration:
                return 0
            else:
                return None


    class SpinAnimation(Animation):
        def __init__(self, duration=2.0, start_angle=0, end_angle=360, loop=False):
            super().__init__(duration, loop)
            self.start_angle = start_angle
            self.end_angle = end_angle

        def execute(self, trns, progress):
            trns.rotate = self.start_angle + (self.end_angle - self.start_angle) * progress


transform spin_with_function(duration=2.0, start_angle=0, end_angle=360, loop=False):
    function SpinAnimation(duration, start_angle, end_angle, loop)


transform time_of_day_spin(duration=2.0, start_angle=0, end_angle=360, loop=False):
    rotate start_angle
    pause 0.5
    linear duration rotate end_angle
