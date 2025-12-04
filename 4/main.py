
INPUT_FILE = "4/test_input.txt"
INPUT_FILE = "4/input.txt"

table = []

with open(INPUT_FILE) as f: 
    for line in f:
        table.append(list(line.strip()))


def get_table_element(row, column, table):
    return table[row][column]

def get_neighborhood(row, column, table):
    result = []

    height = len(table)
    width = len(table[0])

    if row + 1 != height:
        result.append(get_table_element(row+1, column, table))
    if row != 0:
        result.append(get_table_element(row-1, column, table))

    if column + 1 != width:
        result.append(get_table_element(row, column+1, table))
    if column != 0:
        result.append(get_table_element(row, column-1, table))

    if row + 1 != height and column + 1 != width :
        result.append(get_table_element(row+1, column+1, table))
    if row != 0 and column + 1 != width :
        result.append(get_table_element(row-1, column+1, table))
    if row + 1 != height and column != 0 :
        result.append(get_table_element(row+1, column-1, table))
    if row != 0 and column  != 0 :
        result.append(get_table_element(row-1, column-1, table))

    return result


def check_neighborhood(row, column, table):
    neighborhood = get_neighborhood(row, column, table)

    return sum([1 if x=="@" else 0 for x in neighborhood])

def result_after_paper_removal(table):
    result = ""

    for row_index, row in enumerate(table):
        for column_index, column in enumerate(row):
            if column == ".":
                result += "."
                continue

            result += "x" if check_neighborhood(row_index, column_index, table) < 4  else "@"
        result += "\n"

    return result


def first_part():
    result = sum([1 if x=="x" else 0 for x in result_after_paper_removal(table)])

    print(f"Answer to the first part is {result}")


def second_part():
    result = 0
    current_table = table

    while True:

        string_with_marked_paper_for_removal = result_after_paper_removal(current_table)

        number_of_accessible_paper = sum([1 if x=="x" else 0 for x in string_with_marked_paper_for_removal])
        result += number_of_accessible_paper

        if number_of_accessible_paper == 0:
            break

        string_with_paper_removed = string_with_marked_paper_for_removal.replace("x",".")

        current_table = [] 
        for line in string_with_paper_removed.split():
            current_table.append(list(line.strip()))

    print(f"Answer to the second part is {result}")



if __name__ == "__main__":
    first_part()
    second_part()