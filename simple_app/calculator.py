from flask import render_template, Blueprint, request, abort

from simple_app.consts import (
    FIRST_FIBONACCI_ELEMENT,
    SECOND_FIBONACCI_ELEMENT,
    FIBONACCI_SUCCESS_RESULT_TEXT,
    FACTORIAL_SUCCESS_RESULT_TEXT,
    ACKERMANN_SUCCESS_RESULT_TEXT,
    MAX_RECURSION_DEPTH_ERROR_MESSAGE,
    INVALID_ARGUMENT_ERROR_CODE,
    MAXIMUM_SUPPORTED_OUTPUT_VALUE, MAXIMUM_SUPPORTED_OUTPUT_VALUE_EXCEEDED)
from simple_app.validators import (
    FibonacciAPIValidator,
    FactorialAPIValidator,
    AckermannAPIValidator
)

bp = Blueprint('calculator', __name__)


@bp.route('/', methods=["GET"])
def index():
    return render_template('index.html')


@bp.route("/fibonacci", methods=["POST"])
def fibonacci():
    input_number = request.form.get('input_number')

    error = FibonacciAPIValidator.validate([input_number])
    if error is not None:
        abort(INVALID_ARGUMENT_ERROR_CODE, error)

    input_number = int(input_number)
    current_fib, next_fib = FIRST_FIBONACCI_ELEMENT, SECOND_FIBONACCI_ELEMENT

    for i in range(input_number):
        current_fib, next_fib = next_fib, current_fib + next_fib
        if current_fib > MAXIMUM_SUPPORTED_OUTPUT_VALUE:
            abort(INVALID_ARGUMENT_ERROR_CODE, MAXIMUM_SUPPORTED_OUTPUT_VALUE_EXCEEDED)

    return render_template(
        'result.html',
        result=FIBONACCI_SUCCESS_RESULT_TEXT.format(input_number, current_fib)
    )


@bp.route("/factorial", methods=["POST"])
def factorial():
    input_number = request.form.get('input_number')

    error = FactorialAPIValidator.validate([input_number])
    if error is not None:
        abort(INVALID_ARGUMENT_ERROR_CODE, error)

    input_number = int(input_number)
    result = 1
    for number in range(1, input_number + 1):
        result *= number
        if result > MAXIMUM_SUPPORTED_OUTPUT_VALUE:
            abort(INVALID_ARGUMENT_ERROR_CODE, MAXIMUM_SUPPORTED_OUTPUT_VALUE_EXCEEDED)

    return render_template(
        'result.html',
        result=FACTORIAL_SUCCESS_RESULT_TEXT.format(input_number, result)
    )


@bp.route("/ackermann", methods=["POST"])
def ackermann():
    first_input = request.form.get('first_input')
    second_input = request.form.get('second_input')

    error = AckermannAPIValidator.validate([first_input, second_input])
    if error is not None:
        abort(INVALID_ARGUMENT_ERROR_CODE, error)

    first_input, second_input = int(first_input), int(second_input)
    try:
        result = _calculate_ackermann_recursive(first_input, second_input)
    except RecursionError:
        abort(INVALID_ARGUMENT_ERROR_CODE, MAX_RECURSION_DEPTH_ERROR_MESSAGE)

    return render_template(
        'result.html',
        result=ACKERMANN_SUCCESS_RESULT_TEXT.format(first_input, second_input, result)
    )


def _calculate_ackermann_recursive(first_input: int, second_input: int) -> int:
    if first_input == 0:
        return second_input + 1

    if second_input == 0:
        return _calculate_ackermann_recursive(first_input - 1, 1)

    return _calculate_ackermann_recursive(
        first_input - 1,
        _calculate_ackermann_recursive(first_input, second_input - 1))
