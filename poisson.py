import random
import math
import fractions as f
import matplotlib.pyplot as plt


temp = [0.5]
p = [0.5]
for i in range(5):
    # print(i)
    temp.append(temp[i] / 2)
    p.append(temp[i + 1] + p[i])
# print(temp)
# print(p)

t = []
y = [[], [], [], [], []]
status = [0.0, 0.0, 0.0, 0.0, 0.0]
for i in range(1000):
    t.append(i)
    r = random.random()
    for j in range(5):
        if r < p[j]:
            status[j] = status[j] + 1
            break
    for k in range(5):
        y[k].append(status[k] / sum(status))
        # print(y[i].append(status[k]))

print("status: " + str(status))
print("result: " + str(y))

for i in range(5):
    plt.plot(t, y[i])

plt.show()

# Hello world
# x = []
# y = [[], [], [], [], []]
#
# for i in range(1000):
#     x.append(i)
#     for j in range(5):
#         # print(j)
#         p = math.exp(-5 * i) * f.Fraction((5 * i) ** j, math.factorial(j))
#         y[j].append(p)
#
# # print("x: " + str(len(x)));
# # print("y0: " + str(len(y0)));
#
# for i in range(5):
#     p = plt.plot(x, y[i], label=str(i))
#     # print(y[i])
#
# plt.show()
