import sys
opcode={'add':'10000','sub':'10001','movi':'10010','mov':'10011','ld':'101000','st':'10101','mul':'10110','div':'10111','rs':'11000','ls':'11001',
'xor':'11010','or':'11011','and':'11100','not':'11101','cmp':'11110','jmp':'11111','jlt':'11010', "jgt": '01101','je':'01111','hlt':'01010'}

binaryrep={'R0':'000','R1':'001','R2':'010','R3':'011','R4':'100','R5':'101','R6':'110'}

PC=0

def pctobin(PC):
    pcbinary=str(bin(PC).replace('0b',''))
    x=pcbinary[::-1]
    while len(x)<8:
        x+='0'
    return x[::-1]

def regtobin(regx):
    pcbinary=str(bin(regx).replace('0b',''))
    x=pcbinary[::-1]
    while len(x)<16:
        x+='0'
    return x[::-1]

regval={'R0':0,'R1':0,'R2':0,'R3':0,'R4':0,'R5':0,'R6':0,'FLAGS':'0000000000000000'}
key1=0
key2=0
key3=0
imm=0
halted=0

variables={}

def bintodec(imm):
    dec_number= int(imm, 2)
    return dec_number

def add(key1,key2,key3):
    if x=="10000":
        rone=str(instruct[7:10])
        rtwo=str(instruct[10:13])
        rthree=str(instruct[13:16])
        for key,value in binaryrep.items():
            if value==rone:
                key1=key
            if value==rtwo:
                key2=key
            if value==rthree:
                key3=key
        a=regval.get(key1)
        b=regval.get(key2)
        c=regval.get(key3)
        sum=b+c
        regval[key1]=sum        
     
def sub(key1,key2,key3):
    if x=="10001":
        rone=str(instruct[7:10])
        rtwo=str(instruct[10:13])
        rthree=str(instruct[13:16])
        for key,value in binaryrep.items():
            if value==rone:
                key1=key
            if value==rtwo:
                key2=key
            if value==rthree:
                key3=key
        a=regval.get(key1)
        b=regval.get(key2)
        c=regval.get(key3)
        sum=b-c
        regval[key1]=sum
    #print(regval)

def mul(key1,key2,key3):
    if x=="10110":
        rone=str(instruct[7:10])
        rtwo=str(instruct[10:13])
        rthree=str(instruct[13:16])
        for key,value in binaryrep.items():
            if value==rone:
                key1=key
            if value==rtwo:
                key2=key
            if value==rthree:
                key3=key
        a=regval.get(key1)
        b=regval.get(key2)
        c=regval.get(key3)
        sum=b*c
        regval[key1]=sum
    #print(regval)

def OR(key1,key2,key3):
    if x=="11011":
        rone=str(instruct[7:10])
        rtwo=str(instruct[10:13])
        rthree=str(instruct[13:16])
        for key,value in binaryrep.items():
            if value==rone:
                key1=key
            if value==rtwo:
                key2=key
            if value==rthree:
                key3=key
        a=regval.get(key1)
        b=regval.get(key2)
        c=regval.get(key3)
        sum=a|b
        regval[key3]=sum
    #print(regval)

def AND(key1,key2,key3):
    if x=="11100":
        rone=str(instruct[7:10])
        rtwo=str(instruct[10:13])
        rthree=str(instruct[13:16])
        for key,value in binaryrep.items():
            if value==rone:
                key1=key
            if value==rtwo:
                key2=key
            if value==rthree:
                key3=key
        a=regval.get(key1)
        b=regval.get(key2)
        c=regval.get(key3)
        sum=a&b
        regval[key3]=sum
    #print(regval)

def XOR(key1,key2,key3):
    if x=="11010":
        rone=str(instruct[7:10])
        rtwo=str(instruct[10:13])
        rthree=str(instruct[13:16])
        for key,value in binaryrep.items():
            if value==rone:
                key1=key
            if value==rtwo:
                key2=key
            if value==rthree:
                key3=key
        #print(key1,key2,key3)
        a=regval.get(key1)
        b=regval.get(key2)
        c=regval.get(key3)
        sum=a^b
        regval[key3]=sum
    #print(regval)

