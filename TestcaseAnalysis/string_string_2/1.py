import matplotlib.pyplot as plt
import numpy as np
import math


def plotData(inData, color, data):
    x, y = zip(*inData)
    min_i = min(list(map(int, x)))
    max_i = max(list(map(int, x)))

    xAsInts = np.array(list(x))

    x = list(x).sort()

    A = np.vstack([xAsInts, np.ones(len(xAsInts))]).T
    m, c = np.linalg.lstsq(A, np.array(y), rcond=None)[0]

    plt.scatter(xAsInts, y, label=data, color=color)
    plt.plot(xAsInts, xAsInts*m+c, color=color)

    x = np.array(xAsInts)
    y = np.array(xAsInts*m+c)

    fq = np.polyfit(x, y, 1)
    eq = np.poly1d(fq)
    print("- Equation", eq)

    plt.xticks(np.arange(min_i-3, max_i+3, (max_i - min_i)/6))
    plt.legend(loc='best')

    return fq[0], fq[1]


if __name__ == '__main__':
    f1 = open("testcase_new.txt")
    lines = f1.readlines()
    tc_new = []  # sets of [in, out]
    for line in lines[0:10]:
        io_str = line.split()
        tmp2 = []
        for i in io_str:
            tmp = []
            for j in i:
                tmp.append(ord(j))
            tmp2.append(sum(tmp)/len(tmp))
        tc_new.append(tmp2)
    f1.close()
    print(tc_new)

    f2 = open("testcase.txt")
    lines = f2.readlines()
    tc = []  # sets of [in, out]
    tmp3 = []
    for i in range(len(lines)):
        io_str = lines[i].split()
        tmp2 = []
        for i in io_str:
            tmp = []
            for j in i:
                tmp.append(ord(j))
            tmp2.append(sum(tmp)/len(tmp))
        tmp3.append(tmp2)
        if len(tmp3) == 10:
            tc.append(tmp3)
            tmp3 = []
    f2.close()
    print(tc)

    plt.xlabel('X : Testcase Input')
    plt.ylabel('Y : Testcase Output')

    print("\n\n*************************\n")
    print("New Testcase")
    gradient, constant = plotData(tc_new, 'Red', 'New Testcase')
    theta_1 = math.atan(gradient) * 57.3  # 라디안 각도로 변환

    print("\n***Testcase와의 유사도***")
    color = ['Black', 'Grey', 'Blue', 'Green', 'Purple']
    index = 0
    similarity = 0
    for i in range(len(tc)):
        print("\nTestcase", i)
        tmp1, tmp2 = plotData(tc[i], color[i], 'Testcase' + str(i))
        theta_2 = math.atan(tmp1) * 57.3  # 라디안 각도로 변환

        tmp_sim = ((math.cos(abs(theta_1 - theta_2))+1) / 2) * \
            0.9 + max((100 - abs(constant - tmp2)), 0) * 0.01 * 0.1

        print("- Similarity : ", tmp_sim*100, "%")

        if tmp_sim > similarity:
            index = i
            similarity = tmp_sim
            if similarity == 1:
                break

    print("\n\n***Analysis Result***")
    print("Testcase with Highest Similarity : Testcase", index)
    print("Percentage of Similarity with Testcase",
          index, " : ", similarity * 100, "%\n")

    plt.gcf().savefig("analysis.png")
