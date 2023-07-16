import pandas as pd
import numpy as np
import random
import math
from math import sin
'''
THIS IS A SINGLE SERVER MODEL
'''
service_times = []

for i in range(40000):
    num = random.random()
    time = round((10 * (sin(num) + 1) / 2), 2)
    service_times.append(time)

np.asarray(service_times)

arrival_times = []

arrival_time = 10 * random.random()
arrival_times.append(round(arrival_time, 2))

for i in range(39999):
    arrival_time = 10 * random.random() * ((60000 - arrival_times[i]) / 60000) + arrival_times[i]
    arrival_times.append(round(arrival_time, 2))

for i in range(39999):
    arrival_times[i]

inter_arrival_times = [0]

for i in range(1, 40000):
    inter_arrival_time = round(arrival_times[i] - arrival_times[i - 1], 2)
    inter_arrival_times.append(inter_arrival_time)

service_begin_times = [arrival_times[0]]
queue_wait_times = [0.00]
service_end_times = [service_begin_times[0] + service_times[0]]

for i in range(1, 40000):
    if arrival_times[i] > service_end_times[i - 1]:
        service_begin_time = arrival_times[i]
        queue_wait_time = 0.00
    else:
        service_begin_time = service_end_times[i - 1]
        queue_wait_time = round(service_end_times[i - 1] - arrival_times[i])
    service_begin_times.append(service_begin_time)
    queue_wait_times.append(queue_wait_time)

    service_end_time = round(service_times[i] + service_begin_times[i], 2)
    service_end_times.append(service_end_time)

times_in_system = []
for i in range(40000):
    time_in_system = round(queue_wait_times[i] + service_times[i], 2)
    times_in_system.append(time_in_system)

server_idle_times = [0]

for i in range(1, 40000):
    if arrival_times[i] > service_end_times[i - 1]:
        server_idle_time = round(arrival_times[i] - service_end_times[i - 1],2)
    else:
        server_idle_time = 0.00
    server_idle_times.append(server_idle_time)

ss = pd.DataFrame(
    {'service_time': service_times, 'arrival_time': arrival_times, 'inter_arrival_time': inter_arrival_times,
     'time_service_begins': service_begin_times, 'queue_wait_time': queue_wait_times,
     'time_service_ends': service_end_times, 'time_in_system': times_in_system, 'server_idle_time': server_idle_times})
ss.head()
ss.to_csv('admission_data.csv')

average_waiting_time = ss['queue_wait_time'].mean()
average_idle_server_time = ss['server_idle_time'].mean()
average_service_time = ss['service_time'].mean()
average_inter_arrival_time = ss['inter_arrival_time'].mean()
average_time_in_system = ss['time_in_system'].mean()

print(f"The average waiting time is: {round(average_waiting_time,2)}")
print(f"The average idle server time is: {average_idle_server_time}")
print(f"The average service time is: {round(average_service_time, 2)}")
print(f"The average inter arrival time is:{round(average_inter_arrival_time, 2)}")
print(f"The average time a customer spent in the system: {round(average_time_in_system, 2)}")