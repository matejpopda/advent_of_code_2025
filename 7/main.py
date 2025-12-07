
INPUT_FILE = "7/test_input.txt"
INPUT_FILE = "7/input.txt"


lines = []


with open(INPUT_FILE) as f: 
    for line in f:

        lines.append(line.strip())




def first_part():
    result = 0

    assert isinstance(lines[0], str)

    curr_beams = ["."] * len(lines[0])
    curr_beams[lines[0].find("S")] = "|"

    for line in lines:
        for i in range(len(line)):
            if curr_beams[i] == "|" and line[i] == "^":
                curr_beams[i+1] = "|"
                curr_beams[i]  = "."
                curr_beams[i-1] = "|"
                result += 1

    print(f"Answer to the first part is {result}")


def second_part():
    result = 0

    assert isinstance(lines[0], str)

    curr_beams = [0] * len(lines[0])
    curr_beams[lines[0].find("S")] = 1

    for line in lines:
        for i in range(len(line)):
            if curr_beams[i] > 0 and line[i] == "^":
                curr_beams[i+1] += curr_beams[i] 
                curr_beams[i-1] += curr_beams[i] 
                curr_beams[i]  = 0


    result = sum(curr_beams)


    print(f"Answer to the second part is {result}")



if __name__ == "__main__":
    first_part()
    second_part()

