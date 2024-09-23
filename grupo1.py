import random

def lista_fechas_random():
    fechas = []
    variable = (0, 30)
    for i in range(10):
        hora = random.randint(8, 22)
        minutos = random.choice(variable)
        mes = random.randint(1, 12)

        if mes == 2:
            dia = random.randint(1, 28)
        elif mes in [1, 3, 5, 7, 8, 10, 12]:
            dia = random.randint(1, 31)
        else:
            dia = random.randint(1, 30)    
        fecha = f"{dia}/{mes}    {hora:02}:{minutos:02}"
        fechas.append(fecha)
    return fechas

def DiccDoctores():
    lista_de_fechas= lista_fechas_random()
    doctores = [
    "Dr. Juan Pérez", "Dr. María González", "Dr. Carlos Ramírez", "Dr. Ana Martínez", "Dr. José Hernández",
    "Dr. Laura López", "Dr. Luis Fernández", "Dr. Carmen Ortiz", "Dr. Manuel García", "Dr. Elena Díaz",
    "Dr. Alberto Sánchez", "Dr. Patricia Torres", "Dr. Jorge Romero", "Dr. Lucía Castro", "Dr. Andrés Moreno",
    "Dr. Adriana Reyes", "Dr. Antonio Jiménez", "Dr. Beatriz Vargas", "Dr. Ricardo Soto", "Dr. Claudia Peña",
    "Dr. Alejandro Silva", "Dr. Verónica Flores", "Dr. Eduardo Muñoz", "Dr. Gabriela Castillo", "Dr. Francisco Paredes",
    "Dr. Daniela Mendoza", "Dr. Raúl Rivas", "Dr. Teresa Serrano", "Dr. Sergio Aguilar", "Dr. Pilar Ponce"
]
    random.shuffle(doctores)
    dicc_doc = {doctor: lista_de_fechas for doctor in doctores[:5]}
    return dicc_doc

def DiccEspecialidades():
    listadoctor = DiccDoctores()
    especialidades = [
        'Cardiologia', 'Dermatologia', 'Cirugia General', 'Endocrinologia',
        'Gastroenterologia', 'Ginecologia', 'Neumonologia', 'Neurocirugia',
        'Oftalmologia', 'Pediatria', 'Psiquiatria', 'Traumatologia'
    ]

    dicc_especialidades = {i: listadoctor for i in especialidades[:12]}
    return dicc_especialidades

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
especialidades = DiccEspecialidades()
usuario = DatosUsuario()
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
        for i in range(len(lista_especialidad)):
            print(f"{lista_complementaria_especialidad[i]} {lista_especialidad[i]}")

        print()
        
        while True:
            desicion1 = int(input("Ingrese el número correspondiente a la especialidad que desee: "))
            if 1 <= desicion1 <= len(matriz_especialidad):
                especialidad_usuario = lista_especialidad[desicion1 - 1]
                print(f"Has seleccionado: {especialidad_usuario}")
                break 
            else:
                print("Valor fuera de rango. Por favor, ingrese un número válido.")

        doctor = especialidades.get(especialidad_usuario)
        lista_doctor = list(doctor)
        lista_complementaria_doctor = [i+1 for i in range(len(lista_doctor))]
        matriz_doctor = [[lista_complementaria_doctor[i], lista_doctor[i]] for i in range(len(lista_doctor))]
        for i in range(len(lista_doctor)):
            print(f"{lista_complementaria_doctor[i]} {lista_doctor[i]}")
        print()

        while True:
            desicion2 = int(input("Ingrese el número correspondiente al doctor que desee: "))
            if 1 <= desicion2 <= len(matriz_doctor):
                doctor_usuario = lista_doctor[desicion2 - 1]
                break
            else:
                print("Valor fuera de rango. Por favor, ingrese un número válido.")

        horario = doctor.get(doctor_usuario)
        lista_horario = list(horario)
        lista_complementaria_horario = [i+1 for i in range(len(lista_horario))]
        matriz_horario = [[lista_complementaria_horario[i], lista_horario[i]] for i in range(len(lista_horario))]
        for i in range(len(lista_horario)):
            print(f"{lista_complementaria_horario[i]} {lista_horario[i]}")
        print()

        while True:
            desicion3 = int(input("Ingrese el número correspondiente al horario que desee: "))
            if 1 <= desicion3 <= len(matriz_horario):
                horario_usuario = lista_horario[desicion3 - 1]
                break
            else:
                print("Valor fuera de rango. Por favor, ingrese un número válido.")

        ImpresionTurno(especialidad_usuario, doctor_usuario, horario_usuario, usuario)
        break

    else:
        break



