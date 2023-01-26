def add_five(num):
    print(num+5)
add_five(2)
print(add_five) # functions are objects

# functions within funcations
def add_3(num):
    def add_two(num):
        return num+2
    num_add_two = add_two(num)
    num_add_3 = num_add_two + 1
    return num_add_3
print(add_3(3))

# returning functions from functions
def get_math(operation):
    def add(num1,num2):
        return num1+num2
    def sub(num1,num2):
        return num1-num2
    
    if operation == "+":
        return add
    elif operation == "-":
        return sub
    
add_function = get_math("+")
print(add_function(2,2))

sub_function = get_math("-")
print(sub_function(5,3))
    
    
# Decorating a function
def title_decorator(print_a_name):
    def wrapper():
        print("Professor:")
        print_a_name()
    return wrapper

def print_my_name():
    print(input())
    
decorated_function = title_decorator(print_my_name)
decorated_function()

# decorators
@title_decorator
def print_the_name():
    print("Corey")
    
print_the_name()

# decorators with parameters
def also_a_title_decorator(print_a_name):
    def wrapper(*args,**kwargs):
        print("Professor:")
        print_a_name(*args,**kwargs)
    return wrapper

@also_a_title_decorator
def print_my_name(name,age):
    print(name + ", you are " + str(age))
print_my_name("Corey",18)