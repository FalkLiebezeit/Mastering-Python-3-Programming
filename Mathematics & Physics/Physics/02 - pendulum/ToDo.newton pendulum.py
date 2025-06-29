"""

https://www.youtube.com/watch?v=qN2UcshefrA

"""

# Animation of a Newton's Cradle (5 balls) using VPython
# pip install vpython

from vpython import *

# --- Scene setup ---
scene.title = "Newton's Cradle (5 Balls)"
scene.width = 800
scene.height = 400
scene.background = color.white

# --- Parameters ---
num_balls = 5
ball_radius = 0.2
string_length = 2.0
ball_mass = 1.0
spacing = 2.2 * ball_radius  # Slightly more than diameter to avoid overlap
origin = vector(0, 0, 0)
balls = []
strings = []
anchors = []

# --- Create anchor points and balls ---
for i in range(num_balls):
    x = (i - (num_balls - 1) / 2) * spacing
    anchor = vector(x, string_length, 0)
    anchors.append(anchor)
    ball = sphere(pos=vector(x, 0, 0), radius=ball_radius, color=color.gray(0.5), make_trail=False)
    balls.append(ball)
    string = cylinder(pos=anchor, axis=ball.pos - anchor, radius=0.02, color=color.black)
    strings.append(string)

# --- Initial conditions: lift the leftmost ball ---
balls[0].pos = anchors[0] + vector(-string_length * sin(radians(40)), -string_length * cos(radians(40)), 0)

# --- Simulation parameters ---
g = 9.81
dt = 0.005
angles = [0] * num_balls
velocities = [0] * num_balls

# Set initial angle for the first ball (others at rest)
angles[0] = radians(40)

while True:
    rate(200)
    # --- Update positions and velocities for each ball ---
    for i in range(num_balls):
        if i == 0 or i == num_balls - 1:
            # Only move the first and last balls (simple model)
            accel = -g / string_length * sin(angles[i])
            velocities[i] += accel * dt
            angles[i] += velocities[i] * dt
            # Update ball position
            balls[i].pos = anchors[i] + vector(string_length * sin(angles[i]), -string_length * cos(angles[i]), 0)
            strings[i].axis = balls[i].pos - anchors[i]

    # --- Collision detection and energy transfer (simple) ---
    # If leftmost ball reaches vertical, transfer velocity to rightmost ball
    if angles[0] < 0.01 and velocities[0] > 0:
        velocities[0] = 0
        angles[0] = 0
        velocities[-1] = velocities[0] * 0.98  # Slight energy loss
        angles[-1] = 0.01

    # If rightmost ball reaches vertical, transfer velocity to leftmost ball
    if angles[-1] > -0.01 and velocities[-1] < 0:
        velocities[-1] = 0
        angles[-1] = 0
        velocities[0] = -velocities[-1] * 0.98
        angles[0] = -0.01