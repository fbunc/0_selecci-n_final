
"""
manim -pql test.py --disable_caching

"""
import pandas as pd
import sympy as sp
import mpmath as mp 
import numpy as np
from scipy.fft import fft, ifft
from latex2sympy2 import latex2sympy, latex2latex
from manim import *
import calendar
import random
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import image
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation, FFMpegWriter
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.recorder import RecorderService
from manim_voiceover.services.gtts import GTTSService
import warnings
warnings.filterwarnings("ignore")
config.media_width = "100%"
config.verbosity = "WARNING"
import compass_functions as cf
from sympy import symbols, Eq, latex, sqrt,solve ,Function 
from sympy import   I, simplify, expand , print_latex,init_printing
from sympy import Symbol, sin,cos,arg,exp ,integrate,Derivative,Integral  
from sympy.utilities.lambdify import lambdify
sp.init_printing()
from IPython.display import Markdown as md
#DSP con placa de audio 
import sounddevice as sd
# Ajustes del fondo de plot para matplotlib 
plt.rcParams.update({
        "lines.color": "black",
        "patch.edgecolor": "black",
        "text.color": "white",
        "axes.facecolor": "black",
        "axes.edgecolor": "black",
        "axes.labelcolor": "black",
        "xtick.color": "black",
        "ytick.color": "black",
        "grid.color": "gray",
        "figure.facecolor": "black",
        "figure.edgecolor": "black",
        "savefig.facecolor": "black",
        "savefig.edgecolor": "black"})



class Inicio(VoiceoverScene):
    def construct(self):
        # You can choose from a multitude of TTS services,
        # or in this example, record your own voice:
        self.set_speech_service(RecorderService())

        circle = Circle()
        square=Square()
        # Surround animation sections with with-statements:
        with self.voiceover(text="Éste es un ejemplo") as tracker:
            self.play(Create(square), run_time=tracker.duration)
            # The duration of the animation is received from the audio file
            # and passed to the tracker automatically.

        # This part will not start playing until the previous voiceover is finished.
        with self.voiceover(text="De cómo grabar tu voiceover") as tracker:
            self.play(Create(circle), run_time=tracker.duration)
            self.play(circle.animate.shift(2 * LEFT), run_time=tracker.duration)
# test=Inicio()
# test.render()
