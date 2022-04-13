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

f = "json_file.json"

with open('json_file.json', 'w') as f:
    json.dump(sampleJson, f)


jsonified_Dic = f'{{sampleJson}}'
print(jsonified_Dic)