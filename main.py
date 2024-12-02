# import time
# import os
# from auth import registration
# from bookings import book_room, cancel_booking, view_bookings
# from rooms import room_types
# from data import load_data_from_file, save_data_to_file
# from rooms import add_room, delete_room
# def clear_console():
#     command = 'cls' if os.name == 'nt' else 'clear'
#     os.system(command)
#
# menu = """
# ===============================================================
#                      Welcome to HOTEL LUXE
# ===============================================================
#
# 🏨 Your comfort is our priority! 🏨
#
# Please choose an option below by typing the corresponding number:
#
# 1  Register a new account
# 2  Book a room
# 3  Cancel a booking
# 4  View bookings
# 5  Add a room to the system
# 6  Delete a room
# 7  Exit
#
# ===============================================================
# """
#
# def show_menu():
#     clear_console()
#     print(menu)
#
# def main():
#     while True:
#         show_menu()
#         choice = input("Enter your choice: ").strip()
#
#         if choice == "1":
#             print("You selected: Register a new account")
#             # Gather input for registration
#             first_name = input("Enter your first name: ")
#             last_name = input("Enter your last name: ")
#             user_type = input("Enter your user type (admin/guest/manager/): ")
#             username = input("Enter your username: ")
#             email = input("Enter your email: ")
#             password = input("Enter your password: ")
#             is_reg = registration(first_name, last_name, user_type, username, email, password)
#             if is_reg is not None:
#                 user = load_data_from_file('users', param_key='username', param_value=username)
#                 print(f"Registration completed successfully! Your User-id is {user['id']}")
#                 time.sleep(5)
#             else:
#                 time.sleep(5)
#                 pass
#
#         elif choice == "2":
#             print("You selected: Book a room")
#             # Example of booking logic
#             user_id = int(input("Enter your user ID: "))
#             room_id = int(input("Enter room ID: "))
#             check_in = input("Enter check-in date (DD-MM-YYYY): ")
#             check_out = input("Enter check-out date (DD-MM-YYYY): ")
#             is_booked = book_room(user_id, room_id, check_in, check_out)
#             if is_booked is not None:
#                 print(is_booked)
#                 time.sleep(5)
#             else:
#                 time.sleep(5)
#                 pass
#
#         elif choice == "3":
#             print("You selected: Cancel a booking")
#             booking_id = int(input("Enter booking ID: "))
#             is_canceled = cancel_booking(booking_id)
#             if is_canceled is not None:
#                 print(is_canceled)
#                 time.sleep(5)
#             else:
#                 time.sleep(5)
#                 pass
#
#         elif choice == "4":
#             print("You selected: View bookings")
#             user_id = input("Enter user ID: ")
#             if user_id == '':
#                 is_viewed = view_bookings()
#             else:
#                 is_viewed = view_bookings(user_id=int(user_id))
#             if is_viewed is not None:
#                 print(is_viewed)
#                 time.sleep(5)
#             else:
#                 time.sleep(5)
#                 pass
#
#         elif choice == "5":
#             print("You selected: Add a room to the system")
#             room_type = input(f"Available Room Types: \n{'\n'.join([i for i in map(str, room_types.keys())])} \nEnter room type: ")
#             count = int(input("Enter count of rooms: "))
#             is_added_room = add_room(room_type, count)
#             if is_added_room is not None:
#                 print(is_added_room)
#                 time.sleep(5)
#             else:
#                 time.sleep(5)
#                 pass
#
#         elif choice == "6":
#             print("You selected: Delete a room from the system")
#             room_id = int(input("Enter room ID: "))
#             is_deleted = delete_room(room_id)
#             if is_deleted is not None:
#                 print(is_deleted)
#                 time.sleep(5)
#             else:
#                 time.sleep(5)
#                 pass
#
#         elif choice == "7":
#             print("Exiting the system. Goodbye!")
#             time.sleep(3)
#             break
#
#         else:
#             print("Invalid option. Please try again.")
#             time.sleep(3)
#
# if __name__ == "__main__":
#     main()

import time
import os
from auth import registration
from bookings import book_room, cancel_booking, view_bookings
from rooms import room_types
from data import load_data_from_file,save_data_to_file
from rooms import add_room, delete_room

# ANSI ranglar
class Colors:
    BOSH = '\033[95m'
    BLUE = '\033[92m'
    OCHKOK = '\033[96m'
    GREEN = '\033[92m'
    SARIQ= '\033[93m'
    QIZIL = '\033[91m'
    END = '\033[0m'
    OQ = '\033[1m'
    teg_chiziq = '\033[4m'
    ORQA_qora='\033[40m'

def clear_console():
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

menu = f"""
{Colors.teg_chiziq}{Colors.SARIQ}{Colors.ORQA_qora}================================================================{Colors.END}
{Colors.SARIQ}{Colors.ORQA_qora}                   Welcome to HOTEL LUXE                        {Colors.END}
{Colors.SARIQ}{Colors.teg_chiziq}{Colors.ORQA_qora}================================================================{Colors.END}
{Colors.ORQA_qora}                                                                {Colors.END}
{Colors.GREEN}{Colors.ORQA_qora}               🏨 Your comfort is our priority! 🏨              {Colors.END} 
{Colors.ORQA_qora}                                                                {Colors.END}
{Colors.ORQA_qora}                                                                {Colors.END}
{Colors.SARIQ}{Colors.ORQA_qora}Please choose an option below by typing the coresponding number:{Colors.END} 
{Colors.ORQA_qora}                                                                {Colors.END}
{Colors.ORQA_qora}                                                                {Colors.END}
{Colors.GREEN}{Colors.ORQA_qora}1  Register a new account                                       {Colors.END}
{Colors.GREEN}{Colors.ORQA_qora}2  Book a room                                                  {Colors.END}
{Colors.GREEN}{Colors.ORQA_qora}3  Cancel a booking                                             {Colors.END}
{Colors.GREEN}{Colors.ORQA_qora}4  View bookings                                                {Colors.END}
{Colors.GREEN}{Colors.ORQA_qora}5  Add a room to the system                                     {Colors.END}
{Colors.GREEN}{Colors.ORQA_qora}6  Delete a room                                                {Colors.END}
{Colors.GREEN}{Colors.ORQA_qora}7  Exit                                                         {Colors.END}
{Colors.ORQA_qora}                                                                {Colors.END}
{Colors.SARIQ}{Colors.teg_chiziq}{Colors.ORQA_qora}================================================================{Colors.END}
"""


