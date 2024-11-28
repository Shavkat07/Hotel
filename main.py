import time
import os
from auth import registration
from bookings import book_room, cancel_booking, view_bookings
from rooms import room_types
from data import load_data_from_file, save_data_to_file
from rooms import add_room, delete_room
def clear_console():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

menu = """
===============================================================
                     Welcome to HOTEL LUXE                    
===============================================================

🏨 Your comfort is our priority! 🏨

Please choose an option below by typing the corresponding number:

1  Register a new account
2  Book a room
3  Cancel a booking
4  View bookings
5  Add a room to the system
6  Delete a room
7  Exit

===============================================================
"""

def show_menu():
    clear_console()
    print(menu)

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            print("You selected: Register a new account")
            # Gather input for registration
            first_name = input("Enter your first name: ")
            last_name = input("Enter your last name: ")
            user_type = input("Enter your user type (admin/guest/manager/): ")
            username = input("Enter your username: ")
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            is_reg = registration(first_name, last_name, user_type, username, email, password)
            if is_reg is not None:
                user = load_data_from_file('users', param_key='username', param_value=username)
                print(f"Registration completed successfully! Your User-id is {user['id']}")
                time.sleep(5)
            else:
                time.sleep(5)
                pass

        elif choice == "2":
            print("You selected: Book a room")
            # Example of booking logic
            user_id = int(input("Enter your user ID: "))
            room_id = int(input("Enter room ID: "))
            check_in = input("Enter check-in date (YYYY-MM-DD): ")
            check_out = input("Enter check-out date (YYYY-MM-DD): ")
            is_booked = book_room(user_id, room_id, check_in, check_out)
            if is_booked is not None:
                print(is_booked)
                time.sleep(5)
            else:
                time.sleep(5)
                pass

        elif choice == "3":
            print("You selected: Cancel a booking")
            booking_id = int(input("Enter booking ID: "))
            is_canceled = cancel_booking(booking_id)
            if is_canceled is not None:
                print(is_canceled)
                time.sleep(5)
            else:
                time.sleep(5)
                pass

        elif choice == "4":
            print("You selected: View bookings")
            user_id = input("Enter user ID: ")
            if user_id == '':
                is_viewed = view_bookings()
            else:
                is_viewed = view_bookings(user_id=int(user_id))
            if is_viewed is not None:
                print(is_viewed)
                time.sleep(5)
            else:
                time.sleep(5)
                pass

        elif choice == "5":
            print("You selected: Add a room to the system")
            room_type = input(f"Available Room Types: \n{'\n'.join([i for i in map(str, room_types.keys())])} \nEnter room type: ")
            count = int(input("Enter count of rooms: "))
            is_added_room = add_room(room_type, count)
            if is_added_room is not None:
                print(is_added_room)
                time.sleep(5)
            else:
                time.sleep(5)
                pass

        elif choice == "6":
            print("You selected: Delete a room from the system")
            room_id = int(input("Enter room ID: "))
            is_deleted = delete_room(room_id)
            if is_deleted is not None:
                print(is_deleted)
                time.sleep(5)
            else:
                time.sleep(5)
                pass

        elif choice == "7":
            print("Exiting the system. Goodbye!")
            time.sleep(3)
            break

        else:
            print("Invalid option. Please try again.")
            time.sleep(3)

if __name__ == "__main__":
    main()

