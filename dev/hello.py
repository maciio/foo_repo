# this is a Sample script just for fun
def say_hello(name):
    print(f"hello {name}")

def reply():
    reply=input("And whats your name?")
    print(f"it's nice to meet you too {reply} as well")
    return reply

def do_stuff():
    print("...what ever")

def say_bye(name):
    print(f"Good bye {name}!")    

say_hello(input("your name is... "))
say_bye(reply())

