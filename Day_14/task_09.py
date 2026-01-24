from  itertools import groupby
data = [
    {"name": "Apple", "category": "1"},
    {"name": "Carrot", "category": "2"},
    {"name": "Banana", "category": "1"},
    {"name": "Broccoli", "category": "2"},
    {"name": "Strawberry", "category": "1"},
]
data.sort(key=lambda x: x["category"])
grouped_data = {
    key: list(group) for key, group in groupby(data, key=lambda x: x["category"])
}
print(grouped_data)