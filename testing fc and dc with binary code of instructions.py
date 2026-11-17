#1(b): Testing Fetch and Decode Cycles using Binary Code

mem = [0] * 16
pc = 0

mem[0] = 0b000100001010
mem[1] = 0b001000000111
mem[2] = 0b011000001001
mem[3] = 0b111100000000
mem[7] = 8

def fetch(memory):
    global pc

    mar = pc
    pc = pc + 1
    mbr = memory[mar]
    ir = mbr

    cu = ir >> 8
    address = ir & 0xFF

    print("\n=== Instruction Cycle ===")
    print(f"[FETCH] PC={pc-1}, MAR={mar}, MBR={mbr:012b}, IR={ir:012b}")

    return (cu, address)


opCode, address = fetch(mem)
print("[DECODE] PC =", pc-1, "Opcode =", opCode, "Operand =", address)

opCode, address = fetch(mem)
print("[DECODE] PC =", pc-1, "Opcode =", opCode, "Operand =", address)

opCode, address = fetch(mem)
print("[DECODE] PC =", pc-1, "Opcode =", opCode, "Operand =", address)

opCode, address = fetch(mem)
print("[DECODE] PC =", pc-1, "Opcode =", opCode, "Operand =", address)