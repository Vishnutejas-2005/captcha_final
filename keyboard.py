import time
from pynput import keyboard
import matplotlib.pyplot as plt

# List to store time intervals between keystrokes
time_intervals = []

# Variable to store the time of the last keystroke
last_time = None

def on_press(key):
    global last_time
    current_time = time.time()
    if last_time is not None:
        interval = current_time - last_time
        time_intervals.append(interval)
    last_time = current_time

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Plot the time intervals
plt.plot(time_intervals, marker='o')
plt.title('Time Intervals Between Keystrokes')
plt.xlabel('Keystroke Index')
plt.ylabel('Time Interval (seconds)')
plt.show()