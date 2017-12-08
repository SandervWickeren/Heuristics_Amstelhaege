def start_simannealing(grid, placed_houses, rounds):
    """
    1. Generate a random grid with houses, water
    2. Calculate score with score function
    3. Move houses and place it N, calculate score
        - Improved? Houses on new place. Not improved? Further to N.
        - If this is not improved after N steps, next step.
    4. Move houses and place it E, calculate score
        - Improved? Houses on new place. Not improved? Further to E.
        - If this is not improved after N steps, next step.
    5. Move houses and place it S, calculate score
        - Improved? Houses on new place. Not improved? Further to S.
        - If this is not improved after N steps, next step.
    6. Move houses and place it W, calculate score
        - Improved? Houses on new place. Not improved? Further to W.
        - If this is not improved after N steps, stop.
    7. Compare score function solution:
        - Cnew < Cold --> move to new solution
        - Cnew > Cold --> maybe move to new solution
            - Acceptance probability for moving to solution or not.
    8. Repeat step 3-8 until acceptable solution is found, or when reaching
        some maximum number of iterations

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

    # Temperature of which iteration we are on
    # Hierbij heb ik een standaard waarde uitgekozen, kan aangepast worden
    temperature = 1
    # Hierbij ook
    minimal_temperature = 0.0001
    start_temperature = temperature
    count = 0


    # Get start score
	score = generic.calculateScore(grid, placed_houses)
	f_score = score

    while temperature > minimal_temperature:

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


						# Debug
						#print ("Before --- X: {0} , Y: {1}".format(h.x, h.y))

						# Remove the house from the grid
						# newgrid = generic.removeHouse(grid, h)


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

						#print ("After --- X: {0} , Y: {1}".format(h.x, h.y))

						# Try to place the house with the new changed coordinate
						#grid = generic.placeHouse(newgrid, h)
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

                            # When new score is better than old score,
                            # Move to new solution
							if new_score > score:
                                score = new_score

                                # Update same_score_count:
								same_score_count = 0

							# When score stays the same update count.
							elif new_score == score:
								same_score_count += 1

                            # When new score is worse than old score,
                            # Maybe move to new solution
                            elif new_score < score:

                                #hier moet een acceptance probability komen:
                                #The acceptance probability function takes in the old cost,
                                # new cost, and current temperature and spits out a number between 0 and 1,
                                # which is a sort of recommendation on whether or not to jump to the
                                #new solution.

                                #Once the acceptance probability is calculated, it's compared to a
                                #randomly-generated number between 0 and 1. If the acceptance probability
                                #is larger than the random number, you're switching!
                                # (score - new_score)/temperature

                            # Temperature decreasing by multiplying it by a constant called 'a',
                            # typical choices are between 0.8 and 0.99
                            count += 1
                            # Volgens mij kan je met deze de verkorting aangeven, dus linear/exponentieel etc.
                            #of met de acceptatie kans
                            temperature = start_temperature * 0.9
