from MySubPackage import one

print("top-level in two.py")

def func():
    print("func() ran in one.py")

one.func()

if __name__ == "__main__":
    print("two.py is being run directly")
else:
    print("two.py is being imported into another module")