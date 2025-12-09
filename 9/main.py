from dataclasses import dataclass
import math

INPUT_FILE = "9/test_input.txt"
INPUT_FILE = "9/input.txt"





coords = []




with open(INPUT_FILE) as f: 
    for line in f:

        x, y = line.strip().split(",")

        coords.append((int(x), int(y)))


# print(coords)

coords_set = set(coords)




def make_lines(points):
    res = []

    for i in range(len(points)):
        res.append((points[i], points[(i+1 )% len(points)]))
    return res

lines = make_lines(coords)

def area(pointA, pointB):
    return ((abs(pointA[0] - pointB[0])+1) * (abs(pointA[1] - pointB[1])+1) )


def first_part():

    result = 0

    for i in range(len(coords)):
        for j in range(i):
            cur_area = area(coords[i], coords[j])
            result = max(result, cur_area)

    print(f"Answer to the first part is {result}")


def get_red_tiles_with_Y_coord(coord: int, left_bount, right_bound):
    return [x for x in coords_set if x[1] == coord and left_bount <x[0] < right_bound]

def get_red_tiles_with_X_coord(coord: int, bottom_bound, top_bound):
    return [x for x in coords_set if x[0] == coord and bottom_bound < x[1] < top_bound]



def intersects(setA, setB):
    res = []
    for i in setA:
        for j in setB:

            if i[0][0] == i[1][0] and j[0][0] == j[1][0]:
                continue
            if i[0][1] == i[1][1] and j[0][1] == j[1][1]:
                continue

            assert i[0][0] == i[1][0] and j[0][1] == j[1][1] or i[0][1] == i[1][1] and j[0][0] == j[1][0]

            if i[0][0] == i[1][0]:
                vertical = i
                horizontal = j 
            else: 
                vertical = j
                horizontal = i

            leftx = min(horizontal[0][0], horizontal[1][0])
            rightx = max(horizontal[0][0], horizontal[1][0])

            topy = max(vertical[0][1], vertical[1][1])
            bottomy = min(vertical[0][1], vertical[1][1])

            # print(leftx ,vertical[0][0] ,rightx)


            if leftx < vertical[0][0] < rightx:
                if bottomy < horizontal[0][1] < topy:
                    return True
                
            
            # if i[0][0] == i[1][0]: # case when rectangle line is vertical

            #     red_on_edge = get_red_tiles_with_X_coord(i[0][0], bottomy, topy)

            # else:
            #     red_on_edge = get_red_tiles_with_Y_coord(i[0][1], leftx, rightx)
            
            # if len(red_on_edge) > 0:
            #     return True
                
            
            
    

    return False

            

def valid_rectangle(pointA, pointB):

    # if not (pointA[0], pointB[1]) in coords_set and not (pointB[0], pointA[1]) in coords_set:
    #     return False
    # Corners are anticlockwise, top right corner is starting
    #
    #     1 ---- 0
    #     |      |
    #     |      |
    #     2 ---- 3 
    #

    corners = [pointA, (pointA[0], pointB[1]), pointB, (pointB[0], pointA[1])]


    corners.sort(key= lambda x: (x[0],x[1]), reverse=True)
    corners[2], corners[3] = corners[3], corners[2]

    rectangle_lines = make_lines(corners)

    return not intersects(rectangle_lines, lines)

    return not curr_intersections



    # bottom_red_tiles = get_red_tiles_with_Y_coord(corners[2][1], corners[2][0], corners[3][0]) 
    # top_red_tiles = get_red_tiles_with_Y_coord(corners[0][1], corners[1][0], corners[0][0]) 
    
    # left_red_tiles = get_red_tiles_with_X_coord(corners[2][0], corners[2][1], corners[1][1]) 
    # right_red_tiles = get_red_tiles_with_X_coord(corners[0][0], corners[3][1], corners[0][1]) 

    # print(bottom_red_tiles, top_red_tiles, left_red_tiles, right_red_tiles) 

    


    # print(intersections(lines, rectangle_lines))
    

    
    return False


def second_part():
    result = 0

    possible_rectangles = []
    for i in range(len(coords)):
        for j in range(i):
            possible_rectangles.append((coords[i], coords[j], area(coords[i], coords[j])))
    
    possible_rectangles.sort(key=lambda x:x[2], reverse=True)
    # print(possible_rectangles)


    first_pass_rectangles = []
    for rectangle in possible_rectangles:
        # print(rectangle)
        if rectangle[2] > 2363592510:
            continue
        if rectangle[2] < 1414596883:
            break
        # print(rectangle)
        if not valid_rectangle(rectangle[0], rectangle[1]):
            continue
        first_pass_rectangles.append(rectangle)

    # print(first_pass_rectangles)

    for i in first_pass_rectangles:
        print(i)

    print(f"Answer to the second part is {result}")



if __name__ == "__main__":
    first_part()
    second_part()

