from manim import *

def manim_animate_scatter(x, y, sizes, colors, markers, alpha=1.0):
    scatter_group = VGroup()

    for i in range(len(x)):
        dot = Dot([x[i], y[i], 0], fill_opacity=alpha)
        dot.scale(sizes[i])
        dot.set_color(colors[i])
        dot.set_plot_style(markers[i])
        scatter_group.add(dot)

    return scatter_group


class ScatterPlotExample(Scene):
    def construct(self):
        x = [0, 1, 2, 3, 4]
        y = [0, 1, 0, 1, 0]
        sizes = [0.5, 1, 1.5, 2, 2.5]
        colors = [BLUE, RED, GREEN, YELLOW, PURPLE]
        markers = ["o", "d", "s", "*", "x"]

        scatter_group = manim_animate_scatter(x, y, sizes, colors, markers, alpha=0.8)

        self.play(AnimationGroup(*[Create(dot) for dot in scatter_group]))
        self.wait(2)


if __name__ == "__main__":
    scene = ScatterPlotExample()
    scene.render()
