año = 39532

if año % 4 == 0 or año % 100 == 0 and año % 400 == 0:
    print("Bisiesto")
else:
    print("No bisiesto")