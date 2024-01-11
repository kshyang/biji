import sys
from statistics import mean

print("log file analysis\n")
print("=================\n")
print()

log_file = sys.argv[1]

def our_list(log_file):
    with open(log_file, 'r') as file:
        listing = [line.strip().split(',')for line in file]
    return listing

def our_enter(day_list): #to assign how many times have our cat entered the house
    time_diff_our = []
    arrived_time_ours = 0
    left_time_ours = 0
    our_cat = 0
    for i in day_list:
        if i[0] == "OURS":
            our_cat += 1
            arrived_time_ours = int(i[1])
            left_time_ours = int(i[2])
            time_diff_our.append(left_time_ours - arrived_time_ours)
        else:
            continue
    return our_cat, time_diff_our

def their_enter(day_list): #how many of other cats entered our home
    their_cat = 0
    for i in day_list:
        if i [0] == "THEIRS":
            their_cat += 1
        else:
            continue
    return their_cat

def calculate_our_duration(time_diff):
    add = sum(time_diff)
    hours = add // 60
    mins = add % 60
    return hours, mins

def output(time_diff, our_cat, their_cat, hours, mins):
    print(f"max time = {max(time_diff)}")
    print(f"min time = {min(time_diff)}")
    print(f"average time = {round(mean(time_diff))}")
    print(f"The total number of times the correct cat has entered our house = {our_cat}")
    print(f"The total number of times the incorrect cat has entered our house = {their_cat}")
    print(f"Total time inside = {hours} hours {mins} minutes")


day_list = our_list(log_file)
our_cat, time_diff = our_enter(day_list)
their_cat  = their_enter(day_list)
hours, mins = calculate_our_duration(time_diff)

output(time_diff, our_cat, their_cat, hours, mins)
