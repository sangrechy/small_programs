#binary()=STRING TO BINARY
#binlist()=BINARY TO BINARY INT (WITHOUT BASE)
#binstr()=BINARY TO STRING
#convert()=STRING TO BINARY TO STRING
#STRING TO BINARY
def binary(strbin):
    x,y=[],[]
    for i in strbin:
        x.append(ord(i))
    for i in x:
        y.append(bin(i))
    binstr=y
    return binstr
#BINARY TO BINARY INT (WITHOUT BASE)
def binlist(binary):
    x,l=[],[]
    if type(binary)==type([]):
        for i in binary:
            y=i[2:]
            x.append(int(y))
        return x
    else:
        print('ERROR.. GIVEN TYPE MUST BE LIST')
#BINARY TO STRING
def binstr(binstr):
    w=''
    if type(binstr)==type([]):
        for x in binstr:
            x=str(x)
            y=int(x[0])
            x=x[1:]
            for i in x:
                i=int(i)
                y=y*2+i
            w+=chr(y)
        return w
    else:
        x=str(x)
        y=int(x[0])
        x=x[1:]
        for i in x:
            i=int(i)
            y=y*2+i
        w+=chr(y)
        return w
#STRING TO BINARY TO STRING
def convert(x):
    x=binlist(binary(x))
    print('BINARY:',x)
    x=binstr(x)
    print('STRING RETURNED:',x)
    
    
    

        
     
        
