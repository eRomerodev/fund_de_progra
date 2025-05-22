A,p,B = 5,9,5

dif_A_p = abs(A-p)
dif_B_p = abs(B-p)

if dif_A_p > dif_B_p:
    print("Elevador B")
elif dif_B_p > dif_A_p:
    print("Elevador A")
elif dif_B_p == dif_A_p:
    print("Elevador A")
