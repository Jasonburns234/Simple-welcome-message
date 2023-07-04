def greeting(name, age=28, color="red"):
 #Greets user with 'name' from 'input box' and 'age' next year, if available, default age is used
 # also includes favorite color    print(f'Hello {name.title()}, you will be {age + 1} years old next birthday!')
    print(f'We hear you like the color {color.lower()}!')

name = input('Enter your name: ')
age = int(input('Enter your age: '))
color = input('Enter your fave colour')

greeting(name, age, color)
