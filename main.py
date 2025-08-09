# main.py
# Starter template for a cartoon-style 2D animation using manim and moviepy
# This script creates a simple animated character and exports a video.

# main.py
# Animated scenes for School Safety Storyboard using manim
from manim import *

class Scene1_Approach(Scene):
    def construct(self):
        # Load new school background image
        background = ImageMobject("my/frontofschool.jpg").scale_to_fit_width(14).scale_to_fit_height(8)
        self.add(background)

        # Load car image (larger, on the road)
        car = ImageMobject("my/ipt9_kp0x_220405.png").scale(0.75).shift(RIGHT*4 + DOWN*2)
        self.play(FadeIn(car))
        self.wait(0.5)

        # Car moves left toward school
        self.play(car.animate.shift(LEFT*3.5), run_time=2)

        # Narrator text
        narration = Text("A car approaches the school...", font_size=32, color=WHITE).to_edge(DOWN)
        self.play(Write(narration))
        self.wait(2)
        self.play(FadeOut(narration), FadeOut(car))

class Scene2_Arrival(Scene):
    def construct(self):
        # Load school background image
        background = ImageMobject("my/pexels-studioideahd-22626931.jpg").scale_to_fit_width(14).scale_to_fit_height(8)
        self.add(background)

        # Load car image (PNG, smaller size, parked position)
        car = ImageMobject("my/ipt9_kp0x_220405.png").scale(0.15).shift(LEFT*1)
        self.play(FadeIn(car))

        # Narrator text
        narration = Text("...and pulls into the school parking lot.", font_size=32, color=WHITE).to_edge(DOWN)
        self.play(Write(narration))
        self.wait(2)
        self.play(FadeOut(narration))

class Scene3_Exit(Scene):
    def construct(self):
        # Load school background image
        background = ImageMobject("my/pexels-studioideahd-22626931.jpg").scale_to_fit_width(14).scale_to_fit_height(8)
        self.add(background)

        # Load car image (PNG, smaller size)
        car = ImageMobject("my/ipt9_kp0x_220405.png").scale(0.15).shift(LEFT*1)
        self.add(car)

        # Load person image
        person = ImageMobject("my/253.jpg").scale(0.2).shift(LEFT*1.5 + DOWN*0.5)
        self.wait(0.5)

        # Person appears (exits car)
        self.play(FadeIn(person))
        self.play(person.animate.shift(RIGHT*2), run_time=2)

        # Narrator text
        narration = Text("A person gets out of the car and begins walking toward the school.", font_size=28, color=WHITE).to_edge(DOWN)
        self.play(Write(narration))
        self.wait(2)
        self.play(FadeOut(narration), FadeOut(person))

# To render a scene, run:
# manim -pql main.py Scene1_Approach
# manim -pql main.py Scene2_Arrival
# manim -pql main.py Scene3_Exit
