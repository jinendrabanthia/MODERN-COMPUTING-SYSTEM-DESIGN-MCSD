#Objective-1: Design a CPU interprter the data transfer function

#Simple CPU instruction(Data Transfer) interpreter =. Direct instructor interpretation
#Class 0: no operand 


sFile = [
    'LDRL r2', 1,
    'LRDL r0', 4,
    'NOP',
    'STRI r0, {r2}',
    'LRDL r3, {r2}',
    'MOV r1, r2',
    'STOP'
]

reg1 = {'r0':0,'r1':1,'r2':2,'r3':3}
reg2 = {'[r0]':0,'[r1]':1,'[r2]': 2,'[r3]':3}
r = [0]*4
r[0],r[1],r[2],r[3] = 1,2,3,8
m = [0]*8
pc = 0
go = 1
z = 0
while go ==1:
    thisLine = sFile[pc]
    pcOld = pc
    pc += 1 
    pcNew = pc
    temp = thisLine.replace(',','')
    print(temp)
    tokens = temp.split(' ')
    mnemonic = tokens[0]