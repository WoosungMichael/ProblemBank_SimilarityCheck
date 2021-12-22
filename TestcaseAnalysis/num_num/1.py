import matplotlib.pyplot as plt
import numpy as np
import math


def assignIDs(list):
    sortedList = sorted(list)

    seen = set()
    seen_add = seen.add
    uniqueList = [x for x in sortedList if x not in seen and not seen_add(x)]

    return dict(zip(uniqueList, range(len(uniqueList))))


def plotData(inData, color, data):
    x, y = zip(*inData)

    xMap = assignIDs(x)
    xAsInts = np.array([xMap[i] for i in x])

    A = np.vstack([xAsInts, np.ones(len(xAsInts))]).T
    m, c = np.linalg.lstsq(A, np.array(y), rcond=None)[0]

    plt.scatter(xAsInts, y, label=data, color=color)
    plt.plot(xAsInts, xAsInts*m+c, color=color)

    x = np.array(xAsInts)
    y = np.array(xAsInts*m+c)

    fq = np.polyfit(x, y, 1)
    eq = np.poly1d(fq)
    print(eq)

    plt.xticks(list(xMap.values()), list(xMap.keys()))
    plt.legend(loc='best')

    return fq[0]


if __name__ == '__main__':
    f1 = open("testcase_new.txt")
    lines = f1.readlines()
    tc_new = []  # sets of [in, out]
    for line in lines[0:10]:
        line = map(int, line.split())
        tc_new.append(line)
    f1.close()

    f2 = open("testcase.txt")
    lines = f2.readlines()
    tc = []  # sets of [in, out]
    tmp = []
    for i in range(len(lines)):
        lines[i] = map(int, lines[i].split())
        tmp.append(lines[i])
        if len(tmp) == 10:
            tc.append(tmp)
            tmp = []
    f2.close()

    plt.xlabel('X : Testcase Input')
    plt.ylabel('Y : Testcase Output')

    print("\n\n*************************\n")
    print("New Testcase")
    gradient = plotData(tc_new, 'Red', 'New Testcase')
    theta_1 = math.atan(gradient) * 57.3  # 라디안 각도로 변환

    color = ['Black', 'Grey', 'Blue', 'Green', 'Purple']
    min = 1000000000
    index = 0
    similarity = 0
    for i in range(len(tc)):
        print("\nTestcase", i)
        tmp = plotData(tc[i], color[i], 'Testcase' + str(i))
        if abs(gradient - tmp) < min:
            min = abs(gradient - tmp)
            theta_2 = math.atan(tmp) * 57.3  # 라디안 각도로 변환
            index = i
            similarity = (math.cos(abs(theta_1 - theta_2))+1) / 2

    print("\n\n***Analysis Result***")
    print("Testcase with Highest Similarity : Testcase", i)
    print("Percentage of Similarity with Testcase",
          i, " : ", similarity * 100, "%")

    plt.gcf().savefig("analysis.png")
