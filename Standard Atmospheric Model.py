#This model simulates the pressure and temperature between different altitudes
import math
#Troposphere Layer (0 - 11000m)
height = (float(input("Enter the height in numbers: ")))
if height <= 11000:
    # Temperature decreases linearly
    T = 288.15 - 0.0065 * height
    print(T , "Kelvin")   #Standardized unit
    #Finding pressure using Power Law Relation
    P = 101325 * (T/288.15) ** (9.81/(287 * 0.0065))
    print(f"{P:.1f} Pa")  #Pascal

# Lower Stratosphere (11000 - 20000m)
elif height <= 20000:
    #Temperature Remains Constant
    T = 216.65
    print(T, "Kelvin")
    #Pressure using exponential decay
    P = 22632 * math.exp(-9.81 * (height - 11000) / (287*T))
    print(f"{P:.1f} Pa")

#Out of the range
else:
    print("Height is out of range for this model.")

