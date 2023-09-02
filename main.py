
def my_name():
    print("my name is manar")

    
def my_meal(food,drink):
    print(f"i like to eat {food} and while drinking {drink}")

def cube(number):
    return number**3  

def by_three(number):
    if number%3==0:
        return cube(number)
    else:
        return False
    print(by_three(6))

my_name()
my_meal("sushi","m")
print(cube(3))
by_three(3)