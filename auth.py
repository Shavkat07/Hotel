from data import save_data_to_file, load_data_from_file

_is_login = False


def registration(
		first_name: str,
		last_name: str,
		user_type: str,
		username: str,
		email: str,
		password: str
		):

	USER_TYPES = {
		'admin': 'Admin',
		'guest': 'Guest',
		'director': 'director',
		'manager': 'manager',
	}

	user = {
		'id': 0,
		'username': "",
		'first_name': "",
		'last_name': "",
		'email': "",
		'password': "",
		'user_type': "admin",
	}

	if len(first_name) <= 50:
		user['first_name'] = first_name
	else:
		print("Ism Xato!!!")
		return

	if len(last_name) <= 50:
		user['last_name'] = last_name
	else:
		print("Familiya Xato!!!")
		return

	if user_type in USER_TYPES:
		user["user_type"] = user_type
		if user_type == "guest":
			user["bookings"] = 0
	else:
		print(f"User Type is not correct. You can choose from {list(USER_TYPES.keys())}.")
		return

	if load_data_from_file(file_name='users', param_key='username',
	                       param_value=username) is None and username.islower():
		user['username'] = username
	else:
		print("Username already exists!!!")
		return

	if load_data_from_file(file_name='users', param_key='email', param_value=email) is None:
		if email.islower() and "@" in email:
			user['email'] = email
		else:
			print('Email format is invalid!!!')
			return
	else:
		print("Email already exists!!!")
		return

	if len(password) >= 8 and password.isalnum() and not password.isalpha():
		# Bu yerda passwordni hesh lash kerak
		user['password'] = password
	else:
		print("Password must contain at least 8 characters and must contain at least one letter or number!!!")
		return

	if load_data_from_file(file_name='users', param_key='id', ) is not None:
		user['id'] = load_data_from_file(file_name='users', param_key='id', ) + 1
	else:
		user['id'] = 1

	save_data_to_file(data=user, file_name='users')
	return "User created successfully!"

#
# def login_user(username, password):
# 	global _is_login  # global variebles haqida  https://www.w3schools.com/python/python_variables_global.asp
#
# 	if load_data_from_file(file_name='users', param_key='username', param_value=username) is not None:
# 		user = load_data_from_file(file_name='users', param_key='username', param_value=username)
# 		if password == user.get('password'):
# 			_is_login = True
# 			print("Login successfully!")
# 			return _is_login
# 		else:
# 			print("Password does not match")
# 			return
#
# 	else:
# 		print("Username doesn't exist!!!")
# 		return


# def logout():
# 	global _is_login
#
# 	if _is_login:
# 		_is_login = False
#
# 	return "Logout successfully!"
#
#
# def is_logged_in():
# 	return _is_login
