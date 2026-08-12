import json
with open("model.json" , "r") as file :
    model_data = json.load(file)


print(model_data)

print(model_data["name"])
print(model_data["provider"])
print(model_data["size"])

model_data["type"] = "Local LLM"
with open("model.json" , "w") as file:
    json.dump(model_data, file, indent=4)


model_data["creation_time"] = "2024-06-10"
with open("model.json" , "w") as file :
    json.dump(model_data, file, indent=4)