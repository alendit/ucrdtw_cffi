UCRDTW-cffi: Dynamic Time Warping with UCR optimizations
=========================================================

Based on [Searching and Mining Trillions of Time Series Subsequences under Dynamic Time Warping](http://www.cs.ucr.edu/~eamonn/SIGKDD_trillion.pdf) .

C implementation from [libdtw](https://github.com/b/libdtw).

Interface and tests from https://github.com/klon/ucrdtw/.

### Requirements
Python 2.7+ or 3.3+, numpy 1.8+

### Usage
```
from ucrdtw_cffi import dtw_query
import numpy as np
import matplotlib.pyplot as plt

data = np.cumsum(np.random.uniform(-0.5, 0.5, 1000000))
query = np.cumsum(np.random.uniform(-0.5, 0.5, 100))
loc, dist = _ucrdtw.ucrdtw(data, query, 0.05, True)
query = np.concatenate((np.linspace(0.0, 0.0, loc), query)) + (data[loc] - query[0])

plt.figure()
plt.plot(data)
plt.plot(query)
plt.show()
```
