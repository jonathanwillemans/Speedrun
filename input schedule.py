import json
import time
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


def main():
    with open("C:\\Users\\jonat\\Downloads\\speedrun3.json", "r") as json_file:
        speedrun_data = json.load(json_file)
    print(order_by_time(speedrun_data))
if __name__ == "__main__":
    main()
