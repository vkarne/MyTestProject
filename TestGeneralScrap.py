# Contents of TestGeneralScrap.py
# -------------------------------

import math
import numpy as np
import matplotlib.pyplot as plt

mu = 5.0
sigma = 2.0
values = np.random.normal(mu, sigma, 10000)

plt.figure()
plt.plot(1,2)
plt.hist(values, 50)
plt.show()

print(math.sin(2)+math.cos(2))





