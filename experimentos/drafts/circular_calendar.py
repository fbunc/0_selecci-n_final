import os
from manim import *
import calendar
import numpy as np
from colorsys import hsv_to_rgb

class CircularCalendar(Scene):
    def construct(self):
        # Get the names of the months
        months = calendar.month_name[1:]

        # Create angles for each month segment
        angles = np.linspace(0, 2 * np.pi, 13)[:-1]

        # Create a circle for each month
        circles = []
        for i, angle in enumerate(angles):
            color = hsv_to_rgb(i / 12, 1.0, 1.0)
            rgb_color = rgb_to_color(color)
            circle = Circle(radius=0.2, color=BLACK)
            circle.set_fill(color=rgb_color, opacity=1.0)
            circle.shift(1.15 * np.cos(angle) * RIGHT + 1.15 * np.sin(angle) * UP)
            text = Text(months[i], font_size=20, color=WHITE)
            text.next_to(circle, direction=OUT, buff=0.2)
            circle_with_text = Group(circle, text)
            circles.append(circle_with_text)

        # Create the title
        title = Text("Circular Calendar", font_size=40, color=WHITE)
        title.to_edge(UP)

        # Animate the circles
        self.play(Write(title))
        for circle in circles:
            self.play(Create(circle))
        self.wait(2)

        # Rotate the circles
        self.play(Rotate(circles[0], angle=2 * np.pi, run_time=2, rate_func=smooth))
        self.wait(2)

        # Scale the circles
        self.play(ScaleInPlace(circles[0], scale_factor=2, run_time=2, rate_func=smooth))
        self.wait(2)

        # Fade out the circles
        self.play(FadeOut(circles[0]), FadeOut(title))
        self.wait(1)

# # Usage example
# if __name__ == "__main__":
#     module_name = os.path.splitext(os.path.basename(__file__))[0]
#     command = f"manim -p -ql {module_name}.py {CircularCalendar.__name__}"
#     os.system(command)

# # Create and render the video
config.media_width = "100%"  # Adjust the video width (percentage of canvas)
scene = CircularCalendar()
scene.render()
