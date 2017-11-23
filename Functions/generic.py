"""
Contains generic functions that apply to all of the algorithms used.
"""

import math
print ("Generic imported")

def genMap(length, width):
	"""
	Input is a distance in meters. Output is a list
	of lists containing zeros. Representing the grid.

	Example of 2x4:
	[[0, 0, 0, 0],
	 [0, 0, 0, 0]]
	"""
	return [width * [0] for i in range(length)]


def visualizeGrid(grid):
	"""
	Take in a grid and outputs a mapping of
	the grid using various colors.
	"""
	import matplotlib.pyplot as plt
	from matplotlib import colors

	# Define colors [Background, House1, freespace]
	colormap = colors.ListedColormap(["#FFFFFF", "#F9A825", "#8BC34A", "#D66EFF", "#2196F3", "#424242", "#9E9E9E"])
	
	# 0-1: white, 1-5: red etc.
	bounds = [0, 1, 2, 3, 4, 5, 8, 10]
	norm = colors.BoundaryNorm(bounds, colormap.N)

	# Make plot
	fig, ax = plt.subplots()
	ax.imshow(grid, cmap=colormap, norm=norm)

	# Show plot
	plt.show()

	return


def checkOverlap(grid, start_y, start_x, house):
	"""
	Takes as input the grid and the information from a house, it outputs
	true if it can be placed and false if it cannot.
	"""
	
	# Using a small number of significant points to check if overlap
	# occurs saves instructions.
	allowed = [0, 4, 5]
	width = house.width
	length = house.length
	freespace = house.freespace

	# Center
	if grid[start_y + round(length / 2)][start_x  + round(width / 2)] not in allowed:
		return False

	# North-west
	if grid[start_y][start_x] not in allowed:
		return False

	# North-east
	elif grid[start_y][start_x + freespace + width] not in allowed:
		return False

	# South-east
	elif grid[start_y + length + freespace][start_x + width + freespace] not in allowed:
		return False

	# North
	elif grid[start_y][start_x + freespace + round(width / 2)] not in allowed:
		return False

	# South-west
	elif grid[start_y + length + freespace][start_x] not in allowed:
		return False

	# East
	elif grid[start_y + round(length / 2)][start_x + freespace + width] not in allowed:
		return False

	# South
	elif grid[start_y + length + freespace][start_x + round(width / 2)] not in allowed:
		return False

	# West
	elif grid[start_y + round(length / 2)][start_x] not in allowed:
		return False

	# Because there are differen sizes of freespace it is possible that part of a new house is
	# in the freespace of a bigger house. By checking the inner SW, SE, NE and NW it 
	# can be prevented
	# ISW
	elif grid[start_y + length + freespace][start_x + freespace] != 0:
		return False

	# ISE
	elif grid[start_y + length + freespace][start_x + width + freespace] != 0:
		return False

	# INE
	elif grid[start_y + freespace][start_x + width + freespace] != 0:
		return False

	# INW
	elif grid[start_y + freespace][start_x + freespace] != 0:
		return False

	else:
		return True


def placeHouse(grid, house):
	"""
	Takes as input:
	- A unique ID that indicates the house.
	- Length of the house in meters
	- Width of the house in meters
	- The amount of freespace in meters
	- y_cor from where it should be generated
	- x_cor from where it should be generated
	- The current grid

	Output:
	- Grid with the new house added or false if not possible.
	"""
	# Define start coordinates:
	start_y = house.y - house.freespace
	start_x = house.x - house.freespace

	# Placement checking
	if checkOverlap(grid, start_y, start_x, house):

		# Generate the houses.
		# For every possible Y value
		for l in range(house.length + 2 * house.freespace):

			# For every possible X value
			for w in range(house.width + 2 * house.freespace):

				# Try placing the house
				try:

					# First Y freespace meters and last Y freespace
					# meters get ID 5.
					if l < house.freespace:
						grid[start_y + l][start_x + w] = 5
					elif l > (house.length + house.freespace - 1) and l < (house.length + 2 * house.freespace):
						grid[start_y + l][start_x + w] = 5

					else:

						# First X freespace meters and last X freespace
						# meters get ID 5.
						if w < house.freespace:
							grid[start_y + l][start_x + w] = 5
						elif w > (house.width + house.freespace - 1) and w < (house.width + 2 * house.freespace):
							grid[start_y + l][start_x + w] = 5
						
						# Otherwise it's part of the house and
						# gets given ID.
						else:
							grid[start_y + l][start_x + w] = house.id
				except:
					
					# When error return previous correct grid.
					return False
	else:
		print ("Incorrect placement, check overlap.")
		return False
	return grid



