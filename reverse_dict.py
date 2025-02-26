x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
d={}
k=sorted(x.items(),key = lambda item: item[1],reverse=True)
print(type(k))
print(k)
dd=[{"name":"h","age":8},{"name":"v","age":10}]
def getP(data):
    print(data)
    return data["name"]
print(sorted(dd,key=getP ))
print(sorted(dd,key=lambda data:data["age"],reverse=True))
