inicio= int(input("Início -> "))
razao= float(input("Razão -> "))
visualizar= int(input("Quantos elementos quer visualizar -> "))

for i in range (visualizar):
    res=inicio
    print(res)
    inicio *= razao
