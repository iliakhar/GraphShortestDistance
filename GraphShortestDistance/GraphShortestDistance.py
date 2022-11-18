import math

N1 = 0

class Edge:
    def __init__(self, vertex1, vertex2, lenth):
        self.v1 = vertex1
        self.v2 = vertex2
        self.lenth = lenth

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

def MinVal(arr,canUse):
    global N1
    ind = -1
    val = math.inf
    for j in range(0, len(arr)):
        if canUse[j] and val > arr[j]:
            N1 += 2
            val = arr[j]
            ind = j
    return val, ind

def Dijkstra(graph):
    global N1
    N1 = 0
    answ = [[math.inf]*len(graph), [0]*len(graph)]
    answ[0][0] = answ [0][1] = 0
    canUseVert = [True]*(len(graph)-1)
    tmpArr = [graph[0][1:]]
    tmpArr.append([0]*(len(graph)-1))
    for i in range(len(graph) - 1):
        dw,w= MinVal(tmpArr[0], canUseVert)
        lvert = tmpArr[1][w]
        canUseVert[w] = False
        N1 += 1
        answ[0][w + 1] = dw
        answ[1][w + 1] = lvert
        for j in range(len(tmpArr[0])):
            if canUseVert[j] and tmpArr[0][j] > dw + graph[w + 1][j + 1]:
                N1+=2
                tmpArr[0][j] = dw + graph[w + 1][j + 1]
                tmpArr[1][j] = w + 1
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

def ListGrToMatr(adjList, Nvert):
    matr = []
    for i in range(Nvert):
        matr.append([math.inf]*Nvert)
        matr[i][i] = 0

    for lst in adjList:
        matr[lst.v1][lst.v2] = lst.lenth
    return matr


#adjList = [Edge(0,1,10), Edge(0,2,30), Edge(0,3,50), Edge(0,4,10), Edge(2,4,10),
#           Edge(3,1,40), Edge(3,2,20), Edge(4,0,10), Edge(4,2,10), Edge(4,3,30)];

adjList = [Edge(0,1,25), Edge(0,2,15), Edge(0,3,7), Edge(0,4,2), Edge(1,0,25),
           Edge(1,2,6), Edge(2,0,15), Edge(2,1,6), Edge(2,3,4), Edge(3,0,7),
           Edge(3,2,4), Edge(3,4,3), Edge(4,0,2), Edge(4,3,3)];

origGraph = ListGrToMatr(adjList, 5)

answ = FordBell(origGraph[:])
printGraphTable(origGraph)
print('\n',answ[0])
ShowMinPathsToVertexs(answ[1])
print("\nN1: ",N1)
answd = Dijkstra(origGraph)
ShowMinPathsToVertexs(answd[1])
print('\n',answd[0])
print("\nN1: ",N1)
#print(answ[1])
