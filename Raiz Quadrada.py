import math
a= float(input("Digite o valor de a = "))
b= float(input("Digite o valor de b = "))
c= float(input("Digite o valor de c = "))
 
x=(b**2)-(4*a*c)
 
if a == 0 :
        print ("Impossível calcular")

elif( x < 0):
	print ("Impossível calcular")        

else:
        x=math.sqrt(x)
        x1=(-b+x)/(2*a)
        x2=(-b-x)/(2*a)
        print("R1 = {:.0f}" .format(x1))
        print("R2 = {:.0f}" .format(x2))
