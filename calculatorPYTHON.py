def add(x,y):
    return x+y
    def subtract(x, y):
        return x-y
        def multiply(x, y):
            return x*y
            def divide(x, y):
                return x/y
                # Print the various operations
                print("Choose Selection")
                print("a. Add")
                print("b. Subtract")
                print("c. Multiply")
                print("d. Divide")
                # Input numbers within operation
                while True:
                    choice = input("Enter choice a/b/c/d : ")
                    if choice in ("a","b", "c", "d"):
                        num1 = input("Enter the First Number: ")
                        num2 = input("Enter the Second Number: ")
                        # Check if user choice is part
                        if choice == "a":
                            print(num1, "+", num2, "=", add(num1,num2))
                            elif choice == "b":
                                print(num1, "-", num2, "=", subtract(num1, num2))
                                elif == "c":
                                    print(num1, "*", num2, "=", multiply(num1, num2))
                                    elif == "d":
                                        print(num1, "/", num2, "=", divide(num1, num2))
                                        elif:
                                            print("Wromg Result")                    