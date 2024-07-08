usuarios = {
    'leo': '1234345',
    'carlos': '012861',
    'juan': '911212'
}

def verificar_credenciales(usuario, contraseña):

     # Verifica si el nombre de usuario y la contraseña son correctos.
    return usuarios.get(usuario) == contraseña
        

def registrar_usuario(usuario, contraseña):
    """
    Registra un nuevo usuario en el sistema.
    """
    if usuario in usuarios:
        return False
    usuarios[usuario] = contraseña
    return True

def mostrar_mensaje(mensaje):
    """
    Muestra un mensaje al usuario.
    
    :param mensaje: El mensaje a mostrar
    """
    print(mensaje)

def inicio_de_sesion():
    """
    Solicita al usuario que inicie sesión o se registre y verifica las credenciales.
    """
    while True:
        opcion = input("¿Desea iniciar sesión o registrarse? (iniciar/registrar): ").strip().lower()

        if opcion == 'iniciar':
            usuario = input("Nombre de usuario: ")
            contraseña = input("Contraseña: ")
            
            if verificar_credenciales(usuario, contraseña):
                mostrar_mensaje("Inicio de sesión exitoso")
                break
            else:
                mostrar_mensaje("Nombre de usuario o contraseña incorrectos")
        
        elif opcion == 'registrar':
            usuario = input("Elija un nombre de usuario: ")
            contraseña = input("Elija una contraseña: ")
            
            if registrar_usuario(usuario, contraseña):
                mostrar_mensaje("Registro exitoso, ahora puede iniciar sesión")
            else:
                mostrar_mensaje("El nombre de usuario ya existe, elija otro")
        
        else:
            mostrar_mensaje("Opción no válida. Por favor, elija 'iniciar' o 'registrar'.")

# Llamar a la función de inicio de sesión
inicio_de_sesion()
