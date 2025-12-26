from dataclasses import dataclass
import math
from functools import cache
import queue
import itertools
import numpy as np
import scipy.optimize
import cvxpy as cp


INPUT_FILE = "10/test_input.txt"
# INPUT_FILE = "10/input.txt"


@dataclass
class Machine:
    light_diagram: tuple[bool]
    buttons: list[list[int]]
    joltage: tuple[int]


machines: list[Machine] = []




with open(INPUT_FILE) as f: 
    for line in f:

        square_bracket_end_pos = line.find("]")
        squigly_bracket_start_pos = line.find("{")

        light_diagram_str = line[1:square_bracket_end_pos]
        buttons_str = line[square_bracket_end_pos+2:  squigly_bracket_start_pos]

        joltage_str = line[squigly_bracket_start_pos+1: -1].strip("}")


        light_diagram = []
        for symbol in light_diagram_str:
            if symbol == "#":
                light_diagram.append(True)
            else:
                light_diagram.append(False)

        buttons = []
        for button in buttons_str.split():
            x = []
            for actual_button in button.strip().strip("()").split(","):
                x.append(int(actual_button))
            buttons.append(x)


        joltage = []
        for jolt in joltage_str.split(","):
            joltage.append(int(jolt))


        machine = Machine(tuple(light_diagram), buttons, tuple(joltage))
        machines.append(machine)





def calculate_minimum_presses_for_machine_part2(machine:Machine) -> int:

    return 0



def calculate_minimum_presses_for_machine_part1(machine:Machine) -> int:


    already_queued = set()


    def press_button(current_state, button):
        current_state = list(current_state)
        for index in button:
            current_state[index] = not current_state[index]
        return tuple(current_state)


    def func(start_state: tuple):
        state_queue: queue.PriorityQueue[tuple[int, tuple]] = queue.PriorityQueue()
        state_queue.put((0, start_state))
        iter = 1
        while not state_queue.empty():
            priority, queued_state = state_queue.get()
            if priority == iter:
                iter += 1 
            for x in machine.buttons:
                pressed_state = press_button(queued_state, x)

                if machine.light_diagram == pressed_state:
                    return iter
                
                if pressed_state not in already_queued:
                    state_queue.put((iter, pressed_state))
                    already_queued.add(pressed_state)
            


    result = func(tuple([False for x in machine.light_diagram]))

    assert result is not None



    return result



def first_part():

    result = 0

    for i in machines:
        result+= calculate_minimum_presses_for_machine_part1(i)


    print(f"Answer to the first part is {result}")


def second_part():
    result = 0

    for i in machines:
        result+= calculate_minimum_presses_for_machine_part2(i)

    print(f"Answer to the second part is {result}")




if __name__ == "__main__":
    first_part()
    second_part()

