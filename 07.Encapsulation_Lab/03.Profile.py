class Profile:
    min_length_username = 5
    max_length_username = 15
    min_password_length = 8
    min_upper_case_letters_count = 1
    min_digits_count = 1

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __validate_username(self, username):
        username_len = len(username)

        if self.min_length_username > username_len or username_len > self.max_length_username:
            raise ValueError(f'The username must be between {self.min_length_username} '
                             f'and {self.max_length_username} characters.')

    def __validate_password(self, password):
        if len(password) < self.min_password_length:
            raise ValueError('The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.')
        if len([x for x in password if x.isupper()]) < self.min_upper_case_letters_count:
            raise ValueError('The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.')
        if len([x for x in password if x.isdigit()]) < self.min_digits_count:
            raise ValueError('The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.')

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__validate_username(value)
        self.__username = value

    @property
    def password(self):
        return ''.join('*' * len(self.__password))

    @password.setter
    def password(self, value):
        self.__validate_password(value)
        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {self.password}'


# profile_with_invalid_password = Profile('My_username', 'My-password')
# profile_with_invalid_username = Profile('Too_long_username', 'Any')
correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
