#extract keys

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}

keys = ["name", "salary"]

output = {key: sample_dict[key] for key in keys}

print(output)