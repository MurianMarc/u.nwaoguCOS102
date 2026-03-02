
print("1. Simple interest")
print("2. Compound interest")
print("3. Annuity")
print("4. Exit")

while True:
    choice = int(input("\nEnter your choice (1, 2, 3, or 4): "))
    if choice == 1:
        P = float(input("Enter the principal amount: "))
        R = float(input("Enter the interest rate (in %): "))
        T = float(input("Enter the time in years: "))
        SI = (P * R * T) / 100
        print("The Simple Interest after", T, "years is:", SI)
    elif choice == 2:
        P = float(input("Enter the principal amount: "))
        R = float(input("Enter the interest rate (in %): "))
        T = float(input("Enter the time in years: "))
        CI = P * (1 + R / 100) ** T 
        print("The Compound Interest after", T, "years is:", CI)
    elif choice == 3:
        P = float(input("Enter the principal amount: "))
        R = float(input("Enter the interest rate (in %): "))
        T = float(input("Enter the time in years: "))
        A = P * (((1 + R / 100) ** T) - 1) / (R / 100)
        print("The Annuity after", T, "years is:", A)
    elif choice == 4:
        print("Exiting the program.")
        break
    else:
        print("Please enter 1, 2, 3, or 4.")