"""
Earliest time to complete all deliveries
"""

def earliest_time(num_of_building, building_open_time, offload_time):
    earliest = 0
    building_open_time.sort()
    offload_time.sort(reverse=True)
    
    for i in range(num_of_building):
        earliest = max(earliest, building_open_time[i]+offload_time[i*4])     
    return earliest
    
num_of_building = 3
building_open_time = [8, 10, 6] 
offload_time = [2, 2, 3, 1, 8, 7, 4, 5, 9, 10, 23, 11]

earliest_time(num_of_building, building_open_time, offload_time)i

