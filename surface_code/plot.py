import stim
print(stim.__version__)
import numpy as np
import pymatching
import matplotlib.pyplot as plt
import sinter
from typing import List
import os
import scipy.stats


'''
code tasks are:
                    - "repetition_code:memory"
                    - "surface_code:rotated_memory_x"
                    - "surface_code:rotated_memory_z"
                    - "surface_code:unrotated_memory_x"
                    - "surface_code:unrotated_memory_z"
                    - "color_code:memory_xyz"
'''
surface_code_circuit = stim.Circuit.generated(
    "surface_code:rotated_memory_z",
    rounds=9,
    distance=3,
    after_clifford_depolarization=0.001,
    after_reset_flip_probability=0.001,
    before_measure_flip_probability=0.001,
    before_round_data_depolarization=0.001)

fig = str(surface_code_circuit.without_noise().diagram("timeslice-svg"))
import cairosvg
# Save the SVG content to a file
with open('d:/timeslice.svg', 'w') as file:
    file.write(fig)

# Alternatively, convert and save to another format
cairosvg.svg2png(bytestring=fig, write_to='d:/timeslice.png')