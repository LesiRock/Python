import random
import time
nombre = ""
numero_secreto = random.randint (1,100)
numero_ingresado = 0
numeros_ingresados = []
oportunidades = 5

print(f'*****\nJUEGA ADIVINA EL NUMERO\n*****')

time.sleep(5)

nombre=input("Ingresa tu nombre: \n")
numero_ingresado=int(input("Ingresa el numero que crees que esta almacenado: "))
numeros_ingresados.append(numero_ingresado)
print(f'Haz ingresado los numeros {numeros_ingresados}')

while numero_ingresado != numero_secreto and oportunidades > 1:
    oportinudades = oportunidades -1 

    numero_ingresado=int(input("Ingresa el numero que crees que esta almacenado: "))
    numeros_ingresados.append(numero_ingresado)
    if numero_ingresado > numero_secreto:
        print(f'El numero ingresado es mayor que el secreto')
        numero_ingresado=int(input("Ingresa el numero que crees que esta almacenado: "))
        numeros_ingresados.append(numero_ingresado)
        print(f'Haz ingresado los numeros {numeros_ingresados}')
    else:
        print(f'El numero ingresado es menor que el secreto')
        numero_ingresado=int(input("Ingresa el numero que crees que esta almacenado: "))
        numeros_ingresados.append(numero_ingresado)
        print(f'Haz ingresado los numeros {numeros_ingresados}')

if numero_secreto == numero_ingresado:
    print(f'le atinast y te sobraron {oportunidades} oportunidades')

else:
    print(f'Se terminaron tus oportunidades el numero era {numero_secreto} y tu ingresaste {numero_ingresado}')




# meter un buble para no tener que pedir numeros, tiene 5 oportunidades mientras no le atine y decirle que numero has ingresado y en cada oportunidad es mayor o menos que el numero secreto