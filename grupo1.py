import random
import json

def RegistrarUsuario():
    while True:
        mail_usuario = input("Ingrese su mail: ")
        posicion = mail_usuario.find("@gmail.com")
        
        if posicion == -1:
            print("Mail inválido, ingrese nuevamente.")
            continue
        
        try:
            ArchUsuario = open("usuarios.txt", "r")
            mail_existe = False

            for linea in ArchUsuario:
                datos_usuario = linea.split(";")
                if len(datos_usuario) > 0 and datos_usuario[0] == mail_usuario:
                    mail_existe = True
                    break

            ArchUsuario.close()

            if mail_existe:
                print("Este mail ya está registrado. Ingrese un mail diferente.")
                continue

        except FileNotFoundError:
            print("El archivo 'usuarios.txt' no existe, será creado.")
            pass
        except OSError as mensaje:
            print("No se puede abrir el archivo: ", mensaje)
            continue

        pas_usuario = input("Ingrese su contraseña (debe ser alfanumérica y tener mínimo 8 caracteres): ")
        if len(pas_usuario) >= 8 and pas_usuario.isalnum():
            nombre_usuario = input("Ingrese su nombre de usuario (debe ser alfanumérico y tener mínimo 6 caracteres y sin espacios): ")
            if nombre_usuario.isalnum() and len(nombre_usuario) >= 6 and " " not in nombre_usuario:
                while True:
                    nombre_existe = False
                    try:
                        nombres_usuarios = open("nombres_usuarios.txt", "r")
                        
                        for usuario in nombres_usuarios:
                            if nombre_usuario.strip() == usuario.strip():
                                nombre_existe = True
                                break
                        nombres_usuarios.close()

                    except FileNotFoundError:
                        print("El archivo 'nombres_usuarios.txt' no existe, se creará un nuevo archivo.")
                        nombres_usuarios = open("nombres_usuarios.txt", "w")
                        nombres_usuarios.close()

                    if nombre_existe:
                        print("El nombre de usuario ya existe, ingrese nuevamente.")
                        nombre_usuario = input("Ingrese su nombre de usuario (debe ser alfanumérico, de 6 caracteres y sin espacios): ")
                    else:
                        try:
                            nombres_usuarios = open("nombres_usuarios.txt", "a")
                            nombres_usuarios.write(nombre_usuario + "\n")
                            nombres_usuarios.close()
                        except OSError as mensaje:
                            print("No se puede abrir el archivo: ", mensaje)
                        break

                try:
                    turnos_usuario = open(f"turnos_{nombre_usuario}.txt", "a")
                except OSError as mensaje:
                    print("No se puede abrir el archivo: ", mensaje)
                finally:
                    try:
                        turnos_usuario.close()
                    except NameError:
                        pass
                break
        else:
            print("Contraseña inválida, ingrese nuevamente.")

    def DatosUsuario():
        dni= input("Ingrese su DNI: ")
        while True:
            if dni.isdigit() == True and len(dni) == 8:
                break
            else:
                print("El numero de dni fue ingresado de forma erronea")
                dni= input("Ingrese su DNI: ")
        nombre = input("Ingrese su nombre/s: ")
        apellido = input("Ingrese su apellido/s: ")
        obra_social = input("Ingrese su Obra Social: ")
        dic = []
        dic.append(nombre.title())
        dic.append(apellido.title())
        dic.append(dni)
        dic.append(obra_social.title())
        return dic
    
    usuario = DatosUsuario()   
    try:
        ArchUsuario = open("usuarios.txt", "a")
        ArchUsuario.write(mail_usuario + ";" + pas_usuario + ";" + nombre_usuario + ";" + usuario[0] + ";" + usuario[1] + ";" + usuario[2] + ";" + usuario[3] + "\n")
    except OSError as mensaje:
        print("No se puede abrir el archivo: ", mensaje)
    finally:
        try:
            ArchUsuario.close()
        except NameError:
            pass
    return ArchUsuario, turnos_usuario, usuario

