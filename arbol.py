#Clases 
from typing import Optional

class nodoavl:
    def __init__(self, valor):
        self.valor = valor
        self.title = self.valor[0]
        self.department = self.valor[1]
        self.city = self.valor[2]
        self.property_type = self.valor[3]
        self.latitude = self.valor[4]
        self.longitude = self.valor[5]
        self.surface_total = self.valor[6]
        self.surface_covered = self.valor[7]
        self.bedrooms = self.valor[8]
        self.bathrooms = self.valor[9]
        self.operation_type = self.valor[10]
        self.price = self.valor[11]
        self.izquierda = None
        self.derecha = None
        self.altura = 1

            

class ArbolAVL:
    def __init__(self):
        self.raiz = None
        self.string = ""
    
    def _busqueda_por_parametro1(self, target, searchOn, operation): #Busco según ciertos parametros, el valor a buscar, la operacion para hacer y en qué lista se va a buscar
        return self._busqueda_por_parametro_recursivo1(self.raiz, target, searchOn, operation)
    
    def _busqueda_por_parametro_recursivo1(self, nodo_actual, target, searchOn, operation):
        if not nodo_actual:
            return []
        resultados = []
        #Strings
        #0 = title, 1 = department, 2 = city, 3 = property_type, 10 = operation_type
        #Numericos
        #4 = latitude, 5 = longitude, 6 = surface_total, 7 = surface_covered, 8 = bedrooms, 9 = bathrooms, 11 = price

        if searchOn == 0 or searchOn == 1 or searchOn == 2 or searchOn == 3 or searchOn == 10: #Si el valor a buscar es un string solo se habilitan 2 operaciones
            #Exactamente igual que la busqueda por metrica.
            if operation == "Equal":
                if target == nodo_actual.valor[searchOn]:
                    resultados.append(nodo_actual)
                    resultados.extend(self._busqueda_por_parametro_recursivo1(nodo_actual.izquierda, target, searchOn, operation))
                    resultados.extend(self._busqueda_por_parametro_recursivo1(nodo_actual.derecha, target, searchOn, operation))
                else:
                    resultados.extend(self._busqueda_por_parametro_recursivo1(nodo_actual.izquierda, target, searchOn, operation))
                    resultados.extend(self._busqueda_por_parametro_recursivo1(nodo_actual.derecha, target, searchOn, operation))
            elif operation == "Not Equal":
                if target != nodo_actual.valor[searchOn]:
                    resultados.append(nodo_actual)
                    resultados.extend(self._busqueda_por_parametro_recursivo1(nodo_actual.izquierda, target, searchOn, operation))
                    resultados.extend(self._busqueda_por_parametro_recursivo1(nodo_actual.derecha, target, searchOn, operation))
                else:
                    resultados.extend(self._busqueda_por_parametro_recursivo1(nodo_actual.izquierda, target, searchOn, operation))
                    resultados.extend(self._busqueda_por_parametro_recursivo1(nodo_actual.derecha, target, searchOn, operation))
        else: #Si el valor es numerico se habilitan 4 operaciones
            #Exacaamente igual que la busqueda por metrica.
            if operation == "Equal":
                if float(target) == float(nodo_actual.valor[searchOn]):
                    resultados.append(nodo_actual)
                    resultados.extend(self._busqueda_por_parametro_recursivo1(nodo_actual.izquierda, target, searchOn, operation))
                    resultados.extend(self._busqueda_por_parametro_recursivo1(nodo_actual.derecha, target, searchOn, operation))
                else:
                    resultados.extend(self._busqueda_por_parametro_recursivo1(nodo_actual.izquierda, target, searchOn, operation))
                    resultados.extend(self._busqueda_por_parametro_recursivo1(nodo_actual.derecha, target, searchOn, operation))
            if operation == "Not Equal":
                if float(target) != float(nodo_actual.valor[searchOn]):
                    resultados.append(nodo_actual)
                    resultados.extend(self._busqueda_por_parametro_recursivo1(nodo_actual.izquierda, target, searchOn, operation))
                    resultados.extend(self._busqueda_por_parametro_recursivo1(nodo_actual.derecha, target, searchOn, operation))
                else:
                    resultados.extend(self._busqueda_por_parametro_recursivo1(nodo_actual.izquierda, target, searchOn, operation))
                    resultados.extend(self._busqueda_por_parametro_recursivo1(nodo_actual.derecha, target, searchOn, operation))            
            if operation == "Less Than":
                if float(target) > float(nodo_actual.valor[searchOn]):
                    resultados.append(nodo_actual)
                    resultados.extend(self._busqueda_por_parametro_recursivo1(nodo_actual.izquierda, target, searchOn, operation))
                    resultados.extend(self._busqueda_por_parametro_recursivo1(nodo_actual.derecha, target, searchOn, operation))
                else:
                    resultados.extend(self._busqueda_por_parametro_recursivo1(nodo_actual.izquierda, target, searchOn, operation))
                    resultados.extend(self._busqueda_por_parametro_recursivo1(nodo_actual.derecha, target, searchOn, operation))
            if operation == "Greater Than":
                if float(target) < float(nodo_actual.valor[searchOn]):
                    resultados.append(nodo_actual)
                    resultados.extend(self._busqueda_por_parametro_recursivo1(nodo_actual.izquierda, target, searchOn, operation))
                    resultados.extend(self._busqueda_por_parametro_recursivo1(nodo_actual.derecha, target, searchOn, operation))
                else:
                    resultados.extend(self._busqueda_por_parametro_recursivo1(nodo_actual.izquierda, target, searchOn, operation))
                    resultados.extend(self._busqueda_por_parametro_recursivo1(nodo_actual.derecha, target, searchOn, operation))
        return resultados
    
    def busqueda_multiple(self, target1, searchOn1, operation1, target2: Optional[str] = None, searchOn2: Optional[int] = None, operation2: Optional[str] = None, target3: Optional[str] = None, searchOn3: Optional[int] = None,  operation3: Optional[str] = None):
        #Aquí para hacer una busqueda con multiples parametros, pido obligatorio el primer parametro, y el resto será opcional
        resultado1 = self._busqueda_por_parametro1(target1, searchOn1, operation1)
        #Si estos parametros sirven, se hará la busqueda y se guardarán en listas independientes.
        if target2 != None:
            resultado2 = self._busqueda_por_parametro1(target2, searchOn2, operation2)
        if target3 != None:
            resultado3 = self._busqueda_por_parametro1(target3, searchOn3, operation3)
        
        #Aquí se hace la intercepcion de las listas, si hay 3 listas, se hace la intercepcion de las 3, si hay 2, se hace la intercepcion de las 2, y si hay 1, se devuelve el resultado del primer parametro.
        if target2 != None and target3 != None:
            resultado = list(set(resultado1) & set(resultado2) & set(resultado3))
        elif target2 != None and target3 == None:
            resultado = list(set(resultado1) & set(resultado2))
        elif target2 == None and target3 != None:
            resultado = list(set(resultado1) & set(resultado3))
        else:
            resultado = resultado1
        
        #Retorno la lista resultado
        return resultado

    def contar_valores(self):
        return self._contar_valores(self.raiz)

    def _contar_valores(self, nodo):
        if not nodo:
            return 0
        return 1 + self._contar_valores(nodo.izquierda) + self._contar_valores(nodo.derecha)

    #? Buscar según la primera métrica
    def buscar_por_metrica(self, valor1):
        return self._buscar_por_metrica_recursivo(self.raiz, valor1)

    def _buscar_por_metrica_recursivo(self, nodo_actual, valor1):
        resultados = []
        if not nodo_actual:
            return resultados
        
        #Si encuentra el valor, lo agrego a la lista de resultados y hago que siga visitando el resto del arbol
        
        if int(valor1) == int(nodo_actual.valor[12]):
            resultados.append(nodo_actual)
            resultados.extend(self._buscar_por_metrica_recursivo(nodo_actual.izquierda, valor1))
            resultados.extend(self._buscar_por_metrica_recursivo(nodo_actual.derecha, valor1))
        if int(valor1) < int(nodo_actual.valor[12]):
            resultados.extend(self._buscar_por_metrica_recursivo(nodo_actual.izquierda, valor1))
        if int(valor1) > int(nodo_actual.valor[12]):
            resultados.extend(self._buscar_por_metrica_recursivo(nodo_actual.derecha, valor1))

        return resultados
    
    #Buscar según la segunda metrica
    def buscar_por_metrica2(self, valor1):
        return self._buscar_por_metrica2_recursivo(self.raiz, valor1)

    def _buscar_por_metrica2_recursivo(self, nodo_actual, valor1):
        if not nodo_actual:
            return []
        resultados = []
        #Si encuentra el valor, lo agrego a la lista de resultados y hago que siga visitando el resto del arbol
        if valor1 == (nodo_actual.valor[13]):
            resultados.append(nodo_actual)
            resultados.extend(self._buscar_por_metrica2_recursivo(nodo_actual.izquierda, valor1))
            resultados.extend(self._buscar_por_metrica2_recursivo(nodo_actual.derecha, valor1))
        if valor1 < int(nodo_actual.valor[13]):
            resultados.extend(self._buscar_por_metrica2_recursivo(nodo_actual.izquierda, valor1))
        if valor1 > int(nodo_actual.valor[13]):
            resultados.extend(self._buscar_por_metrica2_recursivo(nodo_actual.derecha, valor1))

        return resultados
    
    
    def insertar(self, valor):
        self.raiz = self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo_actual, valor):
        if not nodo_actual:
            return nodoavl(valor)
        #Si el valor es menor que el valor del nodo actual, lo inserto en el subarbol izquierdo
        elif valor[12] < nodo_actual.valor[12]:
            nodo_actual.izquierda = self._insertar_recursivo(nodo_actual.izquierda, valor)
        #Si el valor es mayor que el valor del nodo actual, lo inserto en el subarbol derecho
        elif valor[12] > nodo_actual.valor[12]:
            nodo_actual.derecha = self._insertar_recursivo(nodo_actual.derecha, valor)
        else: #Si el valor es igual al valor del nodo actual, reviso la segunda metrica para insertar
            if valor[13] < nodo_actual.valor[13]: #Si el valor es menor que el valor del nodo actual, lo inserto en el subarbol izquierdo
                nodo_actual.izquierda = self._insertar_recursivo(nodo_actual.izquierda, valor)
            else: #Si el valor es mayor que el valor del nodo actual, lo inserto en el subarbol derecho
                nodo_actual.derecha = self._insertar_recursivo(nodo_actual.derecha, valor)

        #Cosas de balanceo, yo no escribí esto, así que no sé que ha
        nodo_actual.altura = 1 + max(self._obtener_altura(nodo_actual.izquierda), self._obtener_altura(nodo_actual.derecha))
        balance = self._obtener_balance(nodo_actual)

        if balance > 1 and valor[12] < nodo_actual.izquierda.valor[12]:
            return self._rotar_derecha(nodo_actual)

        if balance < -1 and valor[12] > nodo_actual.derecha.valor[12]:
            return self._rotar_izquierda(nodo_actual)

        if balance > 1 and valor[12] > nodo_actual.izquierda.valor[12]:
            nodo_actual.izquierda = self._rotar_izquierda(nodo_actual.izquierda)
            return self._rotar_derecha(nodo_actual)

        if balance < -1 and valor[12] < nodo_actual.derecha.valor[12]:
            nodo_actual.derecha = self._rotar_derecha(nodo_actual.derecha)
            return self._rotar_izquierda(nodo_actual)
        
        if valor[12] == nodo_actual.valor[12]: #Si el valor es igual al valor del nodo actual, reviso la segunda metrica para insertar, revisar esto
            if balance > 1 and valor[13] < nodo_actual.izquierda.valor[13]:
                return self._rotar_derecha(nodo_actual)

            if balance < -1 and valor[13] > nodo_actual.derecha.valor[13]:
                return self._rotar_izquierda(nodo_actual)

            if balance > 1 and valor[13] > nodo_actual.izquierda.valor[13]:
                nodo_actual.izquierda = self._rotar_izquierda(nodo_actual.izquierda)
                return self._rotar_derecha(nodo_actual)

            if balance < -1 and valor[13] < nodo_actual.derecha.valor[13]:
                nodo_actual.derecha = self._rotar_derecha(nodo_actual.derecha)
                return self._rotar_izquierda(nodo_actual)
        return nodo_actual
    
    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, nodo_actual, valor):
        if not nodo_actual:
            return nodo_actual

        # Realiza la búsqueda recursiva para encontrar el nodo a eliminar
        if valor[12] < nodo_actual.valor[12]:
            nodo_actual.izquierda = self._eliminar_recursivo(nodo_actual.izquierda, valor)
        elif valor[12] > nodo_actual.valor[12]:
            nodo_actual.derecha = self._eliminar_recursivo(nodo_actual.derecha, valor)
        else:
            if valor[13] < nodo_actual.valor[13]:
                nodo_actual.izquierda = self._eliminar_recursivo(nodo_actual.izquierda, valor)
            elif valor[13] > nodo_actual.valor[13]:
                nodo_actual.derecha = self._eliminar_recursivo(nodo_actual.derecha, valor)
            else:
                # Nodo a eliminar encontrado

                # Caso 1: Nodo con un solo hijo o sin hijos
                if nodo_actual.izquierda is None:
                    temp = nodo_actual.derecha
                    nodo_actual = None
                    return temp
                elif nodo_actual.derecha is None:
                    temp = nodo_actual.izquierda
                    nodo_actual = None
                    return temp

                # Caso 2: Nodo con dos hijos, se encuentra el sucesor inmediato (nodo más pequeño en el subárbol derecho)
                temp = self._encontrar_minimo(nodo_actual.derecha)
                nodo_actual.valor = temp.valor

                # Elimina el sucesor inmediato
                nodo_actual.derecha = self._eliminar_recursivo(nodo_actual.derecha, temp.valor)

        if nodo_actual is None:
            return nodo_actual

        # Actualiza la altura del nodo actual
        nodo_actual.altura = 1 + max(self._obtener_altura(nodo_actual.izquierda), self._obtener_altura(nodo_actual.derecha))

        # Realiza las rotaciones para mantener el equilibrio
        balance = self._obtener_balance(nodo_actual)

        if balance > 1 and self._obtener_balance(nodo_actual.izquierda) >= 0:
            return self._rotar_derecha(nodo_actual)

        if balance < -1 and self._obtener_balance(nodo_actual.derecha) <= 0:
            return self._rotar_izquierda(nodo_actual)

        if balance > 1 and self._obtener_balance(nodo_actual.izquierda) < 0:
            nodo_actual.izquierda = self._rotar_izquierda(nodo_actual.izquierda)
            return self._rotar_derecha(nodo_actual)

        if balance < -1 and self._obtener_balance(nodo_actual.derecha) > 0:
            nodo_actual.derecha = self._rotar_derecha(nodo_actual.derecha)
            return self._rotar_izquierda(nodo_actual)

        return nodo_actual

    def _rotar_derecha(self, z):
        if not z or not z.izquierda:
            return z
         
        y = z.izquierda
        T3 = y.derecha

        y.derecha = z
        z.izquierda = T3

        z.altura = 1 + max(self._obtener_altura(z.izquierda), self._obtener_altura(z.derecha))
        y.altura = 1 + max(self._obtener_altura(y.izquierda), self._obtener_altura(y.derecha))

        return y

    def _rotar_izquierda(self, z):
        if not z or not z.derecha:
            return z
        y = z.derecha
        T2 = y.izquierda

        y.izquierda = z
        z.derecha = T2

        z.altura = 1 + max(self._obtener_altura(z.izquierda), self._obtener_altura(z.derecha))
        y.altura = 1 + max(self._obtener_altura(y.izquierda), self._obtener_altura(y.derecha))

        return y

    def _obtener_altura(self, nodo_actual):
        if not nodo_actual:
            return 0
        return nodo_actual.altura

    def _obtener_balance(self, nodo_actual):
        if not nodo_actual:
            return 0
        return self._obtener_altura(nodo_actual.izquierda) - self._obtener_altura(nodo_actual.derecha)
    #metodo publico
    def obtener_balance(self, nodo_actual):
        if not nodo_actual:
            return 0
        return self._obtener_altura(nodo_actual.izquierda) - self._obtener_altura(nodo_actual.derecha)

    def _encontrar_minimo(self, nodo_actual):
        while nodo_actual.izquierda:
            nodo_actual = nodo_actual.izquierda
        return nodo_actual

    def _encontrar_maximo(self, nodo_actual):
      while nodo_actual.derecha:
        nodo_actual=nodo_actual.derecha
      return nodo_actual
    
    
    def recorrido(self):
        self._recorrido_recursivo(self.raiz)

    def _recorrido_recursivo(self, nodo_actual):
        global contador_llamadas
        #contador_llamadas += 1
        #print(contador_llamadas)
        if nodo_actual:
            self._recorrido_recursivo(nodo_actual.izquierda)
            contador_llamadas.append(nodo_actual.valor)
            self._recorrido_recursivo(nodo_actual.derecha)
    
    def recorrido_por_niveles_recursivo(self, raiz):
        altura = self.obtener_altura_arbol(raiz)
        for nivel in range(altura + 1):
            self.imprimir_nivel(raiz, nivel)

    def obtener_altura_arbol(self, nodo):
        if nodo is None:
            return -1
        altura_izquierda = self.obtener_altura_arbol(nodo.izquierda)
        altura_derecha = self.obtener_altura_arbol(nodo.derecha)
        return max(altura_izquierda, altura_derecha) + 1

    def imprimir_nivel(self, nodo, nivel_actual):
        if nodo is None:
            return
        if nivel_actual == 0:
            print(nodo.valor[12], end=' ')
        else:
            self.imprimir_nivel(nodo.izquierda, nivel_actual - 1)
            self.imprimir_nivel(nodo.derecha, nivel_actual - 1)
    def obtener_altura(self):
        return self._obtener_altura_recursivo(self.raiz)
    def _obtener_altura_recursivo(self, nodo_actual):
        if not nodo_actual:
            return 0
        return 1 + max(self._obtener_altura_recursivo(nodo_actual.izquierda), self._obtener_altura_recursivo(nodo_actual.derecha))
    
    def obtener_nivel(self, valor):
        return self._obtener_nivel_recursivo(self.raiz, valor)
    
    def _obtener_nivel_recursivo(self, nodo_actual, valor):
        if not nodo_actual:
            return -1  # El valor no se encontró en el árbol
        
        if valor.valor[12] == nodo_actual.valor[12]:
            if valor.valor[13] == nodo_actual.valor[13]:
                return 0  # Encontrado en este nivel
            elif valor.valor[13] < nodo_actual.valor[13]:
                return 1 + self._obtener_nivel_recursivo(nodo_actual.izquierda, valor)
            else:
                return 1 + self._obtener_nivel_recursivo(nodo_actual.derecha, valor)
        elif valor.valor[12] < nodo_actual.valor[12]:
            return 1 + self._obtener_nivel_recursivo(nodo_actual.izquierda, valor)
        else:
            return 1 + self._obtener_nivel_recursivo(nodo_actual.derecha, valor)
        
    def _obtener_balance(self, nodo_actual):
        if not nodo_actual:
            return 0
        return self._obtener_altura(nodo_actual.izquierda) - self._obtener_altura(nodo_actual.derecha)
    #metodo publico
    def obtener_balance(self, nodo_actual):
        if not nodo_actual:
            return 0
        return self._obtener_altura(nodo_actual.izquierda) - self._obtener_altura(nodo_actual.derecha)

    def buscar_padre(self, valor):
        return self._buscar_padre_recursivo(self.raiz, None, valor)

    def _buscar_padre_recursivo(self, nodo_actual, padre_actual, valor):
        if not nodo_actual:
            return None

        if valor[12] < nodo_actual.valor[12]:
            return self._buscar_padre_recursivo(nodo_actual.izquierda, nodo_actual, valor)
        elif valor[12] > nodo_actual.valor[12]:
            return self._buscar_padre_recursivo(nodo_actual.derecha, nodo_actual, valor)
        else:
            # Nodo encontrado, devuelve su padre
            return padre_actual
    
    def buscar_abuelo(self, valor):
        padre = self.buscar_padre(valor)
        if padre:
            return self.buscar_padre(padre.valor)
        else:
            return None

    def buscar_tio(self, valor):
        padre = self.buscar_padre(valor)
        if padre:
            if valor[12] < padre.valor[12]:
                tio = padre.derecha
            else:
                tio = padre.izquierda
            return tio
        else:
            return None
        
    def printLevel(self, root, level, string=""):

        # Caja base
        if root is None:
            return False
    
        if level == 1:
            self.string += root.valor[2] + " "
            print(root.valor[2], end=' ')
    
            # devuelve verdadero si al menos un nodo está presente en un nivel dado
            return True
    
        left = self.printLevel(root.izquierda, level - 1)
        right = self.printLevel(root.derecha, level - 1)
    
        return left or right

# Función para imprimir el recorrido del orden de nivel de un árbol binario dado
    def levelOrderTraversal(self, root):
    
        # comienza desde el nivel 1 — hasta la altura del árbol
        level = 1
    
        # ejecutar hasta que printLevel() devuelva falso
        while self.printLevel(root, level):
            level = level + 1