def vector_fibonacci(x: int):
    numeros=[]
    i=0
    a=0
    b=1
    for i in range(x):
        c=a+b
        numeros.append(c)
        a=b
        b=c

    for i in range(x):
        print(numeros[i])


def edades_alumnos(x):
    edades=[]
    for i in range(x):
        edad=int(input('edad del alumno= '))
        edades.append(edad)

    for i in range(0,x):
        for j in range(0, x-i-1):
           if edades[j]>edades[j+1]:
            edades[j], edades[j+1]=edades[j+1], edades[j] 

    print('ascendente')

    for i in range(x):
        print(edades[i])

    print('descendente')

    for i in range(0,x):
        for j in range(0, x-i-1):
           if edades[j]<edades[j+1]:
            edades[j], edades[j+1]=edades[j+1], edades[j] 

    for i in range(x):
        print(edades[i])
    


def encuesta(x):
    encuestados=[]
    c=0
    j=0
    a=0
    m=0
    for i in range(x):
        name=input('ingrese su nombre y apellido ')
        age=int(input('ingrese su edad '))
        state=int(input('estado civil 1.casado 2.soltero '))
        if 14<=age<=26:
            j=j+1
        elif 27<=age<=59:
            a=a+1
        elif 60<=age:
            m=m+1
        if age>=18 and state==2:
                c=c+1
    
    print(f'el numero de mayores de edad solteros es de {c} \n encuestados entre 14 y 26= {j} \n encuestados entre 27 y 59= {a} \n encuestados de 60 o mas= {m}')

encuesta(5)