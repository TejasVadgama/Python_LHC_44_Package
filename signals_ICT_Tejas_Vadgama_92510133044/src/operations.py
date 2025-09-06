"""
Module: operations.py
Purpose: Perform basic signal operations (time shift, scale, addition, multiplication)
Author: Tejas Vadgama K.
"""

import numpy as np
import matplotlib.pyplot as plt

# ------------------ Time Shift ------------------
def time_shift(signal, t, shift):
    """
    Shift a signal in time.

    Logic:
    - Add shift value to each time index
    - Positive shift → move right, Negative shift → move left
    """
    # Create new time indices by adding shift
    shifted_time = t + shift

    # Plot original signal in blue and shifted signal in red
    plt.stem(t, signal, basefmt=" ", linefmt='b', markerfmt='bo', label='Original')
    plt.stem(shifted_time, signal, basefmt=" ", linefmt='r', markerfmt='ro', label='Shifted')
    plt.title("Time Shift Operation")      # Set the title of the graph
    plt.xlabel("Time Index (n)")           # Label X-axis as Time
    plt.ylabel("Amplitude")                # Label Y-axis as Amplitude
    plt.legend()                           # Show legend
    plt.grid(True)                         # Add grid to graph
    plt.show()                             # Display the plot

    return shifted_time, signal             # Return shifted time and original signal values

# ------------------ Time Scale ------------------
def time_scale(signal, t, scale):
    """
    Scale the time axis of a signal.

    Logic:
    - Multiply each time index by scale factor
    - scale > 1 → compress, scale < 1 → stretch
    """
    # Create new time indices by scaling
    scaled_time = t * scale

    # Plot original signal in blue and scaled signal in red
    plt.stem(t, signal, basefmt=" ", linefmt='b', markerfmt='bo', label='Original')
    plt.stem(scaled_time, signal, basefmt=" ", linefmt='r', markerfmt='ro', label='Scaled')
    plt.title("Time Scaling Operation")     # Set the title of the graph
    plt.xlabel("Time Index (n)")           # Label X-axis
    plt.ylabel("Amplitude")                # Label Y-axis
    plt.legend()                           # Show legend
    plt.grid(True)                         # Add grid
    plt.show()                             # Display the plot

    return scaled_time, signal             # Return scaled time and original signal values

# ------------------ Signal Addition ------------------
def signal_addition(signal1, signal2, t):
    """
    Add two signals point-wise.

    Logic:
    - Add the amplitude of signal1 and signal2 at each time index
    """
    # Add two signals
    added_signal = signal1 + signal2

    # Plot both signals and the resulting added signal
    plt.stem(t, signal1, basefmt=" ", linefmt='b', markerfmt='bo', label='Signal 1')
    plt.stem(t, signal2, basefmt=" ", linefmt='g', markerfmt='go', label='Signal 2')
    plt.stem(t, added_signal, basefmt=" ", linefmt='r', markerfmt='ro', label='Added Signal')
    plt.title("Signal Addition")            # Title of graph
    plt.xlabel("Time Index (n)")           # X-axis label
    plt.ylabel("Amplitude")                # Y-axis label
    plt.legend()                           # Show legend
    plt.grid(True)                         # Add grid
    plt.show()                             # Display the plot

    return added_signal                     # Return the added signal values

# ------------------ Signal Multiplication ------------------
def signal_multiplication(signal1, signal2, t):
    """
    Multiply two signals point-wise.

    Logic:
    - Multiply the amplitude of signal1 and signal2 at each time index
    """
    # Multiply two signals
    multiplied_signal = signal1 * signal2

    # Plot both signals and the resulting multiplied signal
    plt.stem(t, signal1, basefmt=" ", linefmt='b', markerfmt='bo', label='Signal 1')
    plt.stem(t, signal2, basefmt=" ", linefmt='g', markerfmt='go', label='Signal 2')
    plt.stem(t, multiplied_signal, basefmt=" ", linefmt='r', markerfmt='ro', label='Multiplied Signal')
    plt.title("Signal Multiplication")      # Title of graph
    plt.xlabel("Time Index (n)")           # X-axis label
    plt.ylabel("Amplitude")                # Y-axis label
    plt.legend()                           # Show legend
    plt.grid(True)                         # Add grid
    plt.show()                             # Display the plot

    return multiplied_signal               # Return multiplied signal values
