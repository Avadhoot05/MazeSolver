You can watch the working of the project here: https://youtu.be/uAqHXnGlNuc

# MazeSolver
Maze Solver using A* algorithm
code: FinalMaze.py create_maze

input: grid size mouse click on starting grid mouse click on ending grid

constraints: Grid size must be known prior to the user. White and black grids must have same dimensions. There should be only one correct path. (For multiple paths, code is capable of finding solution but does not gaurantee to the shortest path).

Step1: Load a RGB image from specified location into 'img' variable. (openCV converts it into BGR)

Step2: getAttributes() <-- This function takes gridSize as user input and then calculates i) height(No.of rows in img) ii) width(No. of columns in img) iii) rows (No of vertical grids) iv) cols (No of horizontal grids)

Step 3: createGrid() <-- This function creates 1D numpy array containing pointer to each grid where each data in each grid contains attributes as follows: i)xCor of center of each grid ii)yCor of center of each grid iii)color iv)predecer = initially None v)self.Gcost = initially None vi)self.Hcost = initially None

	Then reshape this 1D numpy array into 2D array having order (rows)x(cols) using np.reshape()
Step 4: Get user click for starting grid and ending grid. (startClick,endClick). Now, User can click anywhere in desired grid but for traversal we require only the center coordinates of the grid Hence, getStartandEnd()<-- this function converts the user coordinates into center coordinates of that grid(start,end) and also returns row position and column position of start grid.

Step 5: Update Gcost of start Grid to 0 and Hcost to dist(start coordinate,end coordinate) (Gcost is perpendicular distance between start grid from grid(i) Hcost is perpendicular distance between grid(i) to end grid)

Step 6: call solveMaze() which implements actual algorithm. i)initially current working grid = start grid ii)if current Grid == end grid path is found and call function to print the path iii)else 1)list all the neighbours of current grid 2)list all the traversable neighbours among the above step.(traversable means the grids which are white and not yet visited. All the visited grids are stored in globally declared closeL list)

			if traversale neighbours do not exist (that means either it is dead end or all the neighbours are already traversed)
				recursively call with predecer grid
			else
				find neighbour having lowest value of (Gcost+Hcost)
				make current grid as predecer of neighbour found in above step
				update current grid to new grid.
				recursive call to solveMaze() using new current grid.
step 7: when end pixel is found.
		Now, end grid has the pointer to its preceder grid and so on till the starting grid. So trace the path.

Input Image:


![input](https://user-images.githubusercontent.com/48721257/102319290-a6c24980-3fa0-11eb-82eb-81e857a35a27.png)

Output:


![output](https://user-images.githubusercontent.com/48721257/102319452-ea1cb800-3fa0-11eb-9ae1-ccbd19f851bf.png)
