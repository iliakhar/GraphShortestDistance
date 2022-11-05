import math

N1 = 0

def MyMin(myList):
    global N1
    num = myList[0]
    ind = 0
    for i in range(len(myList)):
        N1 += 1
        if myList[i] < num:
            N1 += 1
            num = myList[i]
            ind = i
    return num, ind

def printGraphTable(origGraph):
    for i in range(len(origGraph)):
        print('\t', i, end = '')
    for i in range(len(origGraph)):
        print('\n',i,':\t', end = '')
        for j in range(len(origGraph)):
            print(origGraph[i][j], end = '\t')
    print()

def FordBell(graph):
    global N1
    N1 = 0
    answ = [[math.inf]*len(graph), [0]*len(graph)]
    answ[0][0] = 0
    isStabilized = False
    pseudoAnsw = [[0]*len(graph), [0]*len(graph)]
    while(not(isStabilized)):
        isStabilized = True
        for j in range(1, len(graph)):
            sumLen = []
            for k in range(len(graph)):
                N1+=1
                sumLen.append(answ[0][k] + graph[k][j])
            minSum, ind = MyMin(sumLen)
            
            if minSum != answ[0][j]:
                N1 += 1
                pseudoAnsw[0][j] = minSum
                pseudoAnsw[1][j] = ind
                isStabilized = False
        answ = pseudoAnsw[:]
    return answ

def ShowMinPathsToVertexs(arr):
    print("\nPaths:")
    for i in range(len(arr)):
        num = arr[i]
        path = [num]
        while(num != 0):
            num = arr[num]
            path.insert(0, num)
        print(i,' - ', path)

origGraph = [[0, 25, 15, 7, 2],
             [25, 0, 6, math.inf, math.inf],
             [15, 6, 0, 4, math.inf],
             [7, math.inf, 4, 0, 3],
             [2, math.inf, math.inf, 3, 0]]
#vertexCount = 5
#for i in range(vertexCount):
#    origGraph.append([math.inf]*vertexCount)
#origGraph[0][0] = origGraph[0][0] = 0
#origGraph[0][1] = origGraph[1][0] = 25
#origGraph[0][2] = origGraph[2][0] = 15
#origGraph[0][3] = origGraph[3][0] = 7
#origGraph[0][4] = origGraph[4][0] = 2
#origGraph[0][4] = origGraph[4][0] = 2
#origGraph[0][4] = origGraph[4][0] = 2
#origGraph[0][4] = origGraph[4][0] = 2

answ = FordBell(origGraph[:])
printGraphTable(origGraph)
print('\n',answ[0])
ShowMinPathsToVertexs(answ[1])
print("\nN1: ",N1)
#print(answ[1])
