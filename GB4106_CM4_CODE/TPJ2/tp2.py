from delta_utils import *
import numpy as np

plt.figure()
plot_box()

dq = 0.5
q1s = np.arange(0., 2*np.pi, dq)
q2s = np.arange(0., 2*np.pi, dq)

for q1 in q1s:
    print(q1)
    for q2 in q2s:
        p = fk_delta(np.array([q1, q2]))
        plt.plot(p[0], p[1], "x")

c = np.array([0., 0.1])
r = 0.05
thetas = np.linspace(0, 2*np.pi, 100)
X = [c[0] + r*np.cos(theta) for theta in thetas]
Y = [c[1] + r*np.sin(theta) for theta in thetas]
plt.plot(X, Y)

plt.show()
