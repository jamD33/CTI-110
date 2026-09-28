#Desarae James
#09/27/2026
#P2LAB2_JAMESDESARAE.py
#Using dictionaries 

cars = {"Camaro": 18.2, "Prius": 52.3, "Model S": 110, "Silverado": 26}
#Get keys from dictionary
car_keys = cars.keys()

print(*car_keys, sep = ", ")

#Get a car from user
car_name = input("Enter a car name: ")

#Get mpg for the given car
mpg = cars.get(car_name)

print(f"The {car_name} gets {mpg} miles per gallon.")

#Get miles from user
miles_driven = float(input("Enter the number of miles driven: "))

#Calculate gallons used
gallons_used = miles_driven/ mpg

#Display results
print(f"The {car_name} used {gallons_used:.2f} gallons of gas to drive {miles_driven} miles.")


