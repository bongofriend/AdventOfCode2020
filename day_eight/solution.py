from os import path
import copy

def process_commands(commands: list[str]) -> list:
    current_instruction: int = 0
    acc: int = 0
    executed_commands: list[int] = list()
    while current_instruction < len(commands):
        if current_instruction in executed_commands:
            return [True, acc]
        command = commands[current_instruction]
        if "acc" in command:
            acc += int(command.split()[1])
            executed_commands.append(current_instruction)
            current_instruction += 1
        elif "jmp" in command:
            value = int(command.split()[1])
            executed_commands.append(current_instruction)
            current_instruction += value
        elif "nop" in command:
            executed_commands.append(current_instruction)
            current_instruction += 1
    return [False, acc]

def run(commands: list[str]):
    for i in range(0, len(commands)):
        command = commands[i]
        if 'acc' in command:
            continue 
        if 'jmp' in command:
            new_command = command.replace('jmp', 'nop')
        elif 'nop' in command:
            new_command = command.replace('nop', 'jmp')
        new_commands = copy.deepcopy(commands)
        new_commands[i] = new_command 
        [hasLoop, acc] = process_commands(new_commands)
        if not hasLoop:
            return acc






current_dir = path.dirname(path.abspath(__file__))
with open(path.join(current_dir, "input.txt"), "r") as f:
    commands = [l.rstrip() for l in f.readlines()]
    result = run(commands)
    print(result)

