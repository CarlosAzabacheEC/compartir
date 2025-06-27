Este script en Python genera datos ficticios de tickets de soporte técnico y los guarda en un archivo Excel llamado tickets_generados_intervalos.xlsx. A continuación te explico línea por línea cada parte:
#### 🔹 1. Importación de librerías
```import pandas as pd
from random import choice, randint
from datetime import datetime, timedelta

```
- pandas: para manipular datos en forma de tabla (DataFrame) y exportarlos a Excel.
- choice y randint: para seleccionar aleatoriamente valores y generar números aleatorios.
- datetime, timedelta: para manipular fechas y horas.
#### 🔹 2. Configuraciones iniciales
```num_rows = 10000

```
- Se crearán 10,000 filas (tickets).
```start_date = datetime(2021, 1, 1, 8)
end_date = datetime(2026, 12, 31, 18)
total_seconds = int((end_date - start_date).total_seconds())

```
- Define un rango de fechas y horas entre el 1 de enero de 2021 a las 8:00 am y el 31 de diciembre de 2026 a las 6:00 pm.
- total_seconds: es el total de segundos en ese rango de fechas.
#### 🔹 3. Valores posibles para los campos
```sistemas = ['S01', 'S02', 'S03', 'S04', 'S05']
tipos_problema = ['T01', 'T02', 'T03', 'T04', 'T05']
prioridades = ['1', '2', '3']
estados = ['A', 'C', 'R', 'P']
tecnicos = ['Tec01', 'Tec02', 'Tec03', 'Tec04', 'Tec05']

```
- Se definen las posibles categorías para distintos campos (como sistema afectado, tipo de problema, etc.).
#### 🔹 4. Generación de datos
```for i in range(1, num_rows + 1):

```
- Bucle que se repite 10,000 veces para generar los tickets.
#### ➤ Generar campos
```ticket_id = f"T{i:04}"  # T0001, T0002, ...
creation_offset = timedelta(seconds=randint(0, total_seconds))
fecha_creacion = start_date + creation_offset

```
- ticket_id: se genera un identificador como T0001.
- fecha_creacion: se genera una fecha aleatoria dentro del rango establecido.
#### ➤ Posible fecha de resolución
```if choice([True, False]):
    tiempo_resolucion = timedelta(hours=randint(1, 72))
    fecha_resolucion = fecha_creacion + tiempo_resolucion
    fecha_resolucion_str = fecha_resolucion.strftime("%Y-%m-%d %H:%M:%S")
else:
    fecha_resolucion_str = ''

```
- 50% de probabilidad de que el ticket tenga fecha de resolución.
- Si la tiene, será entre 1 y 72 horas después de su creación.
#### ➤ Otros campos
```sistema = choice(sistemas)
tipo_problema = choice(tipos_problema)
prioridad = choice(prioridades)
estado = choice(estados)
tecnico = choice(tecnicos)
satisfaccion = randint(1, 5) if estado in ['R', 'C'] else ''
sla = randint(4, 72)

```
- Se eligen aleatoriamente valores para sistema, tipo de problema, prioridad, estado, técnico, satisfacción y SLA.
- La satisfacción del cliente solo se llena si el estado es "R" (resuelto) o "C" (cerrado).
- El SLA (en horas) es un número aleatorio entre 4 y 72.
#### ➤ Guardar fila
```data.append([
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

```
- Se agrega la fila de datos a la lista data.
#### 🔹 5. Crear el DataFrame y exportar a Excel
```columns = ['TicketID', 'FechaCreacion', 'FechaResolucion', 'Sistema', 'TipoProblema', 'Prioridad', 'Estado', 'TecnicoAsignado', 'SatisfaccionCliente', 'SLA']
df = pd.DataFrame(data, columns=columns)
df.to_excel("tickets_generados_intervalos.xlsx", index=False)

```
- Se crea un DataFrame con las columnas indicadas.
- Se guarda como archivo Excel sin incluir el índice ( index=False).
#### ✅ ¿Para qué sirve?
Este script es ideal para:
- Simular bases de datos de soporte técnico.
- Probar visualizaciones en Power BI, Excel u otros.
- Crear casos de prueba para dashboards o modelos de machine learning.
