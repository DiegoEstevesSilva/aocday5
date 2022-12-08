stacks = [
    ['D','L','V','T','M','H','F'],
    ['H','Q','G','J','C','T','N','P'],
    ['R','S','D','M','P','H'],
    ['L','B','V','F'],
    ['N','H','G','L','Q'],
    ['W','B','D','G','R','M','P'],
    ['G','M','N','R','C','H','L','Q'],
    ['C','L','W'],
    ['R','D','L','Q','J','Z','M','T'],
]

def move_stacks(origin:int, destination:int, crates:int):
    """
    Move crates from origin to destination stack.

        origin: Index of the original stack.
        destination: Index of the destination stack.
        crates:  Number of crates to be moved.
    """
    for i in range(0,crates):
        crate = stacks[origin].pop(-1)
        stacks[destination].append(crate)


with open('day5 input.txt', mode='r') as file:
    instructions = file.readlines()

for step in instructions:
    step_parts = step.replace("\n","").split(" ")
    crates = int(step_parts[1])
    origin = int(step_parts[3]) - 1
    destination = int(step_parts[5]) - 1
    move_stacks(origin,destination, crates)

for item in stacks:
    print(item[-1])
