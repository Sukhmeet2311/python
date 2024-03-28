numbers = [1,2,3]
double_mnumbers = [num*2 for num in numbers]
print (double_mnumbers)
even_numbers = [num for num in numbers if num%2 == 0 ]
print (even_numbers,"memory id of list", id(even_numbers))
