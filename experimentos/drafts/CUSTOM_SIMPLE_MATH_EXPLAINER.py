from manim import *

class IntroductionToComplexNumbers(Scene):
    def construct(self):
        # Title
        title = Text("A Friendly Introduction to Complex Numbers at Work:")
        title.to_edge(UP)
        self.play(Write(title)).scale(0.8)

        subtitle = Text("Time Atlas and Compass Numbers")
        subtitle.next_to(title, DOWN)
        self.play(Write(subtitle))

        self.wait(2)

        self.play(FadeOut(title), FadeOut(subtitle))

        # Scene 1: Compass Explanation
        compass_text = [
            "In this friendly introduction to complex numbers,",
            "we will explore the concept using a playful analogy of a compass.",
            "Imagine a large beam compass used to place symbols in a two-dimensional plane.",
            "We define two parameters: the radius, denoted as \"$r$\",",
            "and the angle, denoted as \"$\\theta$\", which represents the position of the compass."
        ]
        self.play_scene(compass_text)

        # Scene 2: Compass Number Explanation
        compass_number_text = [
            "To simplify notation, we introduce a \"phase-generating-number\" called the compass number,",
            "denoted as \"$\\Theta$\". It can be represented as \"$e^i$\" and has the value:",
            "$$\\Theta = e^i = \\cos(1) + i \\sin(1)$$",
            "Using this compass number, we can set the angle of the compass to any value between $-\\pi$ and $\\pi$.",
            "Let's denote this angle as \"$\\theta$\" and represent it as the exponent of $\\Theta$:"
        ]
        self.play_scene(compass_number_text)

        # Scene 3: Compass Number Equation
        compass_number_equation = [
            "$$\\Theta^\\theta = e^{i \\theta} = \\cos(\\theta) + i \\sin(\\theta)$$",
            "We also introduce the concept of the radius, denoted as \"$r$\",",
            "which represents the length from the center of coordinates to the compass's position.",
            "It can be a real number or a complex number (in the form $a + bi$),",
            "which allows us to shift the phase of $\\Theta^\\theta$:"
        ]
        self.play_scene(compass_number_equation)

        # Scene 4: Radius Equation
        radius_equation = [
            "$$r \\Theta^\\theta \\in \\mathbb{C}$$",
            "Complex numbers are formally called as such due to historical reasons",
            "and the way they were discovered or invented.",
            "The \"$i$\" used as an exponent here indicates that the argument",
            "of the exponential function ($\\text{exp}()$) has a value of \"$i \\theta$\",",
            "where \"$i$\" represents the imaginary unit ($\\sqrt{-1}$)."
        ]
        self.play_scene(radius_equation)

        # Scene 5: Circular Calendar Game
        calendar_game_text = [
            "Now, let's apply these concepts to a playful example called the \"Circular Calendar Game\".",
            "In this game, we use a measure called \"$\\omega$\" (omega) to distribute symbols along an arc of $2\\pi$ radians,",
            "representing an integer sequence denoted as \"$k$\".",
            "The value of $\\omega$ is given by $\\omega = \\frac{2\\pi}{T_k}$,",
            "where $T_k$ represents the number of symbols we want to distribute."
        ]
        self.play_scene(calendar_game_text)

        # Scene 6: Example Scenario
        example_scenario_text = [
            "To illustrate this, let's consider the example of hourly data for random climate conditions over many years.",
            "In this discrete-time scenario, we have a main index \"$n$\" that we denote as",
            "\"$h$\" (representing the hour), \"$d$\" (representing the day), \"$m$\" (representing the month),",
            "and \"$y$\" (representing the year)."
        ]
        self.play_scene(example_scenario_text)

        # Scene 7: Example Values
        example_values_text = [
            "For this example, we consider:",
            "- The total number of years to analyze (7 years from 2023 to 2029).",
            "We imagine a mod 7 clock, ranging from 0 to 6, to represent the hourly data for each year:",
            "$$T_y = N$$",
            "$$\\omega_y = \\frac{2\\pi}{T_y}$$",
            "- The number of months in a year:",
            "$$T_m = 12$$",
            "$$\\omega_m = \\frac{2\\pi}{T_m}$$",
            "- The total number of days in a given month, represented by $T_d$.",
            "The choice of 31 as a fixed value for $T_d$ simplifies the visualization of months",
            "with 30 or 28/29 days because some slots in the mod 31 wheel will not have any hour represented:",
            "$$T_d = 31$$",
            "$$\\omega_d = \\frac{2\\pi}{T_d}$$",
            "- The total number of hours in a day:",
            "$$T_h = 24$$",
            "$$\\omega_h = \\frac{2\\pi}{T_h}$$",
            "- The total number of minutes in an hour:",
            "$$T_{\\text{min}} = 60$$",
            "$$\\omega_{\\text{min}} = \\frac{2\\pi}{T_{\\text{min}}}$$",
            "- The total number of seconds in a minute:",
            "$$T_{\\text{sec}} = 60$$",
            "$$\\omega_{\\text{sec}} = \\frac{2\\pi}{T_{\\text{sec}}}$$"
        ]
        self.play_scene(example_values_text)

        # Scene 8: Atlas Explanation
        atlas_explanation_text = [
            "Using these values, we can create compass numbers to represent the example hourly data of $N$ years as an atlas:",
            "- Compass numbers for the year:",
            "$$\\hat{y} = r_y \\Theta^{\\omega_y y}$$",
            "- Compass numbers for the month:",
            "$$\\hat{m} = r_m \\Theta^{\\omega_m m}$$",
            "- Compass numbers for the day:",
            "$$\\hat{d} = r_d \\Theta^{\\omega_d d}$$",
            "- Compass numbers for the hour:",
            "$$\\hat{h} = r_h \\Theta^{\\omega_h h}$$",
            "To obtain the atlas, we can simply add the compass numbers together:",
            "$$\\hat{A} = \\hat{y} + \\hat{m} + \\hat{d} + \\hat{h}$$"
        ]
        self.play_scene(atlas_explanation_text)

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


scene = IntroductionToComplexNumbers()
scene.render()