def MOV(key1,key2):
    if x=="10011":
        rone=str(instruct[10:13])
        rtwo=str(instruct[13:16])
        #print(rone,rtwo)
        for key,value in binaryrep.items():
            if value==rone:
                key1=key
            if value==rtwo:
                key2=key
        #print(key1,key2)
        a=regval.get(key1)
        b=regval.get(key2)
        sum=b
        #print(a,b)
        regval[key1]=sum
    #print(regval)

def MOVI (key1,imm):
    if x== "10010":
        rone=str(instruct[5:8])
        imm = str(instruct[8:16])
        #print(rone,imm)
        for key,value in binaryrep.items():
            if value==rone:
                key1=key
        #print(key1,imm)
        a=regval.get(key1)
        b= bintodec(imm)
        sum=b
        #print(a,b)
        regval[key1]=sum
    #print(regval)

def st():
    var=str(instruct[8:16])
    regbinary=str(instruct[5:8])
    for key,value in binaryrep.items():
        if value==regbinary:
            reg=key
    valofreg=regval.get(reg)
    if var not in variables.keys():
        variables[var]=valofreg

def ld():
    var=str(instruct[8:16])
    regbinary=str(instruct[5:8])
    for key,value in binaryrep.items():
        if value==regbinary:
            reg=key
    if var not in variables.keys():
        variables[var]=0
    else:
        regval[regbinary]=variables[var]
    
def RS (key1,imm):
    if x== "11000":
        rone=str(instruct[5:8])
        imm = str(instruct[8:16])
        #print(rone,imm)
        for key,value in binaryrep.items():
            if value==rone:
                key1=key
        #print(key1,imm)
        a=regval.get(key1)
        b= bintodec(imm)
        sum= a>>b
        #print(a,b)
        regval[key1]=sum
    #print(regval)

def LS (key1,imm):
    if x== "11001":
        rone=str(instruct[5:8])
        imm = str(instruct[8:16])
        #print(rone,imm)
        for key,value in binaryrep.items():
            if value==rone:
                key1=key
        #print(key1,imm)
        a=regval.get(key1)
        b= bintodec(imm)
        sum=a<<b
        #print(a,b)
        regval[key1]=sum
    #print(regval)

def div(key1,key2):
    if x=="10111":
        rone=str(instruct[10:13])
        rtwo=str(instruct[13:16])
        for key,value in binaryrep.items():
            if value==rone:
                key1=key
            if value==rtwo:
                key2=key
        #print(key1,key2)
        a=regval.get(key1)
        b=regval.get(key2)
        quotient=a//b
        remainder=a%b
        #print(a,b)
        regval['R0']=quotient
        regval['R1']=remainder
    #print(regval)

def NOT(key1,key2):
    if x=="11101":
        rone=str(instruct[10:13])
        rtwo=str(instruct[13:16])
        for key,value in binaryrep.items():
            if value==rone:
                key1=key
            if value==rtwo:
                key2=key
        #print(key1,key2)
        a=regval.get(key1)
        b=regval.get(key2)
        sum=~a
        regval[key2]=sum
    #print(regval)

def cmp(key1,key2):
    if x=="11110":
        rone=str(instruct[10:13])
        rtwo=str(instruct[13:16])
        for key,value in binaryrep.items():
            if value==rone:
                key1=key
            if value==rtwo:
                key2=key
        #print(key1,key2)
        a=regval.get(key1)
        b=regval.get(key2)
        flagreg=list(regval['FLAGS'])
        if a==b:
            flagreg[-1]='1'
        if a>b:
            flagreg[-2]='1'
        if a<b:
            flagreg[-3]='1'
        newflag=''
        for i in flagreg:
            newflag+=i
        regval['FLAGS']=newflag

def jmp():
    if x=='11111':
        mem_addr = str(instruct[8:16])
        PC=bintodec(mem_addr)
        return PC

def jlt():
    if regval['FLAGS']=='0000000000000100':
        mem_addr = str(instruct[8:16])
        PC=bintodec(mem_addr)
        #print(PC)
        return PC
    else:
        PC=PC+1
        return PC

