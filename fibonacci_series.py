def fibonacci(n):
  a=0
  b=1
  if n<0:
    print("invalid")
  elif n==0:
    print(a) 
  else:
    for i in range(1,n):
      c=a+b
      a=b
      b=c
      print(b)

fibonacci(12)
