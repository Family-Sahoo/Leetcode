def nestedEvenSum(obj):
    result = 0
    for k, v in obj.items():
        if type(v) is dict:
            result += nestedEvenSum(v)
        elif type(v) is int:
            if v % 2 == 0:
                result += v
    return result


obj1 = {
 "outer": 2,
 "obj": {
    "inner": 2,
    "otherObj": {
        "superInner": 2,
         "notANumber": True,
        "alsoNotANumber": "yup"
        }
    }
}
 
obj2 = {
 "a": 2,
 "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
 "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
 "d": 1,
 "e": {"e": {"e": 2}, "ee": 'car'}
}
 
print(nestedEvenSum(obj1)) # 6
print(nestedEvenSum(obj2)) # 10


