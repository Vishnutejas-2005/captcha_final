import time
import numpy as np
import matplotlib.pyplot as plt
import pyautogui

trajectory = []
change_points = []

def get_mouse_position():
    return pyautogui.position()

# Track for 5 seconds
start_time = time.time()
while time.time() - start_time < 5:
    position = get_mouse_position()
    trajectory.append(position)
    time.sleep(0.01)  # Adjust the sleep time as needed

# Convert trajectory to numpy array for easier manipulation
trajectory = np.array(trajectory)

# Plot the trajectory
plt.plot(trajectory[:, 0], trajectory[:, 1], marker='o')
plt.title('Mouse Trajectory')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.show()