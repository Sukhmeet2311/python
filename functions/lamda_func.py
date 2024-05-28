add = lambda x, y: x+y

print (add(5,7))

def double(z):
    return(z * 2)

sequence = [1,3,5,7]
doubled = [double(z) for z in sequence]
print(doubled)
#alternative to list function applys double to each element in sequence
doubled = list(map(double, sequence))
print(doubled)
# convert it via lambda
newDoubled =[(lambda x: x*2)(x) for x in sequence]
print (list(newDoubled))