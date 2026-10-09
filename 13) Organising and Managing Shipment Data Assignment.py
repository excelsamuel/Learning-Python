# 09/10/2026
# SETS and DICTIONAIRES Assignment


# Question 1:
shipments = {
    "SHP103": "Pending",
    "SHP104": "In Transit",
    "SHP105": "Delivered",
    "SHP106": "Delivered"
}

# We have our dictionary of shipments and their statuses already defined above.
# Let's Retrieve the status of a specific shipment
shipment_status = shipments.get("SHP103")

print("The Status of SHP103: ", shipment_status)



# Question 2:
shipments = {
    "SHP101": "Delivered",
    "SHP102": "In Transit",
    "SHP103": "Pending",
    "SHP104": "Delivered"
}

# Update one of our shipment statuses
shipments["SHP102"] = "Delivered"
shipments["SHP103"] = "In Transit"

# Adding a brand new shipment details
shipments["SHP105"] = "In Transit"
shipments["SHP106"] = "Pending"

# Removing our completed shipments
shipments.pop("SHP101")
shipments.pop("SHP102")
shipments.pop("SHP104")

# Displaying all remaining shipment IDs after we have popped the completed ones
print("\nShipment IDs That Are Not Completed:")
for shipment_id in shipments.keys():
    print(shipment_id)

# Displaying all the current statuses using iteration over the values of the dictionary
print("\nShipment statuses:")
for status in shipments.values():
    print(status)

# Also let's iterate over IDs and statuses together
print("\nShipment summary:")
for shipment_id, status in shipments.items():
    print(f" The shipment {shipment_id}'s status is still {status}")



# Question 3:
# Let's work with sets to manage shipment locations
print("\nWorking with sets to manage shipment locations:")
north = {"New York", "Dallas", "Miami"}
south = {"Miami", "Atlanta", "Dallas"}

# Union: This will help us find all unique cities
all_cities = north.union(south)


# Intersection: cities present in both regions
shared_cities = north.intersection(south)

# Difference: cities served only by the North
north_only = north.difference(south)

# Difference: cities served only by the South
south_only = south.difference(north)

print("All cities present:", all_cities)
print("Cities served by both regions:", shared_cities)
print("Cities served only by the North:", north_only)
print("Cities served only by the South:", south_only)

# Alternatively, we can use the operators for set operations
# Union: '|', Intersection: '&', Difference: '-', Symmetric Difference: '^'
print("\nUsing operators for set operations:")
print("All cities present:", north | south)
print("Cities served by both regions:", north & south)
print("Cities served only by the North:", north - south)
print("Cities served only by the South:", south - north)
print("Cities served by either region but not both:", north ^ south)