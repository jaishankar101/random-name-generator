from fastapi import FastAPI
from pydantic import BaseModel
from faker import Faker


app = FastAPI(
    title="Random Name API", description="The api returns a random name on each request"
)
fake = Faker()

class GetName(BaseModel):
    """Properties shared among all uses"""
    class Config:
        """
        Allows variables to be in snakecase, but API contracts to be in camelcase.
        (Shown as an example)
        """

        allow_population_by_field_name = True

class UserInput(GetName):
    """Properties to receive on communicating with Model"""
    question: str  # question from the user

class UserOutput(GetName):
    name: str|None  # Reply from the Model based on the user input
    error: str |None # Any errors faced during the process

class Person(BaseModel):
    name: str


@app.post("/person/",response_model=UserOutput)
def read_name(query: UserInput) -> UserOutput:
    print("&&&&&&&&&&&&",query)
    if query.question == "what is your name?":
        person = Person(name="")
        person.name = fake.name()
        return UserOutput(name=person.name,error=None)
        # return {"Name":random_name}
    return UserOutput(name=None,error="enter a valid")
