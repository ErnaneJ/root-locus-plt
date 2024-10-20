import warnings
warnings.filterwarnings("ignore") # silence is golden

import matplotlib.pyplot as plt
import control as ctl
import numpy as np

class RootLocusPlotter:
  def __init__(self, G, H):
    """
    Initialize the RootLocusPlotter with transfer functions G and H.
    It automatically calls the plot_LGR function to plot the root locus.
    
    :param G: Transfer function G(s)
    :param H: Transfer function H(s)
    """
    self.G = G
    self.H = H
    self.plot_LGR()

  def plot_LGR(self):
    """
    Function to calculate and plot the Root Locus (LGR) of the open-loop system G(s) * H(s).
    It also prints the poles, zeros, angles, and gain information.
    """
    # Open-loop transfer function: G(s) * H(s)
    GH = self.G * self.H

    # Compute poles and zeros of the open-loop system
    poles, zeros = ctl.pzmap(GH, Plot=False)
    print(f"Poles of the open-loop system: {poles}")
    print(f"Zeros of the open-loop system: {zeros}")

    # Calculate the gain and poles for the root locus
    # gains, poles_rl = ctl.rlocus(GH, Plot=False)  # Returns the gains and poles of the LGR

    print("\nRoot Locus Analysis:")
    print(f"Number of poles: {len(poles)}")
    print(f"Number of zeros: {len(zeros)}")
    
    if len(poles) > 1:
      pole_angles = np.angle(poles, deg=True)  # Angles of the poles in degrees
      print(f"Pole angles (in degrees): {pole_angles}")

    if len(zeros) > 0:
      zero_angles = np.angle(zeros, deg=True)  # Angles of the zeros in degrees
      print(f"Zero angles (in degrees): {zero_angles}")

    # print(f"\nGains for the Root Locus: {gains}")

    plt.figure()
    ctl.rlocus(GH)
    plt.title('Root Locus (LGR)')
    plt.xlabel('Real Axis')
    plt.ylabel('Imaginary Axis')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
  # Define the transfer functions G(s) and H(s)
  num_G = [1]  # Numerator of G(s), e.g., 1
  den_G = [1, 6, 13, 10, 0]  # Denominator of G(s), e.g., s^4 + 6s^3 + 13s^2 + 10s + 0

  num_H = [1]  # Numerator of H(s), e.g., 1
  den_H = [1]  # Denominator of H(s), e.g., 1

  G = ctl.TransferFunction(num_G, den_G)
  H = ctl.TransferFunction(num_H, den_H)

  plotter = RootLocusPlotter(G, H)