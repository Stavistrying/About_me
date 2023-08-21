def main():
    print("Welcome to the Introduction Game!")
    player_name = input("What's your name? ")
    print(f"Hello, {player_name}! Let's get to know each other.")
    
    print("\nYou find yourself in a virtual room.")
    print("To learn more about me, you'll need to make some choices.")
    
    while True:
        print("\nChoose an action:")
        print("1. Ask about my hobbies")
        print("2. Ask about my favorite food")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            print("I enjoy reading, hiking, and coding!")
        elif choice == "2":
            print("I love pizza and sushi!")
        elif choice == "3":
            print("Thanks for playing the Introduction Game. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
