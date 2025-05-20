nombre_completo = str(input("Ingrese su nombre completo: ")).lower()

nombre_separado = nombre_completo.split()

primer_nombre = str(nombre_separado[0])
primer_apellido = str(nombre_separado[2])

print(f"El correo que se debe asignar al usuario ingresado es: {primer_nombre}.{primer_apellido}@keyinstitute.edu.sv")