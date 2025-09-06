"""
Module: trigonometric_signals.py
Purpose: Generate Basic trigonometric signals (sine, cosine, exponential)
Author: Tejas Vadgama K.
"""

import numpy as np # import numpy Library as a np
import matplotlib.pyplot as plt#import matplotlib Library as a plt


"""
Here I Take Variable as a:
Amplitude ----> amp
Frequency ----> Freq
time_array ---> t
sine_wave Variable ---> Sine For As a Variable.

"""
def sine_wave(amp, freq, phase, t):#Create THe Function and Take value And Return The Sine_Wave.
    
    sine = amp * np.sin(2 * np.pi * freq * t + phase) # Apply the Formula For the Generating The Sine Wave.

    # Plot the sine wave
    plt.plot(t, sine, color='blue')# Print The Sine Wave of the 
    plt.title("Sine Wave Signal")#Graph Name here.
    plt.xlabel("Time (s)")# On X axis Time Taken.
    plt.ylabel("Amplitude")# on Y axis Amplitude Taken.
    plt.grid(True)# Grid Display in the Graph.
    plt.show() #Display the Graph.
    
    return sine 

def cosine_wave(amp, freq, phase, t):
    """
    Generate a cosine wave signal With Define Variables.
    Amplitude ----> amp
    Frequency ----> Freq
    time_array ---> t
    cosine_wave Variable ---> Sine For As a Variable.
    """
    # Apply the formula to generate the cosine wave
    cosine = amp * np.cos(2 * np.pi * freq * t + phase)  # Use cosine formula For Generate the Wave.

    # Plot the cosine wave
    plt.plot(t, cosine, color='Red')  # Draw the cosine wave in green
    plt.title("Cosine Wave Signal")# Set the title of the graph
    plt.xlabel("Time (s)")# Label X-axis as Time
    plt.ylabel("Amplitude")# Label Y-axis as Amplitude
    plt.grid(True)# Add a grid for easy reading
    plt.show()# Display the graph

    return cosine

def exponential_signal(amp, alpha, t):
    """
    Generate an exponential signal.
    Amplitude ----> amp
    time_array ---> t
    """
    # Apply the formula to generate the exponential signal
    exp_signal = amp * np.exp(alpha * t)  # Exponential formula: A * e^(alpha * t)

    # Plot the exponential signal
    plt.plot(t, exp_signal, color='Green')  # Draw the exponential wave in red
    plt.title("Exponential Signal")       # Set the title of the graph
    plt.xlabel("Time (s)")                # Label X-axis as Time
    plt.ylabel("Amplitude")               # Label Y-axis as Amplitude
    plt.grid(True)                        # Add a grid for better visualization
    plt.show()                            # Display the graph

    return exp_signal