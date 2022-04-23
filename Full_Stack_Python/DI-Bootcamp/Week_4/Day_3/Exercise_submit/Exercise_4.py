users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"] 
indices = list(range(len(users)))  # [0,1,2,3,4]

disney_users_A = dict(zip(users, indices))
print(disney_users_A)

disney_users_B = dict(zip(indices, users))
print(disney_users_B)

disney_users_C = dict(zip(sorted(users), indices))
print(disney_users_C)

disney_users_D = {key: value for (key,value) in disney_users_A.items() if "i" in key}
print(disney_users_D)

disney_users_E = {key: value for (key,value) in disney_users_A.items() if key.startswith("M") or key.startswith("P")}
print(disney_users_E)