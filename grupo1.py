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

    dicc_especialidades = {esp: listadoctor for esp in range(len(especialidades))}
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
    dic = {dni: [nombre.title(), apellido.title(), obra_social.title()]}
    return dic


#Main
especialidades = DiccEspecialidades()
usuario = DatosUsuario()

especialidad = especialidades.keys()
doctor = especialidades.values()
#horario = doctor.values()

lista_especialidad = list(especialidad)
lista_doctor = list(doctor)
#lista_horario = list(horario)
lista_complementaria_especialidad = []
lista_complementaria_doctor = []
#lista_complementaria_horario = []

for i in range(len(especialidad)):
    lista_complementaria_especialidad.append(i)

for i in range(len(lista_doctor)):
    lista_complementaria_doctor.append(i)

#for i in range(len(lista_horario)):
#    lista_complementaria_horario.append(i)