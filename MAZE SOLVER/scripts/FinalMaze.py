import cv2 as cv
import numpy as np
import math
import time
import winsound
import sys





class Grid:
	def __init__(self,x,y,clr):
		global start,end
		self.xCor = x
		self.yCor = y
		self.color = clr
		self.predecer = None
		self.Gcost = None
		self.Hcost = None


def distance(point1,point2):
	return math.sqrt(pow((point2[1]-point1[1]),2)+pow((point2[0]-point1[0]),2))

def lowestGrid(List,start):
														
	if len(List) == 1: 							
		return List[0]

	temp = list()
	minGrid = min(List, key = lambda x:(x.Gcost+x.Hcost))
	Fcost = minGrid.Gcost+minGrid.Hcost
	for i in List:
		if i.Gcost + i.Hcost == Fcost:
			temp.append(i)
	return min(temp,key = lambda x: x.Hcost)



def createGrid(img,h,w,gsize):
	List = list()

	for i in range(gsize//2,h,gsize):
		for j in range(gsize//2,w,gsize):
			if img[i][j][0] == 0:
				List.append(Grid(j,i,'b'))
				print("b-",end="")
			else:
				List.append(Grid(j,i,'w'))
				print("w-",end="")
		print("")
	return List



def updateCost(src,Nbr):
	global end
	newGcost = src.Gcost + 10
	newHcost = distance((Nbr.xCor,Nbr.yCor),(end[0],end[1]))

	if Nbr.Gcost == None and Nbr.Hcost ==None:
		Nbr.Gcost = newGcost
		Nbr.Hcost = newHcost		
	
	elif newGcost+newHcost < Nbr.Gcost+Nbr.Hcost:
		Nbr.Gcost = newGcost
		Nbr.Hcost = newHcost


def getNeighbours(i,j):
	global mazeMatrix,rw
	Neighbours  = list()
	if j+1 <rw and mazeMatrix[i][j+1].color == 'w':                    #right
		Neighbours.append(mazeMatrix[i][j+1])
		updateCost(mazeMatrix[i][j],mazeMatrix[i][j+1])

	if j-1 >=0 and mazeMatrix[i][j-1].color == 'w': 				  #left
		Neighbours.append(mazeMatrix[i][j-1])
		updateCost(mazeMatrix[i][j],mazeMatrix[i][j-1])

	if i+1 <rw and mazeMatrix[i+1][j].color == 'w':					  #down
		Neighbours.append(mazeMatrix[i+1][j])
		updateCost(mazeMatrix[i][j],mazeMatrix[i+1][j])

	if i-1 >=0 and mazeMatrix[i-1][j].color == 'w':					  #up
		Neighbours.append(mazeMatrix[i-1][j])
		updateCost(mazeMatrix[i][j],mazeMatrix[i-1][j])

	return Neighbours


def printPath(grid):
	global img
	img =  cv.circle(img,(grid.xCor,grid.yCor),4,(0,255,0),-1)
	cv.imshow("i",img)
	cv.waitKey(5)
	if grid.predecer:
		printPath(grid.predecer)
	return 


def getPosof(current):
    for k, x in enumerate(mazeMatrix):
    	x = x.tolist()
    	if current in x:
        	return k, x.index(current)

                                
def solveMaze(mazeMatrix,cr):
	global closeL,start,end,img
	current = cr
	img =  cv.circle(img,(current.xCor,current.yCor),4,(0,0,255),-1)
	cv.imshow("i",img)
	cv.waitKey(5)
	if current not in closeL:
		closeL.append(current)

	if current.xCor == end[0] and current.yCor == end[1]:         		#if current node is target node then stop
		printPath(current)
		while True:
			if cv.waitKey(1) == 27:
				cv.destroyAllWindows()
				exit()


	currentI,currentJ = getPosof(current)

	Neighbours = getNeighbours(currentI,currentJ)

	traversableNBR = [x for x in Neighbours if x not in closeL]

	if not traversableNBR:
										 		#if grid is dead end so we have to backtrack
		solveMaze(mazeMatrix,current.predecer)	
		return
	else:

		nextCurrent = lowestGrid(traversableNBR,start)       			#N stands for neighbours list
		nextCurrent.predecer = current
		solveMaze(mazeMatrix,nextCurrent)




def getStartandEnd(mazeMatrix,point,rw,cl,gridSize,typ):
	for i in range(rw):
		for j in range(cl):
			if point[0]<mazeMatrix[i][j].xCor+gridSize//2 and point[0]>mazeMatrix[i][j].xCor-gridSize//2 and point[1]<mazeMatrix[i][j].yCor+gridSize//2 and point[0]>mazeMatrix[i][j].xCor-gridSize//2:
				if typ == 's':
					return (mazeMatrix[i][j].xCor,mazeMatrix[i][j].yCor),i,j
				else:
					return (mazeMatrix[i][j].xCor,mazeMatrix[i][j].yCor)


def getAttributes(img):
	gridS = int(input("Enter grid size-->"))                            #for instance 20 pixel
	h,w = img.shape[:2]
	rows = h//gridS
	cols = w//gridS
	return w,h,rows,cols,gridS



def click_event(event,x,y,flags,param):
	global img,startClick,endClick
	if event == cv.EVENT_LBUTTONDOWN:
		if not startClick:
			startClick = (x,y)
			print("Start coordinate {}".format(startClick))
		else:
			endClick = (x,y)
			print("Start coordinate {}".format(endClick))
		img =  cv.circle(img,(x,y),4,(0,255,0),-1)
		cv.imshow("image",img)


sys.setrecursionlimit(10000)

img = cv.imread("maze-GridSize_20REDwithblackFinal.png")
img = cv.resize(img,(500,500))
w,h,rw,cl,gridSize = getAttributes(img)
#print(w,h,rw,cl,gridSize,sep="**")
print(rw,cl)

mList  = createGrid(img,h,w,gridSize)                  					#returns a 1D numpy array of the grids  
mazeMatrix = np.reshape(mList,(cl,rw))									#reshape the above numpy array into matrix denoting grids of maze 

startClick,endClick = (),()

#since window is getting offscreen without this lines of code
winname = "image"
cv.namedWindow(winname)        
cv.moveWindow(winname, 300,30) 
cv.imshow(winname,img)
#---------------------------------------------------------

cv.setMouseCallback('image',click_event)
cv.waitKey(0)
cv.destroyAllWindows()
print(startClick,endClick)


start,Startgrid_row,Startgrid_col = getStartandEnd(mazeMatrix,startClick,rw,cl,gridSize,'s')
end = getStartandEnd(mazeMatrix,endClick,rw,cl,gridSize,'e')

mazeMatrix[Startgrid_row][Startgrid_col].Gcost =  0
mazeMatrix[Startgrid_row][Startgrid_col].Hcost =  distance((start[0],start[1]),end)

closeL = []

solveMaze(mazeMatrix,mazeMatrix[Startgrid_row][Startgrid_col])                                 #specify the start grid       


