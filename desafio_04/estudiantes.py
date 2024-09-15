from validaciones import validadr_id_unico,validar_promedio, validar_correo, validar_telefono, validar_codigo_postal, validar_fecha

def crear(matriz):
    '''
    Agrega un nuevo estudiante a la matríz de estudiantes.
    Solicita al usuario el ID, nombre, apellido y promedio del estudiante,
    valida los datos y los añade a la matríz si son correctos
    '''

    id_valido = 0
    while id_valido ==0:
        print("Ingrese el ID del estudiante:")
        id = int(input())
        if validadr_id_unico(matriz,id):
            id_valido = 1
        else:
            print("El ID ya existe, Por favor, ingrese un ID diferente.")
    
    print("Ingrese el nombre del estudiante")
    nombre = input()
    print("Ingrese el apellido del estudiante:")
    apellido = input()

    #correo
    correo_valido = 0
    while correo_valido == 0:
        print("Ingrese el correo electrónico del estudiante:")
        correo = input()
        if validar_correo(correo):
            correo_valido = 1
        else:
            print("El correo electrónico ingresado no es válido.")

    #telefono
    telefono_valido = 0
    while telefono_valido == 0:
        print("Ingrese el número de telefono del estudiante:")
        telefono = input().strip()
        if validar_telefono(telefono):
            telefono_valido = 1
        else:
            print("El telefono ingresado no es válido.")
    
    #Código_postal
    codigop_valido = 0
    while codigop_valido == 0:
        print("Ingrese el código postal del estudiante:")
        codigo = input().strip()
        if validar_codigo_postal(codigo):
            codigop_valido = 1
        else:
            print("El código postal ingresado no es válido. Por favor ingrese nuevamente con el formato (A1245AAA)")

    #Fecha
    fecha_valida = 0
    while fecha_valida == 0:
        print("Ingrese la fecha ")
        fecha = input().strip()
        if validar_fecha(fecha):
            fecha_valida = 1
        else:
            print("La fecha ingresada no es válida. Por favor ingrese nuevamente con el formato(DD-MM-YYYY)")

    #Promedio
    promedio_valido = 0
    while promedio_valido == 0:
        print("Ingrese el promedio del estudiante: ")
        promedio = float(input())
        if validar_promedio(promedio):
            promedio_valido = 1
        else:
            print("El promedio debe estar entre 1 y 10. Por favor, ingrese un promedio válido")

    nombre_capitalizado = nombre.capitalize()
    apellido_capitalizado = apellido.capitalize()

    # Crear una nueva entrada
    new_student = [id, nombre_capitalizado, apellido_capitalizado,correo,telefono, codigo,fecha, promedio]
    print("Estudiante agregado con éxito.")
    matriz.append(new_student)



#Funciones
def mostrar_matriz(matriz):
    '''
    Muestra la matríz de estudiantes en formato tabular, ordenada por promedio y ID.
    '''
    estudiantes = [[id,nombre[:10],apellido[:12],correo[:30],telefono[:18],codigo_postal[:18],fecha[:14],promedio] for id,nombre,apellido,correo,telefono,codigo_postal,fecha,promedio in matriz]

    #Ordena la lista de estudiantes por promedio descendente y luego por ID de forma ascendente
    estudiante_ordenados = sorted(estudiantes, key=lambda x: (-x[7],x[0]))
    
    #se imprimira los encabezados
    print(f"| {'ID':<5} | {'Nombre':<10} | {'Apellido':<12} | {'Correo':<20} | {'telefono':<14} | {'Codigo_postal':<18} | {'fecha':<14} | {'Promedio':>10} |")
    print("-"*120) #Línea de separación de los encabezados 

    #Impresión de filas de datos
    for estudiante in estudiante_ordenados:
        print(f"| {estudiante[0]:<5} | {estudiante[1]:<10} | {estudiante[2]:<10} | {estudiante[3]:<20} | {estudiante[4]:<14} | {estudiante[5]:<18} | {estudiante[6]:<18} | {estudiante[7]:>10.2f} |")


