import keyboard
import time
import json
import pyautogui

pressed_keys = []
start_time = None  # Houd de starttijd bij

# Define the target dark blue color with a tolerance range
target_color = (0, 17, 74)
tolerance_range = 5

def is_darkblue():
    # Get the actual pixel color at the specified position
    pixel_color = pyautogui.pixel(int(pyautogui.size().width * 0.515625), int(pyautogui.size().height * 0.435185185))
    
    # Check if the actual color is within the tolerance range of the target color
    return all(target - tolerance <= actual <= target + tolerance for actual, target, tolerance in zip(pixel_color, target_color, (tolerance_range, tolerance_range, tolerance_range)))

def wait_for_start():
    print("waiting")
    while True:
        if is_darkblue():
            return time.time()

def on_key(event):
    
    key = event.name
    current_time = time.time()


    if event.event_type == keyboard.KEY_DOWN:
        # Voeg een nieuwe entry toe als de toets voor het eerst wordt ingedrukt
        if not any(entry["key"] == key and entry["released"] is None for entry in pressed_keys):
            try:
                pressed_keys.append({
                "key": key,
                "pressed": current_time - start_time,
                "released": None
            })
            except:
                print("double clicked backspace")
    elif event.event_type == keyboard.KEY_UP:
        for key_info in pressed_keys:
            if key_info["key"] == key and key_info["released"] is None:
                key_info["released"] = current_time - start_time
                break

def save_to_json():
    print(pressed_keys)
    with open("speedrun4.json", "w") as json_file:
        json.dump(pressed_keys, json_file, indent=2)
    print("pasted")

def on_backspace(event):
    
    if event.name == "backspace" and len(pressed_keys) > 1:
        save_to_json()
        print("saved")
        # Verwijder alle hooks en leeg pressed_keys
        
        pressed_keys.clear()
        global start_time
        start_time = None
        main()

def main():
    global start_time

    if start_time is None:
        start_time = wait_for_start()
    print("wait done")

    keyboard.hook(on_key)
    keyboard.hook(on_backspace)
    keyboard.wait("esc")
if __name__ == "__main__":
    main()
