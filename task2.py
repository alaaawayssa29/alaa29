fruits = ["Apple", "Strawberry", "Orange", "Banana", "Pineapple"]
print(fruits)
print("The first element is:", fruits[0])
print("The last element is:", fruits[-1])
fruits [1] = "Mango"
print(fruits)
fruits.insert(2, "Watermelon")
print(fruits)

fruit = input("Enter the name of fruit: ")
print(fruit.count(fruit) == 0)

fruits.sort()
print(fruits)