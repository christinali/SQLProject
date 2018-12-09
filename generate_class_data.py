import numpy as np
import math

arr = np.random.normal(4.5, 0.3, 10)
res = []
for value in arr:
    res.append(math.floor(max(1, min(value, 5))))

print(res)
