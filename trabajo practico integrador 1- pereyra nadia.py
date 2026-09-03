#TRABAJO PRÁCTICO N1

#=====================================
# EJERCICIO 1 "CAJA DE KIOSCO"
#=====================================
print(" EJERCICIO 1 - CAJA DE KIOSCO ")


nombre_cliente = input("Ingrese el nombre del cliente: ") # primer requisito

while nombre_cliente == "" or not nombre_cliente.isalpha(): # Inicio del bucle si este no esta escrito con letras.
    print("Error, el nombre debe contener solo letras y no debe estar vacío")
    nombre_cliente = input("Ingrese el nombre del cliente: ")

productos_a_comprar = input("Ingrese la cantidad de productos a comprar: ") # segundo requisito

while not productos_a_comprar.isdigit () or int(productos_a_comprar) <= 0: # Se inicia el bucle si este no esta escrito con dígitos o es igual o menor que 0.
    print("Error, el valor de productos a comprar debe estar escrito númericamente y ser mayor a 0")
    productos_a_comprar = input("Ingrese la cantidad de productos a comprar: ")
        
productos_a_comprar= int (productos_a_comprar) 

# Variables de acumulación
total_con_descuento = 0
total_sin_descuento = 0

# PEDIR PRECIO
for i in range (productos_a_comprar): # Inicia el bucle contador para la cantidad indicada de productos a comprar
    precio = input ("Ingrese el precio del producto: ")
        
    while not precio.isdigit(): # el bucle se inicia si el producto no esta ingresado con dígitos
        print("Error, el precio debe ser un número entero positivo")
        precio = input ("Ingrese el precio del producto: ")

    precio = int(precio) # el precio debe ser un entero

 # CONSULTAR SI EL PRODUCTO TIENE DESCUENTO
    descuento = input("El producto tiene descuento? : ( Resdonde (S) si la respuesta es si, y (N si la respuesta es no)").lower()

    while descuento != "s" and descuento != "n": # Inicia el bucle cuando la respuesta indicada no es la correcta
        print("Error. La respuesta solicitada debe responderse con S o N.")
        descuento = input("El producto tiene descuento? : ( Resdonde (S/N) ").lower()

    # LOS PRECIOS QUE NO POSEEN DESCUENTO:
    if descuento == "n":
        total_sin_descuento += precio # Va acumulando la cantidad de valores sin descuento

    
 # LOS PRECIOS QUE SI POSEEN DESCUENTO:

    if descuento == "s": # si la respuesta es positiva se lo multiplica por 0.90 ( aplicado ya el 10 % de descuento en el total del producto)
        precio_con_descuento = precio * 0.90
    else:
        precio_con_descuento = precio

    total_con_descuento += precio_con_descuento # Va acumulando la cantidad de valores con descuento

# RESULTADOS ESPERADOS
ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / productos_a_comprar

print ("Total sin descuento: ", total_sin_descuento)
print("Total con descuento: ", total_con_descuento)
print("Ahorro: ", ahorro)
print(f"Promedio por producto: {promedio:.2f}")

print("-----------------------------------------")

#==============================================
# EJERCICIO 2 "ACCESO AL CAMPUS Y MENÚ SEGURO"
# ==============================================
print("EJERCICIO 2- ACCESO AL CAMPUS Y MENÚ SEGURO")

# Variables
umbral_de_fallas = 3
usuario_correcto = "alumno"
clave_correcta = "python123"
intentos = 0
acceso = False

# BUCLES

while intentos < umbral_de_fallas: # Inicia el ciclo contando la cantidad de intentos
    print (f" Intento {intentos + 1}/3") # requisito n2

    usuario = input("Usuario: ") # solicita usuario
    clave = input("Clave: ") # solicita clave

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concebido")
        acceso = True
        break
    else:
        print("Error. Usuario y/o clave inválido")
        intentos += 1

if not acceso:
    print("Cuenta bloqueada") # requisito n3

