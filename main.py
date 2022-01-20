from http.client        import HTTPException
from typing             import List
from fastapi            import FastAPI, Request, Body, status
from uuid               import uuid4
from fastapi.encoders   import jsonable_encoder
from fastapi.responses  import JSONResponse
from database           import  database
from model              import People, Person, Gender
from  schema import personEntity, personsEntity
import   bson            


#  App Object
app = FastAPI()


@app.get('/people')
async def people():
    print(personsEntity(database.passengers.find({})))
    # return personsEntity(database.passengers.find({}))
    # ->list:
    #  people = []
    # cursor = database.passengers.find({})
    # for person in cursor:
    #     people.append(People(**person))
    # return people

@app.post("/people")
async def register_people(person: Person)->dict:
    name        = person.name
    survived    = person.survived    
    passengerClass = person.passengerClass
    name        = person.name          
    sex         = person.sex           
    age         = person.age             
    siblingsOrSpousesAboard = person.siblingsOrSpousesAboard
    parentsOrChildrenAboard = person.parentsOrChildrenAboard
    fare        = person.fare
    uuid        = uuid4()

    person_data = {}

    person_data = {
       "name": name,
       "survived": survived,
       "passengerClass": passengerClass,
       "sex": sex,
       "age": age,
       "siblingsOrSpousesAboard": siblingsOrSpousesAboard,
       "parentsOrChildrenAboard": parentsOrChildrenAboard,
       "fare": fare,
       "uuid": uuid
    }
    database.passengers.insert_one(person_data, {'_id': 0})
    return person_data
    


# @app.get('people/{uuid}', response_description="delete this person")
# async def delete(person_id: UUID):
#     cursor = database.passengers.find({})
#     for people in db:
#         if people.uuid == person_id:
#             db.remove()
#             return 
#     raise HTTPException(
#         status_code=404,
#         details=f"user with uuid {person_id} does not exist in the database"
#         )






  







# @app.put('/people/{uuid}')
# async def update_people(uuid: UUID, people_update: UpdatePeople):
#     for people in db:
#         if people.uuid == uuid:
#             if people_update.survived is not None:
#                 people.survived = people_update.survived

#             if people_update.passengerClass is not None:
#                 people.passengerClass = people_update.passengerClass

#             if people_update.name is not None:
#                 people.name = people_update.name

#             if people_update.sex is not None:
#                 people.sex = people_update.sex

#             if people_update.age is not None:
#                 people.age = people_update.age

#             if people_update.siblingsOrSpousesAboard is not None:
#                 people.siblingsOrSpousesAboard = people_update.siblingsOrSpousesAboard

#             if people_update.parentsOrChildrenAboard is not None:
#                 people.parentsOrChildrenAboard = people_update.parentsOrChildrenAboard

#             if people_update.fare is not None:
#                 people.fare = people_update.fare
#             return
#     raise HTTPException(
#         status_code=404,
#         details=f"user with uuid {uuid} does not exist in the database"
#     )


