from copy import deepcopy


class Node: # node class
    graf=[]
    parent=None



def BaseGrafSearch(): # mian function for the start
    global checkForExit
    global init
    global final
    mainInit=baseFrontier[0]
    tempGraf=mainInit.graf
    if baseFrontier==[]:
        checkForExit=False
        return
    del baseFrontier[0]
    for search in finalFrontier:
        if(search.graf==tempGraf):
            checkForExit=False
            init=mainInit
            final=search
            return
        
    baseExplored.append(tempGraf)
    AddToFrontier(mainInit, 1)



def FinalGrafSearch(): # main function for the goal
    global checkForExit
    global init
    global final
    mainInit=finalFrontier[0]
    tempGraf=mainInit.graf
    if finalFrontier==[]:
        checkForExit=False
        return
    del finalFrontier[0]
    for search in baseFrontier:
        if(search.graf==tempGraf):
            checkForExit=False
            final=mainInit
            init=search
            return
        
    finalExplored.append(tempGraf)
    AddToFrontier(mainInit, 2)


def AddToFrontier(node, selector): # find new matrises and put them in the frontier
    tempGrid=node.graf
    location=FindSpace(tempGrid)
    k=0
    while k<len(location):
        i= -1
        while i<2:
            j=-1
            tempi=i+location[k][0]
            while j<2:
                tempj=j+location[k][1]
                if ((j!=0 or i!=0) and (tempi>=0 and tempi<len(tempGrid)) and (tempj>=0 and tempj<len(tempGrid)) and (tempGrid[tempi][tempj]!=0) and (i+j==-1 or i+j==1)):
                    newGrid=deepcopy(tempGrid)
                    newGrid[location[k][0]][location[k][1]], newGrid[tempi][tempj]= newGrid[tempi][tempj], newGrid[location[k][0]][location[k][1]]

                    if(selector==1):
                        checker= newGrid in baseExplored
                        if checker==False:
                            for search in baseFrontier:
                                if(search.graf==newGrid):
                                    checker=True
                                    break
                    else:
                        checker= newGrid in finalExplored
                        if checker==False:
                            for search in finalFrontier:
                                if(search.graf==newGrid):
                                    checker=True
                                    break  

                    if(checker==False):
                        newNode=Node()
                        newNode.parent=node
                        newNode.graf=newGrid
                        if selector==1:
                            baseFrontier.append(newNode)
                        else:
                            finalFrontier.append(newNode)
                j=j+1
            i=i+1
        k=k+1






def FindSpace(graf): # find two empty spaces
    x=[]
    for i in range(4):
        for j in range(4):
            if(graf[i][j]==0):
                x.append([i, j])
                if(len(x)==2):
                    return x



goalOne=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 0, 0]]
goalTwo=[[0, 0, 1, 2], [3, 4, 5, 6], [7, 8, 9, 10], [11, 12, 13, 14]]

intitial =[[0, 2, 3, 0], [1, 5, 10, 4], [9, 6, 8, 7], [13, 14, 11, 12]]

#[[0,2,3,0],[1,5,10,4],[9,6,8,7],[13,14,11,12]]
#[[0,1,2,3],[0,4,5,6],[7,8,9,10],[11,12,13,14]]
#[[1, 2, 3, 4], [5, 0, 6, 7], [8, 9, 0, 10], [11, 12, 13, 14]]

baseFrontier=[]
finalFrontier=[]
baseExplored=[]
finalExplored=[]

init=Node()
final=Node()

init.graf=intitial
final.graf=goalOne

baseFrontier.append(init)
finalFrontier.append(final)


checkForExit=True

while True:
    BaseGrafSearch()
    if checkForExit==False: break
    FinalGrafSearch()
    if checkForExit==False: break


print("-------------------------------------")

totalGraf=[]
while init.parent!=None:
        totalGraf.append(init.graf)
        init=init.parent
totalGraf.append(init.graf)

# show the answer
moves=0
del totalGraf[0]
totalGraf.reverse()
print("Initial State: ", totalGraf[0])
moves=moves+1
del totalGraf[0]
for i in totalGraf:
    print(i)
    moves=moves+1

while final.parent!=None:
        print(final.graf)
        final=final.parent
        moves=moves+1
print("Goal: " + str(final.graf))

print("Moves: ", moves)
print("explored: ", len(finalExplored + baseExplored))
print("frontier: ", len(finalFrontier + baseFrontier))