if acceso:
    acceso = ""
    
   
    while acceso != "4":
        print ("Validación del menú")
        print ("Opciones 1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")

        acceso = input(" Ingrese la opción elegida: (1 a 4): ")

        while not acceso.isdigit() or int(acceso) < 1 or int(acceso) > 4:
            print("Opción fuera de rango")
            acceso = input("Ingrese la opción elegida: (1 a 4)")

        # OPCIONES DE ACCESO 
        if acceso == "1": # Estado de inscripción
             print("Estado de inscripción: Inscripto")
        elif acceso == "2": # Cambio de clave
            cambiar_clave = input ("Ingrese su nueva clave: ")
            if len (cambiar_clave) < 6 :
                print("Error, la clave debe tener como mínimo 6 caracteres")
            else:
                confirmacion_de_clave = input("Confirme la nueva clave: ")
                if cambiar_clave == confirmacion_de_clave:
                    clave_correcta = cambiar_clave
                    print(" La clave ha sido cambiada correctamente")
                else:
                    print("Error, las claves ingresadas no coinciden")

        elif acceso == "3": # Mensaje motivacional
                print("Te felicito, has realizado los pasos correctamente, seguí así. Vas por buen camino")
                break

        elif acceso == "4": # Salir del programa
                print ("Saliendo del programa")

#================================================
# EJERCICIO 3 (ALTA) "AGENDA DE TURNOS CON NOMBRE"
#=================================================
print(" AGENDA DE TURNOS CON NOMBRE")

# Turnos disponibles por día
LUNES = 4
MARTES = 3

# Turnos del día Lunes
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

# Turnos día Martes
martes1 = ""
martes2 = ""
martes3 = ""

#----------------------------------------------
# NOMBRE DEL OPERADOR
#----------------------------------------------

nombre_operador = input (" Ingrese el nombre del operador: ")

while not nombre_operador.replace("","").isalpha():
    print("Error. El nombre debe estar escrito solo por letras")
    nombre_operador = input (" Ingrese el nombre del operador: ")
print ()
print (" Bienvenido/a", nombre_operador)

#----------------------------------------
# OPCIONES DE MENÚ
#----------------------------------------
lunes = "1"
martes = "2"
acceso_al_sistema = ""

while acceso_al_sistema != 5:
    print ()
    print ("Opciones del menú")
    print ("1) Reservar turno")
    print (" 2) Cancelar turno")
    print ("3) Ver agenda del día")
    print ("4) Ver resumen general")

    acceso_al_sistema = input("Ingrese la opción elegida (del 1 al 5): ")

    while not acceso_al_sistema.isdigit() or acceso_al_sistema < "1" or acceso_al_sistema > "5":
        print("Opciones fuera de rango")
        acceso_al_sistema = input("Ingrese la opción elegida (1 a 5): ")

#--------------------------------------
# OPCIÓN 1. RESERVAR TURNO
#---------------------------------------
    if acceso_al_sistema == "1":
        print()
        print("Reservar turno")

        elegir_dia = input ("Ingrese (1) para turnos el día Lunes o (2) para turnos el día Martes")
        while elegir_dia != "1" or elegir_dia != "2":
            print("Opción incorrecta")
            elegir_dia = input ("Ingrese (1) para turnos el día Lunes o (2) para turnos el día Martes")

        nombre_ingresado = input("Ingrese su nombre para la reservación del turno: ")
        while not nombre_operador.isalpha():
            print("Error. El nombre ingresado es inválido (solo debe estar escrito por letras)")
            nombre_ingresado = input("Ingrese su nombre para la reservación del turno: ")

        # RESERVACIÓN DÍA LUNES
        if elegir_dia == lunes:
            if nombre_ingresado == lunes1 or nombre_ingresado == lunes2 or nombre_ingresado == lunes3 or nombre_ingresado == lunes4:
                print(" Ese nombre ya posee un turno reservado para el día Lunes")
            else:
                if lunes1 == "":
                    lunes1 = nombre_ingresado
                    print ("Su turno ha sido confirmado y reservado con éxito")
                elif lunes2 == "":
                    lunes2 = nombre_ingresado
                    print ("Su turno ha sido confirmado y reservado con éxito")
                elif lunes3 == "":
                    lunes3 = nombre_ingresado
                    print ("Su turno ha sido confirmado y reservado con éxito")
                elif lunes4 == "":
                    lunes4 = nombre_ingresado
                    print ("Su turno ha sido confirmado y reservado con éxito")
                else:
                    print ("No hay turnos disponibles para el día Lunes")

         # RESERVACIÓN DÍA MARTES

        elif elegir_dia == martes:
                    if nombre_ingresado == martes1 or nombre_ingresado == martes2 or nombre_ingresado == martes3:
                        print(" Ese nombre ya posee un turno reservado para el día Martes")
                    else:
                        if martes1 == "":
                            martes1 = nombre_ingresado
                            print ("Su turno ha sido confirmado y reservado con éxito")
                        elif martes2 == "":
                            martes2 = nombre_ingresado
                            print ("Su turno ha sido confirmado y reservado con éxito")
                        elif martes3 == "":
                            martes3 = nombre_ingresado
                            print ("Su turno ha sido confirmado y reservado con éxito")
                        else:
                            print("No hay turnos disponibles para el día Martes")

