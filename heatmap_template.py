import matplotlib.pyplot as plt
import numpy as np
import math

x = np.random.randint(10, 50, 24)
y = np.random.randint(12, 60, 24)

fig, ax = plt.subplots()

ax.scatter(x, y)
ax.set_title('Random points')
plt.show()

grid_size = 1
h = 10

x_min = min(x)
x_max = max(x)
y_min = min(y)
y_max = max(y)

x_grid = np.arange (x_min-h, x_max + h, grid_size)
y_grid = np.arange (y_min-h, y_max + h, grid_size)
x_mesh, y_mesh = np.meshgrid(x_grid, y_grid)

#centers of each square
xc = x_mesh + (grid_size / 2)
yc = y_mesh + (grid_size/ 2)

def kde_quartic(d, h):
    dn = d / h
    P = (15/16) * (1 - dn ** 2) ** 2
    return P
    
intensity_list = []
for j in range(len(xc)):
    intensity_row = []
    for k in range(len(xc[0])):
        kde_value_list = []
        for i in range(len(x)):
            # evaluate the distance
            d = math.sqrt((xc[j][k] - x[i]) ** 2 + (yc[j][k] - y[i]) ** 2) 
            if d <= h:
                p = kde_quartic(d,h)
            else:
                p = 0
            kde_value_list.append(p)
        p_total = sum(kde_value_list)
        intensity_row.append(p_total)
    intensity_list.append(intensity_row)
    
intensity = np.array(intensity_list)
plt.pcolormesh(x_mesh, y_mesh, intensity)
plt.plot(x, y,'ro')
plt.colorbar()
plt.show()