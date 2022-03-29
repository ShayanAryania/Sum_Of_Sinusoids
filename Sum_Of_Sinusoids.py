#FourierSeries(Part 1 (Sum Of Two Sinusoids))
#ShayanAryania

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

#Time Domain
Time = np.arange(1, 20, 0.01)

#First Signal
Frequency1 = 1 #hz
S1 = np.sin( Frequency1 * np.pi * Time )

#Second Signal
Frequency2 = 2 #hz
S2 = np.sin( Frequency2 * np.pi * Time )

#Sum Of Signals
S3 = S1 + S2


#Plotting The Signal
fig, axs = plt.subplots(3)
axs[0].plot(Time,S1,"blue")
axs[1].plot(Time,S2,"red")
axs[2].plot(Time,S3,"purple")
plt.show()