"""
Contains functions that apply to the random algorithm only.
"""
import random
import generic
import math
import os
import sys

# Get current location
dir_path = os.path.dirname(os.path.realpath(__file__))

# Add custom classes and functions
sys.path.insert(0, dir_path.split("\\")[-1] + "\Classes")

import class_house


def startGeneration(variant, resolution):
		"""
		Variant is the number of houses that has
		to be placed, resolution changes the size
		of the map.	
		"""
		# Check for valid resolution
		if resolution % 2 != 0:
			print ("Resolution should be an even integer.")
			return 

		# House distirbution:
		familyHome = 0.60 * variant
		bungalow = 0.25 * variant
		maison = 0.15 * variant

		# Initialize Classlist
		placed_houses = []

		# Initialize values
		gr = generic.genMap(180 * resolution, 160 * resolution)

		fam_length = int(resolution * 8)
		fam_width = int(resolution * 8)
		fam_freespace = int(resolution * 2) 

		bung_length = int(resolution * 7.5)
		bung_width = int(resolution * 10)
		bung_freespace = int(resolution * 3) 

		mais_length = int(resolution * 10.5)
		mais_width = int(resolution * 11)
		mais_freespace = int(resolution * 6)

		# Water
		# Generate water parts
		water_parts = genWater(gr)

		# Place water parts in grid:
		for part in range(len(water_parts)):
			W = 0

			# Loop until correctly placed.
			while W != 1:

				ngrid = genHome(gr, water_parts[part][1], water_parts[part][0], 0, 4)

				# Check for success:
				if ngrid == False:
					print ("No succesfull placement Water")
				else:
					print ("Water {0} placed!".format(W))
					gr = list(ngrid)
					W = 1


		# # Maisons
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

		# # Then bungalows
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
		generic.visualizeGrid(gr)


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

def genHome(grid, length, width, freespace, ID):
	"""
	Input is a grid, length, width, freespace and id.
	It calls placeHouse function using random coordinates.
	"""
	y = genY(grid, freespace, length)
	x = genX(grid, freespace, width)
	return generic.placeHouse(ID, width, length, freespace, y, x, grid)

def genWater(grid):
	"""
	Current problems:
	 - Priemgetallen zorgen voor extra loops 
	 	--> misschien eerst testen?
	 - Als eerste getal groot is heb je veel loops
	 - Functie is nog wat rommelig.

	 Takes as input a grid and outputs a list containing
	 tuples of max 4 water spaces using the following layout:
	 (width, length, ratio, size), where the water takes
	 20 percent of the total surface.

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
			# Starting from the square root causes the part to 
			# be more square instead of a straight line.
			init = round(math.sqrt(size))
			for i in range(init, 1, -1):
				if size % i == 0 and 1 <= math.ceil((size / i) / i) <= 4:
					w = i
					l = size / w

					# Reinit allowed surface
					allowed_surface -= size

					# Randomly switch width and length
					#
					#
					#
					#
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