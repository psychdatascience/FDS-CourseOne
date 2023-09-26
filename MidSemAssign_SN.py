import statistics_module as sm

while True:
    print("\nMenu:")
    print("(1) Enter a new set of numbers")
    print("(2) Compute mean")
    print("(3) Compute standard deviation")
    print("(4) Compute standard error")
    print("(5) Calculate z-score of a new observation")
    print("(6) Produce a summary")
    print("(7) Quit")
    
    choice = input("Select an option: ")
    
    if choice == '1':
        # numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
        numbers = []
        print("Enter numbers one by one. Type 'done' when you're finished.")
        num = input("> ")
        while num.lower() != 'done':
            numbers.append(float(num))
            num = input("> ")

    
    elif choice == '2':
        if 'numbers' in locals():
            print("Mean:", sm.mean(numbers))
        else:
            print("Please enter a set of numbers first.")
    
    elif choice == '3':
        if 'numbers' in locals():
            print("Standard Deviation:", sm.std_dev(numbers))
        else:
            print("Please enter a set of numbers first.")
    
    elif choice == '4':
        if 'numbers' in locals():
            print("Standard Error:", sm.std_error(numbers))
        else:
            print("Please enter a set of numbers first.")
    
    elif choice == '5':
        if 'numbers' in locals():
            new_observation = float(input("Enter a new observation: "))
            print("Z-Score:", sm.z_score(new_observation, numbers))
        else:
            print("Please enter a set of numbers first.")
    
    elif choice == '6':
        if 'numbers' in locals():
            print(f"Mean: {sm.mean(numbers)}")
            print(f"Standard Deviation: {sm.std_dev(numbers)}")
            print(f"Standard Error: {sm.std_error(numbers)}")
        else:
            print("Please enter a set of numbers first.")
    
    elif choice == '7':
        print("Goodbye!")
        break
    
    else:
        print("Invalid option. Please try again.")
