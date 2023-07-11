import simpy
import random


# Define the student arrival process
def student_arrival(env, server):
    i = 0
    while True:
        yield env.timeout(random.expovariate(1.0 / 5))
        i += 1
        env.process(student_service(env, 'Student %d' % i, server))


# Define the student service process
def student_service(env, student, server):
    arrival_time = env.now
    print(f"The {student} arrived at minute {round(arrival_time)}")
    with server.request() as request:
        yield request
        yield env.timeout(random.expovariate(1.0 / 7))  # service time of 7 minutes
        print(f"The {student} spent {round(env.now - arrival_time)} minutes in the system ")


# Set up the environment and run the simulation
env = simpy.Environment()
server = simpy.Resource(env, capacity=1)
env.process(student_arrival(env, server))
env.run(until=60)
