data={
    'name':"saiprakash",
    'age':25,
    'place':"hyderabad"
}

print(data['name'])
print(data.keys())
print(data.values())
print(data.items())
print(25 in data.values())
print(data.get('name'))
print(data.get('kiran',"not found")) 
keys={"sai","prakash","reddy"}
values=[1,2,3]
dict1=dict(zip(keys,values))
print(dict1)
print(data.pop('place'))

del data['age']

print(data)