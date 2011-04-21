#!/usr/bin/env python
from wavegen import *
import sys

channels = ((sine_wave(170.0, amplitude=0.1),),
            (sine_wave(178.0, amplitude=0.1),))

samples = compute_samples(channels)
write_wavefile(sys.stdout, samples)