def yozuvchi_animatsiya(text, delay=0.005):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def show_menu():
    clear_console()
    yozuvchi_animatsiya(menu)

def main():
    while True:
        show_menu()
        choice = input(f"{Colors.SARIQ}{Colors.ORQA_qora} Enter your choice: {Colors.END}").strip()

        if choice == "1":
            print(f"{Colors.GREEN}You selected: Register a new account{Colors.END}")
            first_name = input(f"{Colors.OCHKOK}Enter your first name: {Colors.END}")
            last_name = input(f"{Colors.OCHKOK}Enter your last name: {Colors.END}")
            user_type = input(f"{Colors.OCHKOK}Enter your user type (admin/guest/manager/): {Colors.END}")
            username = input(f"{Colors.OCHKOK}Enter your username: {Colors.END}")
            email = input(f"{Colors.OCHKOK}Enter your email: {Colors.END}")
            password = input(f"{Colors.OCHKOK}Enter your password: {Colors.END}")
            is_reg = registration(first_name, last_name, user_type, username, email, password)
            if is_reg is not None:
                user = load_data_from_file('users', param_key='username', param_value=username)
                print(f"{Colors.GREEN}Registration completed successfully! Your User-id is {user['id']}{Colors.END}")
            else:
                print(f"{Colors.QIZIL}Registration failed. Please try again.{Colors.END}")
            time.sleep(5)

        elif choice == "2":
            print(f"{Colors.GREEN}You selected: Book a room{Colors.END}")
            user_id = int(input(f"{Colors.OCHKOK}Enter your user ID: {Colors.END}"))
            room_id = int(input(f"{Colors.OCHKOK}Enter room ID: {Colors.END}"))
            check_in = input(f"{Colors.OCHKOK}Enter check-in date (DD-MM-YYYY): {Colors.END}")
            check_out = input(f"{Colors.OCHKOK}Enter check-out date (DD-MM-YYYY): {Colors.END}")
            is_booked = book_room(user_id, room_id, check_in, check_out)
            if is_booked is not None:
                print(f"{Colors.GREEN}{is_booked}{Colors.END}")
            else:
                print(f"{Colors.QIZIL}Booking failed. Please try again.{Colors.END}")
            time.sleep(5)

        elif choice == "3":
            print(f"{Colors.GREEN}You selected: Cancel a booking{Colors.END}")
            booking_id = int(input(f"{Colors.OCHKOK}Enter booking ID: {Colors.END}"))
            is_canceled = cancel_booking(booking_id)
            if is_canceled is not None:
                print(f"{Colors.GREEN}{is_canceled}{Colors.END}")
            else:
                print(f"{Colors.QIZIL}Cancellation failed. Please try again.{Colors.END}")
            time.sleep(5)

        elif choice == "4":
            print(f"{Colors.GREEN}You selected: View bookings{Colors.END}")
            user_id = input(f"{Colors.OCHKOK}Enter user ID (Leave blank for all bookings): {Colors.END}")
            if user_id == '':
                is_viewed = view_bookings()
            else:
                is_viewed = view_bookings(user_id=int(user_id))
            if is_viewed is not None:
                print(f"{Colors.GREEN}{is_viewed}{Colors.END}")
            else:
                print(f"{Colors.QIZIL}Failed to view bookings. Please try again.{Colors.END}")
            time.sleep(5)

        elif choice == "5":
            print(f"{Colors.GREEN}You selected: Add a room to the system{Colors.END}")
            room_type = input(f"{Colors.OCHKOK}Available Room Types: \n{'\n'.join([i for i in map(str, room_types.keys())])} \nEnter room type: {Colors.END}")
            count = int(input(f"{Colors.OCHKOK}Enter count of rooms: {Colors.END}"))
            is_added_room = add_room(room_type, count)
            if is_added_room is not None:
                print(f"{Colors.GREEN}{is_added_room}{Colors.END}")
            else:
                print(f"{Colors.QIZIL}Failed to add room. Please try again.{Colors.END}")
            time.sleep(5)


        elif choice == "6":
            print(f"{Colors.GREEN}You selected: Delete a room from the system{Colors.END}")
            room_id = int(input(f"{Colors.OCHKOK}Enter room ID: {Colors.END}"))
            is_deleted = delete_room(room_id)
            if is_deleted is not None:
                print(f"{Colors.GREEN}{is_deleted}{Colors.END}")
            else:
                print(f"{Colors.QIZIL}Failed to delete room. Please try again.{Colors.END}")
            time.sleep(5)

        elif choice == "7":
            print(f"{Colors.GREEN}Exiting the system. Goodbye!{Colors.END}")
            time.sleep(3)
            break

        else:
            print(f"{Colors.QIZIL}Invalid option. Please try again.{Colors.END}")
            time.sleep(3)

if __name__ == "__main__":
    main()


