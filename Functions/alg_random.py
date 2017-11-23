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
		familyHome_count = 0.60 * variant
		bungalow_count = 0.25 * variant
		maison_count = 0.15 * variant

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

				Water = class_house.house(water_parts[part][1], water_parts[part][0], 
									   0, 0, 0, 4, "W", resolution)

				ngrid = genHome(gr, Water)

				# Check for success:
				if ngrid == False:
					print ("No succesfull placement Water")
				else:
					print ("Water {0} placed!".format(W))
					gr = list(ngrid)
					W = 1


		# Maisons
		M = 0
		while M != maison_count:

			# Define class instance
			Maison = class_house.house(mais_length, mais_width, 
									   mais_freespace, 610000, 6, 1, "M", resolution)

			ngrid = genHome(gr, Maison)

			# Check if house succsfully placed:
			if ngrid == False:
				print ("No succesfull placement Maison")
			else:
				print ("Maison {0} placed!".format(M))
				gr = list(ngrid)

				# Add maison to list
				placed_houses.append(Maison)


				M += 1

		# Then bungalows
		B = 0
		while B != bungalow_count:

			# Define class instance
			Bungalow = class_house.house(bung_length, bung_width, 
									   bung_freespace, 399000, 4, 2, "B", resolution)

			ngrid = genHome(gr, Bungalow)

			# Check for succes:
			if ngrid == False:
				print ("No succesfull placement Bungalow")
			else:
				print ("Bungalow {0} placed!".format(B))
				gr = list(ngrid)

				# Add maison to list
				placed_houses.append(Bungalow)

				B += 1 

		# Then Family homes
		F = 0
		while F != familyHome_count:

			# Define class instance
			Familyhome = class_house.house(fam_length, fam_width, 
									   fam_freespace, 285000, 3, 3, "F", resolution)

			ngrid = genHome(gr, Familyhome)

			# Check for succes:
			if ngrid == False:
				print ("No succesfull placement Family Home")
			else:
				print ("Family home {0} placed!".format(F))
				gr = list(ngrid)

				# Add maison to list
				placed_houses.append(Familyhome)

				F += 1


		# Calculate score using Placed houses
		print ("Score of the map is: {0}".format(generic.calculateScore(gr, placed_houses)))


		# Visualize the grid
		print ("Generating map..")
		# for x in placed_houses:
		# 	print ("({0},{1})".format(x.y,x.x))
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

def genHome(grid, house):
	"""
	Input is a grid, length, width, freespace and id.
	It calls placeHouse function using random coordinates.
	"""
	y = genY(grid, house.freespace, house.length)
	x = genX(grid, house.freespace, house.width)
	house.setX(x)
	house.setY(y)
	return generic.placeHouse(grid, house)

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
					coinflip = random.randint(1, 2)
					if coinflip == 1:
						water_surfaces.append((w, int(l), round(l / w, 2), size))
					else:
						water_surfaces.append((int(l), w, round(l / w, 2), size))
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