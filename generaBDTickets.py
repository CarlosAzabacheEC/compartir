import pandas as pd
from random import choice, randint
from datetime import datetime, timedelta

# Número de filas
num_rows = 10000

# Rango de fechas
start_date = datetime(2021, 1, 1, 8)
end_date = datetime(2026, 12, 31, 18)
total_seconds = int((end_date - start_date).total_seconds())

# Listas de valores posibles
sistemas = ['S01', 'S02', 'S03', 'S04', 'S05']
tipos_problema = ['T01', 'T02', 'T03', 'T04', 'T05']
prioridades = ['1', '2', '3']
estados = ['A', 'C', 'R', 'P']
tecnicos = ['Tec01', 'Tec02', 'Tec03', 'Tec04', 'Tec05']

# Lista para almacenar los datos
data = []

# Generar los datos
for i in range(1, num_rows + 1):
    ticket_id = f"T{i:04}"
    creation_offset = timedelta(seconds=randint(0, total_seconds))
    fecha_creacion = start_date + creation_offset

    if choice([True, False]):
        tiempo_resolucion = timedelta(hours=randint(1, 72))
        fecha_resolucion = fecha_creacion + tiempo_resolucion
        fecha_resolucion_str = fecha_resolucion.strftime("%Y-%m-%d %H:%M:%S")
    else:
        fecha_resolucion_str = ''

    sistema = choice(sistemas)
    tipo_problema = choice(tipos_problema)
    prioridad = choice(prioridades)
    estado = choice(estados)
    tecnico = choice(tecnicos)
    satisfaccion = randint(1, 5) if estado in ['R', 'C'] else ''
    sla = randint(4, 72)

    data.append([
        ticket_id,
        fecha_creacion.strftime("%Y-%m-%d %H:%M:%S"),
        fecha_resolucion_str,
        sistema,
        tipo_problema,
        prioridad,
        estado,
        tecnico,
        satisfaccion,
        sla
    ])

# Definir columnas y crear DataFrame
columns = [
    'TicketID',
    'FechaCreacion',
    'FechaResolucion',
    'Sistema',
    'TipoProblema',
    'Prioridad',
    'Estado',
    'TecnicoAsignado',
    'SatisfaccionCliente',
    'SLA'
]

df = pd.DataFrame(data, columns=columns)

# Guardar en Excel
df.to_excel("tickets_generados_intervalos.xlsx", index=False)
