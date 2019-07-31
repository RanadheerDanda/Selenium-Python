#from MySubPackage import two


def func():
    print("func() ran in one.py")

print("top-level print inside of one.py")

if __name__ == "__main__":
    print("one.py is being run directly")
    func()
else:
    print("one.py is being imported into another module")