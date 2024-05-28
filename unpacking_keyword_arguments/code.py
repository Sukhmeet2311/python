def named(**kwargs):
    print(kwargs)

# put into the dictionary
named(name="Nishtha",age=25)    

def new_named(name, age):
    print(name,age)

name_dict = {'name': 'Nishtha', 'age': 25}

new_named(name_dict,25) #full dict as name
new_named(**name_dict)

def both(*args,**kwargs):
    print(args)
    print(kwargs)

both(1,2,3,4,name='Sukhmeet',age=35)