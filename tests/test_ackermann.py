from tests.base import BaseSimpleAppTestClass


class SimpleAppTestFibonacci(BaseSimpleAppTestClass):
    def test_ackermann_should_return_correct_value_for_valid_input(self):
        response = self.client.post(
            "ackermann",
            data={
                "first_input": "1",
                "second_input": "2",
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"The Ackermann of 1 and 2 is 4.", response.data)

    def test_ackermann_should_return_bad_request_for_too_large_output(self):
        response = self.client.post(
            "ackermann",
            data={
                "first_input": "5",
                "second_input": "4",
            }
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Stack overflow, recursion depth exceeded! Please try with smaller values.", response.data)

    def test_ackermann_should_return_bad_request_for_negative_integer_input(self):
        response = self.client.post(
            "ackermann",
            data={
                "first_input": "-1",
                "second_input": "2",
            }
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Input should be positive integer!", response.data)

    def test_ackermann_should_return_bad_request_for_no_input(self):
        response = self.client.post(
            "ackermann",
            data={}
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Input is required!", response.data)

    def test_ackermann_should_return_bad_request_for_non_integer_input(self):
        response = self.client.post(
            "ackermann",
            data={
                "first_input": "0.3",
                "second_input": "2",
            }
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"Input should be an integer!", response.data)