#--------------------------
# OPCIÓN 2: CANCELAR TURNO
# -------------------------  

    elif acceso_al_sistema == "2":
        print()
        print ("Cancelar turno")
        elegir_dia = input ("Ingrese (1) para turnos el día Lunes o (2) para turnos el día Martes")

        while elegir_dia != "1" and elegir_dia != "2":
                    print("Opción incorrecta")
                    elegir_dia = input ("Ingrese (1) para turnos el día Lunes o (2) para turnos el día Martes")
        
        nombre_ingresado = input("Ingrese su nombre para la cancelación del turno: ")
        while not nombre_operador.isalpha():
                print("Error. El nombre ingresado es inválido")
                nombre_ingresado = input("Ingrese su nombre para la cancelación del turno: ")
        
        # CANCELACIÓN DÍA LUNES
        if elegir_dia == lunes:
             
            if lunes1 == "":
                lunes1 = nombre_ingresado
                print ("Su turno ha sido canceladocon éxito")
            elif lunes2 == "":
                lunes2 = nombre_ingresado
                print ("Su turno ha sido cancelado con éxito")
            elif lunes3 == "":
                lunes3 = nombre_ingresado
                print ("Su turno ha sido cancelado con éxito")
            elif lunes4 == "":
                lunes4 = nombre_ingresado
                print ("Su turno ha sido confirmado y reservado con éxito")
            else:
                print ("No se encontró registrado ningún paciente con el nombre ingresado")
        
        # RESERVACIÓN DÍA MARTES
        
        elif elegir_dia == martes:

            if martes1 == "":
                martes1 = nombre_ingresado
                print ("Su turno ha sido cancelado con éxito")
            elif martes2 == "":
                martes2 = nombre_ingresado
                print ("Su turno ha sido cancelado con éxito")
            elif martes3 == "":
                martes3 = nombre_ingresado
                print ("Su turno ha sido cancelado con éxito")
            else:
                print("No se encontró registrado ningún paciente con el nombre ingresado")

    #---------------------------------------
    # OPCIÓN 3 : VER AGENDA
    #---------------------------------------

    elif acceso_al_sistema == "3":
         print()
         print("Ver agenda del día")
         elegir_dia = input ("Ingrese (1) para turnos el día Lunes o (2) para turnos el día Martes")
         
         while elegir_dia != "1" and elegir_dia != "2":
                print("Opción incorrecta")
                elegir_dia = input ("Ingrese (1) para turnos el día Lunes o (2) para turnos el día Martes")

        # DÍA LUNES
         if elegir_dia == lunes:
              print()
              print("AGENDA DEL DÍA LUNES")

              if lunes1 == "":
                print("Primer turno: Libre")
              else:
                print("turno 1 :", lunes1)
                
              if lunes2 == "":
                print("Segundo turno: Libre")
              else:
                 print("turno 2 :", lunes2)

              if lunes3 == "":
                    print("Tercer turno: Libre")
              else:
                    print("turno 3 :", lunes3)
            
              if lunes4 == "":
                print("Cuarto turno: Libre")
              else:
                print("turno 1 :", lunes1)

        # DÍA MARTES
         elif elegir_dia == martes:
                      print()
                      print("AGENDA DEL DÍA MARTES")
        
                      if martes1 == "":
                        print("Primer turno: Libre")
                      else:
                        print("turno 1 :", martes1)
                        
                      if martes2 == "":
                        print("Segundo turno: Libre")
                      else:
                         print("Turno 2: ", martes2)
        
                      if martes3 == "":
                            print("Tercer turno: Libre")
                      else:
                            print("turno 3 :", martes3)

