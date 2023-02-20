class ValidateMixin:
    @staticmethod
    def validate_name(value, error_massage):
        if value.strip() == '':
            raise ValueError(error_massage)
