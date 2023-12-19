#PRE:Escriu un programa en Python3 que llegeixi de l’usuari una llista de tuples,
#on cada tupla representa un estudiant amb la següent informació: (Nom, Cognom, Edat, Nota1, Nota2, Nota3).

#Le pido al usuario cuantos alumnos quiere registar
#Pido toda la información sobre el alumno para después poder evaluar su nota
#Quiero comparar la nota del estudiante y dependiendo de lo que tiene puede tener diferente medias de nota 
nom= input("Donam el nom:")
congnom=input("Donal el teu cognom:")
edat=int(input("Donm la teva edat:"))
nota1=int(input("Donam la nota3:"))
nota2=int(input("Donam la nota2:"))
nota3=int(input("Dona la nota3:"))

nota_final= (nota1+0,30)*(nota2+0,40)*(nota3+0,30) 
