temperatura=int(input())
tosse=(input())

if temperatura >=37 and tosse=="S":
    print ("Exames Especiais")

elif temperatura >=37 and tosse=="N":
    print ("Exames Basicos")

elif temperatura <37 and tosse=="N":
    print ("Liberado")
else:
    print("Erro")