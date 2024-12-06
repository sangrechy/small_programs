def eqn(x=''):
  x=x.replace('-','+-')
  print(x)
  x=x.split('+')
  y=list(x)
  for i in x:
    for j in i:
       if j.isalpha():
          variable=j
          break
  a,b,c=0,0,0
  for i in y:
     if variable+'**2' in i:
        i=i.replace(variable+'**2','')
        if i=='':
            i=1
        a=int(i)
     elif variable in i:
        i=i.replace(variable,'')
        if i=='':
            i=1
        b=int(i)
     else:
        if i=='':
            i=1
        c=int(i)
  if b**2 >= 4*a*c:
      a1=((b**2)-(4*a*c))**0.5
      b1=(-1*b)+a1
      b2=(-1*b)-a1
      if b1%1 == 0:
          c1=b1/(2*a)
      else:
          c1=str(b1)+r'/'+str(2*a)
      if b2%1 == 0:
          c2=b2/(2*a)
      else:
          c2=str(b2)+r'/'+str(2*a)
  else:
      c1='ROOTS IS NOT POSSIBLE'
      c2=''
  return(c1,c2)
        
