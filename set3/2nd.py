#add delete update

def add(obj,name,age):
  obj[name] = age

def DeleteData(obj,name):
  if name in obj:
    del obj[name]

def UpdateVal(obj,name,age):
  if name in obj:
    obj[name] = age

data = {}
add(data,"John",26)
print(data)
UpdateVal(data,"John",36)
print(data)
DeleteData(data,"John")
print(data)