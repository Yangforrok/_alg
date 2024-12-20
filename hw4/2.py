import numpy as np

# 定義函數
def f(x, y, z):
    return 3 * x**2 + y**2 + 2 * z**2


num_samples = 1000000  
x_min, x_max = 0, 1    
y_min, y_max = 0, 1    
z_min, z_max = 0, 1    

x_random = np.random.uniform(x_min, x_max, num_samples)
y_random = np.random.uniform(y_min, y_max, num_samples)
z_random = np.random.uniform(z_min, z_max, num_samples)

f_values = f(x_random, y_random, z_random)

volume = (x_max - x_min) * (y_max - y_min) * (z_max - z_min)  
monte_carlo_result = np.mean(f_values) * volume

print(f"蒙地卡羅法近似積分結果：{monte_carlo_result}")
