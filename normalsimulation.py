import random
import math
import fractions as f
from queue import Queue

# Parameters
n = 1000
order_time = 3
arrival_chance = 0.75
countdown = 0
server_num = 2

# Auxilary storage
q = Queue()
servers = []

# Initialize the server array (to take each customer)
for i in range(server_num):
    servers.append(0)

# Simulation
for i in range(n):
    r = random.random() # Probability for arriving customer
    if r < arrival_chance:
        q.put(order_time)
    if (q.not_empty):
        for j in range(server_num):
            if servers[j] == 0:
                servers[j] += q.get()
    
    for j in range(server_num):
        if servers[j] > 0:
            servers -= 1
