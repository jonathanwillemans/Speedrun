import json
import time
import pyautogui
import keyboard  # Import the keyboard module
from datetime import datetime, timedelta


def is_darkblue():
    try:
        target_color = (0, 17, 74)
        tolerance_range = 10
        
        # Set the game resolution (replace with your actual game resolution)
        game_resolution = (640, 480)

        # Calculate the coordinates based on the game resolution
        x_coord = int(game_resolution[0] * 0.515625)
        y_coord = int(game_resolution[1] * 0.435185185)

        # Get the pixel color at the calculated coordinates
        pixel_color = pyautogui.pixel(x_coord, y_coord)


        # Check if the pixel color is within the tolerance range
        return all(target - tolerance <= actual <= target + tolerance for actual, target, tolerance in zip(pixel_color, target_color, (tolerance_range, tolerance_range, tolerance_range)))
    except OSError:
        print("error")
        return is_darkblue()
        
    
def wait_for_start():
    print("Waiting for start...")
    while not is_darkblue():
        time.sleep(0.2001)
    return time.time()

def order_by_time(speedrun_data):
    r = []

    for i in speedrun_data:
        r.append({"key": i["key"], "action": "press", "time": i["pressed"]})
        r.append({"key": i["key"], "action": "release", "time": i["released"]})

    # Filter out entries with None values for 'time'
    r = filter(lambda x: x['time'] is not None, r)

    # Sort the list of dictionaries based on the 'time' key
    r = sorted(r, key=lambda x: x['time'])

    return r


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
    for i in speedrun_data:
        
        if i["action"] == "press":
            time.sleep(start_time + i["time"] - time.time())
            keyboard.press(i["key"])
        else:
            time.sleep(start_time + i["time"] - time.time())
            keyboard.release(i["key"])
            

def main():
    with open("C:\\Users\\jonat\\Downloads\\Speedrun\\speedrun4.json", "r") as json_file:
        speedrun_data = json.load(json_file)
    speedrun_data = reformat(speedrun_data)
    speedrun_data = order_by_time(speedrun_data)

    start = wait_for_start()
    play_data(speedrun_data, start_time=start)

if __name__ == "__main__":
    main()
    print("DONE")
