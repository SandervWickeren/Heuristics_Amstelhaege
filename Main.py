"""Teamname: Sandy & Co
Names and StudentID:
- Tom Dekker (11031735)
- Laura Geerars (11007699)
- Sander van Wickeren (11060999)

Description:
"""

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

	def checkOverlap(grid, start_y, start_x, width, length, freespace):
		
		# Using a small number of significant points to check if overlap
		# occurs saves instructions.
		allowed = [0, 5]

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


	def placeHouse(ID, width, length, freespace, y_cor, x_cor, grid):
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
		# Define start coordinates:
		start_y = y_cor - freespace
		start_x = x_cor - freespace

		# Placement checking
		if checkOverlap(grid, start_y, start_x, width, length, freespace):

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
							grid[start_y + l][start_x + w] = 5
						elif l > (length + freespace - 1) and l < (length + 2 * freespace):
							grid[start_y + l][start_x + w] = 5

						else:

							# First X freespace meters and last X freespace
							# meters get ID 5.
							if w < freespace:
								grid[start_y + l][start_x + w] = 5
							elif w > (width + freespace - 1) and w < (width + 2 * freespace):
								grid[start_y + l][start_x + w] = 5
							
							# Otherwise it's part of the house and
							# gets given ID.
							else:
								grid[start_y + l][start_x + w] = ID
					except:
						
						# When error return previous correct grid.
						return False
		else:
			print ("Incorrect placement, check overlap.")
			return False
		return grid

	def genHome(grid, length, width, freespace, ID):
		y = genY(grid, freespace, length)
		x = genX(grid, freespace, width)
		return placeHouse(ID, width, length, freespace, y, x, grid)

	def genWater(grid):
		"""
		Current problems:
		 - Priemgetallen zorgen voor extra loops 
		 	--> misschien eerst testen?
		 - Als eerste getal groot is heb je veel loops
		 - Functie is nog wat rommelig.
		"""

		grid_surface = len(grid) * len(grid[0])

		# Amount of surface for the water.
		allowed_surface = round(0.2 * grid_surface)

		# Collection of the created surfaces
		water_surfaces = []

		# Min size of one water piece.
		min_single_size = 4

		run = 0

		# Loop until 4 and enough surface:
		while allowed_surface != 0:
			run += 1
			print (allowed_surface)
			w = 0
			l = 0

			# Only generate random if we have more then 1 option left.
			if len(water_surfaces) < 3 and min_single_size != allowed_surface and allowed_surface > 5:
				size = random.randint(min_single_size, allowed_surface)

			
			# Otherwise the size is the allowed surface
			else:
				size = allowed_surface

			
			# Shouldn't go below 0
			if allowed_surface - size >= 0:
			
				# Calculate width and length if possible.
				init = round(math.sqrt(size))
				for i in range(init, 1, -1):
					if size % i == 0 and 1 <= math.ceil((size / i) / i) <= 4:
						w = i
						l = size / w

						# Reinit allowed surface
						allowed_surface -= size
						water_surfaces.append((w, int(l), round(l / w, 2), size))
						break
						
			if run > 4:
				# Drop last try and remake the surface.
				print ("Drop")
				try:
					run = 2
					allowed_surface += water_surfaces[-1][3]
					water_surfaces = water_surfaces[:-1]
				except:
					print ("wat")

		return water_surfaces

	def placeWater():
		# Actually places water on the map.
		return


	def visualizeGrid(grid):
		"""
		Take in a grid and outputs a mapping of
		the grid using various colors.
		"""
		import matplotlib.pyplot as plt
		from matplotlib import colors

		# Define colors [Background, House1, freespace]
		colormap = colors.ListedColormap(["#FFFFFF", "#3F51B5", "#009688", "#4CAF50", "#FFCDD2"])
		
		# 0-1: white, 1-5: red etc.
		bounds = [0, 1, 2, 3, 5, 8]
		norm = colors.BoundaryNorm(bounds, colormap.N)

		# Make plot
		fig, ax = plt.subplots()
		ax.imshow(grid, cmap=colormap, norm=norm)

		# Show plot
		plt.show()

		return 0


	def calcScore(grid):
		return 0


	def startGeneration(variant, resolution):
		"""
		Variant is the number of houses that has
		to be placed		
		"""
		# Check for valid resolution
		if resolution % 2 != 0:
			print ("Resolution should be an even integer.")
			return 

		# House distirbution:
		familyHome = 0.60 * variant
		bungalow = 0.25 * variant
		maison = 0.15 * variant

		# Initialize values
		gr = genMap(180 * resolution, 160 * resolution)

		fam_length = int(resolution * 8)
		fam_width = int(resolution * 8)
		fam_freespace = int(resolution * 2) 

		bung_length = int(resolution * 7.5)
		bung_width = int(resolution * 10)
		bung_freespace = int(resolution * 3) 

		mais_length = int(resolution * 10.5)
		mais_width = int(resolution * 11)
		mais_freespace = int(resolution * 6)

		# Start with maisons
		M = 0
		while M != maison:

			ngrid = genHome(gr, mais_length, mais_width, mais_freespace, 1)

			# Check if house succsfully placed:
			if ngrid == False:
				print ("No succesfull placement Maison")
			else:
				print ("Maison {0} placed!".format(M))
				gr = list(ngrid)
				M += 1

		# Then bungalows
		B = 0
		while B != bungalow:

			ngrid = genHome(gr, bung_length, bung_width, bung_freespace, 2)

			# Check for succes:
			if ngrid == False:
				print ("No succesfull placement Bungalow")
			else:
				print ("Bungalow {0} placed!".format(B))
				gr = list(ngrid)
				B += 1 

		# Then Family homes
		F = 0
		while F != familyHome:

			ngrid = genHome(gr, fam_length, fam_width, fam_freespace, 3)

			# Check for succes:
			if ngrid == False:
				print ("No succesfull placement Family Home")
			else:
				print ("Family home {0} placed!".format(F))
				gr = list(ngrid)
				F += 1 

		# Visualize the grid
		print ("Generating map..")
		visualizeGrid(gr)


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
			ah = placeHouse(1, width, length, freespace, 
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

	#startGeneration(60, 10)
	gr = genMap(160, 180)
	print (placeWater(gr))
	
	


if __name__ == "__main__":
	#import pygame
	import random
	import copy
	import math
	main()


	

	
