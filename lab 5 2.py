# Simple CPU instruction(Data Transfer) interpreter.
# Direct instruction interpretation.
# Class 0: no operand NOP
# Class 1: register,literal LDRL r2,1
# Class 2: register,register MOV r1,r2
# Class 3: register,[register] LDRI r1,[r2]
#JINENDRA BANTHIA 25E102A24
sFile = ['LDRL r2,1','LDRL r0,4','NOP','STRI r0,[r2]',
         'LDRI r3,[r2]', 'MOV r1,r2','STOP']

codes = {'NOP':[0],'STOP':[0],'LDRL':[1],
         'MOV':[2],'LDRI':[3],'STRI':[3]}

reg1 = {'r0':0,'r1':1,'r2':2,'r3':3}
reg2 = {'[r0]':0,'[r1]':1,'[r2]':2,'[r3]':3}

r = [0] * 4
r[0],r[1],r[2],r[3] = 1,2,3,8

m = [0] * 8
pc = 0
go = 1
z = 0

while go == 1:

    thisLine = sFile[pc]
    pcOld = pc
    pc = pc + 1
    pcNew = pc

    temp = thisLine.replace(',', ' ')
    print(temp)

    tokens = temp.split()
    mnemonic = tokens[0]
    opClass = codes[mnemonic][0]

    print(f'opcode Class:{opClass}')

    rD,rDval,rS1,rS1val,rS2,rS2val,lit, \
    rPnt,rPntV = 0,0,0,0,0,0,0,0,0

    if opClass in [0]:
        pass

    if opClass in [1,2,3]:
        rD = reg1[tokens[1]]
        print(f'Destination Register:{rD}')
        rDval = r[rD]

    if opClass in [1]:
        lit = int(tokens[-1])
        print(f'literal is:{lit}')

    if opClass in [2]:
        rS1 = reg1[tokens[2]]
        print(rS1)
        rS1val = r[rS1]

    if opClass in [3]:
        rPnt = reg2[tokens[2]]
        rPntV = r[rPnt]

    if mnemonic == 'STOP':
        go = 0
        print('Program terminated')

    elif mnemonic == 'NOP':
        pass

    elif mnemonic == 'MOV':
        r[rD] = rS1val

    elif mnemonic == 'LDRL':
        r[rD] = lit

    elif mnemonic == 'LDRI':
        r[rD] = m[rPntV]

    elif mnemonic == 'STRI':
        m[rPntV] = rDval

    regs = ' '.join('%02x' % b for b in r)
    mem = ' '.join('%02x' % b for b in m)

    print('pc_Old =','{:<3}'.format(pcOld),
          'pc_New =','{:<3}'.format(pcNew),
          '{:<14}'.format(thisLine),
          'Regs =',regs, 'Mem =',mem, 'z =', z)

    x = input('>>> ')