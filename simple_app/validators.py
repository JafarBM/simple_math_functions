from typing import Optional, List

from simple_app.consts import (
    NON_POSITIVE_INPUT_VALUE_ERROR_MESSAGE,
    NON_INTEGER_INPUT_VALUE_ERROR_MESSAGE,
    ELEMENT_NUMBER_REQUIRED_ERROR_MESSAGE
)


class BaseInputValidator:
    @classmethod
    def validate(cls, elements: Optional[List], **kwargs) -> Optional[str]:
        for element_number in elements:
            if not cls._is_input_provided(element_number):
                return ELEMENT_NUMBER_REQUIRED_ERROR_MESSAGE
            if not cls._is_input_integer(element_number):
                return NON_INTEGER_INPUT_VALUE_ERROR_MESSAGE
            if not cls._is_input_positive(int(element_number)):
                return NON_POSITIVE_INPUT_VALUE_ERROR_MESSAGE

        return None

    @staticmethod
    def _is_input_provided(element) -> bool:
        return element

    @staticmethod
    def _is_input_integer(element) -> bool:
        try:
            int(element)
            return True
        except ValueError:
            return False

    @staticmethod
    def _is_input_positive(element) -> bool:
        return element >= 0


class FibonacciInputValidator(BaseInputValidator):
    pass


class FactorialInputValidator(BaseInputValidator):
    pass


class AckermannInputValidator(BaseInputValidator):
        pass
