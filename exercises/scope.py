def run():
    print("What does this print?\nWhy?\n\nx = 10")
    

    def change():
        print("def change():\n    x = 11\n    x += 20\n    print(x)")
        x = 11
        x += 20
        print(x)
    def another_change():
        print("def another_change():\n    y = 50\n    print(y)")
        y = 50
        print(y)
    def answer():
        print("Answers:\nx=10 is global scope, the x and y in the functions are local and do not affect the global scope")

    change()
    another_change()
    answer()