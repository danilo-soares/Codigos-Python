num=int(input("Fatorial do -> "))
res=1

for i in range(1,num+1):
    res *= i
    
print("{}! -> {}" .format(num,res))
