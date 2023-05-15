import random
import math
import fractions as f
import matplotlib.pyplot as plt


p = []
p.append(0.5)
for i in range(5):
    p.append(p[i] / 2)

t = []
length = []
length.append(0)
for i in range(1000):
    length.append(p[i] )

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
