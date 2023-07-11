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
    with server.request() as request:
        yield request
        yield env.timeout(random.expovariate(1.0 / 7))
        print('%s served at %g minutes.' % (student, env.now - arrival_time))


# Set up the environment and run the simulation
env = simpy.Environment()
server = simpy.Resource(env, capacity=1)
env.process(student_arrival(env, server))
env.run(until=60)
