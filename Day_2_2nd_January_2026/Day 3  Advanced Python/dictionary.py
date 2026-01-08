# Create a dictionary where:
# Keys are numbers from 1 to 10
# Values are their cubes

dictionary = {}
# print(dict.keys())
# print(dict.values())
# print(dict.items())
for c in range(1,11):
    dictionary[c] = c**3
print(dictionary)



# Given a dictionary of items and prices:
# Create a new dictionary with only items costing more than 500

item = {
    "watter_bottle" : "20",
    "chips_packet" : "10",
    "chair" : "100",
    "book" : "40",
    "pendrive" : "600",
    "RAM" : "4000",
    "SSD" : "7000",
    "HDD" : "4000",
    "monitor" : "5000"
}
print(item)
filtered_item = {k:v for k,v in item.items() if int(v)>500}
print(filtered_item)