import sys
opcode={'add':'10000','sub':'10001','ld':'101000','st':'10101','mul':'10110','div':'10111','rs':'11000',
'ls':'11001','xor':'11010','or':'11011','and':'11100','not':'11101','cmp':'11110','jmp':'11111','jlt':'11010',
"jgt": '01101','je':'01111','hlt':'01010'}

binaryrep={'R0':'000','R1':'001','R2':'010','R3':'011','R4':'100','R5':'101','R6':'110','FLAGS':'111'}

typea=['add','sub','mul','xor','or','and']
typeb=['ls','rs']
typec=['div','not','cmp']
typee=['jmp','jlt','jgt','je']
typed=['ld','st']

memadd=dict()
var=[]

def con(x):
    z=x.split()
    for i in z:
        p=i.replace("$","")
        p.rstrip()
    q=int(p)         
    bi = bin(q).replace('0b','')
    x = bi[::-1]
    while len(x) < 8:
        x += '0'
    bi = x[::-1]
    return bi


lines=sys.stdin.readlines()
flag=0
count=-1
lcount=-1
lcount2=-1
vcount=0
chklab=0
temp=''
tvar=''
lab=''
assc=[]
var=[]
cerror=[]
def l_f(lines, cerror):
    if lines[0][0:3]!="var":
        x ="ERROR at line "+ str(count+1) +" : "+"Variable not declared in the beginning"
        cerror+=[x]

for i in lines:
    if i[0:3]=="var":
        var.append(i[4:len(i)-1])
        vcount+=1
    else:
        lcount+=1
#print(var)
for i in range(1,vcount+1):
    dv=lcount+i
    memadd[var[i-1]]=dv
#print(memadd)

