a = 5
b = 2
k = 10


d = str(a/b) # string cabal

dot_spot = d.find(".")
whole = d[:dot_spot] # parte entera del cociente

decimals = d[dot_spot+1:] # los decimales

len_decimals = decimals[:k] # tomo los decimales desde el primero hasta el k decimal

print(f"{whole}.{len_decimals}") #imprimo en un string la parte entera, un punto y los k decimales