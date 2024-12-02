from xml.sax.handler import property_interning_dict

from auth import *
from rooms import *
from bookings import *
from data import *


""" auth.py """

# registration('Jhon2', "Doe2", 'director',"jhondoe2", 'jhon122883@gmail.com', 'import123')
# login_user('shavkat', 'fasfsdfasfdsf123')

""" rooms.py """
# add_room("presidential_room", 15)
# print(load_data_from_file(file_name='rooms', param_key='id', param_value=3))
# update_room_status(1)
# delete_room(3)


""" data.py """
# update_data(file_name='users', id=1, param_key='first_name', new_param_value="Shava")
#
# delete_data('users', param_key='username', param_value='jhondoe2')
# print(load_data_from_file('rooms', param_key='type', param_value='standard_double_room', ))

""" bookings.py """
# book_room(3,4, '12-11-2024', '23-11-2024')
# cancel_booking(1)
# view_bookings(3)

# load_data_from_file('rooms', param_key="")

# print(save_data_to_file(data={
#         "id": 2,
#         "first_name": 3,
#         "last_name": 1,
#     }, file_name='test'))
#

# book_room(user_id=3, room_id=5, check_in="13-09-2024", check_out="15-10-2024")

# a = {
# 	 "apple": 1,
#      "banana": 2,
#     }

# l = [1,3,3,5,2, "ASDFd",]
#
# t = ('afdasdf', 124,1234,1234,1234,1234,1234,1234,1234,134,134,1234,)

# You can choose from these: standard_single_room, standard_double_room, deluxe_single_room, deluxe_double_room, presidential_room

# with open("DataBase/users.json", 'r') as f:
# 	data = json.loads(f.read())


# delete_data(file_name="rooms", param_key="id", param_value="34")
# print(load_data_from_file(file_name='users', param_key='username', param_value='shavkat'))
# registration('Shavkat', "asdfa", 'guest', 'user', 'asdkjfhkf@gmail.com', '12356634sdffgsd')


# print(registration(
# 	first_name="Senpai",
#     last_name="Aziz",
# 	user_type="admin",
# 	username="azi243ez",
# 	email="aksjdfhkjdfgak@gmail.com",
# 	password="aziz23423",
# ))




# a = []
#
# a.append(input())
#
# print(a),



#
# # try:
# a = 1
#
# b = 0

# print(a / b)

# except ZeroDivisionError:
# 	print("dhhfsghh")


a = load_data_from_file(file_name="rooms", param_key="type", param_value="presidential_room", quantity="all")


print(a)










