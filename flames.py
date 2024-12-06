#
def flames(x,y):
    x,y=x.lower(),y.lower()
    for i in x:
        m=y.find(i)
        if m!=-1:
            x=x.replace(i,'',1)
            y=y.replace(i,'',1)
    n=len(x+y)#value7
    x=int(n)
    st='flames'#string
    xl=len(st)#length
    d1,d=0,0#default
    if x==0:
        return('SAME NAME..')
        

    for i in range(xl-1):#5strikes
        n=x
        xl=len(st)
        while xl<n+d1:
            d=0
            n=n-xl
        d1=d1+n-1
        i=st[d1]
        st=st.replace(i,'')
        d=d1
    if st=='f':
        return ('FRIENDS')
    elif st=='l':
        return('LOVERS')
    elif st=='a':
        return('AFFECTION')
    elif st=='m':
        return('MARRAIGE')
    elif st=='e':
        return('ENIEMIES')
    elif st=='s':
        return('SIBLINGS')
    else:
        return('ERROR')
for i in range(10):
    x=input('NAME 1')
    y=input('NAME 2')
    print( flames(x,y))    
