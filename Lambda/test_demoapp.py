import unittest
from demoapp import lambda_handler


class TestLambdaDDB(unittest.TestCase):
    def test_handler(self):

        # Call lambda handler from demoapp and test demoapp handler on demotable.
        Response1 = lambda_handler(0, 0)
        Response2 = lambda_handler(0, 0)
        print(Response1, Response2)

        # Check lambda status codes to make sure they return first. Print response body
        self.assertEqual(200, Response1['statusCode'])
        self.assertEqual(200, Response2['statusCode'])
        print(Response1['body'], Response2['body'])

        # Then Run unit test against Response values to make sure that second response is an increment.
        self.assertEqual(int(Response2['body']), (int(Response1['body'])+1))
        
if __name__ == '__main__':
    unittest.main()
