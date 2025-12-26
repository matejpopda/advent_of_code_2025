from dataclasses import dataclass
import math


INPUT_FILE = "12/input.txt"




gifts: list["Gift"] = []

trees: list["Tree"] = []

@dataclass
class Tree():
    width: int
    height: int
    requirements: tuple[int]

    @property
    def area(self):
        return self.width * self.height

@dataclass
class Gift():
    gift: tuple[tuple, tuple, tuple]

    @property
    def area_taken(self):
        res = 0
        for i in self.gift:
            for j in i:
                if j == "#":
                    res+=1
        return res

with open(INPUT_FILE) as f: 
    lines = f.readlines()

    for i in range(6):
        gift = Gift(gift=(tuple(lines[1+i*5].strip()),
                tuple(lines[2+i*5].strip()),
                tuple(lines[3+i*5].strip())))

        gifts.append(gift)

    for i in lines[30:]:

        i = i.strip()
        
        xpos = i.find("x")
        colon_pos = i.find(":")



        width = int(i[:xpos])
        height = int(i[xpos+1:colon_pos])

        requirements:tuple[int] = tuple(int(x) for x in i[colon_pos+1:].strip().split()) # type: ignore


        tree = Tree(width=width, height=height, requirements=requirements)

        trees.append(tree)



def gifts_take_more_area_than_under_tree(tree: Tree):

    min_gift_area = 0
    for gift_index, how_many_gifts in enumerate(tree.requirements):
        min_gift_area += gifts[gift_index].area_taken * how_many_gifts



    return min_gift_area > tree.area

def do_we_need_to_interlock(tree: Tree):
    total_gifts = sum(tree.requirements)

    gifts_that_fit_without_interlocks = (tree.height//3) * (tree.width//3)


    return total_gifts > gifts_that_fit_without_interlocks


def first_part():

    result = 0

    for tree in trees:
        print(tree)

        if gifts_take_more_area_than_under_tree(tree):
            continue

        if do_we_need_to_interlock(tree):
            assert False
            continue
        
        result+=1
    

    
    print(f"Answer to the second part is {result}")

def second_part():
    result = 0

    print(f"Answer to the second part is {result}")




if __name__ == "__main__":
    first_part()
    second_part()

