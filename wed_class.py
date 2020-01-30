# myList=[]
# animals = ["h","ch","g",5]

# animals[0] = "c"
# print(len(animals))

# print(animals[0]+" and " + animals[2] + "  "+str(animals[3]%2))
# print(animals)

# todos = ["pet the cat", "go to work", "shop for groceries", 
# "go home", "feed the cat"]
# todos.append("binge watch a show")
# todos.append("go to sleep")
# print(todos)
# index = 0
# while index < len(todos):
#     print(f"{index + 1}: {todos[index]}", end = "      ")
#     index += 1

# a = [1,4,5,3,8]

# b =[4,3,0]

# a.extend([99,101])

# c = a + b
# del a[0]

# a = a + b

# a[0]=b[1]-5
# print (c)

# print(b*3)
# print(a + b)

# thing = input("Please add a thing to your todo? ")
# list =[]

# while len(thing)>0:
#     list.append(thing)
#     index = 0

#     while index < len(list):
#         print(f'{index+1}: {list[index]}')
#         index += 1
#     thing = input("Please add a thing to your todo? ")

# numbers = [1, 2, 3, 4, 5,"do",7,'haha',11]
# numbers.sort()
# print(numbers)
# print(numbers)

# numbers.insert(3, 6)
# print(numbers)

# print(numbers.pop())

# print(numbers)

# print(numbers.index('haha'))

# numbers.sort()
# print(numbers)

# newNum = numbers.copy()

# newNum[2] = 888

# print(numbers)
# print(newNum)

# x = [[2,6],[6,2],[8,2],[5,12]]
# print(x[2])
# print(x[2][1])

# my_string = "Hello World"

# print(my_string[4:])
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# index = 0
# while index < len(alphabet):
#     print(alphabet[index])
#     index += 1
# alph2 = list(alphabet)
# print(alph2)

# alphabet = "abcdefghijklmnopqrstuvwxyz"
# alphalist = list(alphabet)
# print(alphalist)
# revlist=[]
# revlist.append(alphalist.pop())
# rev_alphabet = "_".join(revlist)
# print(rev_alphabet)
# print(type(alphabet))
# names = ['George', 'W', 'Bush']
# for name in names:
# print(name)

## for (condition) in range
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# for character in alphabet :
#     print(character, end="")

# print(" ")


# for number in range(1,1000,2):
#     print(number)

for x in range(1,11):
    for y in range(1,11):
        product= x * y
        print(f'{x} X {y} = {product}')

        