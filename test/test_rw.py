from ucrdtw_cffi import dtw_query
import sys, os
import numpy as np
import matplotlib.pyplot as plt
import math
# plt.style.use('ggplot')


def test_rw():
    data = np.cumsum(np.random.uniform(-0.5, 0.5, 1000000)).astype(np.double)
    query = np.cumsum(np.random.uniform(-0.5, 0.5, 100)).astype(np.float)
    loc, dist = dtw_query(query, data, 0.05)

    assert loc > 0
    assert dist > 0

    # query = np.concatenate((np.linspace(0.0, 0.0, loc), query)) + (data[loc] - query[0])
    # plt.figure()
    # plt.plot(data)
    # plt.plot(query)
    # plt.show()

def test_sin():
    data = np.cos(np.linspace(0.0, math.pi * 6, 600)) + (np.random.uniform(-0.5, 0.5, 600) / 10)
    query = np.sin(np.linspace(0.0, math.pi * 2, 200))


    loc, dist = dtw_query(query, data, 0.05)

    assert loc > 0
    assert dist > 0

    # matched = np.concatenate((np.linspace(0.0, 0.0, loc), query))
    # plt.figure()
    # plt.plot(data)
    # plt.plot(query)
    # plt.plot(matched)
    # plt.show()

def test_static_data():
    data = np.fromfile(os.path.join(os.path.dirname(__file__), 'data/data.txt'), dtype="double", sep="\n")
    query = np.fromfile(os.path.join(os.path.dirname(__file__), 'data/query.txt'), dtype="double", sep="\n")

    loc, dist = dtw_query(query, data, 0.05)
    assert loc > 0
    assert dist > 0

    # plt.figure()
    # plt.plot(data)
    # plt.plot(query)
    # matched = np.concatenate((np.linspace(0.0, 0.0, loc), query))
    # plt.plot(matched)
    # plt.show()

if __name__=="__main__":
    test_rw()
