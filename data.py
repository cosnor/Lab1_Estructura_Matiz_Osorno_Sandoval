import csv

with open('co_properties_final.csv', mode='r', encoding='utf-8') as archivo_csv:
    # Crea un objeto lector de CSV
    lector_csv = csv.reader(archivo_csv)

    database = []
    # Itera a través de las filas del archivo CSV
    #Se borra la primera fila que contiene los nombres de las columnas	
    for fila in lector_csv:
        # Cada fila es una lista de valores separados por comas
        # Puedes acceder a los valores por índice o por nombre de columna
        title = fila[0]
        department = fila[1]
        city = fila[2]
        property_type = fila[3]
        latitude = fila[4]
        longitude = fila[5]
        surface_total = fila[6]
        surface_covered = fila[7]
        bedrooms = fila[8]
        bathrooms = fila[9]
        operation_type = fila[10]
        price = fila[11]
        #Metrica segun la ciudad
        if city == "Bogotá D.C" or city == "Medellín" or city == "Barranquilla" or city == "Cali":
            metrica2 = float(surface_covered)/float(surface_total)
        else:
            metrica2 = (float(surface_covered)/float(surface_total)) * 0.25
        data = [title, department, city, property_type, latitude, longitude, surface_total, surface_covered, bedrooms, bathrooms, operation_type, price, float(price)/float(surface_total), metrica2]
        database.append(data)
