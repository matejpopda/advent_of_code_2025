
INPUT_FILE = "3/test_input.txt"
INPUT_FILE = "3/input.txt"

banks = []

with open(INPUT_FILE) as f: 
    banks = [x.strip() for x in f.readlines()]



def highest_substring(bank:str):
    first_index, first_char = highest_number_in_string(bank[:-1])
    second_index, second_char = highest_number_in_string(bank[first_index + 1:])

    return int(first_char + second_char)


        
def highest_number_in_string(string:str):
    max_index, max_char = -1, "-1"
    for index, char in enumerate(string):
        if int(char) > int(max_char):
            max_index = index
            max_char = char
    assert max_char != "-1"
    return max_index, max_char



def first_part():
    result = 0
    for bank in banks:
        result += highest_substring(bank)
    
    print(f"Answer to the first part is {result}")



def highest_substring_part_2(bank:str, substring_length:int = 12):
    result = ""
    index = 0
    for i in range(substring_length - 1,-1,-1):

        subsubstring = bank[index:-i]

        if subsubstring == "":
            subsubstring = bank[index:]

        subsubstring_index, subsubstring_char = highest_number_in_string(subsubstring)
        index += subsubstring_index + 1
        result += subsubstring_char
    return int(result)

def second_part():
    result = 0
    for bank in banks:
        result += highest_substring_part_2(bank)
    
    print(f"Answer to the second part is {result}")



if __name__ == "__main__":
    first_part()
    second_part()