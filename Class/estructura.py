#PRE:Escriu un programa en Python3 que llegeixi de l’usuari una llista de tuples,
#on cada tupla representa un estudiant amb la següent informació: (Nom, Cognom, Edat, Nota1, Nota2, Nota3).

#Le pido al usuario cuantos alumnos quiere registar
#Pido toda la información sobre el alumno para después poder evaluar su nota
#Quiero comparar la nota del estudiante y dependiendo de lo que tiene puede tener diferente medias de nota 
nom= input("Donam el nom:")
congnom=input("Donal el teu cognom:")
edat=int(input("Donm la teva edat:"))
nota1=int(input("Donam la nota1:"))
nota2=int(input("Donam la nota2:"))
nota3=int(input("Dona la nota3:"))

nota_mitjana=nota1*0,3+nota2*0,4+nota3*0,3
print(nota_mitjana)
#Condicion 
if nota_mitjana>7:
    print("La teva mitjana es superior a 7")
#Clasificar els estudiants en dues llistes
elif nota_mitjana>8:
    print("Tens una nota superior a 8")
#Fer un print amb el titol o nom representatitu de la llistaa