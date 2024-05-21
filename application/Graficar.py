import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import io
import urllib, base64
from math import *

class Graficas:

    def __init__(self):
        self.function_text = "x^2"
        self.grid = False
        self.x_axis_domain = [-7, 7]
        self.y_axis_domain = [None, None]

    def set_function_text(self, function_text):
        self.function_text = function_text

    def toggle_grid(self):
        self.grid = not self.grid

    def set_x_axis_domain(self, domain):
        self.x_axis_domain = domain

    def set_y_axis_domain(self, domain):
        self.y_axis_domain = domain

    def graph_function(self):
        intervalo = np.arange(self.x_axis_domain[0], self.x_axis_domain[1], 0.1)
        y = [eval(self.function_text, {'x': x, 'log': log, 'sin': sin}) for x in intervalo]

        fig, ax = plt.subplots()

        ax.plot(intervalo, y, color='#6F42C1')
        ax.grid(self.grid, lw=0.5, color='gray')
        ax.axhline(0, color='black', linewidth=1)
        ax.axvline(0, color='black', linewidth=1)
        ax.text(0, max(y), 'Y', ha='center', va='center', fontweight='bold')
        ax.text(max(intervalo), 0, 'X', ha='center', va='center', fontweight='bold')

        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        string = base64.b64encode(buf.read())

        img_uri = 'data:image/png;base64,' + urllib.parse.quote(string)

        plt.close('all')

        return img_uri
