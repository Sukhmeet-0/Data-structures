a = {'name':'sukhmeet','age':21}
a['age'] =16  # ----------------->O(1)
a['contact']=7814583191  # ----------------->O(1)
# a.clear()
# b=a.copy()
# print(b)

# c = {}.fromkeys([1,2,3],0)
# print(a.get('name'))
# a.popitem()

# print(a.items())
# print(a.keys())
# print(a.values())
# a.pop('name')

a.setdefault('address','kot kuljas rai')
b={1:'1',2:'2',3:'3'}
a.update(b)

print(a)
