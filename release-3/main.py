
#1
def fullName(obj):
    return obj["surname"] + " " + obj["name"]

print(fullName({
    "name": "Petya",
     "surname": "Proger",
      "age": 14
    }))



def checkForPropertyAndValue(obj, key):
    if key in obj and obj[key] > 0:
        return True
    else:
        return False

print(checkForPropertyAndValue({"key: 5"}, "key"))