#------------------------------
#  OPCIÓN 4: RESUMEN
# ------------------------------
    elif acceso_al_sistema == "4":
        ocupados_lunes = 0
        ocupados_martes = 0

        # CONTADOR DÍA LUNES
        if lunes1 != "":
            ocupados_lunes += 1
        if lunes2 != "":
            ocupados_lunes += 1
        if lunes3 != "":
            ocupados_lunes += 1
        if lunes4 != "":
            ocupados_lunes += 1

        # CONTADOR DÍA MARTES
        if martes1 != "":
                ocupados_martes += 1
        if martes2 != "":
                ocupados_martes += 1
        if martes3 != "":
                ocupados_martes += 1

        print()
        print("RESUMEN GENERAL")

        print("Lunes - ocupados: ", ocupados_lunes)
        print("Lunes - disponibles: ", 4 - ocupados_lunes)

        print("Martes - ocupados : ", ocupados_martes)
        print("Martes - disponibles: ", 3 - ocupados_martes)

        if ocupados_lunes > ocupados_martes:
             print("El lunes tiene más turnos ocupados")
        elif ocupados_martes > ocupados_lunes:
             print("El martes tiene más turnos ocupados")
        else:
             print("Hay empate entre los turnos del día lunes y martes")
#-------------------------------------
# OPCIÓN 5
#------------------------------------
print ()
print ("Sistema cerrado")
print("Hasta pronto", nombre_operador)
        


#=====================================
# EJERCICIO 4: ESCAPE ROOM
#====================================

# VARIABLES

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""

nombre = input ("Ingrese el nombre del agente: ")

while not nombre.isalpha():
     print(" Error. El nombre solo debe contener letras")
     nombre = input ("Ingrese el nombre del agente: ")

print()
print("Bienvenido/a: ", nombre)
print("Comienza el juego de Escape Room")
print ()

# Variable contadora
forzar_seguidas = 0

#Bucle mientras se cumplan las condiciones

print("-----------------------")
print("Estado actual")
print ("Energía: ", energia)
print("Tiempo: ", tiempo)
print("Cerraduras abiertas: ", cerraduras_abiertas)
print("Código parcial: ", codigo_parcial)
print("----------------------")

print("1. Forzar cerradura")
print("2. Hackear panel")
print("3. Descansar")

opcion = input("Elija una opción: ")

# Validar que sea un número
while not opcion.isdigit():
    print("Error. Debe ingresar un número.")
    opcion = input("Elija una opción: ")

    opcion = int(opcion)

    # Validar que la opción sea 1, 2 o 3
    while opcion < 1 or opcion > 3:
        print("Error. Opción incorrecta.")
        opcion = input("Elija una opción: ")

        while not opcion.isdigit():
            print("Error. Debe ingresar un número.")
            opcion = input("Elija una opción: ")
            opcion = int(opcion)


    # --------------------------------
    # OPCIÓN 1: FORZAR CERRADURA
    # --------------------------------

    if opcion == 1:

        forzar_seguidas = forzar_seguidas + 1

        energia = energia - 20
        tiempo = tiempo - 2

        print()
        print("Intentando forzar la cerradura...")

        # Regla anti-spam
        if forzar_seguidas == 3:

            print("¡La cerradura se trabó!")
            print("¡Se activa la alarma!")
            alarma = True

        else:

            # Si la energía es menor a 40
            if energia < 40:

                numero = input("Hay riesgo de alarma.")
                numero = input("Ingrese un número del 1 al 3: ")

                while not numero.isdigit():
                    print("Error. Debe ingresar un número.")
                    numero = input("Ingrese un número del 1 al 3: ")

                numero = int(numero)

                while numero < 1 or numero > 3:
                    print("Error. Ingrese un número entre 1 y 3.")
                    numero = input("Ingrese un número del 1 al 3: ")

                    while not numero.isdigit():
                        print("Error. Debe ingresar un número.")
                        numero = input("Ingrese un número del 1 al 3: ")

                    numero = int(numero)

                if numero == 3:
                    alarma = True
                    print("¡Elegiste el número 3!")
                    print("¡Se activa la alarma!")

            # Si no hay alarma, se abre la cerradura
            if alarma == False:

                cerraduras_abiertas = cerraduras_abiertas + 1

                print("¡Cerradura abierta!")
                print("Cerraduras abiertas:", cerraduras_abiertas)


    # --------------------------------
    # OPCIÓN 2: HACKEAR PANEL
    # --------------------------------

    elif opcion == 2:

        # Se corta la racha de forzar
        forzar_seguidas = 0

        energia = energia - 10
        tiempo = tiempo - 3

        print()
        print("Iniciando hackeo del panel...")

        # 4 pasos de hackeo
        for i in range(4):

            codigo_parcial = codigo_parcial + "A"

            print("Paso", i + 1, "- Código:", codigo_parcial)

        # Si el código tiene 8 caracteres
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:

            cerraduras_abiertas = cerraduras_abiertas + 1

            print("¡Hackeo exitoso!")
            print("¡Se abrió una cerradura automáticamente!")

        else:
            print("El código todavía no es suficiente.")


    # --------------------------------
    # OPCIÓN 3: DESCANSAR
    # --------------------------------

    elif opcion == 3:

        # Se corta la racha de forzar
        forzar_seguidas = 0

        energia = energia + 15

        # La energía máxima es 100
        if energia > 100:
            energia = 100

        tiempo = tiempo - 1

        # Si hay alarma, pierde 10 de energía extra
        if alarma == True:
            energia = energia - 10

        print()
        print("Descansaste.")
        print("Recuperaste 15 de energía.")


