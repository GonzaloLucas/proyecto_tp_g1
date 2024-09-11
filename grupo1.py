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

print(lista_fechas_random())