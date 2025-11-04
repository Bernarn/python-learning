# def square(number):
#     return number*number
# print(square(300))



def trip_cost(distance, fuel_efficiency, fuel_price=180):
    # liters of fuel needed
    Fuelneeded=distance/fuel_efficiency
    #total coast for the trip
    TripCost= Fuelneeded*fuel_price
    return TripCost
RunningTotalTripsCost=0
numberoftrips=int(input("Please enter the total number of trips"))
for i in range(1, numberoftrips+1):
      distance=float(input(f"Enter the distance of the trip{i}: "))
      fuel_efficiency=float(input(f"Please enter your car's fuel efficiency in km per liters{i} : "))
      fuel_price= input(f"Please enter the current  fuel price {i}: ")
      if fuel_price =="":
          fuel_price=180
      else:
         fuel_price=float(fuel_price)
      print("Your total cost for the trip is ", trip_cost(distance, fuel_efficiency, fuel_price))
      RunningTotalTripsCost +=trip_cost(distance,fuel_efficiency, fuel_price)
      print("Your running total is " , RunningTotalTripsCost)

