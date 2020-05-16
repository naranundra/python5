# pop -> list ees salgaj awna
names = ["bat " , "bold" , 'delger'] 
a = names.pop(2)
print(names)
print(a)


# remove -> shuud ustgana 
names = ["bat " , "bold" , 'delger'] 
a = names.remove("bat ")
print(a)

#clear
names = ["bat " , "bold" , 'delger'] 
names.clear()
print(names)



# del 
names = ["bat " , "bold" , 'delger'] 
del names
print(names) 

# элемент тоолоход Count ашиглана
numbers = [2, 0, 6, 1, ]
c = numbers.count(2)
print(c)

# index oloh
numbers = [2, 0, 6, 1]
numbers1 = [9, 9, 6]
c = numbers.count(2)
i = numbers.index(0)
print("too: " , c)
print("index: " , i)
print(numbers + numbers1)

# sort эрэмбэлэх
numbers = [2, 0, 6, 1]
numbers1 = [9, 9, 6]
c = numbers.count(2)
i = numbers.index(0)
print("too: " , c)
print("index: " , i)
print(numbers + numbers1)
print(numbers.sort())
print(numbers1.reverse())

# if ашиглах
names = ["bat " , "bold" , 'delger'] 
if 'bat' in names:
    print("bvrtgegdsen")
else: 
    print("bvrtgegdegvi")

# for ашиглах 
for i in names:
    print(i)

