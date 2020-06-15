from random import choices
import matplotlib.pyplot as plt
import random
import LoadBalancer

types_of_users = [1,2,3]
portion_of_requests = [0.25, 0.45, 0.3]


def send_request(class_val):
    lb = LoadBalancer.RequestLoadBalancer()
    client = random.randint(0, 10000000)
    users = ['FREE USER', 'PARTIALLY-PAID USER', 'PAID USER']
    print("USER ID:", client, users[class_val - 1])
    lb.service(client, class_val)

def plot(x):
    plt.plot(range(len(x[1])), x[1], label='FREE USER')
    plt.plot(range(len(x[2])), x[2], label='PARTIALLY PAID USER')
    plt.plot(range(len(x[3])), x[3], label='PAID USER')
    plt.legend(loc='upper right')
    plt.ylabel('Resources Allocated ------>')
    plt.xlabel("Requests Made ------>")
    plt.show()

for i in range(1000):
   user_type = choices(types_of_users, portion_of_requests)
   send_request(user_type[0])

lb = LoadBalancer.RequestLoadBalancer()

plot(lb.resource_final)


