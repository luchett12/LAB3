

#-----------------------------CREA EL EXCEL------------------------------------------------


from openpyxl import Workbook #IMPORTAMOS EL SUBMODULO "WORKBOOK"


wb = Workbook() #CREAMOS EL OBJETO WORKBOOK


filesheet = "./TP3EXCEL.xlsx" #ESPECIFICAMOS EL NOMBRE Y LA RUTA DEL ARCHIVO


wb.save(filesheet) #GUARDAMOS EL ARCHIVO


#-----------------------------INSERTA LOS DATOS PRECARGADOS EN EL EXCEL-------------------


from openpyxl import load_workbook #IMPORTAMOS LOAD_WORKBOOK

filesheet = "./TP3EXCEL.xlsx" #RUTA DE NUESTRO ARCHIVO

wb = load_workbook(filesheet) #CREAMOS EL OBJETO LOAD_WORKBOOK


sheet = wb.active #SELECCIONA LOS ARCHIVOS

datos = [('ID', 'NOMBRE', 'EDAD'), #ESCRIBIMOS LOS DATOS CON SUS RESPECTIVAS FILAS Y COLUMNAS
   (0, "LUCAS", 21),
   (1, "FACU", 21),
   (2, "LAUTI", 20)]

for row in datos: #RECORREMOS LAS COLUMNAS Y ESCRIBIMOS LOS DATOS
 sheet.append(row)

wb.save(filesheet) #GUARDAMOS LOS CAMBIOS


#------------------------LEE EL EXCEL---------------------------------


from openpyxl import load_workbook #IMPORTAMOS LOAD_WORKBOOK

filesheet = "./TP3EXCEL.xlsx" #RUTA DE NUESTRO ARCHIVO

wb = load_workbook(filesheet) #CREAMOS EL OBJETO LOAD_WORKBOOK

sheet = wb.active #SELECCIONAMOS EL ARCHIVO

A1 = sheet['A1'].value # OBTENEMOS EL VALOR DE LA CELDA A1
A2 = sheet['A2'].value # OBTENEMOS EL VALOR DE LA CELDA A2
A3 = sheet['A3'].value # OBTENEMOS EL VALOR DE LA CELDA A3
A4 = sheet['A4'].value # OBTENEMOS EL VALOR DE LA CELDA A4

B1 = sheet['B1'].value # OBTENEMOS EL VALOR DE LA CELDA B1
B2 = sheet['B2'].value # OBTENEMOS EL VALOR DE LA CELDA B2
B3 = sheet['B3'].value # OBTENEMOS EL VALOR DE LA CELDA B3
B4 = sheet['B4'].value # OBTENEMOS EL VALOR DE LA CELDA B4

C1 = sheet['C1'].value # OBTENEMOS EL VALOR DE LA CELDA C1
C2 = sheet['C2'].value # OBTENEMOS EL VALOR DE LA CELDA C2
C3 = sheet['C3'].value # OBTENEMOS EL VALOR DE LA CELDA C3
C4 = sheet['C4'].value # OBTENEMOS EL VALOR DE LA CELDA C4

celdas = [(A1,B1,C1), (A2,B2,C2), (A3,B3,C3), (A4,B4,C4)] # MOSTRAMOS LOS VALORES 
for valor in celdas:
 print(valor)