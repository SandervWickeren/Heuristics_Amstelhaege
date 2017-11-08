"""Teamname: Sandy & Co
Names and StudentID:
- Tom Dekker (11031735)
- Laura Geerars (11007699)
- Sander van Wickeren (11060999)

Description:
~"""

def main():
	"""
	explain
	"""

	def genMap(length, width):
		"""
		Input is a distance in meters. Output is a list
		of lists containing zeros. Representing the grid.

		Example of 2x4:
		[[0, 0, 0, 0],
		 [0, 0, 0, 0]]
		"""
		# Fixes .5
		width = 2 * width
		length = 2 * length

		return [width * [0] for i in range(length)]

	def genY(grid, freespace, height):
		"""
		Input is a grid, the amount of freespace and the
		height of the dedicated house.
		Output a random Y value from the grid.
		"""
		return random.randint(freespace, len(grid) - freespace - height)

	def genX(grid, freespace, length):
		"""
		Input is a grid, the amount of freespace and the
		length of the dedicated house.
		Output a random Y value from the grid.
		"""
		return random.randint(freespace, len(grid[0]) - freespace - length)

	def placeHouse(width, length, freespace, y_cor, x_cor, grid):
		"""
		Takes as input:
		- Length of the house in meters
		- Width of the house in meters
		- The amount of freespace in meters
		- y_cor from where it should be generated
		- x_cor from where it should be generated
		- The current grid

		Output:
		- Grid with the new house added.
		"""
		# Assign variabele:
		newgrid = copy.deepcopy(grid)

		# Remove the .5 problem
		width = int(2 * width)
		length = int(2 * length)
		freespace = int(2 * freespace)

		# Place house
		for l in range(length):
			try:
				
				# Internal house
				for w in range(width):
					newgrid[y_cor + l][x_cor + w] = 1

				# Freespace
				for f in range(1, freespace + 1):
					
					# At the sides
					newgrid[y_cor + l][x_cor - f] = 5
					newgrid[y_cor + l][x_cor + width + f - 1] = 5

			except:
				# False placement:
				return grid
				

		# Partial freespace
		for w in range(width):
			try:
				for f in range(1, freespace + 1):

					# At top/bottom
					newgrid[y_cor - f][x_cor + w] = 5
					newgrid[y_cor + length + f - 1][x_cor + w] = 5

			except:
				print ("Unexpected error:", sys.exc_info()[0])
				print ("Retry.")
				return grid
				
		return newgrid

	def placeHouse2(ID, width, length, freespace, y_cor, x_cor, grid):
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
		- Grid with the new house added.
		"""
		# Assign variabele:
		newgrid = copy.deepcopy(grid)

		# Remove the .5 problem
		# width = int(2 * width)
		# length = int(2 * length)
		# freespace = int(2 * freespace)

		# Define start coordinates:
		start_y = y_cor - freespace
		start_x = x_cor - freespace

		# Generate the houses.
		# For every possible Y value
		for l in range(length + 2 * freespace):

			# For every possible X value
			for w in range(width + 2 * freespace):

				# Try placing the house
				try:

					# First Y freespace meters and last Y freespace
					# meters get ID 5.
					if l < freespace:
						newgrid[start_y + l][start_x + w] = 5
					elif l > (length + freespace - 1) and l < (length + 2 * freespace):
						newgrid[start_y + l][start_x + w] = 5

					else:

						# First X freespace meters and last X freespace
						# meters get ID 5.
						if w < freespace:
							newgrid[start_y + l][start_x + w] = 5
						elif w > (length + freespace - 1) and w < (length + 2 * freespace):
							newgrid[start_y + l][start_x + w] = 5
						
						# Otherwise it's part of the house and
						# gets given ID.
						else:
							newgrid[start_y + l][start_x + w] = ID
				except:
					
					# When error return previous correct grid.
					return grid
		
		return newgrid



	def visualizeGrid(grid):
		"""
		Take in a grid and outputs a mapping of
		the grid using various colors.
		"""
		import matplotlib.pyplot as plt
		from matplotlib import colors

		# Define colors [Background, House1, freespace]
		colormap = colors.ListedColormap(["#FFFFFF", "#D50000", "#FF8A80"])
		
		# 0-1: white, 1-5: red etc.
		bounds = [0, 1, 5, 8]
		norm = colors.BoundaryNorm(bounds, colormap.N)

		# Make plot
		fig, ax = plt.subplots()
		ax.imshow(grid, cmap=colormap, norm=norm)


		# Show plot
		plt.show()

		return 0


	def calcScore(grid):
		return 0


	def test():
		"""
		Temporarily test function.
		"""
		gr = genMap(50, 50)

		# House information:
		# Should be 2 times the original size
		length = 8
		width = 8
		freespace = 2

		# Place 5 house test:
		t = 0
		while t != 10:

			#ah = placeHouse(4, 4, 1, genY(gr), genX(gr), gr)
			ah = placeHouse2(1, width, length, freespace, 
							 genY(gr, freespace, length), 
							 genX(gr, freespace, width),
							  gr)

			if ah != gr:
				gr = list(ah)
				t += 1
			else:
				print ("What is causing it?")
		
		visualizeGrid(ah)
		return 0

	test()
	


if __name__ == "__main__":
	#import pygame
	import random
	import copy
	main()


	

	
