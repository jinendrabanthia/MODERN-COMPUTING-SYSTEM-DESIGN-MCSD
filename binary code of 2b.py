mem = [0] * 12
pc = 0
r0 = 0

mem[0] = 0b000100001010
mem[1] = 0b001000000111
mem[2] = 0b011000001001
mem[3] = 0b111100000000
mem[7] = 8


def fetch(memory):
    global pc

    ir = memory[pc]
    pc = pc + 1

    print(f"\n[FETCH] PC = {pc-1}, IR = {ir:012b}")

    return (ir >> 8, ir & 0xFF)


run = 1

while run == 1:
    opcode, operand = fetch(mem)
    print(f"[DECODE] Opcode={opcode:04b}, Operand={operand}")

    if opcode == 0b1111:
        run = 0
        print("[EXECUTE] HALT encountered. Stopping execution.")

    elif opcode == 0b0001:
        r0 = operand
        print(f"[EXECUTE] r0 <- {operand} ({r0})")

    elif opcode == 0b0010:
        mar = operand
        mbr = mem[mar]
        r0 = mbr + r0
        print(f"[EXECUTE] r0 <- r0 + mem[{mar}] ({mbr}) = {r0}")

    elif opcode == 0b0110:
        mem[operand] = r0
        print(f"[EXECUTE] mem[{operand}] <- r0 ({r0})")

    print('PC =', pc - 1, 'Opcode =', opcode, 'Register r0 =', r0)

print("\nFinal Memory:", mem)