import numpy as np
from src import unitary_signals
from src import trigonometric_signals
from src import operations

#_______________Generate The Unit Step Signal and plot In the graph_______________ 

n = np.arange(-7, 13) # Here We Give Array Range To n variable means Time_indices and Then Call.
# Also Here take General value For all the Functions Here.

#Que.1.1 - unit_step(n) – Generates a unit step signal.
Unit_Step = unitary_signals.unit_step(n) #Then Here We Take Form the src Folder Then From File Call The Function given the n value. 
print("----- Unit Step Signal Values -------") # Print The name of Value To Identify it.
print(Unit_Step) # here print The Logic Applied Resulted Array graph also Plot here.

#Que.1.2 - unit_impulse(n) – Generates a unit impulse signal.
Unit_Impulse = unitary_signals.unit_impulse(n) # here For the n Value Take Same the Value and Call it In the Function and Put it.
print("----- Unit Impulse Signal Values -----") # Print the name To identify the Which Is it.
print(Unit_Impulse)# Here print the value of the Array In it in the array.

#Que.1.3 - ramp_signal(n) – Generates a ramp signal.
ramp_signal = unitary_signals.ramp_signal(n) # here Takes Smae n value and Give Into function called vlaue.
print("----- ramp Signal Values -----")# Print To identify the ramp signal By print.
print(ramp_signal)# Print the ramp signal Array Here.


#Que.2.1 
time = np.arange(0, 1, 0.01)

#Genreate The Sine wave By Calling the Function From the File.
Sine = trigonometric_signals.sine_wave(amp=2, freq=5, phase=0, t=time) # Take Time From the uppar Given and Call the Function Form The File.
#Display the Sne Wave With Input Value in the Function.

# Generate the cosine wave by calling the function
#Here The Time Value Is Sae Taken.
Cosine = trigonometric_signals.cosine_wave(amp=2, freq=5, phase=0, t=time)# Cosine Wave Generated Here.

# Generate the exponential signal by calling the function
#Here The Time Value Is Sae Taken.
Exponential = trigonometric_signals.exponential_signal(amp=4, alpha=0.8, t=time)

#Que.3 - operations File 
"""
Use the same n array as used for generating Unit_Step and ramp_signal
This ensures all signals and the time array have the same length
No need to redefine n
"""

# ------------------ 1. Time Shift Example ------------------
# Shift sine wave by +0.05 seconds
shifted_time, shifted_sine = operations.time_shift(Sine, time, shift=0.1)

# ------------------ 2. Time Scale Example ------------------
# Scale sine wave time axis by factor 2
scaled_time, scaled_sine = operations.time_scale(Sine, time, scale=1.5)

# ------------------ 3. Signal Addition Example ------------------
# Add unit step and ramp signal
added_signal = operations.signal_addition(Unit_Step, ramp_signal, n)

# ------------------ 4. Signal Multiplication Example ------------------
# Multiply sine and cosine signals point-wise
multiplied_signal = operations.signal_multiplication(Sine, Cosine, time)


#-------- Main Script Codes Are Now By changing it. --------
# ------------------ 1. unit step signal and a unit impulse signal of length 20 ------------------
Two = np.arange(-9, 11)

# ------------------ 2. Generate Unit Step Signal ------------------
Unit_Step = unitary_signals.unit_step(Two)
print("----- Unit Step Signal Values -----")
print(Unit_Step)  # Print the array values

# ------------------ 3. Generate Unit Impulse Signal ------------------
Unit_Impulse = unitary_signals.unit_impulse(Two)
print("----- Unit Impulse Signal Values -----")
print(Unit_Impulse)  # Print the array values


#----------- 2. sine wave of amplitude 2, frequency 5 Hz, phase 0, over t = 0 to 1 sec ------------
# t from 0 to 1 second, step 0.01
time2 = np.arange(0, 1, 0.01)

# ------------------ 2. Generate Sine Wave ------------------
Sine = trigonometric_signals.sine_wave(amp=2, freq=5, phase=0, t=time2)

#-------------- time shifting on the sine wave by +5 units and plot both original and shifted signals --------------
shifted_time, shifted_sine = operations.time_shift(Sine, time2, shift=0.05)

# ------------------ 4. addition of the unit step and ramp signal ------------------
# Add unit step and ramp signals
added_signal = operations.signal_addition(Unit_Step, ramp_signal, Two)
print("----- Added Signal (Unit Step + Ramp) -----")
print(added_signal)

# ------------------ 5. Multiply a sine and cosine wave of same frequency ------------------
# Multiply sine and cosine signals point-wise
multiplied_signal = operations.signal_multiplication(Sine, Cosine, time2)  # Multiplication