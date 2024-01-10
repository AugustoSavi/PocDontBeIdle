#!/usr/bin/env python3

from random import randint
import pyautogui, time, os, sys

running_content = "running"  # Content written when the script is running
stopping_content = "stop"    # Content written when the script is about to stop

current_directory = os.path.dirname(os.path.abspath(__file__))

# Path to the flag file
flag_file_path = os.path.join(current_directory, "script_running.flag")

# Check if the flag file exists
if os.path.exists(flag_file_path):
    # If it exists, the script is already running, so stop it
    os.remove(flag_file_path)
    sys.exit()  # Exit the script
else:
    # If the file doesn't exist, create it
    with open(flag_file_path, 'w') as file:
        file.write(running_content)

def write_stop_if_file_exists():
    if os.path.exists(flag_file_path):
        # If the file exists, write 'stop' to it
        with open(flag_file_path, 'w') as file:
            file.write(stopping_content)

def read_file_content():
    if os.path.exists(flag_file_path):
        # If the file exists, read its content
        with open(flag_file_path, 'r') as file:
            return file.read()

def should_program_continue_running():
    content = read_file_content()
    return content == running_content

def stop_program():
    if os.path.exists(flag_file_path):
        os.remove(flag_file_path)  # Ensure to remove the flag file when exiting
    sys.exit()  # Exit the script

def update_running_flag():
    global running
    if should_program_continue_running():
        running = True
    else:
        running = False
        stop_program()

running = True

try:
    while running:
        update_running_flag()
        x_init, y_init = pyautogui.position()
        time.sleep(3)
        x_after, y_after = pyautogui.position()
        if x_init == x_after and y_init == y_after:
            pyautogui.moveTo(randint(x_init - 50, x_init + 50), randint(y_init - 50, y_init + 50), 1, pyautogui.easeOutQuad)
finally:
    if os.path.exists(flag_file_path):
        os.remove(flag_file_path)  # Ensure to remove the flag file when exiting