def DiccEspecialidades():
    variable = (0, 30)
    
    def PrimerasFechas():
        fechas_1 = []
        for i in range(10):
            hora_1 = random.randint(7, 14)
            minutos = random.choice(variable)
            mes = random.randint(1, 12)

            if mes == 2:
                dia = random.randint(1, 28)
            elif mes in [1, 3, 5, 7, 8, 10, 12]:
                dia = random.randint(1, 31)
            else:
                dia = random.randint(1, 30)    
            fecha_1 = f"{dia}/{mes}    {hora_1:02}:{minutos:02}"
            fechas_1.append(fecha_1)
        return fechas_1
    
    def SegundasFechas():
        fechas_2 = []
        for i in range(10):
            hora_2 = random.randint(15, 22)
            minutos = random.choice(variable)
            mes = random.randint(1, 12)

            if mes == 2:
                dia = random.randint(1, 28)
            elif mes in [1, 3, 5, 7, 8, 10, 12]:
                dia = random.randint(1, 31)
            else:
                dia = random.randint(1, 30)
            
            fecha_2 = f"{dia}/{mes}    {hora_2:02}:{minutos:02}"
            fechas_2.append(fecha_2)
        return fechas_2

    especialidades = ['Cardiologia', 'Dermatologia', 'Cirugia General', 'Endocrinologia', 'Gastroenterologia',
                     'Ginecologia', 'Neumonologia', 'Neurocirugia', 'Oftalmologia', 'Pediatria',
                     'Psiquiatria', 'Traumatologia']

    doctores = [
        "Dr. Juan Pérez", "Dr. María González", "Dr. Carlos Ramírez", "Dr. Ana Martínez", "Dr. José Hernández",
        "Dr. Laura López", "Dr. Luis Fernández", "Dr. Carmen Ortiz", "Dr. Manuel García", "Dr. Elena Díaz",
        "Dr. Alberto Sánchez", "Dr. Patricia Torres", "Dr. Jorge Romero", "Dr. Lucía Castro", "Dr. Andrés Moreno",
        "Dr. Adriana Reyes", "Dr. Antonio Jiménez", "Dr. Beatriz Vargas", "Dr. Ricardo Soto", "Dr. Claudia Peña",
        "Dr. Alejandro Silva", "Dr. Verónica Flores", "Dr. Eduardo Muñoz", "Dr. Gabriela Castillo", "Dr. Francisco Paredes",
        "Dr. Daniela Mendoza", "Dr. Raúl Rivas", "Dr. Teresa Serrano", "Dr. Sergio Aguilar", "Dr. Pilar Ponce",
        "Dr. Diego Núñez", "Dr. Valentina Morales", "Dr. Ricardo Fernández", "Dr. Gloria Vega", "Dr. Roberto Medina",
        "Dr. Susana Castro", "Dr. Francisco Núñez", "Dr. Elisa Serrano", "Dr. Martín Muñoz", "Dr. Camila Rodríguez",
        "Dr. Javier Pérez", "Dr. Liliana Blanco", "Dr. Emilio Torres", "Dr. Natalia Salazar", "Dr. Miguel Reyes",
        "Dr. Esteban Castillo", "Dr. Catalina Silva", "Dr. Héctor López", "Dr. Silvia Ramos", "Dr. Sergio Gómez",
        "Dr. Ingrid Ortega", "Dr. Óscar Benítez", "Dr. Iván Aguilera", "Dr. Marcos Gutiérrez", "Dr. Gabriela Acosta",
        "Dr. Claudia Guzmán", "Dr. Ramón Herrera", "Dr. Andrés Flores", "Dr. Mónica Gallardo", "Dr. Estefanía Ruiz"
    ]
    
    random.shuffle(doctores)
    
    especialidades_1 = ['Cardiologia', 'Dermatologia', 'Cirugia General', 'Endocrinologia', 'Gastroenterologia',
                     'Ginecologia']
    especialidades_2 = ['Neumonologia', 'Neurocirugia', 'Oftalmologia', 'Pediatria',
                     'Psiquiatria', 'Traumatologia']

    dicc_especialidades = {}

    with open('especialidades.json', 'w') as file:
        file.write('{\n')

        for i, especialidad in enumerate(especialidades):
            if len(doctores) < 5:
                break

            doctores_asignados = doctores[:5]
            doctores = doctores[5:]

            if especialidad in especialidades_1:
                fechas = PrimerasFechas()
            elif especialidad in especialidades_2:
                fechas = SegundasFechas()

            file.write(f'  "{especialidad}": {{\n')

            for doc_i, doctor in enumerate(doctores_asignados):
                fechas_str = json.dumps(fechas)
                file.write(f'    "{doctor}": {fechas_str}')
                if doc_i < len(doctores_asignados) - 1:
                    file.write(',\n')
                else:
                    file.write('\n')

            if i < len(especialidades) - 1:
                file.write('  },\n')
            else:
                file.write('  }\n')

        file.write('}\n')
    
    return dicc_especialidades


def ImpresionTurno(especialidad_usuario, doctor_usuario, horario_usuario, usuario):
    print("-"*63)
    print("Reserva de turno".center(40))
    print()
    print(f'Especialidad:{"."*28} {especialidad_usuario}')
    print(f'Doctor:{"."*34} {doctor_usuario}')
    print(f'Horario:{"."*33} {horario_usuario}')
    print(f'Nombre completo:{"."*25} {usuario[0]} {usuario[1]}')
    print(f'DNI:{"."*37} {usuario[2]}')
    print(f'Obra Social:{"."*29} {usuario[3]}')
    print("-"*63)
    print()

