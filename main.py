from astronauts import people_in_space
from iss_tracker import iss_position
from news_or_stock import news_or_stock_menu

def main_menu():
    while True:
        print("\n=== Live Data Reporter ===")
        print("1. View astronauts in space")
        print("2. Track ISS position")
        print("3. View news or stock data")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            people_in_space()
        elif choice == '2':
            iss_position()
        elif choice == '3':
            news_or_stock_menu()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
