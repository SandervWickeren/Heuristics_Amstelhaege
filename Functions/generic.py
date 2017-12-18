"""
Uitleg:

Dit bestand bevat alle functies die voor alle
algoritme nodig zijn. Onder andere voor het
maken van de visualisatie of het berekenen
van de score. Uitleg over deze functies
staat onder de functie zelf.
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


def visualizeGrid(grid, name):
    """
    Takes in a grid and outputs a mapping of
    the grid using various colors using matplotlib.
    """
    import matplotlib.pyplot as plt
    from matplotlib import colors

    # Define colors [Background, house1, house2, house3, water, etc.]
    colormap = colors.ListedColormap(["#FFFFFF", "#F9A825", "#8BC34A", 
        "#D66EFF", "#2196F3", "#424242", "#9E9E9E"])

    # 0-1: white, 1-5: red etc.
    bounds = [0, 1, 2, 3, 4, 5, 8, 10]
    norm = colors.BoundaryNorm(bounds, colormap.N)

    # Make plot
    fig, ax = plt.subplots()
    ax.imshow(grid, cmap=colormap, norm=norm)

    # Give name
    plt.title(name)

    # Show plot
    plt.show()

    return


def checkOverlap(grid, start_y, start_x, house):
    """
    Takes as input the grid and the information from a house, it outputs
    true if it can be placed and false if it cannot.

    The way it works is quite simple. It checks al outside points based
    on a compass. It checks all eight furthest corners
    (from the freespace) and the  four corners of the house. Doing it
    this way is enough to prevent any overlap without checking
    every point.
    """

    # Using a small number of significant points to check if overlap
    # occurs saves instructions.
    allowed = [0, 4, 5]
    width = house.width
    length = house.length
    freespace = house.freespace

    try:
        # Check if not below zero
        if start_y < 0 or start_x < 0:
            return False

        # Check if correctly inside map (y)
        if start_y + 2 * freespace + length > len(grid):
            return False

        # Check if correctly in map (x)
        if start_x + 2 * freespace + width > len(grid[0]):
            return False

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

        # Because there are different sizes of freespace it is possible that part of a new house is
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
    except IndexError:
        print ("Index Error")
        return False


def placeHouse(grid, house):
    """
    Takes as input the grid and an instance of the house class.
    It tries to place the house on the coordinates given from the
    house. When succesfull it 'll return the grid with the house
    placed, otherwise it 'll return false.
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


def removeHouse(grid, house):
    """
    Takes as input the grid and an instance of the
    house class. It returns a grid with the house
    removed.
    """

    # Define start coordinates:
    start_y = house.y - house.freespace
    start_x = house.x - house.freespace

    # Remove house
    for y in range(0, house.freespace * 2 + house.length):
        for x in range(0, house.freespace * 2 + house.width):
            try:
                grid[start_y + y][start_x + x] = 0
            except Exception as e:
                print (e)
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
    SW = (y + length + freespace, x - freespace)
    SE = (y + length + freespace, x + width + freespace)
    check_coor = [(NW[0], NW[1]),  # NW
                  (NW[0], NW[1] + width + 2* freespace),  # NE
                  (NW[0] + length + freespace, NW[1]),  # SW
                  (NW[0] + length + 2 * freespace, NW[1] + width + 2* freespace)]  # SE

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
                    return False
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
                    return False
        except:
            pass

    # NW-SW
    for y in range(SW[0] - NW[0]):

        # Set coordinates
        point_y = NW[0] + y 
        point_x = NW[1] 
        
        try:
            if 0 <= point_x <= max_x and 0 <= point_y <= max_y:
                if grid[point_y][point_x] not in allowed:
                    return False
        except:
            pass

    # If everything went fine, return
    return True


def calculateScore(grid, placed_houses):
    """
    It takes as input the grid and placed_houses.
    Using the allowedFreespace function it can
    determine the maximum amount of extra freespace the
    current house can have. Important to note here is that
    the extra space outside of the map is counted as infinity
    so when a house is placed at the left border and the 
    nearest house is 5 extra meters further it 'll count 5
    extra meters freespace. Based on the price of the
    house and its price increase per meter it 'll add 
    the amount to the total price. Finally it returns
    the value or the score of the grid.
    """
    total_price = 0

    for h in placed_houses:
        if h.h_type != "W":

            # Points that are allowed as extra freespace (water)
            allowed = [0, 5, 4]

            check = True
            distance = 0
            while check:
                distance += 1
                total_distance = h.freespace + distance
                check = allowedFreespace(grid, h, total_distance, allowed)              

            # Calc extra meters rounding to lowest integer.
            extra_meters = math.floor(distance / h.resolution)

            # Calculate the price
            sell_price = h.price * (1 + (h.priceimprovement / 100) * extra_meters)

            total_price += sell_price

    return total_price


# Helper functions
def printGrid(grid):
    """
    Prints the raw grid in a visual pleasing
    manner. 
    """
    for x in grid:
        print (x)


def transformtoGrid(placed_houses, resolution):
    """
    Converts a list of instances of the class house
    into a grid
    """

    # Generate grid
    grid = genMap(180 * resolution, 160 * resolution)

    for obj in placed_houses:
        grid = placeHouse(grid, obj)
        
        # Return false if it isn't a valid map.
        if grid is False:
            return False

    return grid