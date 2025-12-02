import re

# INPUT_FILE = "2/test_input.txt"
INPUT_FILE = "2/input.txt"


ranges = []

with open(INPUT_FILE) as f: 
    line = f.readline()
    ranges = line.split(",")



def range_from_input_range(range_string: str):
    # input is for example "132-156"
    numbers = range_string.split("-")
    return range(int(numbers[0]), int(numbers[1]) + 1)

def number_of_digits(number:int):
    return len(str(number))


def first_part():
    result = 0
    for i in ranges:
        for number in range_from_input_range(i):
            length_of_number = number_of_digits(number)
            if length_of_number % 2 == 1:
                continue
            

            half_index = length_of_number//2
            if str(number)[:half_index] == str(number)[half_index:]:
                result += number

    print(f"Result of the first part is {result}")




def check_if_repeating(number):
    pattern: re.Pattern = re.compile(r"(\b\d+)\1{1,}\b")

    return pattern.match(str(number))

def second_part():
    result = 0
    for i in ranges:
        for number in range_from_input_range(i):
            re_result = check_if_repeating(number)
            if re_result is None:
                continue
            
            assert isinstance(re_result, re.Match)

            result += number



    print(f"Result of the first part is {result}")



if __name__ == "__main__":
    first_part()
    second_part()