def actualizar(matriz):
    '''
    Actualiza los datos del estudiante existente en la matriz.
    Solicita al usuario el ID del estudiante, busca el estudiante por su ID,
    y actualiza su nombre, apellido y promedio si el estudiante existe.
    '''
    print("Ingrese el ID del estudiante que desea actualizar:")
    id = int(input())

    #Busca el estudiante por su ID
    for i in range(len(matriz)):
        if matriz[i][0]==id :
            print("Estudiante encontrado")

            #Nombre       
            print("Ingrese el nuevo nombre del estudiante:")
            nombre = input()

            #Apellido
            print("Ingrese el nuevo apellido del estudiante:")
            apellido = input()

            #Solicita y valida el nuevo correo
            correo_valido = 0
            while correo_valido == 0:
                print("Ingrese el nuevo correo electrónico del estudiante:")
                correo = input()
                if validar_correo(correo):
                    correo_valido = 1
                else:
                    print("El correo electrónico ingresado no es válido.")

            #Solicita y valida el nuevo teléfono
            telefo_valido = 0
            while telefo_valido == 0:
                print("Ingrese el nuevo número de telefono del estudiante:")
                telefono = input().strip()
                if validar_telefono(telefono):
                    telefo_valido = 1
                else:
                    print("El número de teléfono ingresado no es válido.")

            #Solicita y valida el nuevo código postal
            codigop_valido = 0
            while codigop_valido == 0:
                print("Ingrese el nuevo código postal del estudiante:")
                codigo_postal = input().strip()
                if validar_codigo_postal(codigo_postal):
                    codigop_valido = 1
                else:
                    print("El código postal ingresado no es válido. Por favor ingrese nuevamente con el formato(A1234AAA)")

            #Solicita y valida la nueva fecha
            fecha_valida = 0
            while fecha_valida == 0:
                print("Ingrese la nueva fecha (DD-MM-YYYY):")
                fecha = input().strip()
                if validar_fecha(fecha):
                    fecha_valida = 1
                else:
                    print("La fecha ingresada no es válida. Por favor ingrese nuevamente con el formato (DD-MM-YYYY)")



            #Promedio
            flag=0
            while flag==0: #Verificamos que el promedio este entre 1 y 10
                flag=1
                print("Ingrese el nuevo promedio del estudiante: ")
                promedio = float(input())
                if 1>promedio or promedio>10:
                    flag=0
                    print("El promedio debe estar entre 1 y 10") 
            #Capitalizar los nombre y apellidos de los nuevos datos ingresados
            nombre_capitalizado = nombre.capitalize()
            apellido_capitalizado = apellido.capitalize()

            #Actualización de los datos
            matriz[i]=[id,nombre_capitalizado,apellido_capitalizado,correo,telefono,codigo_postal,fecha,promedio]
            print("Los datos fueron actualizados")
            return matriz
    print("Estudiante no encontrado.")
    return matriz


def eliminar(matriz):
    '''
    elimina al estudiante de la matriz por su ID.
    Solicita al usuario el ID del estudiante, busca al estudiante por su ID,
    y lo elimina si el estudiante existe. 
    '''
    flag = 0 #Se asume que el estudiante no ha sido encontrado
    while flag == 0:
        print("Ingrese el ID del estudiante que desea eliminar:")
        id = int(input())

        #usa el bucle while para buscar el estudiante
        i=0
        while i < len(matriz):
            if matriz[i][0] == id:
                matriz.pop(i) #La función pop eliminar los datos de la matriz que se encuentra en el ID ingresado
                print("Estudiante eliminado con éxito")
                flag = 1 #Establece el flag a 1 indicando con el estudiante ha sido encontrado y eliminado
            else:
                i+=1 #Continua iterando si el estudiante no es encontrado
        
        #Si el estudiante no es encontrado
        if flag == 0:
            print("Estudiante no fue encontrado. Intente nuevamente.") 
    
    return matriz