def allowedFreespace(grid, house, freespace, allowed):
	"""
	Takes as input a list of allowed points, the grid and the information
	from a house. It returns True if the amount of freespace given is 
	possible, otherwise it returns False.

	"""
	# Define max_y and max_x:
	max_y = len(grid)
	max_x = len(grid[0])

	# Define other variables:
	y = house.y
	x = house.x
	width = house.width
	length = house.length	

	# Generate the compas points
	NW = (y - freespace, x - freespace)
	NE = (y - freespace, x + width + freespace)
	SW = (y + length + freespace , x - freespace)
	SE = (y + length + freespace, x + width + freespace)
	check_coor = [(NW[0], NW[1]), #NW
				  (NW[0], NW[1] + width + 2* freespace), #NE
				  (NW[0] + length + freespace, NW[1]), #SW
				  (NW[0] + length + 2 * freespace, NW[1] + width + 2* freespace)] #SE
	# print (NW, NE, SW, SE)
	# print ("------------", freespace, "------------")
	# print (width, length, freespace)



	# Checks all points from NW-NE (NE_y - NW_y):
	for x in range(NE[1] - NW[1]):
		
		# Set coordinates:
		point_y = NW[0]
		point_x = NW[1] + x

		# Ignore if outside of map
		try:
			if 0 <= point_x <= max_x and 0 <= point_y <= max_y:
				
				# If the specific point is not a valid
				# freespace, return false.
				if grid[point_y][point_x] not in allowed:
					#print ("At p1")
					return False
				#else:
					# For visualisation
				 	# grid[point_y][point_x] = 8
		except:
			pass

	# SW-SE
	for x in range(SE[1] - SW[1]):

		# Set coordinates
		point_y = SW[0] - 1
		point_x = SW[1] + x 
		
		try:
			if 0 <= point_x <= max_x and 0 <= point_y <= max_y:
				if grid[point_y][point_x] not in allowed:
					#print ("At p2", grid[point_y][point_x])
					return False
		except: 
			pass

	# Check all Points from NE-SE:
	for y in range(SE[0] - NE[0]):

		# Set coordinates
		point_y = NE[0] + y 
		point_x = NE[1] - 1
	
		
		try:
			if 0 <= point_x <= max_x and 0 <= point_y <= max_y:
				if grid[point_y][point_x] not in allowed:
					#print ("At p3", grid[point_y][point_x])
					return False
		except:
			pass

	#NW-SW
	for y in range(SW[0] - NW[0]):

		# Set coordinates
		point_y = NW[0] + y 
		point_x = NW[1] 
		
		
		try:
			if 0 <= point_x <= max_x and 0 <= point_y <= max_y:
				if grid[point_y][point_x] not in allowed:
					#print ("At p4", grid[point_y][point_x], point_y, point_x)
					return False
		except:
			pass

	# Check all points from SW-SE:
	# printGrid(grid)
	# print (" ")

	# If everything went fine, return
	return True

def calculateScore(grid, placed_houses):
	total_price = 0

	for h in placed_houses:

		allowed = [0, 5, 4]

		check = True
		distance = 0
		while check:
			distance += 1
			check = allowedFreespace(grid, h, h.freespace + distance, allowed)
			

		# Calc extra meters rounding to lowest integer.
		extra_meters = math.floor((distance - h.freespace) / h.resolution)

		# Calculate the price
		sell_price = h.price * (1 + (h.priceimprovement / 100) * extra_meters)
		total_price += sell_price
		# print ("Gevonden afstand {0} met een prijs van {1}".format(distance, sell_price))

	return total_price

# Helper functions
def printGrid(grid):
	"""
	Prints the raw grid in a visual pleasing
	manner. 
	"""
	for x in grid:
		print (x)
