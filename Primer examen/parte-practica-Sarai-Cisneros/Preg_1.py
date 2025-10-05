'''
1. Usando los tipos de datos y sus conversiones realizar lo siguiente. (4 ptos) Reglas:
- Asignar en variables los datos de tu nombre, salario, edad y compañía para un usuario e identificar sus tipos de variables
- Edad tiene que ser tipo string, para usarla más adelante tiene que aplicarse una conversión de datos
- Identificar si la edad es mayor a 30, mostrar un mensaje ingresado “Usted tiene un bono de 10% en el mes de diciembre”
caso contrario mostrar “Usted tiene un bono del 5% en el mes diciembre”
- Mostrar el bono final que es: potencia de 2 del salario más el 5 o 10 % de su salario, según corresponda.
'''

print('\n*** RESULTADO PREGUNTA 01 ***\n')

nombre = "Sarai Cisneros Lovaton"
salario = 1000
edad = "38"
compañia = "Claro"

print ( "la variable nombre es tipo: ",type(nombre))
print ( "la variable salario es tipo: ",type(salario))
print ( "la variable edad es tipo: ",type(edad))
print ( "la variable compañia es tipo: ",type(compañia))

print('\n')
if int(edad)>30:
   print ("Usted tiene un bono de 10% en el mes de diciembre")
else:
   print("Usted tiene un bono del 5% en el mes diciembre")

if int(edad) > 30:
    print("Su bono final es",(salario ** 2) + (0.10 * salario) )
else:
    print("Su bono final es",(salario ** 2) + (0.05 * salario) )
