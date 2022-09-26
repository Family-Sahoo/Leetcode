def stringifyNumbers(obj):
    new_obj = {}
    for key, val in obj.items():
        if type(val) is dict:
            new_obj[key] = stringifyNumbers(val)
        else:
            if type(val) is int:
                new_obj[key] = str(val)
            else:
                new_obj[key] = val    

    return new_obj  


obj = {
 "num": 1,
 "test": [],
 "data": {
 "val": 4,
 "info": {
    "isRight": True,
    "random": 66
    }
 }
}
 
print(stringifyNumbers(obj))