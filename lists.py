from lib2to3.pgen2 import driver


friends = ["Carlos", "Roberto", "Lucas" ,"Gabriel", "Kevin"]
numList = [1, 2, 3]

print(friends[0])
print(friends[0:3])

# friends.extend(numList)
# print(friends)

friends[1] = "Juvenal"
print(friends[1])

friends.insert(1, "Bruno")
print(friends)

friends.remove("Carlos")
print(friends)

friends.pop()
print(friends)

print(friends.index("Lucas"))

print(friends.count("Gabriel"))

friends.sort()
print(friends)

numList.reverse()
print(numList)

friends2 = friends.copy()
print(friends2)