# --------------------------------
# FIN DEL JUEGO
# --------------------------------

print()
print("================================")
print("          FIN DEL JUEGO")
print("================================")

# Victoria
if cerraduras_abiertas == 3:

    print("¡VICTORIA!")
    print("Lograste abrir las 3 cerraduras.")

# Derrota por bloqueo de alarma
elif alarma == True and tiempo <= 3:

    print("¡DERROTA!")
    print("El sistema se bloqueó por la alarma.")

# Derrota por energía o tiempo
elif energia <= 0 or tiempo <= 0:

    print("¡DERROTA!")
    print("Te quedaste sin energía o sin tiempo.")

# Derrota por alarma
elif alarma == True:

    print("¡DERROTA!")
    print("La alarma se activó.")

print()
print("Energía final:", energia)
print("Tiempo final:", tiempo)
print("Cerraduras abiertas:", cerraduras_abiertas)
print("Código final:", codigo_parcial)

#===============================================
# EJERCICIO 5: ESCAPE ROOM: LA ARENA DEL GRADIADOR
#================================================

print("=== BIENVENIDO A LA ARENA ===")

# Pedimos el nombre
nombre = input("Nombre del Gladiador: ")

while not nombre.isalpha():
    print("Error: Solo se permiten letras")
    nombre = input("Nombre del Gladiador: ")

print("Nombre del Gladiador:", nombre)


# Variables iniciales
vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_base = 15
danio_enemigo = 12
turno_gladiador = True


print("=== INICIO DEL COMBATE ===")


while vida_jugador > 0 and vida_enemigo > 0:

    print()
    print(nombre, "(HP:", vida_jugador, ")")
    print("Enemigo (HP:", vida_enemigo, ")")
    print("Pociones:", pociones)

    print()
    print("Elige una acción:")
    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    opcion = input("Opción: ")

    # Validamos que sea un número
    while not opcion.isdigit():
        print("Error: Ingrese un número válido.")
        opcion = input("Opción: ")

    opcion = int(opcion)

    # Validamos que sea 1, 2 o 3
    while opcion < 1 or opcion > 3:

        print("Error: Elija una opción entre 1 y 3.")

        opcion = input("Opción: ")

        while not opcion.isdigit():
            print("Error: Ingrese un número válido.")
            opcion = input("Opción: ")

        opcion = int(opcion)


    # OPCIÓN 1: ATAQUE PESADO
    if opcion == 1:

        if vida_enemigo < 20:
            danio = danio_base * 1.5
            print("¡Golpe crítico!")
        else:
            danio = danio_base

        vida_enemigo = vida_enemigo - danio

        print("¡Atacaste al enemigo por", danio, "puntos de daño!")


    # OPCIÓN 2: RÁFAGA VELOZ
    elif opcion == 2:

        print("¡Inicias una ráfaga de golpes!")

        danio = 0

        for i in range(3):

            vida_enemigo = vida_enemigo - 5
            danio = danio + 5

            print("Golpe", i + 1, "conectado por 5 de daño")

            if vida_enemigo <= 0:
                break

        print("Daño total:", danio)


    # OPCIÓN 3: CURAR
    elif opcion == 3:

        if pociones > 0:

            vida_jugador = vida_jugador + 30
            pociones = pociones - 1

            print("Te curaste 30 puntos de vida.")

        else:

            print("¡No quedan pociones!")


    # TURNO DEL ENEMIGO
    if vida_enemigo > 0:

        vida_jugador = vida_jugador - danio_enemigo

        print("¡El enemigo te atacó por",
              danio_enemigo, "puntos de daño!")


# FIN DEL JUEGO

if vida_jugador > 0:

    print()
    print("=== VICTORIA ===")
    print(nombre, "ha ganado la batalla.")

else:

    print()
    print("=== DERROTA ===")
    print("Has caído en combate.")