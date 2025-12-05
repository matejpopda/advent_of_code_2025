import copy

INPUT_FILE = "5/test_input.txt"
INPUT_FILE = "5/test_input_extra.txt" # the original test input doesnt contain one specific test case thats tested here
INPUT_FILE = "5/input.txt"

fresh_ingredient_ranges = []
available_ingredients = []

with open(INPUT_FILE) as f: 
    found_empty_line_flag = False

    for line in f:

        if line.strip() == "":
            found_empty_line_flag = True
            continue

        if not found_empty_line_flag:
            cur_line = [int(x) for x in line.strip().split("-")]
            fresh_ingredient_ranges.append(cur_line)
        else:
            available_ingredients.append(int(line.strip()))


def check_if_fresh(ingredient_id:int):
    for i,j in fresh_ingredient_ranges:
        assert i<=j
        if i <= ingredient_id <= j:
            return True
    return False





def range_overlap(range1, range2):

    if range1[0] <= range2[0] <= range1[1]:
        return True

    if range2[0] <= range1[1] <= range2[1]:
        return True
    
    return False


def overlap(ranges: list):
    list_of_ranges = copy.deepcopy(ranges)

    list_of_ranges.sort(key=lambda x: (x[0], x[1]))

    bad_indexes = set()

    i = -1
    while i < len(list_of_ranges)-1:
        i += 1
        curr_min_index = i

        for j in range(i+1, len(list_of_ranges)):

            if list_of_ranges[curr_min_index][1] >= list_of_ranges[j][0]:
                if list_of_ranges[curr_min_index][1] < list_of_ranges[j][1]:
                    list_of_ranges[curr_min_index][1] = list_of_ranges[j][1]

                bad_indexes.add(j)
            else:
                break

    good_indexes = [x if x not in bad_indexes else 0 for x in range(len(list_of_ranges))]
    good_indexes = list(set(good_indexes))


    ranges_without_overlap = [list_of_ranges[x] for x in good_indexes]

    result = sum([x[1] - x[0]+1 for x in ranges_without_overlap])

    return result
        






    




def first_part():

    result = sum([1 if check_if_fresh(x) else 0 for x in available_ingredients])
    print(f"Answer to the first part is {result}")


def second_part():
    print(f"Answer to the second part is {overlap(fresh_ingredient_ranges)}")



if __name__ == "__main__":
    first_part()
    second_part()