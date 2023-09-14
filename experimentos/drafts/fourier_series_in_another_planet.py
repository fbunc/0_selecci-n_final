from manim import *

class AlienFourier(Scene):
    def construct(self):
        # Title
        title = Text("An alien planet's version for a").scale(0.8)
        title.to_edge(UP)
        self.play(Write(title))

        subtitle = Text(" Fourier Series Introduction").scale(0.8)
        subtitle.next_to(title, DOWN)
        self.play(Write(subtitle))

        self.wait(2)

        self.play(FadeOut(title), FadeOut(subtitle))


    def play_scene(self, text_lines):
        scene_text = []
        for line in text_lines:
            scene_text.append(Tex(line))

        for i in range(len(scene_text)):
            scene_text[i].scale(0.8)
            scene_text[i].to_edge(UP * 2)
            if i > 0:
                self.play(FadeOut(prev_text))
            self.play(Write(scene_text[i]))
            self.wait(2)
            prev_text = scene_text[i]

        self.play(FadeOut(prev_text))


scene = AlienFourier()
scene.render()
