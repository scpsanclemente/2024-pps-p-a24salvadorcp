from datetime import datetime, timedelta

# Definimos el horario de clases para cada día
horario_clases = {
    'lunes': ["16:00", "16:50", "17:40", "18:30", "19:20", "20:10", "21:00", "21:50"],
    'martes': ["16:00", "16:50", "17:40", "18:30", "19:20", "20:10", "21:00"],
    'miércoles': ["16:00", "16:50", "17:40", "18:30", "19:20", "20:10", "21:00", "21:50"],
    'jueves': ["16:00", "16:50", "17:40", "18:30", "19:20", "20:10", "21:00"],
    'viernes': ["16:00", "16:50", "17:40", "18:30", "19:20"]
}

def obtener_hora_actual():
    ahora = datetime.now()
    dia_semana = ahora.strftime("%A").lower()
    hora_actual = ahora.strftime("%H:%M")
    return dia_semana, hora_actual
    

def calcular_tiempo_restante(horarios, hora_actual):
    hora_actual_dt = datetime.strptime(hora_actual, "%H:%M")
    for i in range(len(horarios) - 1):
        inicio_clase = datetime.strptime(horarios[i], "%H:%M")
        fin_clase = datetime.strptime(horarios[i+1], "%H:%M")
        
        if inicio_clase <= hora_actual_dt < fin_clase:
            # Si estamos en clase, calcula el tiempo restante hasta que termine la clase
            tiempo_restante_clase = fin_clase - hora_actual_dt
            return f"Estás en clase. Quedan {tiempo_restante_clase} para que termine la clase actual."
    
    # Si no estamos en clase, calcula cuánto falta para que termine el día de clases
    fin_dia = datetime.strptime(horarios[-1], "%H:%M")
    if hora_actual_dt < fin_dia:
        tiempo_restante_dia = fin_dia - hora_actual_dt
        return f"No estás en clase. Quedan {tiempo_restante_dia} para que termine el día de clases."
    else:
        return "El día de clases ha terminado."

# Ejecución del script
dia_actual, hora_actual = obtener_hora_actual()

# Verificamos si es un día de clases
if dia_actual in horario_clases:
    resultado = calcular_tiempo_restante(horario_clases[dia_actual], hora_actual)
else:
    resultado = "Hoy no tienes clases."


print(dia_actual)
print(hora_actual)
print(resultado)
