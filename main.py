import simpy
import random

# Parameters
avg_interarrival_time = 5.0  # minutes
arrival_rate = 1.0 / avg_interarrival_time
avg_service_time = 8.0  # minutes
service_rate = 1.0 / avg_service_time
num_students = 400
service_duration = 8 * 60  # 8 hours


def student_arrivals(env, servers, queue_capacity):
    for i in range(num_students):
        if servers.count + len(servers.queue) < queue_capacity:
            service_time = random.expovariate(service_rate)
            yield env.process(student(env, servers, service_time))
        yield env.timeout(random.expovariate(arrival_rate))


def student(env, servers, service_time):
    arrival_time = env.now
    with servers.request() as req:
        yield req
        yield env.timeout(service_time)
        waiting_times.append(env.now - arrival_time)


optimal_conditions = {
    'num_servers': None,
    'queue_capacity': None,
    'avg_waiting_time': float('inf'),
    'num_days': float('inf')
}

for num_servers in range(2, 7):
    for queue_capacity in range(60, 101):
        waiting_times = []
        env = simpy.Environment()
        servers = simpy.Resource(env, num_servers)
        env.process(student_arrivals(env, servers, queue_capacity))
        env.run(until=num_students / arrival_rate)
        avg_waiting_time = sum(waiting_times) / len(waiting_times)
        num_days = int(env.now // service_duration) + 1
        if avg_waiting_time < optimal_conditions['avg_waiting_time']:
            optimal_conditions = {
                'num_servers': num_servers,
                'queue_capacity': queue_capacity,
                'avg_waiting_time': avg_waiting_time,
                'num_days': num_days
            }

print('Optimal conditions:')
print('Number of servers:', optimal_conditions['num_servers'])
print('Queue capacity:', optimal_conditions['queue_capacity'])
print('Average waiting time:', round(optimal_conditions['avg_waiting_time'], 2), 'minutes')
print('Service days:', optimal_conditions['num_days'])
