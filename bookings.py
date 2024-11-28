from datetime import datetime

from data import load_data_from_file, save_data_to_file, update_data, delete_data
from rooms import update_room_status, room_types


def book_room(user_id: int, room_id: int, check_in: str, check_out: str):
	if load_data_from_file(file_name='users', param_key='id', param_value=user_id) is None:
		print("Пользователь не найден.")
		return

	if load_data_from_file('rooms', 'id', room_id) is None:
		print("Номер не найден.")
		return

	try:
		check_in_date = datetime.strptime(check_in, "%d-%m-%Y").date()
		check_out_date = datetime.strptime(check_out, "%d-%m-%Y").date()
	except ValueError:
		print("Ошибка: даты должны быть в формате DD-MM-YYYY.")
		return

	# 2. Проверка логической последовательности дат
	if check_in_date >= check_out_date:
		print("Ошибка: дата выезда должна быть позже даты заезда.")
		return

	bookings = load_data_from_file(file_name='bookings', param_key='room_id', param_value=room_id, quantity='all')

	if bookings is not None:
		for booking in bookings:
			if not (check_out_date <= datetime.strptime(booking["check_in"], "%d-%m-%Y").date()
			        or check_in_date >= datetime.strptime(booking["check_out"], "%d-%m-%Y").date()):
				print("Номер занят на указанные даты.")
				return
	if load_data_from_file('bookings', param_key='all') is not None:
		booking_id = load_data_from_file(file_name='bookings', param_key='id') + 1
	else:
		booking_id = 1

	booking = {
		"id": booking_id,
		"user_id": user_id,
		"room_id": room_id,
		"check_in": check_in,
		"check_out": check_out
	}

	user = load_data_from_file(file_name='users', param_key='id', param_value=user_id)
	room = load_data_from_file(file_name="rooms", param_key='id', param_value=room_id)

	update_data(file_name='users', obj_id=user_id, param_key='bookings', new_param_value=user['bookings'] + 1)

	if room["status"] == 0:
		update_room_status(room_id=room_id)
	save_data_to_file(file_name='bookings', data=booking)
	# print()
	return f"Бронирование успешно! ID бронирования: {booking_id}"


def cancel_booking(booking_id):
	booking = load_data_from_file(file_name='bookings', param_key='id', param_value=booking_id)

	if booking is not None:
		user = load_data_from_file(file_name='users', param_key='id', param_value=booking['user_id'])

		update_data(file_name='users', obj_id=booking['user_id'], param_key='bookings',
		            new_param_value=user['bookings'] - 1)

		delete_data(file_name='bookings', param_key='id', param_value=booking_id)

		if load_data_from_file(file_name='bookings', param_key='room_id', param_value=booking['room_id']) is None:
			update_room_status(room_id=booking['room_id'])
	else:
		# print()
		return f"Booking with ID {booking_id} doesn't exist."


def view_bookings(user_id=None):
	if user_id is None:
		bookings = load_data_from_file(file_name='bookings', param_key='all')

		print("Все бронированные номера:")
		for booking in bookings:
			user = load_data_from_file(file_name='users', param_key='id', param_value=booking['user_id'])
			print(
				f"ID: {booking['id']}, "
				f"Комната с номером: {booking['room_id']}, "
				f"Имя гостя: {user['first_name']} {user['last_name']} "
				f"На период с {booking['check_in']} до {booking['check_out']}")
		return "Это все брони."

	user = load_data_from_file(file_name='users', param_key='id', param_value=user_id)
	print(f"Все бронированные номера пользователя: {user['first_name']} {user['last_name']}")
	bookings = load_data_from_file(file_name='bookings', param_key='user_id', param_value=user_id, quantity='all')

	for booking in bookings:
		room = load_data_from_file(file_name="rooms", param_key='id', param_value=booking['room_id'])
		print(
			f"ID: {booking['id']}, "
			f"Комната с номером: {booking['room_id']}, "
			f"Тип комнаты {room_types[room['type']]} "
			f"На период с {booking['check_in']} до {booking['check_out']}")

	return  "Это все брони."








































