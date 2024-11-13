from datetime import datetime, timedelta


# Definimos el horario de clases para cada día
horario_clases = {
    'monday': ["16:00", "17:40", "20:10", "21:00", "21:50"],
    'tuesday': ["16:00",  "18:30", "21:00"],
    'wednesday': ["16:00",  "17:40",  "19:20", "21:50"],
    'thursday': ["16:00", "17:40", "19:20", "21:50"],
    'friday': ["16:00",  "18:30", "20:10"]
}

def obtener_hora_actual():
    ahora = datetime.now()
    dia_semana = ahora.strftime("%A").lower()
    hora_actual = ahora.strftime("%H:%M")
    return dia_semana, ahora 

def calcular_tiempo_restante(horarios, hora_actual):
    for i in range(len(horarios) - 1):
        inicio_clase = datetime.strptime(horarios[i], "%H:%M")
        fin_clase = datetime.strptime(horarios[i + 1], "%H:%M")
        
        # Q coincida con la fecha actual en `hora_actual`
        inicio_clase = inicio_clase.replace(year=hora_actual.year, month=hora_actual.month, day=hora_actual.day)
        fin_clase = fin_clase.replace(year=hora_actual.year, month=hora_actual.month, day=hora_actual.day)
        
        if inicio_clase <= hora_actual < fin_clase:
            #  stamos en clase - calcular tiempo restante
            tiempo_restante_clase = fin_clase - hora_actual
            horas, segundos_restantes = divmod(tiempo_restante_clase.seconds, 3600)
            minutos, segundos = divmod(segundos_restantes, 60)
            return f"Estás en clase. Quedan {horas} horas, {minutos} minutos y {segundos} segundos para que termine la clase actual."
    
    

# Ejecución del script
dia_actual, hora_actual = obtener_hora_actual()

# es sabado o domingo?
if dia_actual in horario_clases:
    resultado = calcular_tiempo_restante(horario_clases[dia_actual], hora_actual)
else:
    resultado = "Hoy no tienes clases."

print(resultado)
