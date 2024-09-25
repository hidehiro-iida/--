color = "re"

if color == "red":
    print("赤です")
elif color == "blue":
    print("青です")
else:
    print("その他")

numbers = [1,2,3,4,5]
print(numbers)

if 1 in numbers and 2 in numbers:
    print("含まれてる")

names =["佐藤","田中","鈴木"]
for index,name in enumerate(names,10):
    message = "{0} 番目は{1}です".format(index,name)
    print(message)

foods = ["米","パン","スープ"]
drinks = ["水","茶"]
for food ,drink in zip(foods,drinks):
    print(food,drink)



table = [[y*x for x in range(1,10)] for y in range(1,10)]
print(table)
