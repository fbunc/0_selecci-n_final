from manim import *

class CustomScenes(Scene):
    def construct(self, num_scenes=3, **scenes):
        for i in range(1, num_scenes + 1):
            text = scenes.get(f"text_scene_{i}")
            equation = scenes.get(f"formula_scene_{i}")

            if text and equation:
                self.play_scene(text, equation)

    def play_scene(self, text, equation):
        # Create text and equation objects
        text_obj = Tex(text).scale(1)
        equation_obj = MathTex(equation).scale(1.2)

        # Fade in text and equation
        self.play(Write(text_obj))
        self.wait(1)
        self.play(text_obj.animate.to_edge(UP))
        self.play(Write(equation_obj))
        self.wait(2)

        # Fade out text and equation
        self.play(FadeOut(text_obj), FadeOut(equation_obj))

# Usage example
def CreateScenes(num_scenes=3, **scenes):
    # Create the Manim scene
    scene = CustomScenes()

    # Call the construct method with the provided arguments
    scene.construct(num_scenes, **scenes)

    # Configure Manim
    config.output_file = "./custom_scenes.mp4"
    config.frame_rate = 20

    # Render and save the animation as a video
    scene.render()

# Call the function with your scenes data
CreateScenes(
    num_scenes=3,
    text_scene_1="Imagine a large beam-compass  $r\\Theta^{\\theta}$",
    formula_scene_1="e^{i\\theta}=\\Theta^{\\theta}",
    text_scene_2="Imagine you also set the radius  $r$",
    formula_scene_2="e^{i2\\pi}=1",
    text_scene_3="So what about $\\phi$ ?",
    formula_scene_3="e^{i2\\pi/\\phi}=1",
    text_scene_4="Text 2 mixed with in-line LaTeX $\\phi$",
    formula_scene_4="e^{i2\\pi}=1"
)
