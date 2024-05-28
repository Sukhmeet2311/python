users= {
   (0,"Bob","password"),
   (1,"Nishtha","sukhi123"),
   (2,"Sukhmeet","nish123"),
   (2,"Sukhnish","nish1234"),
}

username_mapping = {user[1]: user for user in users}

print (username_mapping)

_, name, password = username_mapping["Bob"]

print (password)
