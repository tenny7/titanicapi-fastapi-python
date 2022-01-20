def personEntity(person) -> dict:
    return {
        "id": str(person["_id"]),
        "age": int(person["age"]),
        "fare": person["fare"],
        "name": person["name"],
        "passengerClass": person["passengerClass"],
        "sex": person["sex"],
        "survived": bool(person["survived"]),
        "parentsOrChildrenAboard":  person["parentsOrChildrenAboard"],
        "siblingsOrSpousesAboard": person["siblingsOrSpousesAboard"],
        "uuid": person["uuid"]
    }

def personsEntity(entity) -> list:
    return [personEntity(person) for person in entity]