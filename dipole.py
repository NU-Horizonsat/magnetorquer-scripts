import math
N = 100  # turns
I = 0.1  # current in Amperes
r = 0.045  # radius in meters
B = 0.00005  # Earth's magnetic field in Teslas

# coil area
A = math.pi * r ** 2

#dipole moment
m = N * I * A

# For maximum torque, theta = 90 degrees, so sin(theta) = 1
theta_degrees = 90
theta_radians = math.radians(theta_degrees)
# torque
tau = m * B * math.sin(theta_radians)

print()
print(f"Area: {A}, dipole moment: {m}, torque at {theta_degrees} degrees and {theta_radians} radians: {tau}")

print("---")
print()

# Angles between the magnetorquer's dipole moment and the Earth's magnetic field in degrees
angles_degrees = {'X-axis': 45, 'Y-axis': 60, 'Z-axis': 30}
angles_radians = {axis: math.radians(angle) for axis, angle in angles_degrees.items()}

# Calculate the torque for each magnetorquer based on the angle
torques = {axis: m * B * math.sin(angle) for axis, angle in angles_radians.items()}

print(torques)

print("---")
print()

"""
assume the moment of inertia I is the same for all axes and equals 10^-3 kg*m^2
and we apply the torque for 10 seconds (Δt=10s).
"""
# dummy values
I = 1e-3  # moment of inertia in kg*m^2
delta_t = 10  # time interval in seconds

# Calculate the change in angular velocity for each axis
delta_omega = {axis: (torque / I) * delta_t for axis, torque in torques.items()}

print(delta_omega)