def jgt():
    if regval['FLAGS']=='0000000000000010':
        mem_addr = str(instruct[8:16])
        PC=bintodec(mem_addr)
        regval['FLAGS']=='0000000000000000'
        return PC
    else:
        PC=PC+1
        return PC

def je():
    if regval['FLAGS']=='0000000000000001':
        mem_addr = str(instruct[8:16])
        PC=bintodec(mem_addr)
        return PC
    else:
        PC=PC+1
        return PC

d=sys.stdin.readlines()
instructionumber={}
instructions=[]
for i in d:
    instructions.append(i.replace('\n',''))
for i in range(len(instructions)):
    instructionumber[i+1]=instructions[i]
#print(instructionumber)
while halted!=1:
    instruct=instructionumber[PC+1]
    x= instruct[0:5]
    print(pctobin(PC),regtobin(regval['R0']),regtobin(regval['R1']),regtobin(regval['R2']),regtobin(regval['R3']),regtobin(regval['R4']),
    regtobin(regval['R5']),regtobin(regval['R6']),regval['FLAGS'])
    if(x in opcode.values()):
        if x=="10000":
            add(key1,key2,key3)
            #print("add")
            regval['FLAGS']=='0000000000000000'
            PC+=1
        if(x=="10001"):
            sub(key1,key2,key3)
            #print("sub")
            regval['FLAGS']=='0000000000000000'
            PC+=1
        if x=="10011":
            MOV(key1,key2)
            regval['FLAGS']=='0000000000000000'
            PC+=1
        if(x=="10010"):
            MOVI (key1,imm)
            #print("mov immediate")
            regval['FLAGS']=='0000000000000000'
            PC+=1
        if(x=="10100"):
            #print("ld")
            ld()
            regval['FLAGS']=='0000000000000000'
            PC+=1
        if(x=="10101"):
            #print("st")
            st()
            regval['FLAGS']=='0000000000000000'
            PC+=1
        if(x=="10110"):
            mul(key1,key2,key3)
            #print("mul")
            regval['FLAGS']=='0000000000000000'
            PC+=1
        if(x=="10111"):
            div(key1,key2)
            #print("div")
            regval['FLAGS']=='0000000000000000'
            PC+=1
        if(x=="11000"):
            RS (key1,imm)
            #print("rs")
            regval['FLAGS']=='0000000000000000'
            PC+=1
        if(x=="11001"):
            LS (key1,imm)
            #print("ls")
            regval['FLAGS']=='0000000000000000'
            PC+=1
        if(x=="11010"):
            XOR(key1,key2,key3)
            #print("xor")
            regval['FLAGS']=='0000000000000000'
            PC+=1
        if(x=="11011"):
            OR(key1,key2,key3)
            #print("or")
            regval['FLAGS']=='0000000000000000'
            PC+=1
        if(x=="11100"):
            AND(key1,key2,key3)
            #print("and")
            regval['FLAGS']=='0000000000000000'
            PC+=1
        if(x=="11101"):
            NOT(key1,key2)
            #print("not")
            regval['FLAGS']=='0000000000000000'
            PC+=1
        if(x=="11110"):
            cmp(key1,key2)
            #print("cmp")
            PC+=1
        if(x=="11111"):
            #print("jmp")
            regval['FLAGS']=='0000000000000000'
            PC=jmp()
        if(x=="11010"):
            #print("jlt")
            regval['FLAGS']=='0000000000000000'
            PC=jlt()
        if(x=="01101"):
            if regval['FLAGS']=='0000000000000010':
                mem_addr = str(instruct[8:16])
                PC=bintodec(mem_addr)
                regval['FLAGS']=='0000000000000000'
            else:
                PC=PC+1
        if(x=="01111"):
            #print("je")
            regval['FLAGS']=='0000000000000000'
            PC=je()
        if(x=="01010"):
            halted=1

noofins=len(instructions)
noofvar=len(variables)
numzero=256-noofins-noofvar
for i in instructionumber:
    print(instructionumber[i])
for key in variables.items():
    print(key)
for i in range(numzero):
    print('0000000000000000')
#PC VALUE NOT UPDATING
#OVERFLOW