import pandas as pd
import numpy as np
import random
from math import sin
'''
THIS IS A DUAL SERVER MODEL
'''
# Number of servers
n_servers = 2

service_times = []
for i in range(40000):
    num = random.random()
    time = round((10 * (sin(num) + 1) / 2), 2)
    service_times.append(time)

np.asarray(service_times)

arrival_times = [round(10 * random.random(), 2)]
for i in range(1, 40000):
    arrival_time = 10 * random.random() * ((60000 - arrival_times[i-1]) / 60000) + arrival_times[i-1]
    arrival_times.append(round(arrival_time, 2))

inter_arrival_times = [0]
for i in range(1, 40000):
    inter_arrival_time = round(arrival_times[i] - arrival_times[i - 1], 2)
    inter_arrival_times.append(inter_arrival_time)

service_begin_times = [[arrival_times[0]] for _ in range(n_servers)]
queue_wait_times = [[0.00] for _ in range(n_servers)]
service_end_times = [[service_begin_times[0][0] + service_times[0]] for _ in range(n_servers)]
times_in_system = [[service_times[0]] for _ in range(n_servers)]
server_idle_times = [[0] for _ in range(n_servers)]

for i in range(1, 40000):
    # Find the server that ends service earliest
    server_id = np.argmin([service_end_times[j][-1] for j in range(n_servers)])

    if arrival_times[i] > service_end_times[server_id][-1]:
        service_begin_time = arrival_times[i]
        queue_wait_time = 0.00
        server_idle_time = arrival_times[i] - service_end_times[server_id][-1]
    else:
        service_begin_time = service_end_times[server_id][-1]
        queue_wait_time = service_end_times[server_id][-1] - arrival_times[i]
        server_idle_time = 0.00

    service_end_time = round(service_times[i] + service_begin_time, 2)
    time_in_system = round(queue_wait_time + service_times[i], 2)

    service_begin_times[server_id].append(service_begin_time)
    queue_wait_times[server_id].append(queue_wait_time)
    service_end_times[server_id].append(service_end_time)
    times_in_system[server_id].append(time_in_system)
    server_idle_times[server_id].append(server_idle_time)

# Creating a separate DataFrame for each server
for i in range(n_servers):
    ss = pd.DataFrame(
        {'service_time': service_times[:len(service_begin_times[i])],
         'arrival_time': arrival_times[:len(service_begin_times[i])],
         'inter_arrival_time': inter_arrival_times[:len(service_begin_times[i])],
         'time_service_begins': service_begin_times[i],
         'queue_wait_time': queue_wait_times[i],
         'time_service_ends': service_end_times[i],
         'time_in_system': times_in_system[i],
         'server_idle_time': server_idle_times[i]
        })

    ss.to_csv(f'admission_data_server_{i}.csv')
