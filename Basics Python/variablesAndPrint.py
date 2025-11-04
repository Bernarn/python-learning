#program to calculate
distance=float(input("Enter the distance of the trip"))
FuelEfficiency=float(input("Enter your car's fuel efficiency (km per liter)"))
fuelPrice=float(input("Enter the current fuel price"))

# liters of fuel needed
Fuelneeded=distance/FuelEfficiency
#total coast for the trip
TripCost= Fuelneeded*fuelPrice

# print result

print(f"The total amount of fuel needed {Fuelneeded:.2f}")
print(f"Hi , the total cost for your trip is {TripCost}")


