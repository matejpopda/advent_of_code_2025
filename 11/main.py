from typing import Iterable
from functools import lru_cache

test_input = False


INPUT_FILE = "11/input.txt"

if test_input:
    INPUT_FILE = "11/test_input_part1.txt"


connection_dict: dict[str, list[str]] = {}

with open(INPUT_FILE) as f: 
    for line in f:
        key, contents_str = line.strip().split(":")
        connection_dict[key] = contents_str.split()



def first_part():
    result = 0

    x = ["you"]

    def helper(stuff_to_go_over: list[str]):
        nonlocal result
        next_iter: list[str] = []
        for i in stuff_to_go_over:

            if i == "out":
                result += 1
                continue

            next_iter = next_iter + connection_dict[i]

        return next_iter
    
    while len(x) > 0:
        x = helper(x)

    

    print(f"Answer to the first part is {result}")


if __name__ == "__main__":
    first_part()


if test_input:
    INPUT_FILE = "11/test_input_part2.txt"

connection_dict: dict[str, list[str]] = {}

with open(INPUT_FILE) as f: 
    for line in f:
        key, contents_str = line.strip().split(":")
        connection_dict[key] = contents_str.split()



inverted_connection_dict: dict[str, list[str]] = {"out":[]}
for i in connection_dict:
    inverted_connection_dict[i] = []

for i in connection_dict:
    for j in connection_dict[i]:
        inverted_connection_dict[j].append(i)


def second_part():
    ending_point = ("out", True, True)

    @lru_cache(None)
    def paths_into_port(port_nfo:tuple[str, bool, bool]) -> int: 

        port, visited_fft, visited_dac = port_nfo

        if port == "fft": 
            visited_fft = False
        if port == "dac":
            visited_dac = False

        if port == "svr":
            if (not visited_dac) and (not visited_fft):
                return 1
            else:
                return 0

        result = 0
        for input_port in inverted_connection_dict[port]:

            result += paths_into_port((input_port, visited_fft, visited_dac))

        return result
    

    print(f"Answer to the second part is {paths_into_port(ending_point)}")





if __name__ == "__main__":
    second_part()
