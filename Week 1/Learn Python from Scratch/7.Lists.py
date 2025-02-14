#Lists in Python Programming Language

fruits=["Apple","Mango","Orange"]
#printing the list elements one by one using index numbers
print(fruits[0])     
print(fruits[1])     
print(fruits[2])
#adding an element to the list at the end of the list 
fruits.append("Banana")
print(fruits)
#changing an element in the list using index number 
fruits[1]="Grapes"
print(fruits)
#removing an element from the list using the element name 
fruits.remove("Orange")
#length of the list 
length=len(fruits)
print(length)
#clearing the list 
fruits.clear()
print(fruits)