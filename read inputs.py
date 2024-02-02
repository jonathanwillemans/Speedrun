import json
import time
import pyautogui
import keyboard  # Import the keyboard module
from datetime import datetime, timedelta


def is_darkblue():
    # Function to check if the pixel color is dark blue
    target_color = (0, 17, 74)
    tolerance_range = 5
    pixel_color = pyautogui.pixel(int(pyautogui.size().width * 0.515625), int(pyautogui.size().height * 0.435185185))
    return all(target - tolerance <= actual <= target + tolerance for actual, target, tolerance in zip(pixel_color, target_color, (tolerance_range, tolerance_range, tolerance_range)))

def wait_for_start():
    print("Waiting for start...")
    while not is_darkblue():
        time.sleep(0.0001)
    return time.time()

def hold_key_down(key):

    keyboard.press(key)

def release_key(key):
    keyboard.release(key)
def reformat(speedrun_data):
    for i in range (len(speedrun_data)):
        if speedrun_data[i]["key"] == "up":
            speedrun_data[i]["key"] = "ctrl"
        elif speedrun_data[i]["key"] == "left":
            speedrun_data[i]["key"] = "shift"
        elif speedrun_data[i]["key"] == "right":
            speedrun_data[i]["key"] = "alt"
        elif speedrun_data[i]["key"] == "down":
            speedrun_data[i]["key"] = "space"
    return speedrun_data



def play_data(speedrun_data, start_time=time.time()):
    unused_data = speedrun_data
    current_time = start_time  # Get current time in seconds since the epoch

    # Convert the current time to a datetime object
    current_datetime = datetime.fromtimestamp(current_time)

    # Add 1 second to the current time
    new_datetime = current_datetime + timedelta(seconds=10)

    # Convert the new datetime back to seconds since the epoch
    new_time = new_datetime.timestamp()
    last_time = speedrun_data[-1]['pressed'] + new_time
    data_in_progress = []
    pop_items = []
    pop_items2 = []
    while time.time() <= last_time:
        for i in unused_data:
            if i["pressed"] + start_time <= time.time():
                hold_key_down(i["key"])
                data_in_progress.append(i)
                pop_items2.append(i)
            else:
                break
        for i in data_in_progress:
            if i["released"] is not None and i["released"] + start_time <= time.time():
                release_key(i["key"])
                pop_items.append(i)
        for i in pop_items:            
            data_in_progress.remove(i)
            
        pop_items = []
        for i in pop_items2:
            
            unused_data.remove(i)
        pop_items2 = []
            

def main():
    with open("C:\\Users\\jonat\\Downloads\\speedrun3.json", "r") as json_file:
        speedrun_data = json.load(json_file)
    speedrun_data = reformat(speedrun_data)
    start = wait_for_start()
    play_data(speedrun_data, start_time=start)

if __name__ == "__main__":
    main()
    print("DONE")
