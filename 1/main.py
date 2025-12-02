



DIAL_START_NUMBER = 50
DIAL_SIZE = 100

class Dial():
    def __init__(self):
        self.dial_size = DIAL_SIZE
        self.current_number = DIAL_START_NUMBER

    def one_step(self, direction, step_size):
        
        if direction == "L":
            self.current_number = (self.current_number - step_size) % self.dial_size
        elif direction == "R":
            self.current_number = (self.current_number + step_size) % self.dial_size
        else:
            raise ValueError()
        
    def check_if_zero(self):
        return self.current_number == 0


def parse_line(line: str):
    direction = line[0]
    step_size = int(line[1:])
    return direction, step_size



def first_part():
    dial = Dial()
    result = 0

    with open("1/input.txt") as file:
        for line in file:
            direction, step_size = parse_line(line)
            dial.one_step(direction=direction, step_size=step_size)

            if dial.check_if_zero():
                result += 1

    print(f"Result for the first part is {result}.")


def second_part():
    dial = Dial()
    result = 0

    with open("1/input.txt") as file:
        for line in file:
            direction, step_size = parse_line(line)

            # multiple rotations get taken of here
            result += step_size // DIAL_SIZE

            previous_number = dial.current_number
            dial.one_step(direction=direction, step_size=step_size)
            current_number = dial.current_number


            if direction == "L" and previous_number == 0:
                previous_number = 100
            # print(previous_number,current_number, direction)
            if direction == "L" and previous_number < current_number:
                result += 1
            elif direction == "R" and previous_number > current_number: 
                result += 1
            elif dial.check_if_zero():
                result += 1

    print(f"Result for the second part is {result}.")



if __name__ == "__main__":
    first_part()
    second_part()


