class Validator:
    @staticmethod
    def raise_exception_when_value_is_empty_string_or_white_space(value, error_message):
        if value.strip() == '':
            raise ValueError(error_message)

