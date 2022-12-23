crime_delator = input()

if crime_delator != 'roubo' and crime_delator != 'tráfico' and crime_delator != 'homicídio':
    print("Crime inválido.")
else:
    if crime_delator == 'roubo' or crime_delator == 'tráfico':
        valor_crime_delator = int(input())

    crime_delatado = input()

    if crime_delatado != "roubo" and crime_delatado != 'tráfico' and crime_delatado != 'homicídio':
        print("Crime inválido.")
    else:
        if crime_delatado == 'roubo' or crime_delatado == 'tráfico':
            valor_crime_delatado = int(input())

    if crime_delator == 'roubo':
        if crime_delatado == 'homicídio':
            print("Delação concedida.")
        elif crime_delatado == 'roubo':
            if valor_crime_delatado > valor_crime_delator * 5:
                print("Delação concedida.")
            else:
                print("Delação rejeitada.")
        elif crime_delatado == 'tráfico':
            if valor_crime_delatado > valor_crime_delator * 3:
                print("Delação concedida.")
            else:
                print("Delação rejeitada.")

    elif crime_delator == 'tráfico':
        if crime_delatado == 'homicídio':
            print("Delação concedida.")
        elif crime_delatado == 'tráfico':
            if valor_crime_delatado > valor_crime_delator * 5:
                print("Delação concedida.")
            else:
                print("Delação rejeitada.")
    elif crime_delator == 'homicídio':
        if crime_delatado == 'homicídio':
            print("Delação concedida.")
        else:
            print("Delação rejeitada.")