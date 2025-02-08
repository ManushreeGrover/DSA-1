def findfloor(arr,x):
  st=0
  end=len(arr)-1
  mid=(st+end)//2
  ans=-1;
  while st<=end:
    if arr[mid]<=x:
      ans=arr[mid]
      st=mid+1
    elif arr[mid]>x:
      end=mid-1
    
    mid=(st+end)//2
  
  return ans

def findceil(arr,x):
  st=0
  end=len(arr)-1
  mid=(st+end)//2
  ans=-1;
  while st<=end:
    if arr[mid]>=x:
      ans=arr[mid]
      end=mid-1
    elif arr[mid]<x:
      st=mid+1
    
    mid=(st+end)//2
  
  return ans

# Taking input from the user
length=int(input("Enter length of array: "))
arr=[]
for i in range(length):
  arr.append(int(input("Enter element: ")))
x = int(input("Enter x: "))

# Calling the function
floorval = findfloor(arr,x)
print("floor value = ",floorval)

ceilval=findceil(arr,x)
print("ceil value = ",ceilval)
