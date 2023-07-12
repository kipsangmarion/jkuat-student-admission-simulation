# Student Admission Queuing System Simulation

## Overview

This Python code simulates the queueing process of student admissions at a university. 
It models both in-person and server-based admissions, aiming to find the optimal number of servers and queue capacity to minimize student waiting times.

The simulation is based on principles from queueing theory, using the `simpy` library to model events in the system.

## Requirements

Please ensure that the `simpy` library is installed in your Python environment. 
If not, you can install it using pip (Python package installer) by running this command in your terminal:

```bash
pip install simpy
```

## Simulation Details

The main variables and parameters in the model are:

- `avg_interarrival_time`: Average time between arrivals of students.
- `avg_service_time`: Average time it takes to serve a student.
- `num_students`: The total number of students to be served.
- `service_duration`: The duration of service in a single day (8 hours).

The simulation runs with a varying number of servers (from 2 to 6) and queue capacities (from 60 to 100). 
It calculates the average waiting time and total number of days needed to serve all students under each combination of servers and queue capacity. 
The conditions that result in the minimum average waiting time are considered the optimal conditions.

## Code Description

The code contains two key functions:

- `student_arrivals(env, servers, queue_capacity)`: This function simulates the arrivals of students to the admissions office. It continuously generates students until the total number of students (`num_students`) is reached, respecting the queue capacity limit. 

- `student(env, servers, service_time)`: This function simulates a single student being served. The student requests a server from the available servers and waits until a server is available. The waiting time for each student is calculated and stored in a list.

The main loop in the code iterates over different numbers of servers and queue capacities, running the simulation under each condition. After each run, the average waiting time and number of days required to serve all students are calculated. The conditions with the shortest average waiting time are recorded as the optimal conditions.

## Running the Simulation

To run the simulation, simply run the Python script. The output will display the optimal number of servers and queue capacity, along with the associated average waiting time and total number of days needed to serve all students.

## Assumptions

The model makes the following assumptions:

1. The calling population (students) is infinite. That is, there are always students waiting to be served.
2. Both in-person and server-based admissions are modeled as a single queue with multiple servers.
3. Students arrive following a Poisson process, with an average inter-arrival time of `avg_interarrival_time`.
4. Service times follow an exponential distribution, with an average service time of `avg_service_time`.
5. There is no priority system in the queue; all students are served in the order they arrive.

