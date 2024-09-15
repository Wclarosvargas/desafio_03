from validaciones import validadr_id_unico,validar_promedio
from estudiantes import crear, actualizar, mostrar_matriz, eliminar


#Este main o tambien conocido como archivo menu servira para el usuario de modo que ingrese los datos 

estudiante = [
    [101,"weimar","claros","weimarc@gmail.com","011 1223-8945","C1425ABG","10-11-2024",8.5],
    [105,"juana","pantilla","juanap@gmail.com","011 2424-2354","T3489TRE","12-01-2022",6.8],
    [102,"juana","pantilla","juanapantilla10@gmail.com","011 4567-9345","Y9845JUT","24-05-2024",6.8]
]


def conversion(matriz):
    '''
    convertira el primer caracter de nombre y apellido en mayuscula
    '''
    for i in range(len(matriz)):
        id,nombre,apellido,correo,telefono,codigo_postal,fecha,promedio = matriz[i]
        nombre_capitalizado = nombre.capitalize()
        apellido_capitalizado = apellido.capitalize()
        matriz[i] = [id,nombre_capitalizado,apellido_capitalizado,correo,telefono,codigo_postal,fecha,promedio]
    return matriz


def mostrar_menu():
    '''
    Muestra el menú de opciones del CRUD.
    '''
    print('Opciones dentro del programa:')
    print('(1) Crear')
    print('(2) Leer')
    print('(3) Actualizar')
    print('(4) Eliminar')
    print('(5) Salir del programa')
    print('-'*80)

def main():
    #Matríz estudiante, los primeros tres datos seran ingresados por defecto del programa
    estudiante = [
        [101,"weimar","claros","weimar@gmail.com","011 1223-8945","C1425ABG","10-11-2024",8.5],
        [105,"juana","pantilla","juanap@gmail.com","011 2424-2354","T3489TRE","12-01-2022",6.8],
        [102,"juana","pantilla","juanap@gmail.com","011 4567-9345","Y9845JUT","24-05-2024",6.8]
    ]

    '''
    Las funciones creadas son llamadas en está función main
    Los datos son ingresados por teclado
    1 = crear, 2=mostrar, 3=actualizar, 4= eliminar, y 5 = salir 
    '''
    #Las funciones creadas son llamadas en esta función main 
    #Los datos son ing

    flag = 0

    while flag  == 0:
        estudiante_capitalizado = conversion(estudiante)
        mostrar_menu()
        accion = int(input().strip())

        if accion == 1:
            crear(estudiante_capitalizado)
            estudiante_capitalizado = conversion(estudiante_capitalizado) #Hace la capitalización para nuevos datos
        elif accion == 2:
            mostrar_matriz(estudiante_capitalizado)
        elif accion == 3:
            actualizar(estudiante_capitalizado)
        elif accion == 4:
            eliminar(estudiante_capitalizado)
        elif accion == 5:
            print('Saliendo del programa')
            flag = 1
        else:
            print('Opción no válida, por favor ingrese nuevamente el dígito: ')        

main() #Hace el llamdo de la función main, donde se ejecuta todo el programa

