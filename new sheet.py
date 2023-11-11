import math

pi = 3.49
print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(math.sqrt(pi))
pi = -3.49
print(abs(pi))
print(pow(pi,2))
x = 1
y = 2
z = 3
print(max(x,y,z))
print(min(x,y,z))

name = "ashim kar"
first_name = name[0:3]
last_name = name[6:9]
other_name = name[0:9:2]
reversed_name = name[::-1]
print(first_name)
print(last_name)
print(other_name)
print(reversed_name)

website1 = "http://google.com"
website2 = "http://yahoo.com"
slice = slice(7,-4)
print(website1[slice])
print(website2[slice])

age = int(input("how old are you?: "))
if age == 100:
    print("you are a century old")
elif age >= 18:
    print("you are an adult")
elif age < 0:
    print("you haven't been born yet")
else:
    print("you are a child")

temp = int(input("what is the temperature outside?: "))
if not(temp >= 0 and temp <= 30):
    print("the temperature is good today. " "go outside")
elif temp < 0 or temp > 30:
    print("the temperature is very bad. " "don't go out there")
name = ""
while len(name) == 0:
    name = input("enter your name: ")
print("hello "+ name)
