"""
Uitleg:

Het hillclimb algoritme werkt in een aantal 
	stappen:

	1. Voor elke windrichting / kant: Noord, oost, zuid
	en west voer stap 2 uit
	2. Voor elk huis in de grid voer stap 3-5 uit

	3. Verplaats het huis naar de gegeven richting
	4. Check de score
	5. Bij verbetering of gelijke score, verplaatst het
	huis verder naar de gegeven richting. Bij een daling
	laat je het huis staan op de plek voor de daling.

We hebben gekozen om het voor elke kant doen omdat
dit beter garandeert dat alle huizen zo ver mogelijk
uit elkaar worden gedreven. Stappen van 5 worden gekozen,
omdat er slechts per meter een prijsstijging plaastvindt
en het grid in decimeters werkt, waardoor verplaatsing per
meter in het slechtse geval maximaal na 10 berekeningen
pas verbetert, waardoor het een heel langzaam algoritme
wordt.
"""


def start_hillclimb(grid, placed_houses, rounds):
	"""
	Takes as input the grid, a list of instances from
	the house Class (placed_houses) and the number of 
	full rounds it should do.

	It saves the found grid to a file and returns the
	new grid and updated placed_houses list.
	"""
	import random
	import generic
	import sys
	import os
	import platform

	# Get current os
	os_name = platform.system()

	if os_name == "Windows":
		sp = "\\"
		i = -1
	elif os_name == "Darwin":
		sp = "/"
		i = -1

	# Get current location
	dir_path = os.path.dirname(os.path.realpath(__file__))

	sys.path.insert(0, dir_path.split(sp)[i] + "\Results")
	import read_write


	# Check if grid is given
	if grid == False:
		# Generate the grid
		grid = generic.transformtoGrid(placed_houses, 10)

	# Choose to amount of steps it should take for
	# every loop 1 = 0.1 meter
	step = 5

	# Get start score
	score = generic.calculateScore(grid, placed_houses)
	f_score = score

	for loop in range(rounds):
		print ("Round {0}/{1}".format(loop + 1, rounds))
		print ("--------------")
		for side in range(4):
			for h in placed_houses:
				print ("Checking house {0}/{1} - Side: {2}/4".format(placed_houses.index(h), len(placed_houses), side + 1))
				if h.h_type != "W":

					# Counts the amount of times the same score is produced
					same_score_count = 0
					
					# Used to break the for loop.
					abort = False
					loops = 0

					# Loop the given amount of times.
					while abort == False:

						# Save the old coordinates
						old_x = h.x
						old_y = h.y
						if grid == False:
							print ("Returned False")
							abort = True
						else:
							old_grid = list(grid)

						# Check which side it has to move to:
						if side == 0:
							# Reduce y to move to the north.
							h.reduce_y(step)

						elif side == 1:
							# Increase x to move to the east
							h.increase_x(step)

						elif side == 2:
							# Increase y to move to the south
							h.increase_y(step)

						elif side == 3:
							# Decrease x to move to the west
							h.reduce_x(step)
						

						# Try to place the house with the new changed coordinate
						grid = generic.transformtoGrid(placed_houses, 10)
						if grid == False:
							print ("Returned False")

						# Check if valid positioned
						if grid != False:

							# Get the new score
							new_score = generic.calculateScore(grid, placed_houses)

							# Score feedback print
							if new_score != score:
								print ("Loop {0}: O: {1} -- N: {2} -- D: {3}".format(loops,
									score, new_score, new_score - score))
							
							# Only stop when the score decreases
							if new_score < score:
								abort = True

							# When score stays the same update count.
							elif new_score == score:
								same_score_count += 1

							# Otherwise set new score
							else:
								score = new_score

								# Update same_score_count:
								same_score_count = 0


						# Abort when it cannot be placed on a valid spot.
						else:
							abort = True

						# Add one to loops:
						loops += 1

						# temporary max:
						if same_score_count == 30:
							abort = True


					# Give back the best coordinates
					h.set_x(old_x)
					h.set_y(old_y)

					# Visualize change
					print ("In {0} loops".format(loops))
					print ("Old score: {0}, New score: {1}".format(f_score, score))
					print ("X: {0}, Y: {1}".format(h.x, h.y))

	
	# Save result
	variant = 20
	fname = "Type{0}HC - {1}".format(variant, score)
	read_write.write(fname, placed_houses)
	print ("Writing to file..")

	return old_grid, score

print ("alg_hillclimb imported")