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
book_room(3,4, '12-11-2024', '23-11-2024')
# cancel_booking(1)
# view_bookings(3)


# You can choose from these: standard_single_room, standard_double_room, deluxe_single_room, deluxe_double_room, presidential_room