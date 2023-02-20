class Validator:
    @staticmethod
    def raise_exception_when_it_is_empty_string_or_white_space(value, error_message):
        if value.strip() == "":
            raise ValueError(error_message)

    @staticmethod
    def raise_exception_when_it_is_0_or_less(value, error_message):
        if value <= 0:
            raise ValueError(error_message)