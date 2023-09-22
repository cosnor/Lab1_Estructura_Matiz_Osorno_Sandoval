def contiene_no_numero(lista_palabras):
    for palabra in lista_palabras:
        try:
            # Intenta convertir la palabra en un número
            float(palabra)
        except ValueError:
            # Si se genera una excepción ValueError, significa que la palabra no es un número
            return True
    # Si ninguna palabra en la lista generó una excepción ValueError, todas son números
    return False

def es_default(lista_palabras):
    for palabra in lista_palabras:
        if palabra in ["Departamento", "Ciudad      ", "Tipo          ","Cuartos    ", "Baños        ", "Operación    ", "", " ", "  ", "   ", "    "]:
            return True
    return False

def eliminar_saltos_de_linea(cadena):
    return cadena.replace('\n', '')
