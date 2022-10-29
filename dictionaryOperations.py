a = { 'one':'uno','two':'dos','three':'tres','four':'cwarto'}
print('one' in a)  # ------------------>O(1)
print('uno' in a.values()) # ------------------>O(n)

for key in a:
    print(key,end=" ") # ------------------>O(n)

print()
b={1:True,2:True,3:False}

print(all(b))
print(any(b))
print(len(a))
print(sorted(a))
print(sorted(a,reverse=True))
print(sorted(a,key=len))