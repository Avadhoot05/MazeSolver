#consiser grid size=20 pixels
import cv2 as cv

rw = int(input("Enter dim-->"))
gridS = int(input("Enter gridsize-->")) 
img = cv.imread("C:\\Users\\khede\\Downloads\\maze-master\\maze-master\\blank.png")
img = img[:rw*gridS+1,:rw*gridS+1]

pt = 0
for i in range(0,rw+1):
	img = cv.line(img,(pt,0),(pt,len(img)),(0,0,0),1)
	img = cv.line(img,(0,pt),(len(img),pt),(0,0,0),1)
	pt+=gridS


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret,threshImg = cv.threshold(gray,2,255,cv.THRESH_BINARY)
st = "maze-GridSize_"+str(gridS)+".png"
cv.imwrite(st,threshImg)

