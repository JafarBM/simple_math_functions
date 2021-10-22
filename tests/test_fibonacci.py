from tests.base import BaseSimpleAppTestClass


class SimpleAppTestFibonacci(BaseSimpleAppTestClass):
    def test_fibonacci_should_return_correct_value_for_valid_input(self):
        response = self.client.post(
            "fibonacci",
            data={"input_number": "10"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"The 10th element of Fibonacci series is 55.", response.data)

    def test_fibonacci_should_return_bad_request_for_too_large_output(self):
        response = self.client.post(
            "fibonacci",
            data={"input_number": "10000"}
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Output value is too large! please try with smaller inputs!", response.data)

    def test_fibonacci_should_return_bad_request_for_negative_integer_input(self):
        response = self.client.post(
            "fibonacci",
            data={"input_number": "-1"}
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Input should be positive integer!", response.data)

    def test_fibonacci_should_return_bad_request_for_no_input(self):
        response = self.client.post(
            "fibonacci",
            data={}
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Input is required!", response.data)

    def test_fibonacci_should_return_bad_request_for_non_integer_input(self):
        response = self.client.post(
            "fibonacci",
            data={"input_number": "0.3"}
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Input should be an integer!", response.data)
