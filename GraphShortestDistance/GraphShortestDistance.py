import math

N1 = 0

class Edge:
    def __init__(self, vertex1, vertex2, lenth):
        self.v1 = vertex1
        self.v2 = vertex2
        self.lenth = lenth

class Edge1:
    def __init__(self, vertex1, vertex2):
        self.v1 = vertex1
        self.v2 = vertex2

def MyMin(myList):
    global N1
    num = myList[0]
    ind = 0
    for i in range(len(myList)):
        #N1 += 1
        if myList[i] < num:
            N1 += 1
            num = myList[i]
            ind = i
    return num, ind


def FordBell(graph, vertCount, startVert):
    global N1
    N1 = 0
    answ = [[math.inf]*vertCount, [0]*vertCount]
    answ[0][startVert] = 0
    isStabilized = False
    pseudoAnsw = [[math.inf]*vertCount, [0]*vertCount]
    pseudoAnsw[0][startVert] = 0
    pseudoAnsw[1][startVert] = None
    val = 0
    count = 0
    while(not(isStabilized)):

        isStabilized = True
        for j in range(0, vertCount):
            if j!= startVert:
                sumLen = []
                for k in range(vertCount):
                    N1+=1
                    val =  graph[(k,j)] if (k,j) in graph else math.inf
                    sumLen.append(answ[0][k] + val)
                minSum, ind = MyMin(sumLen)
            
                if minSum != answ[0][j]:
                    N1 += 1
                    pseudoAnsw[0][j] = minSum
                    pseudoAnsw[1][j] = ind
                    isStabilized = False
        answ = pseudoAnsw[:]
        if(count == vertCount):
            print("\nNegative cycle!\n")
            break
        count+=1
    return answ, count == vertCount

def MinVal(arr,canUse):
    global N1
    ind = -1
    val = math.inf
    for j in range(0, len(arr)):
        N1+=1
        if canUse[j] and val > arr[j]:
            N1 += 1
            val = arr[j]
            ind = j
    return val, ind

def Dijkstra(graph, vertCount, startVert):
    global N1
    N1 = 0
    answ = [[math.inf]*vertCount, [0]*vertCount]
    answ[0][startVert] = 0
    answ [1][startVert] = None
    canUseVert = [True]*vertCount
    canUseVert[startVert] = False
    tmpArr = [[0]*vertCount]
    val = 0
    for i in range(vertCount):
        tmpArr[0][i] = graph[(startVert,i)] if (startVert,i) in graph else math.inf
    tmpArr.append([startVert]*vertCount)
    for i in range(vertCount - 1):
        dw,w= MinVal(tmpArr[0], canUseVert)
        lvert = tmpArr[1][w]
        canUseVert[w] = False
        N1 += 1
        answ[0][w] = dw
        answ[1][w] = lvert
        for j in range(len(tmpArr[0])):
            val = graph[(w,j)] if (w ,j) in graph else math.inf
            if canUseVert[j] and tmpArr[0][j] > dw + val:
                N1+=2
                tmpArr[0][j] = dw + val
                tmpArr[1][j] = w
    return answ



def ShowMinPathsToVertexs(arr, startVert):
    print("\nPaths:")
    for i in range(len(arr)):
        num = arr[i]
        path = [num]
        while(num != startVert and num != None):
            num = arr[num]
            path.insert(0, num)
        print(i,' - ', path)


def ShowTable(mp, Nvert):
    for i in range(Nvert):
        print('\t', i, end = '')

    for i in range(Nvert):
        print('\n',i,'\t', end = '')
        for j in range(Nvert):
            if i == j: print(0,end = '\t')
            else: print(mp[(i,j)] if (i,j) in mp else math.inf, end = '\t')
    print()



mp = {(0,1): 25, (0,2): 15, (0,3):7, (0,4):2, (1,0):25,
       (1,2):6, (2,0):15, (2,1):6, (2,3):4, (3,0):7,
       (3,2):4, (3,4):3, (4,0):2, (4,3):3}
vertCount = 5

#mp = {(0,0):0, (0,1):2, (0,2):7, (0,3):4, (0,4):6, (0,5):3,
#      (1,0):3, (1,1):0, (1,2):4, (1,3):5, (1,4):6, (1,5):1,
#      (2,0):2, (2,1):4, (2,2):0, (2,3):8, (2,4):7,
#      (3,0):4, (3,2):8, (3,3):0, (3,4):5, (3,5):7,
#      (4,1):7, (4,2):8, (4,3):4, (4,4):0, (4,5):3,
#      (5,0):2, (5,1):4, (5,3):7, (5,4):8, (5,5):0}

#mp = {(0,1):10, (0,2):30, (0,3):50, (0,4):10, (2,4):10,
#      (3,1):40, (3,2):20, (4,0):10, (4,2):10, (4,3):30};



ShowTable(mp,vertCount)
stV = 2

answ, isNeg = FordBell(mp, vertCount, stV)
print('\n',answ[0])
if isNeg == False:
    ShowMinPathsToVertexs(answ[1],stV)
print("\nN1: ",N1)
answd = Dijkstra(mp, vertCount, stV)
ShowMinPathsToVertexs(answd[1],stV)
print('\n',answd[0])
print("\nN1: ",N1)
