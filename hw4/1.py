import numpy as np

def f(x, y, z):
    return 3 * x**2 + y**2 + 2 * z**2

n = 100 
x_vals = np.linspace(0, 1, n)
y_vals = np.linspace(0, 1, n)
z_vals = np.linspace(0, 1, n)

dx = dy = dz = 1 / (n - 1)  

riemann_sum = 0
for x in x_vals:
    for y in y_vals:
        for z in z_vals:
            riemann_sum += f(x, y, z) * dx * dy * dz

print(f"黎曼和法近似結果：{riemann_sum}")

