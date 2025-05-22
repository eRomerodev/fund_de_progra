
a = "999"
b = "1"
a = list(a)
b = list(b)

if len(a) > len(b):  
    while len(a) > len(b):
        b.insert(0,"0")

if len(b) > len(a):
    while len(b) > len(a):
        a.insert(0,"0")

digitos = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

sum_final = []

def str_a_int(string):
    for i in range(10):
        if string == digitos[i]:
            return i
        
def strsote_a_numerote(cadena):
    numerote = []
    for i in cadena:
        numerote.append(str_a_int(i))
    return numerote

a_int = strsote_a_numerote(a)
b_int = strsote_a_numerote(b)

lleva = 0

for i in range(len(a)-1, -1, -1):
    sumita = a_int[i] + b_int[i] + lleva
    if sumita >= 10:
        lleva = 1
        sumita -= 10
    else:
        lleva = 0
    sum_final.insert(0, sumita)
if lleva > 0:
    sum_final.insert(0, lleva)

sum_final_str = ""
for numero in sum_final:
    sum_final_str += str(numero)

print(sum_final_str)



