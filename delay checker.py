import json
import time

def main():
    with open("C:\\Users\\jonat\\Downloads\\Speedrun\\speedrun4.json", "r") as json_file:
        speedrun_data = json.load(json_file)
    with open("C:\\Users\\jonat\\Downloads\\Speedrun\\speedrun5.json", "r") as json_file:
        program_data = json.load(json_file)
    
    total_absolute_time_difference = 0
    biggest_time_difference = 0
    smallest_time_difference = 999
    c =0

    if len(speedrun_data) != len(program_data):
        raise IndexError 

    for i in range(len(speedrun_data)):
        td = speedrun_data[i]["pressed"] - program_data[i]["pressed"]
        td = abs(td)
        total_absolute_time_difference += td
        if td > biggest_time_difference:
            biggest_time_difference =td
        elif td < smallest_time_difference:
            smallest_time_difference = td
        c+=1
    for i in range(len(speedrun_data)):
        if speedrun_data[i]["released"] is not None and program_data[i]["released"] is not None:
            
            td = speedrun_data[i]["released"] - program_data[i]["released"]
            td = abs(td)
            total_absolute_time_difference += td
            if td > biggest_time_difference:
                biggest_time_difference =td
            elif td < smallest_time_difference:
                smallest_time_difference = td
            c+=1
        else:
            print("error" , i)
    average_time_difference = total_absolute_time_difference / (c)
    print("rapport", {"total_absolute_time_difference":total_absolute_time_difference, 
                      "biggest_time_difference":biggest_time_difference, 
                      "smallest_time_difference":smallest_time_difference,
                      "average_time_difference":average_time_difference})
if __name__ == "__main__":
    main()
    print("DONE")