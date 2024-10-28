from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# Lista de productos
productos = [
    "Manzanas", "Peras", "Melón", "Sandia", "Tomate", "Mezclum", "Pan Bimbo", 
    "Pan De Pipas", "Pan De Semillas (1)", "Pan De Semillas (2)", "Pan Blanco", 
    "Granolas", "Choco Krispis", "Pan Payes De Cereales", "Zumo De Naranja", 
    "Zumo De Piña Y Uva", "Zumo De Melocotón", "Leche", "Cruasanes", 
    "Napolitanas", "Donuts Chocolate", "Donuts Blancos", "Tartas", "Nueces", 
    "Mermelada Fresa", "Mermelada Melocoton", "Mantequilla", "Jamon York", 
    "Jamon Serrano", "Salchichon", "Chorizo", "Queso Cheddar", "Queso Havarti", 
    "Queso", "Yogur", "Huevos", "Beicon"
]

# Crear el PDF
pdf = SimpleDocTemplate("Checklist_Final_Updated_v4.pdf", pagesize=A4)

# Crear la cabecera de la tabla
header1 = ["Hay", "Productos", "Relación de productos consumidos"]
header2 = ["", ""] + ["Comens."] * 7  # Coloca "Comens." y "Fecha" en la misma celda
header3 = ["", ""] + ["Fecha"] * 7  # Abreviaturas para la cabecera
data = [header1, header2, header3]

# Añadir los productos como la primera columna y columnas vacías para checklists
for producto in productos:
    row = ["", producto, "", "", "", "", "", "", ""]
    data.append(row)

# Crear la tabla
table = Table(data, colWidths=[25, 100, 40, 40, 40, 40, 40, 40, 40])

# Estilo de la tabla
style = TableStyle([
    ('TEXTCOLOR', (0, 0), (-1, 2), colors.black),  # Cambia el color del texto a negro
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),  # Alinear todo a la izquierda
    ('FONTNAME', (0, 0), (-1, 2), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 2), 8),  # Tamaño de fuente para el encabezado 1
    ('FONTSIZE', (2, 0), (-1, 0), 5),  # Tamaño de fuente 5 para header2
    ('FONTSIZE', (2, 1), (-1, 1), 5),  # Tamaño de fuente 5 para header3
    ('FONTSIZE', (0, 0), (-1, -1), 6),  # Tamaño de fuente 6 para el resto
    ('BOTTOMPADDING', (0, 0), (-1, 2), 6),
    ('BACKGROUND', (0, 3), (-1, -1), colors.beige),  # Fondo beige para el resto de la tabla
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('SPAN', (0, 0), (0, 2)),  # Combina "Hay" en la primera columna
    ('SPAN', (1, 0), (1, 2)),  # Combina "Productos" en la segunda columna
    ('SPAN', (2, 0), (8, 0))    # Combina las cabeceras de la fila 1
])

table.setStyle(style)

# Añadir la tabla al PDF
elements = [table]
pdf.build(elements)

print("PDF creado en el directorio actual.")
