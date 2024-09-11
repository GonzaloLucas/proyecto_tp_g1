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

def ListaDoctores():
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
    listadoc = [{doctor: lista_de_fechas} for doctor in doctores[:5]]
    for i in listadoc:
        print(i)
    return listadoc

ListaDoctores()