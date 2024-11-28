from data import save_data_to_file, load_data_from_file, update_data, delete_data

room_types = {
	"standard_single_room": "Standard Single room",
	"standard_double_room": "Standard Double room",
	"deluxe_single_room": "Deluxe Single room",
	"deluxe_double_room": "Deluxe Double room",
	"presidential_room": "Presidential room",
}

def add_room(room_type: str, count: int):


	room = {
		"id": 0,
		"type": "standard_single_room",
		"status": 0,
		"floor": 1,

	}

	if load_data_from_file(file_name="rooms", param_key='id') is not None:
		room["id"] = load_data_from_file(file_name="rooms", param_key='id') + 1
	else:
		room["id"] = 1

	if room_type in room_types:
		room["type"] = room_type
		if room_type == "standard_single_room" or room_type == "standard_double_room":
			room["floor"] = 1
		elif room_type == "deluxe_single_room" or room_type == "deluxe_double_room":
			room["floor"] = 2
		elif room_type == "presidential_room":
			room["floor"] = 3

		# agar room type single bulsa birinchi qavat, delux ikkinchi qavat, presidential uchinchi qavatda
	else:
		print("Invalid room type")
		print("You can choose from these: " + ", ".join(room_types.keys()))
		return

	for i in range(1, count + 1):
		save_data_to_file(data=room, file_name="rooms")
		room["id"] += 1

	return "Room Added Successfully"


def update_room_status(room_id):
	room = load_data_from_file(file_name="rooms", param_key='id', param_value=room_id)
	if room["status"] == 0:
		update_data(file_name="rooms", obj_id=room_id, param_key='status', new_param_value=1)
		return "Room Status Updated Successfully"
	else:
		update_data(file_name="rooms", obj_id=room_id, param_key='status', new_param_value=0)
		return "Room Status Updated Successfully"



def delete_room(room_id):
	delete_data(file_name="rooms", param_key='id', param_value=room_id)

# def view_rooms(id: int='all', room_type: str='all', status = -1):
# 	if status == -1 and room_type == "all" and id == "all":
# 		load_data_from_file("rooms", param_key='all')
# 	else:
# 		load_data_from_file("rooms", param_key='status', param_value=status)