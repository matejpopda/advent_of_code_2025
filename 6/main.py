from warnings import deprecated

INPUT_FILE = "6/test_input.txt"
INPUT_FILE = "6/input.txt"



MAX_NUMBER_LENGTH = 5

numbers = []
operations = []

input_file_string = ""

with open(INPUT_FILE) as f: 
    for line in f:
        if "+" in line or "*" in line:
            operations = line.strip().split()
            break
        numbers.append(line.strip().split())
        input_file_string += line






def column_op(index, char_table):

    if operations[index] == "*":
        result = 1

        for i in range(len(char_table)):
            character = char_table[i][index]
            result *= int(character)

    elif operations[index] == "+":
        result = 0

        for i in range(len(char_table)):
            character = char_table[i][index]
            result += int(character)
    else:
        raise RuntimeError

    return result


@deprecated("Use the faster one")
def parse_for_second_task():
    # first we rotate the string
    list_of_input = input_file_string.split("\n")
    input_chars = [list(x) for x in list_of_input if len(x) != 0]

    result_string = ""
    for column in range(len(input_chars[0])): 
        for line in range(len(input_chars)): 
            result_string += input_chars[line][column]
        result_string += "\n"

    # then we parse
    result = [[] for _ in range(len(operations))]
    result_index = 0
    for num in result_string.split("\n"):
        num = num.strip()


        if num == "":
            result_index += 1
            continue

        result[result_index].append(num)


    return result

def parse_for_second_task_faster():

    # first we rotate the string
    list_of_input = input_file_string.split("\n")
    input_chars = [list(x) for x in list_of_input if len(x) != 0]

    result = [[] for _ in range(len(operations))]
    result_index = 0


    for column in range(len(input_chars[0])): 
        result_string = ""

        for line in range(len(input_chars)): 
            result_string += input_chars[line][column]

        num = result_string.strip()


        if num == "":
            result_index += 1
            continue

        result[result_index].append(num)


    return result

def column_op_for_part_2(index, parsed_list):

    if operations[index] == "*":
        result = 1

        for i in parsed_list[index]:
            result *= int(i)

    elif operations[index] == "+":
        result = 0

        for i in parsed_list[index]:
            result += int(i)
    else:
        raise RuntimeError

    return result


def first_part():
    result = 0

    for i in range(len(operations)):
        result += column_op(i, numbers)

    print(f"Answer to the first part is {result}")


def second_part():
    result = 0

    for i in range(len(operations)):
        result += column_op_for_part_2(i, parse_for_second_task_faster())

    print(f"Answer to the second part is {result}")



if __name__ == "__main__":
    first_part()
    second_part()

