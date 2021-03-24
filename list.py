fruits=["apple","banana","cherry"]
print(fruits)

list2=[1,2,3,4,["apple","banana","cherry"],[True,False]]
print(list2)
print(list2[1])
print(list2[2])
print(list2[3])
print(list2[0])
print(list2[3:-1])
print(list2[3:6])
if "apple" in fruits:
  print("yes, 'apple' is in the fruit list")
fruits=["apple","banana","cherry","orange","kiwi","manngo"]
fruits[1]="blackcurrent"
print(fruits)
fruits[1:3]=["watermelon"]
fruits.insert(2,"passion")