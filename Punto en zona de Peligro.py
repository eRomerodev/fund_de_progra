x,y =-4,-3
if (x > 0 and y > 0) and (x*x + y*y <=25):
    print("Peligro")
elif (x > 0 and y > 0) and (x*x + y*y >25):
    print("Seguro")
elif (x < 0 or y < 0) and (x*x + y*y <=25):
    print("Peligro")
else:
    print("Seguro")