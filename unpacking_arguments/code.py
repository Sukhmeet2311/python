
def test(*args):
 print(*args)
   
test(1,2,3) 

def add(x,y):
 return x+y

nums = [1,2]

print(add(*nums))

nums_dict = {"x":1, "y" :2}

print(add(**nums_dict))

def multiply(*args):
 total=1
 for arg in args:
  total = total *arg 

 return total

def apply ( *args, operator) :
 if (operator== "+"):
  return sum (args)
 elif(operator == "*"):
  return multiply(*args)
 else:
  return "Sorry no Operator found!!"


print (multiply(2,3,4)) 
print (apply(3,5,7,8,operator="+"))
print (apply(3,5,7,8,operator="*"))

