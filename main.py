import os
os.system("cls")

BICICLETERO_MENSUAL = 15000
CANDADO = 9000


try:   
    dia = int(input("Ingrese la cantidad de días que usó el bicicletero\n"))
    persona = input("¿Usted es estudiante? S:si N:no\n").lower()

    if dia > 0 or persona == 's' or persona == 'n':
    
        if dia >=20 and persona == 's':
            descuento_bicicletero = BICICLETERO_MENSUAL * 0.25
        elif dia >=20 and persona == 'n':
            descuento_bicicletero = BICICLETERO_MENSUAL * 0.15
        elif (dia >=10 and dia <20) and persona == 's':
            descuento_bicicletero = BICICLETERO_MENSUAL * 0.15
        elif (dia >=10 and dia <20) and persona == 'n':
            descuento_bicicletero = BICICLETERO_MENSUAL * 0.08
        else:
            descuento_bicicletero = 0
    
        valor_final_bicicletero = BICICLETERO_MENSUAL - descuento_bicicletero
    
        if persona == 's':
            descuento_candado = CANDADO * 0.10
            if dia >=15:
                descuento_candado_dia = CANDADO * 0.05
            else:
                descuento_candado_dia = CANDADO * 0
            
            suma_de_descuentos = descuento_candado + descuento_candado_dia
            
        else:
            descuento_candado = CANDADO * 0
            suma_de_descuentos = descuento_candado
        valor_final_candado = CANDADO - suma_de_descuentos

        print(f"El valor del bicicletero es:{valor_final_bicicletero}")
        print(f"El valor del candado es:{valor_final_candado}")
    
    else:
        print("Error: el dato ingresado es incorrecto")
        
except:
    print("Un dato ingresado no es válido. Intente nuevamente")
