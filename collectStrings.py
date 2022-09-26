def collectStrings(obj):
    obj_arr = []
    for key, val in obj.items():
        if type(val) is dict:
            obj_arr.extend(collectStrings(val))
        else:
            obj_arr.append(val)

    return obj_arr        

    

obj = {
 "stuff": 'foo',
 "data": {
     "val": {
        "thing": {
            "info": 'bar',
             "moreInfo": {
                "evenMoreInfo": {
                "weMadeIt": 'baz'
                }
            }
        }
    }
    }
}
 
print(collectStrings(obj)) # ['foo', 'bar', 'baz']