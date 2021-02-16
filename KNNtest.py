import KNN
import numpy as np
import pandas as pd
group, label = KNN.creatDataSet()
print(group)
print(label)
import matplotlib.pyplot as plt

# plt.plot(group)

datingDataMat, datingLabels = KNN.file2matrix("datingTestSet.txt")
print(datingDataMat)
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,1], datingDataMat[:,2])
plt.show()