def search(arr,x):
  for i in range(len(arr)):
    if arr[i]==x:
      return i
  
  print("This element is not in the list")  
a=[1,2,3,4,7,8,9]
search(a,4)
