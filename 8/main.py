from dataclasses import dataclass
import math

INPUT_FILE = "8/test_input.txt"
INPUT_FILE = "8/input.txt"


if "test" in INPUT_FILE:
    ITERATION_COUNT = 10
else:
    ITERATION_COUNT = 1000


boxes = []

@dataclass
class Box():
    x:int
    y:int
    z:int


with open(INPUT_FILE) as f: 
    for line in f:

        x,y,z = tuple(line.split(","))

        box = Box(int(x),int(y),int(z))

        boxes.append(box)


def distance(a: Box, b: Box):
    return math.sqrt((a.x - b.x)**2 + (a.y - b.y)**2 + (a.z - b.z) ** 2)

distance_matrix = [[math.inf]* len(boxes) for _ in range(len(boxes))]
connected_matrix = [[False]* len(boxes) for _ in range(len(boxes))]

for i in range(len(boxes)):
    for j in range(i):
        distance_matrix[i][j] = distance(boxes[i], boxes[j])

def find_closest_unused_index():
    cur_min = math.inf
    min_i = None
    min_j = None
    for i in range(len(boxes)):
        for j in range(len(boxes)):
            if connected_matrix[i][j]:
                continue

            if distance_matrix[i][j] < cur_min:
                cur_min = distance_matrix[i][j]
                min_i = i
                min_j = j
    
    assert min_i is not None
    assert min_j is not None
    return min_i, min_j


current_circuits: list[list[int]] = [[x] for x in range(len(boxes))]

def connect_closest():

    i,j = find_closest_unused_index()

    connected_matrix[i][j] = True


    copy_indexes = []
    for k, circuit in enumerate(current_circuits):
        if i in circuit:
            copy_indexes.append(k)
        if j in circuit:
            copy_indexes.append(k)
    
    assert len(copy_indexes) == 2

    if copy_indexes[0] == copy_indexes[1]:
        return
    
    # Could be more efficient, would need a different data structure
    for box in current_circuits.pop(max(copy_indexes)):
        current_circuits[min(copy_indexes)].append(box)

    return i,j



def first_part():
    for _ in range(ITERATION_COUNT):
        connect_closest()

    current_circuits.sort(key=lambda x: len(x), reverse=True)

    result = math.prod([len(current_circuits[x]) for x in range(3)])


    print(f"Answer to the first part is {result}")


def second_part():

    result_indexes = None

    while len(current_circuits) > 1:
        temp = connect_closest()
        if temp is not None:
            result_indexes = temp


    assert result_indexes is not None


    result = boxes[result_indexes[0]].x * boxes[result_indexes[1]].x

    print(f"Answer to the second part is {result}")



if __name__ == "__main__":
    first_part()
    second_part()

