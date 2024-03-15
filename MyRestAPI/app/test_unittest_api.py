try:
    import os
    import unittest
    import app
    import json
    import requests
    from API import app

except Exception as e:
    print(e)



class FlaskTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    
    @classmethod
    def tearDownClass(cls):
        pass
    
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def tearDown(self):
        pass

    def test_health_endpoint(self):
        """
        Check Whether Response is 200
        """
        tester = app.test_client(self)
        response = tester.get("/health_check")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


if __name__ == "__main__":
    unittest.main()