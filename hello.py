# print("Hello World!")

print("What is your name?")
name = input()
print("Hello, " + name)


#print("age")
print ("Do you want to know your age?")

user_input = input ("Enter your birth year: ")

age =int( 2020 ) - int(user_input)
print ("You are " + str ( age ) + " years old!")


#ch.py file added here
print ("Write a number to know Digit or Number !")
num = int( input())
if num <=  9:
    print ("Its  Digit")
else : 
    if num > 9 :
        print ("Its not digit but number")
#calorie.py file added here
print (" Today's date? ")
date = input ()
print ( "Breakfast calories?(Kcal)")
breakfast =  float(input ())
print ("Lunch calories?(Kcal)")
lunch = float(input())
print ("Dinner claories?(Kcal)")
dinner = float(input())
print ("Snack calories?(Kcal)")
snack = float(input())
sum = str((breakfast) + (lunch) + (dinner) + (snack))
print ("Calorie content for " + str( date )+" :" +   sum  +" Kilo-calories" )

#if.py file added here
value = input('Would you like to continue? ')

if value == 'y' or value == 'yes':
    print('Continuing ...')
    print('Complete!')
elif value == 'n' or value == 'no':
    print('Exiting')
else:
    print('Please try again and respond with yes or no.')
