from main import app,UserInput,UserOutput
import unittest
from fastapi.testclient import TestClient

class NameTestCases(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)



    def test_get_incorrect_name_response(self):
        input_body=UserInput(question="what is your name?")
        response = self.client.post(
            "/person/",
            json={"question":"df"},
        )
        
        self.assertEqual(response.json(),UserOutput(name=None,error="enter a valid").model_dump())

    
    def test_get_correct_name_response(self):
        input_body=UserInput(question="what is your name?")
        response = self.client.post(
            "/person/",
            json={"question":"what is your name?"},
        )
        
        self.assertEqual(response.json().get("error"),None)

    
if __name__ == "__main__":
    unittest.main()