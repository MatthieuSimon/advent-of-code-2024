def combo_operand(operand, registers):
    operand_map = {
        4: registers[0],
        5: registers[1],
        6: registers[2]
    }
    return operand_map.get(operand, operand)

def divide_register(register_index, registers, operand):
    numerator = registers[0]
    denominator = 2 ** combo_operand(operand, registers)
    registers[register_index] = numerator // denominator

def run_instruction(opcode, operand, i, registers, output):
    if opcode == 0:
        divide_register(0, registers, operand)
    elif opcode == 1:
        registers[1] = registers[1] ^ operand
    elif opcode == 2:
        registers[1] = combo_operand(operand, registers) % 8
    elif opcode == 3:
        if registers[0] != 0:
            return operand
    elif opcode == 4:
        registers[1] = registers[1] ^ registers[2]
    elif opcode == 5:
        output.append(str(combo_operand(operand, registers) % 8) + ",")
    elif opcode == 6:
        divide_register(1, registers, operand)
    elif opcode == 7:
        divide_register(2, registers, operand)
    return i + 2

def main():
    inputs, registers, output = [], [], []
    with open("../input.txt") as file:
        inputs = []
        for line in file:
            inputs.append([x for x in line.strip()])

    for i in range(3):
        num = int("".join(inputs[i]).split(" ")[2])
        registers.append(num)

    program = [int(x) for x in inputs[4] if x.isdigit()]

    i = 0
    while i < len(program):
        opcode = program[i]
        operand = program[i+1]
        i = run_instruction(opcode, operand, i, registers, output)
    print("".join(output))

    
if __name__ == "__main__":
    main()