for line in lines:

    if len(lines)>256:
        print('ERROR: Assembler cannot read more than 256 lines')
    words=line.split()
    #print(words)
    count+=1
    for i in range(len(words[0])):
        if words[0][i]==':':
            chklab=1
            lab=words[0].strip(':')
    if words[0]!="var":
        lcount2+=1
    if words[0]=='mov'and words[2][0]=='$': #IMM
        if len(words)<3 or len(words)>3:
            x="ERROR at line "+ str(count+1) +' : '+'mov requires two operands'
            cerror+=[x]
            continue
        if (words[2][0]=="$"):
            temp=words[2].lstrip('$')
            if temp.isdigit()==False:
                x="ERROR at line "+ str(count+1) +" : "+ "Illegal Immediate Values"
                cerror+=[x]
                continue
            if int(temp)>255 or int(temp)<0:
                x="ERROR at line "+ str(count+1) +":"+"Illegal Immediate Values"
                cerror+=[x]
                continue
            else:
                y='10010'+ str(binaryrep[words[1]]) + con(words[2])
                assc+=[y]
            
    elif words[0]=='mov': #TYPE C
        if len(words)<3 or len(words)>3:
            x="ERROR at line "+ str(count+1) +' : '+'mov requires two operands'
            cerror+=[x]
            continue
        if words[1] not in binaryrep.keys():
            x='ERROR at line '+ str(count+1) +' : '+'invalid operand',words[1]
            cerror+=[x]
            continue
        if words[2] not in binaryrep.keys():
            x='ERROR at line '+ str(count+1) +' : '+'invalid operand',words[2]
            cerror+=[x]
            continue
        
        if words[1] =="FLAGS":
            y=('10011'+'00000'+str(binaryrep[words[1]])+ str(binaryrep[words[2]]))
            assc+=[y]
        else:
            y=('10011'+'00000'+str(binaryrep[words[1]])+str(binaryrep[words[2]]))
            assc+=[y]
        

    elif words[0]=='rs':
        if len(words)<3 or len(words)>3:
            x="ERROR at line "+ str(count+1) +' : '+'rs requires two operands'
            cerror+=[x]
            continue
        if words[1] not in binaryrep.keys():
            x='ERROR at line ' + str(count+1) +' : ','invalid operand',words[1]
            cerror+=[x]
            continue
        if words[1]=='FLAGS':
            x='ERROR at line '+ str(count+1) +' : ','invalid use of flags'
            cerror+=[x]
            continue
        else:
            y=(str(opcode[words[0]])+str(binaryrep[words[1]])+con(words[2]))
            assc+=[y]
        
        
    elif words[0]=='ls':
        if len(words)<3 or len(words)>3:
            x="ERROR at line "+ str(count+1) +' : '+'rs requires two operands'
            cerror+=[x]
            continue
        if words[1] not in binaryrep.keys():
            x='ERROR at line '+ str(count+1) +' : ','invalid operand',words[1]
            cerror+=[x]
            continue
        if words[1]=='FLAGS':
            x='ERROR at line '+ str(count+1) +' : ','invalid use of flags'
            cerror+=[x]
            continue
        else:
            y=(str(opcode[words[0]])+str(binaryrep[words[1]])+con(words[2]))
            assc+=[y]
        
        
    elif words[0]=='add':
        if len(words)<4 or len(words)>4:
            x="ERROR at line "+ str(count+1) +' : ','add requires three operands'
            cerror+=[x]
            continue
        if words[1] not in binaryrep.keys():
            x='ERROR at line '+ str(count+1) +' : ','invalid operand',words[1]
            cerror+=[x]
            continue
        if words[2] not in binaryrep.keys():
            x='ERROR at line '+ str(count+1) +' : '+'invalid operand',words[2]
            cerror+=[x]
            continue
        if words[3] not in binaryrep.keys():
            x='ERROR at line '+ str(count+1) +' : '+'invalid operand',words[3]
            cerror+=[x]
            continue
        if words[1]=='FLAGS':
            x='ERROR at line '+ str(count+1) +' : '+'invalid use of flags'
            cerror+=[x]
            continue
        else:
            y=(str(opcode[words[0]])+'00'+str(binaryrep[words[1]])+str(binaryrep[words[2]])+str(binaryrep[words[3]]))
            assc+=[y]
        
        
    elif words[0]=='sub':
        if len(words)<4 or len(words)>4:
            x="ERROR at line "+ str(count+1) +' : '+'sub requires three operands'
            cerror+=[x]
            continue
        if words[1] not in binaryrep.keys():
            x='ERROR at line '+ str(count+1) +' : '+'invalid operand',words[1]
            cerror+=[x]
            continue
        if words[2] not in binaryrep.keys():
            x='ERROR at line '+ str(count+1) +' : '+'invalid operand',words[2]
            cerror+=[x]
            continue
        if words[3] not in binaryrep.keys():
            x='ERROR at line '+ str(count+1)  +' : '+'invalid operand',words[3]
            cerror+=[x]
            continue
        if words[1]=='FLAGS':
            x='ERROR at line '+ str(count+1) +' : '+'invalid use of flags'
            cerror+=[x]
            continue
        else:
            y=(str(opcode[words[0]])+'00'+str(binaryrep[words[1]])+str(binaryrep[words[2]])+str(binaryrep[words[3]]))
            assc+=[y]
        

    elif words[0]=='mul':
        if len(words)<4 or len(words)>4:
            x="ERROR at line "+ str(count+1) +' : '+'mul requires three operands'
            cerror+=[x]
            continue 
        if words[1] not in binaryrep.keys():
            x='ERROR at line '+ str(count+1) +' : '+'invalid operand'+ words[1]
            cerror+=[x]
            continue 
        if words[2] not in binaryrep.keys():
            x='ERROR at line '+ str(count+1) +' : '+'invalid operand',words[2]
            cerror+=[x]
            continue
        if words[3] not in binaryrep.keys():
            x='ERROR at line '+ str(count+1) +' : '+'invalid operand',words[3]
            cerror+=[x]
            continue
        if words[1]=='FLAGS':
            x='ERROR at line '+ str(count+1) + ' : '+ 'invalid use of flags'
            cerror+=[x]
            continue
        else:
            y=(str(opcode[words[0]])+'00'+str(binaryrep[words[1]])+str(binaryrep[words[2]])+str(binaryrep[words[3]]))
            assc+=[y]
        
        
    elif words[0]=='xor':
        if len(words)<4 or len(words)>4:
            x="ERROR at line " + str(count+1) +' : '+'xor requires three operands'
            cerror+=[x]
            continue
        if words[1] not in binaryrep.keys():
            x='ERROR at line' + str(count+1) +' : '+'invalid operand'+ words[1]
            cerror+=[x]
            continue
        if words[2] not in binaryrep.keys():
            x='ERROR at line '+ str(count+1) +' : '+'invalid operand' + words[2]
            cerror+=[x]
            continue
        if words[3] not in binaryrep.keys():
            x='ERROR at line '+ str(count+1) +' : '+'invalid operand',words[3]
            cerror+=[x]
            continue
        if words[1]=='FLAGS':
            x='ERROR at line '+ str(count+1) +' : '+'invalid use of flags'
            continue
        else:
            y=(str(opcode[words[0]])+'00'+str(binaryrep[words[1]])+str(binaryrep[words[2]])+str(binaryrep[words[3]]))
            assc+=[y]
        
    elif words[0]=='or':
        if len(words)<4 or len(words)>4:
            x="ERROR at line "+ str(count+1) +' : '+'or requires three operands'
            cerror+=[x]
            continue
        if words[1] not in binaryrep.keys():
            x='ERROR at line '+ str(count+1) +' : '+'invalid operand',words[1]
            cerror+=[x]
            continue
        if words[2] not in binaryrep.keys():
            x='ERROR at line '+ str(count+1) + ' : '+ 'invalid operand',words[2]
            cerror+=[x]
            continue
        if words[3] not in binaryrep.keys():
            x='ERROR at line '+ str(count+1) + ' : '+'invalid operand',words[3]
            cerror+=[x]
            continue
        if words[1]=='FLAGS':
            x='ERROR at line '+ str(count+1) + ' : '+'invalid use of flags'
            cerror+=[x]
            continue
        else:
            y=(str(opcode[words[0]])+'00'+str(binaryrep[words[1]])+str(binaryrep[words[2]])+str(binaryrep[words[3]]))
            assc+=[y]
        
    elif words[0]=='and':
        
        if len(words)<4 or len(words)>4:
            print('a')
            x="ERROR at line "+ str(count+1) + ' : '+'and requires three operands'
            cerror+=[x]
            continue
        if words[1] not in binaryrep.keys():
            print('a')
            x='ERROR at line '+ str(count+1) +' : '+'invalid operand',words[1]
            cerror+=[x]
            continue
        if words[2] not in binaryrep.keys():
            print('a')
            x='ERROR at line '+ str(count+1) + ' : '+'invalid operand',words[2]
            cerror+=[x]
            continue
        if words[3] not in binaryrep.keys():
            print('a')
            x='ERROR at line '+ str(count+1) + ' : '+'invalid operand'+ words[3]
            cerror+=[x]
            continue
        if words[1]=='FLAGS':
            print('a')
            x= 'ERROR at line '+ str(count+1) +' : '+'invalid use of flags'
            cerror+=[x]
            continue
        else:
            print('a')
            y=(str(opcode[words[0]])+'00'+str(binaryrep[words[1]])+str(binaryrep[words[2]])+str(binaryrep[words[3]]))
            assc+=[y]
        

    elif words[0]=='div':
        if len(words)<3 or len(words)>3:
            x="ERROR at line "+ str(count+1) + ' : '+'div requires two operands'
            cerror+=[x]
            continue
        if words[1] not in binaryrep.keys():
            x='ERROR at line '+ str(count+1) +' : '+'invalid operand',words[1]
            cerror+=[x]
            continue
        if words[1]=='FLAGS':
            x='ERROR at line '+ str(count+1) +' : '+'invalid use of flags'
            cerror+=[x]
            continue
        else:
            y=(str(opcode[words[0]])+'00000'+str(binaryrep[words[1]])+str(binaryrep[words[2]]))
            assc+=[y]
        

    elif words[0]=='not':
        if len(words)<3 or len(words)>3:
            x="ERROR at line " + str(count+1) +' : '+'not requires two operands'
            cerror+=[x]
            continue
        if words[1] not in binaryrep.keys():
            x='ERROR at line '+ str(count+1) + ' : '+'invalid operand',words[1]
            cerror+=[x]
            continue
        if words[1]=='FLAGS':
            x='ERROR at line '+ str(count+1) + ' : '+'invalid use of flags'
            cerror+=[x]
            continue
        else:
            y=(str(opcode[words[0]])+'00000'+str(binaryrep[words[1]])+str(binaryrep[words[2]]))
            assc+=[y]
        
        
    elif words[0]=='cmp':
        if len(words)<3 or len(words)>3:
            x="ERROR at line "+ str(count+1) +' : '+'div requires two operands'
            cerror+=[x]
            continue
        if words[1] not in binaryrep.keys():
            x='ERROR at line '+ str(count+1) +' : '+'invalid operand',words[1]
            cerror+=[x]
            continue
        if words[1]=='FLAGS':
            x='ERROR at line ' + str(count+1) + ' : '+'invalid use of flags'
            cerror+=[x]
            continue
        else:
            y=(str(opcode[words[0]])+'00000'+str(binaryrep[words[1]])+str(binaryrep[words[2]]))
            assc+=[y]
        
        
    elif words[0]=='ld':
        if len(words)<3 or len(words)>3:
            x="ERROR at line " + str(count+1) + ' : ' +'ld requires two operands'
            cerror+=[x]
            continue
        if words[1] not in binaryrep.keys():
            x='ERROR at line '+ str(count+1) + ' : '+'invalid operand',words[1]
            cerror+=[x]
            continue
        if words[1]=='FLAGS':
            x='ERROR at line '+ str(count+1) + ' : ' + 'invalid use of flags'
            cerror+=[x]
            continue
        if words[2] not in memadd.keys():
            x='ERROR at line '+ str(count+1) +' : '+'invalid variable',words[2]
            cerror+=[x]
        else:
            y=(str(str(opcode[words[0]])+str(binaryrep[words[1]])+con(str(memadd[words[2]]))))
            assc+=[y]
        

    elif words[0]=='st':
        if len(words)<3 or len(words)>3:
            x="ERROR at line "+ str(count+1) + ' : '+ 'st requires two operands'
            cerror+=[x]
            continue
        if words[1] not in binaryrep.keys():
            x='ERROR at line '+ str(count+1) + ' : '+'invalid operand',words[1]
            cerror+=[x]
            continue
        if words[1]=='FLAGS':
            x='ERROR at line '+ str(count+1) +' : '+'invalid use of flags'
            continue
        if words[2] not in memadd.keys():
            print(memadd)
            x='ERROR at line '+ str(count+1) +' : '+'invalid variable',words[2]
            cerror+=[x]
        else:
            y=(str(str(opcode[words[0]])+str(binaryrep[words[1]])+con(str(memadd[words[2]]))))
            assc+=[y]
        
        
    elif words[0]=='jmp':
        if len(words)<2 or len(words)>2:
            x= "ERROR at line " + str(count+1) + ' : ' + 'jmp requires one operand'
            cerror+=[x]
            continue
        if words[1]!=lab:
            x='ERROR at line '+ str(count+1) + ' : ' + 'no label detected',words[1]
            cerror+=[x]
            continue
        if words[1]=='FLAGS':
            x= 'ERROR at line ' + str(count+1) + ' : ' + 'invalid use of flags'
            continue
        else:
            y=(str(opcode[words[0]])+'000'+con(str(addr)))
            assc+=[y]
        
        
    elif words[0]=='jlt':
        if len(words)<2 or len(words)>2:
            x="ERROR at line " + str(count+1) + ' : ' + 'jlt requires two operands'
            cerror+=[x]
            continue
        if words[1]!=lab:
            x='ERROR at line '+ str(count+1) + ' : ' + 'no label detected',words[1]
            cerror+=[x]
            continue
        if words[1]=='FLAGS':
            x= 'ERROR at line '+ str(count+1) + ' : ' + 'invalid use of flags'
            cerror+=[x]
            continue
        else:
            y=(str(opcode[words[0]])+'000'+con(str(addr)))
            assc+=[y]
       
        
    elif words[0]=='jgt':
        if len(words)<2 or len(words)>2:
            x="ERROR at line "+ str(count+1) + ' : ' + 'jgt requires two operands'
            cerror+=[x]
            continue
        if words[1]!=lab:
            x= 'ERROR at line '+ str(count+1) + ' : ' + 'no label detected',words[1]
            cerror+=[x]
            continue
        if words[1]=='FLAGS':
            x= 'ERROR at line '+ str(count+1) + ' : '+ 'invalid use of flags'
            cerror+= [x]
            continue
        else:
            y=(str(opcode[words[0]])+'000'+con(str(addr)))
            assc+=[y]
    
    elif words[0]=='je':
        if len(words)<2 or len(words)>2:
            x="ERROR at line "+ str(count+1) +' : '+ 'je requires two operands'
            cerror+=[x]
            continue
        if words[1]!=lab:
            x='ERROR at line '+ str(count+1) + ' : '+ 'no label detected'+ words[1]
            cerror+=[x]
            continue
        if words[1]=='FLAGS':
            x='ERROR at line '+ str(count+1) +' : '+'invalid use of flags'
            cerror+=[x]
            continue
        else:
            y=(str(opcode[words[0]])+'000'+con(str(addr)))
            assc+=[y]
            
    elif words[0]==lab+':':
        if len(words)<2:
            print('ERROR: Incomplete Label Command')
            continue
        try:
            if words[1] in typea:
                y=(str(opcode[words[1]])+'00'+str(binaryrep[words[2]])+str(binaryrep[words[3]])+str(binaryrep[words[4]]))
                assc+=[y]
            if words[1] in typeb:
                y=(str(opcode[words[0]])+str(binaryrep[words[1]])+con(words[2]))
                assc+=[y]
            if words[1] in typec:
                y=(str(opcode[words[0]])+'00000'+str(binaryrep[words[1]])+str(binaryrep[words[2]]))
                assc+=[y]
            if words[1] in typed:
                y=(str(str(opcode[words[0]])+str(binaryrep[words[1]])+con(str(lcount+1))))
                assc+=[y]
            if words[1] in typee:
                y=(str(opcode[words[0]])+'000'+con(str(lcount+1)))
                assc+=[y]
            addr=lcount2
        except:
            print('ERROR: Incorrect use of labels')


    elif words[0]=='hlt':
        if (count+1)!=len(lines):
            x="ERROR at line "+ str(count+1) + " : "+ "Incorrect position of hlt"
            cerror+=[x]
            count+=1
            continue 
        else:
            y=(str(opcode[words[0]])+'00000000000')
            assc+=[y]
            flag=1

    elif words[0]=="var":
        l_f(lines ,cerror)
        if vcount<=count:
            x= "ERROR at line "+ str(count+1) + " : ","Variable not declared in the beginning"
            cerror+=[x]

        if len(words)==1:
            x='ERROR at line' + str(count+1) + ' : ','var requires one operand'
            cerror+=[x]
    else:
        x='ERROR at Line '+ str(count+1) + ' :  Invalid Instruction'
        cerror+=[x]

if flag==0:
    x='ERROR: No HLT Instruction at end of file'
    cerror+=[x]

if(len(cerror)==0):
    for i in assc:
        print(i)
else:
    for i in cerror:
        print(i)