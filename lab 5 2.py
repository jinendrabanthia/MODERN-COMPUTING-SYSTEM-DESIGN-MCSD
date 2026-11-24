# Simple CPU instruction interpreter with memory and Branch instruction.
# Direct instruction interpretation.
# Class 0: no operand NOP
# Class 1: literal BEQ 3
# Class 2: register INC r1
# Class 3: register,literal LDRL r1,5
# Class 4: register,register, MOV r1,r2
# Class 5: register,register,literal ADDL r1,r2,5
# Class 6: register,register,register ADD r1,r2,r3
# Class 7: register,[register] LDRI r1,[r2]
#JINENDRA BANTHIA 25E102A24
sFile = ['LDRL r2,1','LDRL r0,4','NOP','STRI r0,[r2]',
         'LDRI r3,[r2]','INC r3','ADDL r3,r3,2','NOP',
         'DEC r3','BNE -2','DEC r3','STOP']

codes = {'NOP':[0],'STOP':[0],'BEQ':[1],'BNE':[1],'BRANCH':[1],
         'INC':[2],'DEC':[2],'CMPL':[3],'LDRL':[3],
         'MOV':[4],'CMP':[4],'SUBL':[5],'ADDL':[5],
         'ANDL':[5],'ADD':[6],'SUB':[6],'AND':[6],
         'LDRI':[7],'STRI':[7]}

reg1 = {'r0':0,'r1':1,'r2':2,'r3':3}
reg2 = {'[r0]':0,'[r1]':1,'[r2]':2,'[r3]':3}

r = [0] * 4
r[0],r[1],r[2],r[3] = 1,2,3,4

m = [0] * 8
pc = 0
go = 1
z = 0

while go == 1:

    thisLine = sFile[pc]
    pcOld = pc
    pc = pc + 1

    temp = thisLine.replace(',', ' ')
    print(temp)

    tokens = temp.split()
    mnemonic = tokens[0]
    opClass = codes[mnemonic][0]

    print(opClass)

    rD,rDval,rS1,rS1val,rS2,rS2val,lit, \
    rPnt,rPntV = 0,0,0,0,0,0,0,0,0

    if opClass in [0]:
        pass

    if opClass in [2,3,4,5,6,7]:
        rD = reg1[tokens[1]]
        print(rD)
        rDval = r[rD]

    if opClass in [4,5,6]:
        rS1 = reg1[tokens[2]]
        print(rS1)
        rS1val = r[rS1]

    if opClass in [6]:
        rS2 = reg1[tokens[3]]
        rS2val = r[rS2]

    if opClass in [1,3,5]:
        lit = int(tokens[-1])
        print(lit)

    if opClass in [7]:
        rPnt = reg2[tokens[2]]
        rPntV = r[rPnt]

    if mnemonic == 'STOP':
        go = 0
        print('Program terminated')

    elif mnemonic == 'NOP':
        pass

    elif mnemonic == 'INC':
        r[rD] = rDval + 1
        z = 0
        if r[rD] == 0:
            z = 1

    elif mnemonic == 'DEC':
        r[rD] = rDval - 1
        z = 0
        if r[rD] == 0:
            z = 1

    elif mnemonic == 'BRA':
        pc = pc + lit - 1

    elif mnemonic == 'BEQ':
        if z == 1:
            pc = pc + lit - 1

    elif mnemonic == 'BNE':
        if z == 0:
            pc = pc + lit - 1

    elif mnemonic == 'ADD':
        r[rD] = rS1val + rS2val

    elif mnemonic == 'ADDL':
        r[rD] = rS1val + lit

    elif mnemonic == 'SUB':
        r[rD] = rS1val - rS2val
        z = 0
        if r[rD] == 0:
            z = 1

    elif mnemonic == 'SUBL':
        r[rD] = rS1val - lit
        z = 0
        if r[rD] == 0:
            z = 1

    elif mnemonic == 'CMPL':
        diff = rDval - lit
        z = 0
        if rDval == lit:
            z = 1

    elif mnemonic == 'CMP':
        diff = rDval - rS1val
        z = 0
        if rDval == rS1val:
            z = 1

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

    print('pc =','{:<3}'.format(pcOld),
          '{:<14}'.format(thisLine),
          'Regs =',regs, 'Mem =',mem, 'z =', z)

    x = input('>>> ')