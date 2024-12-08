import matplotlib.pyplot as plt
import numpy as np
import random

plt.style.use('_mpl-gallery')


x = np.linspace(0, 8, 100)
y = random.randint(0, 6) + 1 * np.sin(2 * x)
x2 = np.linspace(0, 10, 25)
y2 = random.randint(0, 6) + 1 * np.sin(2 * x2)


fig, ax = plt.subplots()

ax.plot(x2, y2 + 2.5, 'x', markeredgewidth=2)
ax.plot(x, y, linewidth=2.0)
ax.plot(x2, y2 - 2.5, 'o-', linewidth=2)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(-2, 8), yticks=np.arange(-2, 8))

plt.show()

x = np.linspace(0, 2 * np.pi, 400)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()


plt.style.use('_mpl-gallery')

np.random.seed(19680801)
n = 100
rng = np.random.default_rng()
xs = rng.uniform(23, 32, n)
ys = rng.uniform(0, 100, n)
zs = rng.uniform(-50, -25, n)

# Plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.scatter(xs, ys, zs)

ax.set(xticklabels=[],
       yticklabels=[],
       zticklabels=[])

plt.show()