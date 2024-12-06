#matrix operations
def pmatrix(l):#print matrix
    for i in l:
        print(i)
        
def order(o,name=''):#order matrix
    o=o.lower()
    o=o.replace('by','*')
    o=o.replace('x','*')
    o=o.replace('×','*')
    o=o.split('*')
    if len(o)==2 and o[0].isdigit() and o[1].isdigit():
        x,y=int(o[0]),int(o[1])
        return x,y
    else:
        print('INVALID ORDER')
        return order(name)
    
def forder(m):#find the order
    x=len(m)
    y=len(m[0])
    return str(x)+'*'+str(y)

def create(o=False,name='a'):#create a matrix
    x,y=order(o,name)
    r=[]
    for i in range(x):
        c=[]
        for j in range(y):
            e=input(name+str(i+1)+str(j+1)+':')
            if e=='':
               e=0
            c.append(int(e))
        r.append(c)
    return r

def multiply(p,q):#multiply a matrix
    r=[]
    for i in range(len(p)):
        c=[]
        for j in range(len(p[0])):
            z=0
            for k in range(len(q)):
              z+=p[i][k]*q[k][j]
            c.append(z)
        r.append(c)
    return r

def power(m,p=0):#power the matrix
    if p==0:
        return 1
    p=int(p)
    n=list(m)
    for i in range(p-1):
        n=multiply(m,n)
    return n
        
