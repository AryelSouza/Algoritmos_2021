cor=input()
bor=input()
preco=int(input())

if preco >45:
       print("rejeitada")
elif cor=="preta" and bor=="bordada" and preco <=35:
    print("aceita")
elif cor=="azul" and bor=="bordada" and preco <=35:
    print("aceita")
elif cor=="marrom" and bor=="bordada" and preco <=35:
    print("aceita")
elif cor=="verde" and bor=="bordada" and preco <=35:
    print("aceita")
elif cor=="preta" and bor=="serigrafia" and preco <=35:
    print("rejeitada")
elif cor=="azul" and bor=="serigrafia" and preco <=35:
    print("rejeitada")
elif cor=="marrom" and bor=="serigrafia" and preco <=35:
    print("rejeitada")
elif cor=="verde" and bor=="serigrafia" and preco <=35:
    print("rejeitada")
elif cor=="branca" and bor=="serigrafia" or bor=="bordada" and preco <=35:
    print("aceita")
elif cor=="amarela" and bor=="serigrafia" or bor=="bordada" and preco <=35:
    print("aceita")
elif cor=="rosa" and bor=="serigrafia" or bor=="bordada" and preco <=35:
    print("aceita")
elif cor=="preta" and bor=="bordada" and preco >35:
    print("analisar em ultimo caso")
elif cor=="marrom" and bor=="bordada" and preco >35:
    print("analisar em ultimo caso")
elif cor=="azul" and bor=="bordada" and preco >35:
    print("analisar em ultimo caso")
elif cor=="verde" and bor=="bordada" and preco >35:
    print("analisar em ultimo caso")

