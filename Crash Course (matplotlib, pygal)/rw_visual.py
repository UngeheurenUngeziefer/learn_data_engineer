import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Построение случайного блуждания и нанесение точек на диаграмму
rw = RandomWalk(10000)
rw.fill_walk()
plt.figure(figsize=(10, 6), dpi=128)
point_numbers = list(range(rw.num_points))
plt.scatter(rw.x_values, rw.y_values,
 s=1, c=point_numbers, cmap=plt.cm.Greens, edgecolor='None')

# plt.scatter(0, 0, c='Red', edgecolor='None', s=100)
# plt.scatter(rw.x_values[-1], rw.y_values[-1], c='Red', edgecolor='None', s=100)

plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.show()
