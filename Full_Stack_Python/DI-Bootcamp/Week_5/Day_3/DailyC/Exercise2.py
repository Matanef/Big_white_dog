import json
sampleJson = { 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}

print(sampleJson['company']["employee"]["payable"]["salary"])
print(sampleJson["company"]["employee"]["payable"].get("salary"))

sampleJson["company"]["employee"] = {"BirthDate"}
print(sampleJson)

jason_file = "Exercise2Json.json"

with open("Exercise2Json.json", 'w') as file_obj:
    json.dump(sampleJson, file_obj)