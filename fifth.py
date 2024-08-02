'''def greeter():
    name = input("What is your name good sir ")
    default_name = "J"
    if len(name) > 0:
        print("Good morning", name)
    else:
        print("Good morning", default_name)
    

greeter()
'''

def greet(name = "J"):
    return "Good morning " + name + "!"

print(greet("jas"))
print(greet())

