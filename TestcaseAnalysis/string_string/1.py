idx = 2
nGram_Cnt = 0


def splitString(str):
    strList = []

    for i in range(len(str)-idx+1):
        strList.append(str[i:i+idx])

    return strList


def nGram(input, output):

    global nGram_Cnt

    inputList = splitString(input)
    outputList = splitString(output)

    intersectionList = []
    unionList = outputList.copy()
    for w in inputList:
        if w in outputList:
            intersectionList.append(w)
        else:
            unionList.append(w)

    similarity = len(intersectionList) / len(unionList) * 100

    return similarity


def averageSimilarity(similarityList):
    sum = 0
    cnt = 0
    avgSimList = []
    for i in range(len(similarityList)):
        sum += similarityList[i]
        cnt += 1
        if cnt == 10:
            avgSimList.append(sum/10)
            sum = 0
            cnt = 0

    return avgSimList


if __name__ == '__main__':
    f1 = open("testcase_new.txt")
    lines = f1.readlines()
    tc_new = []  # sets of [in, out]
    for line in lines[0:10]:
        line = line.split()
        tc_new.append(line)
    f1.close()

    f2 = open("testcase.txt")
    lines = f2.readlines()
    tc = []  # sets of [in, out]
    tmp = []
    for i in range(len(lines)):
        lines[i] = lines[i].split()
        tmp.append(lines[i])
        if len(tmp) == 10:
            tc.append(tmp)
            tmp = []
    f2.close()

    similarityList = []
    for i in tc_new:
        similarityList.append(nGram(i[0], i[1]))

    newAvgSim = averageSimilarity(similarityList)

    similarityList = []
    for i in tc:
        for j in i:
            similarityList.append(nGram(j[0], j[1]))

    avgSim = averageSimilarity(similarityList)

    print("\n\n*************************\n")
    print("New Testcase의 input-output 문자열 유사도")
    print(newAvgSim[0], "%")

    min = 100
    index = 0
    print("\n***Testcase와의 유사도***")
    for i in range(len(avgSim)):
        print("\nTestcase", i, "의 input-output 문자열 유사도")
        print(avgSim[i], "%")
        if abs(newAvgSim[0] - avgSim[i]) < min:
            min = abs(newAvgSim[0] - avgSim[i])
            index = i

    if min < 15:
        similarity = 100 - (min * 2)
    else:
        similarity = max(70 - min, 0)

    print("\n\n***Analysis Result***")
    print("Testcase with Highest Similarity : Testcase", index)
    print("Percentage of Similarity with Testcase",
          index, " : ", similarity, "%\n")
