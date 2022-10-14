person = {"name":"Kohli","gender":"Male","Age":38,"address":"Haryana"}
key=input("what info do you want?").lower()
result=person.get(key,"info invalid")
print(result)