#Main
print("Bienvenido/a A Nuestro Sistema de Reserva de Turnos Médicos, Que desea hacer?")
primer_menu = ["Registrarse", "Iniciar Sesión"]
lista_complementaria_primer_menu = [i+1 for i in range(len(primer_menu))]
print("\n" + "=" * 40 + "\n")
print("Sistema de reserva de turnos médicos")
print("-" * 40)
for i in range(len(primer_menu)):
    print(f"{lista_complementaria_primer_menu[i]} {primer_menu[i]}")
            
print("\n" + "=" * 40 + "\n")
print()
while True:
    try:
        desicion = int(input("Ingrese el número correspondiente a lo que desee: "))
        if 1 <= desicion <= len(lista_complementaria_primer_menu):
            turno_usuario = primer_menu[desicion - 1]
            print(f"Has seleccionado: {turno_usuario}")
            if turno_usuario == "Registrarse":
                ArchUsuario, turnos_usuario, usuario = RegistrarUsuario()
            break
        else:
            print("Valor fuera de rango. Por favor, ingrese un número válido.")
    except ValueError:
        print("Entrada no válida. Por favor, ingrese un número.")

DiccEspecialidades()
with open('especialidades.json', 'r') as file:
    especialidades = json.load(file)
especialidad = especialidades.keys()
lista_especialidad = list(especialidad)
lista_complementaria_especialidad = [i+1 for i in range(len(lista_especialidad))]
especialidad_usuario = 0
doctor = 0
lista_doctor = 0
lista_complementaria_doctor = 0
doctor_usuario = 0
horario = 0
lista_horario = 0
lista_complementaria_horario = 0
horario_usuario = 0
decision = input("Desea reservar un turno? (y/n): ")
matriz_especialidad = [[lista_complementaria_especialidad[i], lista_especialidad[i]] for i in range(len(lista_especialidad))]

while True:
    if decision == "y":
        print("\n" + "=" * 40 + "\n")
        print("Especialidades")
        print("-" * 40)
        for i in range(len(lista_especialidad)):
            print(f"{lista_complementaria_especialidad[i]} {lista_especialidad[i]}")
            
        print("\n" + "=" * 40 + "\n")
        print()
        
        while True:
            try:
                desicion1 = int(input("Ingrese el número correspondiente a la especialidad que desee: "))
                if 1 <= desicion1 <= len(matriz_especialidad):
                    especialidad_usuario = lista_especialidad[desicion1 - 1]
                    print(f"Has seleccionado: {especialidad_usuario}")
                    break
                else:
                    print("Valor fuera de rango. Por favor, ingrese un número válido.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")


        doctor = especialidades.get(especialidad_usuario)
        lista_doctor = list(doctor)
        lista_complementaria_doctor = [i+1 for i in range(len(lista_doctor))]
        matriz_doctor = [[lista_complementaria_doctor[i], lista_doctor[i]] for i in range(len(lista_doctor))]
        print("\n" + "=" * 40 + "\n")
        print(f"Doctores correspondiente a la especialidad: {especialidad_usuario}")
        print("-" * 40)
        for i in range(len(lista_doctor)):
            print(f"{lista_complementaria_doctor[i]} {lista_doctor[i]}")
        print("\n" + "=" * 40 + "\n")
        print()

        while True:
            try:
                desicion2 = int(input("Ingrese el número correspondiente al doctor que desee: "))
                if 1 <= desicion2 <= len(matriz_doctor):
                    doctor_usuario = lista_doctor[desicion2 - 1]
                    print(f"Has seleccionado: {doctor_usuario}")
                    break
                else:
                    print("Valor fuera de rango. Por favor, ingrese un número válido.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")

        horario = doctor.get(doctor_usuario)
        lista_horario = list(horario)
        lista_complementaria_horario = [i+1 for i in range(len(lista_horario))]
        matriz_horario = [[lista_complementaria_horario[i], lista_horario[i]] for i in range(len(lista_horario))]
        print("\n" + "=" * 40 + "\n")
        print(f"Horarios correspondientes al Dr/Dra: {doctor_usuario}")
        print("-" * 40)
        for i in range(len(lista_horario)):
            print(f"{lista_complementaria_horario[i]} {lista_horario[i]}")
        print("\n" + "=" * 40 + "\n")
        print()

        while True:
            try:
                desicion3 = int(input("Ingrese el número correspondiente a la especialidad que desee: "))
                if 1 <= desicion3 <= len(matriz_horario):
                    horario_usuario = lista_horario[desicion3 - 1]
                    print(f"Has seleccionado: {horario_usuario}")
                    break
                else:
                    print("Valor fuera de rango. Por favor, ingrese un número válido.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")

        ImpresionTurno(especialidad_usuario, doctor_usuario, horario_usuario, usuario)
        break
    else:
        break