"""
Module: unitary_signals.py
Purpose: Generate basic unit signals (Unit Step, Unit Impulse, Ramp)
Author: Tejas Vadgama K.
"""

import numpy as np
import matplotlib.pyplot as plt

# ------------------ Unit Step ------------------
#Que.1.1 - Step signal
def unit_step(n):
    """ 
    # Here signal have Generated The Unit Step Signal or Return The Array.
    # Here n is Represent The Time index Array. as For Ex - Take from -5 to 6.
    # Here n is represent the Time_Indices.
    # It's Returns Array of Unit Step signal Values.
    """
    # Here We Can Apply the Condition:
    Signal = np.array([1 if i >= 0 else 0 for i in n]) # here I  Create Array then Check In the if-else condition that n=0,1 if n>=0 else n=0 &
    # Return it, also for-in loop to check 1 by 1 value it's Takes from Array.
    
    #Now Plot the Graph Here it.
    plt.stem(n, Signal, basefmt=" ") # To Display the Signal
    plt.title("Unit Step Signal") # name of the Plot Title 
    plt.xlabel("n") # X-axis Label Name
    plt.ylabel("u[n]") # Y-axis Label Name
    plt.grid(True) # Show Grid Square lines.
    plt.show() # Show THe Graph
    
    return Signal # It's Return The Numpy Array... in the Terminal

# ------------------ Unit Impulse ------------------
#Que 1.2 -impulse Signal
def unit_impulse(n):
    """
    - Here We Generate The Unit_impulse Signal .
    - Also same n represent Time_indices.
    - now signal impulse value.
    Logic: 
    - if Value >= 0 -> 1 else it's 0
    """
    #Here Apply The Condition For the Impulse Signal.
    signal = np.array([1 if t==0 else 0 for t in n]) #Check The if t==0 then only value is 1 else is 0 value in the Array.

        # Plot the signal
    plt.stem(n, signal, basefmt=" ") # display the Graph For the Digital Value.
    plt.title("Unit Impulse Signal") # Give The Title here of The Graph
    plt.xlabel("Time Index (n)")# Array Index on X-Axis.
    plt.ylabel("Amplitude δ[n]")# Delta[n] on the y-Axis.
    plt.grid(True) # Apply the Grid To Indetify and Understand.
    plt.show()# show The Plot.
    
    return signal # Return In array of the Unit_Impulse Signal.

# ------------------ ramp_signal ------------------
#Que 1.3 -ramp signal
def ramp_signal(n):
    
    Signal = np.array([t if t >= 0 else 0 for t in n])
    # Plot the ramp signal
    plt.stem(n, Signal, basefmt=" ")# Here Put Display the Digital Value.
    plt.title("Ramp Signal")# Graph Name here.
    plt.xlabel("Time Index (n)")# Array Index on X-Axis.
    plt.ylabel("Amplitude r[n]")# Delta[n] on the y-Axis.
    plt.grid(True)# Apply the Grid To Indetify and Understand.
    plt.show()# show The Plot.

    return Signal # Return The Value in Array of the ramp signal.

    #All the 3 Given Code Done With the Logic Here.