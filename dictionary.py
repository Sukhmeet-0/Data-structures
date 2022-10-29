# a = dict()
# print(a)
# b= {}
# print(b)
# c= { 1:"one",2:"two"}  # ----------------->O(1)
# print(c.values())
# print(c[1])


# insert update element

a = {'name':'sukhmeet','age':21}
print(a)
a['age'] =16  # ----------------->O(1)
a['contact']=7814583191  # ----------------->O(1)
print( a)


# traverse

def traverse(dict):
    for key in dict:  # ----------------->O(n)
        print(key, dict[key])  # ----------------->O(1)


traverse(a)


# search for element

def search(dict,value):
    for key in dict:  # ----------------->O(n)
        if dict[key] ==  value:  # ----------------->O(1)
            print(key, value)  # ----------------->O(1)
            break
    else:
        print('value doesnt exist')  # ----------------->O(1)


search(a, 16)


# delete an element

# a.pop('name')
# a.popitem()
# a.clear()
del a['name']
print(a)