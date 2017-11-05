"""Teamname: Sandy & Co
Names and StudentID:
-
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

	def genY(grid):
		"""
		Input is a grid, output a random Y value from the grid.
		"""
		return random.randint(0, len(grid))

	def genX(grid):
		"""
		Input is a grid, output a random X value from the grid.
		"""
		return random.randint(0, len(grid[0]))

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

		# Place 5 house test:
		t = 0
		while t != 10:

			ah = placeHouse(4, 4, 1, genY(gr), genX(gr), gr)

			if ah != gr:
				gr = list(ah)
				t += 1
			else:
				print "Retry."
		
		visualizeGrid(ah)
		return 0

	test()
	


if __name__ == "__main__":
	#import pygame
	import random
	import copy
	main()


	

	
