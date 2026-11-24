# Program: Addition of 10 numbers

#0 LDRL r0 0
#1 LDRL r1 0
#2 Loop ADDL r1 r1 1
#3 ADD r0 r0 r1
#4 CMPL r1 10
#5 BNE Loop
#6 STOP
#JINENDRA BANTHIA 25E102A24
prog = ['LDRL r0 0','LDRL r1 0','ADDL r1 r1 1',
        'ADD r0 r0 r1','CMPL r1 10','BNE 2','STOP']

r = [0] * 8
z = 0
run = True
pc = 0

while run == True:

    inst = prog[pc] 
    oldPC = pc
    pc = pc + 1
    inst = inst.split(' ')

    if inst[0] == 'ADD':
        rd = int(inst[1][1])
        rS1 = int(inst[2][1])
        rS2 = int(inst[3][1])
        r[rd] = r[rS1] + r[rS2]
        print('PC = ',oldPC,'Instruction',inst[0],
              'r0 = ',r[0],'r1 = ',r[1])

    elif inst[0] == 'ADDL':
        rd = int(inst[1][1])
        rS1 = int(inst[2][1])
        literal = int(inst[3])
        r[rd] = r[rS1] + literal
        print('PC = ',oldPC,'Instruction',inst[0],
              'r0 = ',r[0],'r1 = ',r[1])

    elif inst[0] == 'BNE':
        print('PC = ',oldPC,'Instruction',inst[0],
              'r0 = ',r[0],'r1 = ',r[1],'z = ',z)
        if z == 0:
            pc = int(inst[1])
        print("**********************************************************************")

    elif inst[0] == 'CMPL':
        z = 0
        rVal = r[int(inst[1][1])]
        intVal = int(inst[2])
        if rVal == intVal:
            z = 1
        print('PC = ',oldPC,'Instruction',inst[0],
              'r0 = ',r[0],'r1 = ',r[1],'z = ',z)

    elif inst[0] == 'LDRL':
        rd = int(inst[1][1])
        print(rd)
        data = int(inst[2])
        r[rd] = data
        print('PC = ',oldPC,'Instruction',inst[0],
              'r0 = ',r[0],'r1 = ',r[1],'z = ',z)

    elif inst[0] == 'STOP':
        run = False
        print('End of program reached')
        print('PC = ',oldPC,'Instruction',inst[0],
              'r0 = ',r[0],'r1 = ',r[1],'z = ',z)

    else:
        run = False
        print('Error: illegal instruction ',inst)
        print('PC = ',oldPC,'Instruction',inst[0],
              'r0 = ',r[0],'r1 = ',r[1],'z = ',z)