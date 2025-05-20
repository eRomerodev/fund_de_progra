cuenta = float(input("¿Cuánto costó tu comida en $? "))

propina = float(input("¿Qué porcentaje de propina quieres dar? "))
fraccion = propina/100

total = cuenta + fraccion*cuenta

print(f"En total debes pagar {total} $ con una propina de {fraccion*cuenta} $")
