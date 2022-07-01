from delta_utils import *

"""
q = np.array([pi/2,pi/2]) #Joint configuration

#plot the robot in configuration q:
plot_box()
plot_delta(q)
plt.show()

#plot the robot in two configurations:
plot_box()
plot_delta(q)
q = np.array([2.0,0.5]) 
plot_delta(q)
plt.show()

#plot the robot and a 2d point:
q = np.array([2.0,0.5])
p = np.array([0.05,0.10]) # x-y point
plot_box()
plot_delta(q)
plt.plot(p[0],p[1],"x",markersize=20)
plt.show()
"""
plot_box()

q0 = np.linspace(0,2*np.pi,60)
q1 = np.linspace(0,2*np.pi,60)

for i in range (len(q0)):
    for j in range(len(q1)):
        q = np.array([q0[i],q1[j]])
        p = fk_delta(q)
        plt.plot(p[0],p[1],"x",markersize=20)

plt.show()

        
                   