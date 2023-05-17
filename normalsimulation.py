import random
from queue import Queue


def main():
    # Parameters
    n = 1000
    order_time = 3
    arrival_chance = 0.75
    server_num = 2
    balk_chance = 0.1

    # Simulation
    def simulate():
        # Auxiliary storage
        q = Queue()
        q_size = 0
        servers = []
        q_length_arr = [0, 0]
        customers_served = 0

        # Initialize the server array (to take each customer)
        for i in range(server_num):
            servers.append(0)

        # Simulate
        for i in range(n):
            r = random.random() # Probability for arriving customer
            if r < arrival_chance:
                q.put(order_time)
                q_size += 1
                
            # Serve customers
            for j in range(server_num):
                # If the server is processing the order
                if servers[j] > 0:
                    servers[j] -= 1
                    # If the order is done
                    if servers[j] == 0: 
                        customers_served += 1
                # If the server is free and there is a customer in the queue
                elif servers[j] == 0 and not q.empty():
                    servers[j] = 0
                    servers[j] += q.get()
                    q_size -= 1
            
            b = random.random() # Probability for balk
            # Look into each customer in the queue
            for j in range(q_size):
                if b < balk_chance:
                    q.get()
                    q_size -= 1
            # Update the queue length array
            if q_size > len(q_length_arr)-1:
                q_length_arr.append(0)
            q_length_arr[q_size] += 1

        print(f'Queue length distribution: {q_length_arr}')
        print(f'Number of customers served: {customers_served}')

    for i in range(10):
        simulate()

if __name__ == "__main__":
    main()