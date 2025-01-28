shopping_list = ['apples', 'banana', 'carrorts', 'bread', 'milk']

seperator = input("Please enter your preferred item seperator (e.g., ',',,'/', '-'): ")
ending = input("Please enter your preferred ending phrase (e.g., 'Ending of list', 'Thats all!'): ")

print("Your shopping list: ", end="\n\n")
for item in shopping_list:
    if item == shopping_list [-1]:
        print(item)
else:
    print(item, end=seperator + " ")
print("\n\n" + ending)