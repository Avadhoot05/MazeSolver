import cv2 as cv
import numpy as np




img = cv.imread("C:\\Users\\khede\\Downloads\\maze-master\\maze-master\\maze.png")
gridSize = int(input("Enter grid size-->"))
h,w = img.shape[:2]
rows = h//gridSize
cols = w//gridSize

print("Width {} -- Height {}".format(w,h))
print("No.of horizontal grids {} \nNo.of vertical grids {}".format(rows,cols))



'''


gr = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


h,w = img.shape[:2]

cl,rw = 10,10													#This depends on the maze
gridSize = 20   												#This depends on the maze 

start,end = (10,10),(190,190)											#grids (Not the pixels)				

mList  = createGrid(gr,h,gridSize)                  					#returns a 1D numpy array of the grids  '''