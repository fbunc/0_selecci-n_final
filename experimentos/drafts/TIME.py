from manim import *

class ComplexNumbersVideo(Scene):
    def construct(self):
        # Title
        title = Tex("A Friendly Introduction to Complex Numbers at Work").scale(0.9)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # Compass analogy
        compass_analogy = Tex("In this friendly introduction to complex numbers,")
        compass_analogy_cont = Tex("we will explore the concept using a playful analogy of a compass.")
        compass_analogy.to_edge(UP)
        compass_analogy_cont.to_edge(UP)
        compass_analogy_cont.shift(DOWN)
        self.play(Write(compass_analogy))
        self.play(Write(compass_analogy_cont))
        self.wait(1)

        # Compass number
        compass_number = Tex("To simplify notation, we introduce a \"phase-generating-number\" called the compass number.")
        compass_number_val = Tex("It can be represented as \"$e^i$\" and has the value:")
        compass_number.to_edge(UP)
        compass_number_val.to_edge(UP)
        compass_number_val.shift(DOWN)
        self.play(Write(compass_number))
        self.play(Write(compass_number_val))
        self.wait(1)

        # Compass number equation
        compass_eq = MathTex("\\Theta = e^i = \\cos(1) + i \\sin(1)").scale(0.9)
        compass_eq.next_to(compass_number_val, DOWN)
        self.play(Write(compass_eq))
        self.wait(1)

        # Compass angle
        compass_angle = Tex("Using this compass number, we can set the angle of the compass to any value between $-\\pi$ and $\\pi$.")
        compass_angle_val = Tex("Let's denote this angle as \"$\\theta$\" and represent it as the exponent of $\\Theta$:")
        compass_angle.to_edge(UP)
        compass_angle_val.to_edge(UP)
        compass_angle_val.shift(DOWN)
        self.play(Write(compass_angle))
        self.play(Write(compass_angle_val))
        self.wait(1)

        # Compass radius
        compass_radius = Tex("We also introduce the concept of the radius, denoted as \"$r$\", which represents the length from the center of coordinates to the compass's position.")
        compass_radius_cont = Tex("It can be a real number or a complex number (in the form $a + bi$), which allows us to shift the phase of $\\Theta^\\theta$:")
        compass_radius.to_edge(UP)
        compass_radius_cont.to_edge(UP)
        compass_radius_cont.shift(DOWN)
        self.play(Write(compass_radius))
        self.play(Write(compass_radius_cont))
        self.wait(1)

        # Complex numbers
        complex_numbers = Tex("Complex numbers are formally called as such due to historical reasons and the way they were discovered or invented.")
        complex_numbers_cont = Tex("The \"$i$\" used as an exponent here indicates that the argument of the exponential function ($\\exp()$) has a value of \"$i\\theta$\", where \"$i$\" represents the imaginary unit ($\\sqrt{-1}$).")
        complex_numbers.to_edge(UP)
        complex_numbers_cont.to_edge(UP)
        complex_numbers_cont.shift(DOWN)
        self.play(Write(complex_numbers))
        self.play(Write(complex_numbers_cont))
        self.wait(1)

        self.play(FadeOut(VGroup(
            title, compass_analogy, compass_analogy_cont, compass_number, compass_number_val, compass_eq,
            compass_angle, compass_angle_val, compass_radius, compass_radius_cont, complex_numbers, complex_numbers_cont
        )))

        # Circular calendar
        circular_calendar = Tex("Now, let's apply these concepts to a playful example called the \"Circular Calendar Game.\"")
        circular_calendar_val = Tex("In this game, we use a measure called \"$\\omega$\" (omega) to distribute symbols along an arc of $2\\pi$ radians, representing an integer sequence denoted as \"$k$.\"")
        circular_calendar.to_edge(UP)
        circular_calendar_val.to_edge(UP)
        circular_calendar_val.shift(DOWN)
        self.play(Write(circular_calendar))
        self.play(Write(circular_calendar_val))
        self.wait(1)

        # Example hourly data
        example_hourly = Tex("To illustrate this, let's consider the example of hourly data for random climate conditions over many years.")
        example_hourly_cont = Tex("In this discrete-time scenario, we have a main index \"$n$\" that we denote as \"$h$\" (representing the hour), \"$d$\" (representing the day), \"$m$\" (representing the month), and \"$y$\" (representing the year).")
        example_hourly.to_edge(UP)
        example_hourly_cont.to_edge(UP)
        example_hourly_cont.shift(DOWN)
        self.play(Write(example_hourly))
        self.play(Write(example_hourly_cont))
        self.wait(1)

        # Year compass
        year_compass = Tex("For this example, we consider:")
        year_eq1 = Tex("$T_y = N$")
        year_eq2 = Tex("$\\omega_y = \\frac{2\\pi}{T_y}$")
        year_compass.to_edge(UP)
        year_eq1.next_to(year_compass, DOWN)
        year_eq2.next_to(year_eq1, DOWN)
        self.play(Write(year_compass))
        self.play(Write(year_eq1))
        self.play(Write(year_eq2))
        self.wait(1)

        # Month equation
        month_eq1 = Tex("$T_m = 12$")
        month_eq2 = Tex("$\\omega_m = \\frac{2\\pi}{T_m}$")
        month_eq1.next_to(year_eq2, DOWN)
        month_eq2.next_to(month_eq1, DOWN)
        self.play(Write(month_eq1))
        self.play(Write(month_eq2))
        self.wait(1)

        # Day equation
        day_eq1 = Tex("$T_d = 31$")
        day_eq2 = Tex("$\\omega_d = \\frac{2\\pi}{T_d}$")
        day_eq1.next_to(month_eq2, DOWN)
        day_eq2.next_to(day_eq1, DOWN)
        self.play(Write(day_eq1))
        self.play(Write(day_eq2))
        self.wait(1)

        # Hour equation
        hour_eq1 = Tex("$T_h = 24$")
        hour_eq2 = Tex("$\\omega_h = \\frac{2\\pi}{T_h}$")
        hour_eq1.next_to(day_eq2, DOWN)
        hour_eq2.next_to(hour_eq1, DOWN)
        self.play(Write(hour_eq1))
        self.play(Write(hour_eq2))
        self.wait(1)

        self.play(FadeOut(VGroup(
            circular_calendar, circular_calendar_val, example_hourly, example_hourly_cont, year_compass,
            year_eq1, year_eq2, month_eq1, month_eq2, day_eq1, day_eq2, hour_eq1, hour_eq2
        )))

        # Atlas equation
        atlas_eq = Tex("Using these values, we can create compass numbers to represent the example hourly data of $N$ years as an atlas:")
        atlas_eq.to_edge(UP)
        self.play(Write(atlas_eq))
        self.wait(1)

        # Compass numbers for the year
        year_compass_numbers = Tex("$\\hat{y} = r_y \\Theta^{\\omega_y y}$")
        year_compass_numbers.next_to(atlas_eq, DOWN)
        self.play(Write(year_compass_numbers))
        self.wait(1)

        # Compass numbers for the month
        month_compass_numbers = Tex("$\\hat{m} = r_m \\Theta^{\\omega_m m}$")
        month_compass_numbers.next_to(year_compass_numbers, DOWN)
        self.play(Write(month_compass_numbers))
        self.wait(1)

        # Compass numbers for the day
        day_compass_numbers = Tex("$\\hat{d} = r_d \\Theta^{\\omega_d d}$")
        day_compass_numbers.next_to(month_compass_numbers, DOWN)
        self.play(Write(day_compass_numbers))
        self.wait(1)

        # Compass numbers for the hour
        hour_compass_numbers = Tex("$\\hat{h} = r_h \\Theta^{\\omega_h h}$")
        hour_compass_numbers.next_to(day_compass_numbers, DOWN)
        self.play(Write(hour_compass_numbers))
        self.wait(1)

        # Atlas equation
        atlas_eq2 = Tex("To obtain the atlas, we can simply add the compass numbers together:")
        atlas_eq2.next_to(hour_compass_numbers, DOWN)
        self.play(Write(atlas_eq2))
        self.wait(1)

        # Final atlas equation
        final_atlas_eq = Tex("$\\hat{A} = \\hat{y} + \\hat{m} + \\hat{d} + \\hat{h}$")
        final_atlas_eq.next_to(atlas_eq2, DOWN)
        self.play(Write(final_atlas_eq))
        self.wait(1)

        self.play(FadeOut(VGroup(
            atlas_eq, year_compass_numbers, month_compass_numbers, day_compass_numbers, hour_compass_numbers,
            atlas_eq2, final_atlas_eq
        )))

if __name__ == "__main__":
    scene = ComplexNumbersVideo()
    scene.render()
