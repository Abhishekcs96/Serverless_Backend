# Import mock first before importing anything else.
import boto3
import os
import unittest
from demoapp import lambda_handler

# Mocked AWS Credentials for moto to create a mock aws env. Always create this for safety.
# Always use mock decorator before making any boto3 calls. It could mutate real infrastructure.
# Moto decorator to mock out all calls to virtual mock aws environment setup

class TestLambdaDDB(unittest.TestCase):
    def test_handler(self):

        # Run lambda
        Response1 = lambda_handler(0, 0)
        Response2 = lambda_handler(0, 0)

        # Run unit test against Lambda status code
        self.assertEqual(int(Response2['body']), (int(Response1['body'])+1))


if __name__ == '__main__':
    unittest.main()
