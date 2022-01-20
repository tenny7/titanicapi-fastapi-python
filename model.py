from   typing          import List, Optional
from   pydantic        import BaseModel, Field
from   bson            import ObjectId
from   enum            import Enum
import uuid





class PyObjectId(str):
    
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def vlaidate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')


        


class Gender(str, Enum):
    male    = "male"
    female  = "female"
    other   = "other"


class People(BaseModel):
    # id: Optional[PyObjectId] = Field(alias='_id')
    age: Optional[int]              = Field(alias="age")
    fare: Optional[float]           = Field(alias="fare")
    name: Optional[str]             = Field(alias="name")
    passengerClass: Optional[int]   = Field(alias="passengerClass")
    sex: Optional[Gender]           = Field(alias="sex")
    survived: Optional[bool]        = Field(alias="survived")
    siblingsOrSpousesAboard: Optional[int] = Field(alias="siblingsOrSpousesAboard")
    parentsOrChildrenAboard: Optional[int] = Field(alias="parentsOrChildrenAboard")
    
    uuid: Optional[str]            = Field(alias="uuid")

    class Config:   
        arbitrary_types_allowed = True
        allow_population_by_field_name = True
        # json_encoders = {
        #     ObjectId: lambda x: str(x)            
        # }

class Person(BaseModel):
    # id: PyObjectId = Field(default_factory=PyObjectId,alias='_id')
    age: Optional[int]              = Field(alias="age")
    fare: Optional[float]           = Field(alias="fare")
    name: Optional[str]             = Field(alias="name")
    passengerClass: Optional[int]   = Field(alias="passengerClass")
    sex: Optional[Gender]           = Field(alias="sex")
    survived: Optional[bool]        = Field(alias="survived")
    siblingsOrSpousesAboard: Optional[int] = Field(alias="siblingsOrSpousesAboard")
    parentsOrChildrenAboard: Optional[int] = Field(alias="parentsOrChildrenAboard")
    uuid: Optional[str]             = Field(alias="uuid")
    # default_factory=uuid.uuid4, 

    # class Config:   
    #     arbitrary_types_allowed = True
    #     allow_population_by_field_name = True
    #     json_encoders = {
    #         ObjectId: lambda x: str(x)           
    #     }

class UpdatePeople(BaseModel):
    survived: Optional[bool]
    passengerClass: Optional[int]
    name: Optional[str]
    sex: Optional[List[Gender]]
    age: Optional[int]
    siblingsOrSpousesAboard: Optional[int]
    parentsOrChildrenAboard: Optional[int]
    fare: Optional[int]


