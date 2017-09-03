inicio= int(input("Início -> "))
razao= int(input("Razão -> "))
visualizar= int(input("Quantos elementos quer visualizar -> "))
print("P.G -> ", end="")
for i in range (visualizar):
    res=inicio
    print(res, end=" ")
    inicio *= razao
