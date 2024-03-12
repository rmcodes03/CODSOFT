def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by 0"
    return a / b

while True:
    print("------------------------------------------------")
    try:
        a = float(input("> Enter value of number a: "))
        b = float(input("> Enter value of number b: "))
    except:
        print("> Enter valid integer.")
        continue
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Divsion")
    
    while True:
        choice = input("\n> Choose operation to be performed: ")
        if choice == '1':
            print(f"\n> Addition of {a} & {b} = " + str(add(a, b)))
            break
        elif choice == '2':
            print(f"\n> Subtraction of {a} & {b} = " + str(subtract(a, b)))
            break
        elif choice == '3':
            print(f"\n> Multiplication of {a} & {b} = " + str(multiply(a, b)))
            break
        elif choice == '4':
            print(f"\n> Division of {a} & {b} = {divide(a, b)}")
            break
        else:
            print("> Invalid input. Enter number from 1-5.")
            continue

    while True:
        choice2 = input("\n> Do you want to continue (y/n): ")
        if choice2.lower() == 'y':
            break
        elif choice2.lower() == 'n':
            exit()
        else:
            print("> Invalid input. Enter yes (y) or no (n).")
            continue
        
        
