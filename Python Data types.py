#PYTHON DATA TYPES

#1.PYTHON NUMERIC DATA TYPES
number1=4
print(number1,'is of types',type(number1))

number2=2.3
print(number2,'is of type',type(number2))

number3=2+3j
print(number3,'is of type',type(number3))

'''________________________________________________________'''

#2.PYTHON LIST DATA TYPES
fruits=["Apple","Banana","Mango","Grapes","Orange"]
print(fruits,'is of type',type(fruits))

#access items in list using index numbers
fruits=["Apple","Banana","Mango","Grapes","Orange"]
print(fruits[0])
print(fruits[1])
print(fruits[3])

'''_______________________________________________________'''

#3.PYTHON TUPLE DATA TYPE
numbers=(24,35,1,2,34,5,6,56)
print(numbers,'is of type',type(numbers))

#accessing tuple items using index numbers
print(numbers[1])
print(numbers[4])

'''______________________________________________________'''


#4.PYTHON STRING DATA TYPE
animal='Elephant'
print(animal,'is of type',type(animal))


'''_____________________________________________________'''


#5.PYTHON SET DATA TYPE

student_id={101,102,103,104,105}
print(student_id)
print(student_id,'is of type',type(student_id))

'''_______________________________________________________'''



#6.PYTHON DICTIONARY DATA TYPE

student_fav_food={'Haritha':'Biryani','Hema':'Poori','Usha':'Chapati','Gowthami':'Noodles'}
print(student_fav_food)
print(student_fav_food,"is of type",type(student_fav_food))

#accessing DICTIONARY values Using keys
print(student_fav_food['Usha'])
print(student_fav_food['Haritha'])
