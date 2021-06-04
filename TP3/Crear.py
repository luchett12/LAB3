
from openpyxl import Workbook #Importamos el submodulo "Workbook"


wb = Workbook() #Creamos el objeto Workbook


filesheet = "./TP3EXCEL.xlsx" #Especificamos el nombre y la ruta del archivo


wb.save(filesheet) #Guardamos el archivo