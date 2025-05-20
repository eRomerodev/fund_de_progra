contraseña = "123holaerick"


largo = False
if len(contraseña) >= 8:
    largo = True


digito = False
for i in contraseña:
    if i.isdigit:
        digito = True

mayus = False
for i in contraseña:
    if i.isupper:
        mayus = True

if largo and digito and mayus == True:
    print("Contraseña segura")
else:
    print("Contraseña no segura")