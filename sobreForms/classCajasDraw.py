# Para hacer copias profundas de una lista
import copy



""" 
listaEstructura=[
    ['c:0', 'c:1','c:2','c:3'], 
    ['c:4', 'c:5','c:6','c:7'], 
    ['c:8', 'c:9','c:10','c:11']
    ]

listaEstructura=[
    ['c:0', ['f:1'] , 'c:3' ] , 
    ['c:4', ['f:3','f:4'],'c:7'], 
    ['c:8', 'c:9','c:10','c:11']
    ]

 """




class CajasDraw(): 
    """ 
    >>> Ejemplo Uso:
    >>> listaEstructura=[
            ["c:0", ["f:0","f:1","f:3"]], 
            ["c:1", "c:3"], 
            ["c:2"]
        ]
    SttK=CajasDraw(listaEstructura=listaEstructura)
    """
    def __init__(self, listaEstructura):

        self.listaEstructura = listaEstructura        
        """ >>> Lista PPAL de la Clase. 
        >>> Contiene la Estructura de Entrada. 
        >>> De esta variable salen todas las demás.
        """
        self.cuentaListasInternas=0
        """ >>> Contador dedicado a las funciones recursivas. 
        >>> Contadores de Pasos 
        """
        self.numFilas=len(self.listaEstructura)
        """ >>> Numero de elementos del Nivel 2
        """
        self.numListasInternas=self.level(self.listaEstructura)
        """ >>> Profundidad maxima de ListaEstructura.
        """
        self.listaValues=copy.deepcopy(self.listaEstructura)
        """ >>> Copia profunda de ListaEstructura.  import copy
        """        
        self.listaKeys=self.getListaPlana_ByEstructura(lista=self.listaEstructura)
        """ >>> Lista de str. Lista PLANA de los datos de ListaEstructura. 
        Es la Base de todos los elementos que hay en la ListaEstructura 
        """
        # ______________________
        self.dictEstructura={key:self.getPosicion_ByObj(lista=listaEstructura, objBuscado=str(key)) for key in self.listaKeys}        
        """ >>> Diccionario de key(listaKeys) pejm 'c:3' , value(posicion en formato lista, pejem [1,0,0,3]) 
        """
        self.lst_valid_char=['c', 'f']
        """ >>> lista de los caracteres válidos para la aplicacion enfileitor. 
        ...Para otro tipo de uso hay que actualizar este valor con getters and setters
        """
        self.dicc_data_rcsv=self.getData_RCSV(self.listaEstructura)
        """ >>> DICCIONARIO DE DATOS TOTAL de self.listaEstructura.
        Ya se puede sacar todo de aquí......please update me!! 
        """
        # print(f'\nDiccionario (key-posicion)\n{self.dictEstructura}')        
        # ______________________
        # Validacion de la estructura(c o f ; repetidos):
        if self.validaEstructura()==False: 
            self.listaEstructura=None
            self.numFilas=None
            self.cuentaListasInternas=None
            self.numListasInternas=None
            self.listaValues=None
            self.listaKeys=None
            self.dictEstructura=None
            print("Estructura No Registrada :( ")
        else:
            print("Estructura Registrada :) ")
        pass

        self.cuentaRcsvBase=0
        """ >>> Contador de Pasos. Atributo Dedicado a self.BaseRCSV(). Funcion Recursiva. No hace nada, es el ppio. 
        """
        self.cuentaRcsvImpr=0
        """ >>> Contador de Pasos. Atributo Dedicado a self.get_lst_dataStr(). Funcion Recursiva. 
        >>> self.get_lst_dataStr() da una lista de str. En deshuso. Cambiada por self.imprDiccDATA()
        """
        self.cuentaRcsvDicc=0
        """ >>> Contador de Pasos. Atributo Dedicado a self.getData_RCSV(). Funcion Recursiva.  
        """

    # ____________________
    # PARA IMPRIMIR TODOS LOS DATOS DE LA CLASE....FALTA COMPLETAR.
    def __str__(self):
        tit=f'\n{'*'*30} IMPRIMIR DATOS CajasDraw {'*'*30}\n'
        uno=f'Numero de Items: {self.numFilas}\n'
        dos=f'Estructura: {self.listaEstructura}\n\n'
        tres=f'listaKeys: {self.listaKeys}\n'
        siete=f'listaValues: {self.listaValues}\n'
        cuatro=f'Diccionario (key):(posicionEstruct): \n{self.dictEstructura}\n'
        cinco=f'Numero de listas internas: {self.cuentaListasInternas}\n'
        seis=''
        for i, item in enumerate(self.listaEstructura):
            seis=seis+(f'item {i}: {item}\n')
        fin=f'{'='*90}'
        return tit+uno+dos+tres+siete+cuatro+cinco+seis+fin

    # ============================================================================= >
    # BASE RECURSIVA(No usada).... L o   p r i m e r o ,   f u e   e l   V E R B O 
    # ============================================================================= >
    def BaseRCSV(self, item, level=None):        
        """ 
        Base para Recorrer Toda la Lista Recursivamente!!!!!
        identifica el tipo list o str, key de listaKeys
        Aquí tengo un contador global (self.cuentaRcsvBase) dedicado y un (level) de ejemplo
        [level] indica el nivel de profundidad desde la lista inicial(item)
        Ademas, de gratis ;) busco la posicion del item y la muestro, para ver las causalidades.
        """
        if level==None: level=0        
        self.cuentaRcsvBase+=1
        if isinstance(item, list):
            level+=1
            for subList in item:

                self.BaseRCSV(subList, level)

        else:
            polposition=self.getPosicion_ByObj(str(item))
            print(f'Item: {item} - Level: {level} - Contador: {self.cuentaRcsvBase}- Posicion: {polposition}')
    
    # ____________________
    # GETTER DE self.lst_valid_char
    def get_lst_valid_char(self):
        return self.lst_valid_char
    # ____________________
    # SETTER DE self.lst_valid_char
    def set_lst_valid_char(self, char=''):
        if char=='' or char==None: return None
        if char in self.lst_valid_char: return self.lst_valid_char
        self.lst_valid_char.append(char)
        return self.lst_valid_char
    
    # ____________________
    # PARA OBTENER LISTAVALUES, O BIEN EL ORIGINAL DE LA CLASE O BIEN UNA COPIA PROFUNDA.
    def get_VALStrcTK(self, byCopy=True):
        """ 
        Devuelve una copia o el original, por defecto una copia """
        if byCopy:
            return copy.deepcopy(self.listaValues)
        else:
            return self.listaValues

    # ____________________
    # OBTIENE UNA FILA DE LISTAESTRUCTURA
    def getFila(self, indexFila):
        """ 
        Def: obtiene una sola item, pasada como argumento.
        """
        if 0<=indexFila<len(self.listaEstructura):
            return self.listaEstructura[indexFila]
        pass

    # Rcsv.... CON RETORNO DE LISTA. CREA UNA LISTA DE LISTAS DE STR PARA IMPRIMIR (sustituir X imprDiccData)
    # ============================================================================= >
    def get_lst_dataStr(self, item, level=None, retorno=None):        
        """ 
        Recorre la lista Recursivamente y devuelve una lista con los datos 
        del diccionario generado en getData_RCSV
        ....en teoria, esto falta y de momento doy estos datos
        """
        if level==None: level=0        
        if retorno==None: retorno=[]        
        self.cuentaRcsvImpr+=1
        if isinstance(item, list):
            level+=1
            for subList in item:
                # -----Llamada Recursiva
                self.get_lst_dataStr(subList, level, retorno)
        else:
            polposition=self.getPosicion_ByObj(str(item))
            if polposition:
                FilaR=polposition[0]
                ColumnR=polposition[1]
                # coord1=polposition[0]
                data = str(item) , str(level), str(self.cuentaRcsvImpr), str(polposition), str(FilaR), str(ColumnR)
                # print(f'Item: {item} - Level: {level} - Contador: {self.cuentaRcsvImpr}- Posicion: {polposition}')
                retorno.append(data)

        # Pongo la fila de Titulos justo al final para que cuando retorne haga pop() y los recupere
        # listaCabecera='Item:' , 'Level:' , 'Contador:' ,'Posicion:', 'FilaRel', 'ColRel'
        # retorno.append(listaCabecera)

        return retorno

    # ===================================
    # LISTA DE DICCIONARIO DE DATOS...sobre la Base Recursiva
    def getData_RCSV(self, item, level=None, retorno=None):        
        """ 
        -Usa la Base para Recorrer Toda la Lista Recursivamente!!!!!
        [item]: Es la Lista a Recorrer Recursivamente. self.listaEstructura, pero puede ser cualquiera.
        [level]: NO INTRODUCIR EN LA LLAMADA A LA FUNCION. Sirve para calcular el nivel de profundidad, 
        [retorno]: NO INTRODUCIR EN LA LLAMADA A LA FUNCION. Lista de diccionarios (k):keyStrucTK  (v):level, cuentaRecursiva, listaPosicion, 2 primeras cooordenadas, 2 últimas coordenadas, FilaAbsolua , Fila/Columna Relativa. 
        """
        # _____________________________
        # Inicializo los parametros de entrada. IMPORTANTE!!: No values en la llamada
        if level==None: 
            level=0        
            self.cuentaRcsvDicc=0
        if retorno==None: retorno=[]

        self.cuentaRcsvDicc+=1
        if isinstance(item, list):
            level+=1
            for subList in item:
                self.getData_RCSV(item=subList, level=level, retorno=retorno)
        else:
            # _____________________
            # Cojo Datos:
            polposition=self.getPosicion_ByObj(str(item))
            if not polposition: 
                return None
            coord1=polposition[0]
            coord2=polposition[1]
            # _____________________
            # Dos últimas coordenadas
            coord3=polposition[-2]
            coord4=polposition[-1]
            # _____________________
            # OBTIENE EL VALOR DEL ELEMENTO EN listaValues
            valor_item=self.getValue(datoBusca=str(item))
            # _____________________
            # Imprime los datos de las Vueltas que va Dando
            printitem = (f'Item: {item} - Level: {level} - Contador: {self.cuentaRcsvDicc}')
            print_posicion=(f'- Posicion: {polposition}')
            fila_columna=(f' - Fila Abs: {coord1} - coord2: {coord2} - pre-last: {coord3} - last: {coord4} - valor: {valor_item}')
            # print(printitem+print_posicion+fila_columna)
            # _____________________
            # Creo el diccionario con los datos recogidos
            # diccRetorno={str(item):[level, self.cuentaRcsvDicc, polposition, coord1, coord2, coord3, coord4, valor_item]}
            diccRetorno={str(item):[level, self.cuentaRcsvDicc, polposition, coord1, coord2, coord3, coord4, valor_item]}
            # _____________________
            # Añado el diccionoario a la lista retorno
            retorno.append(diccRetorno)

        return retorno

    # ===============================
    # Obtiene la POSICION de una keyStrucTK (objBuscado)
    def getPosicion_ByObj(self, objBuscado, lista=None, posicion=None):
        """ 
        Def: Devuelve una lista de posiciones haasta llegar al Objeto. Es la base de las busquedas de datos en listaEstructura
        [objBuscado]: una keyStucTK , pejempl "c:3"
        >>> lista=NO USAR EN LA LLAMADA. self.ListaEstrucutra es la lista Inicial. , 
        >>> [posicion]=NO USAR EN LA LLAMADA
        Retorno: lista de int. Pejem: [0,1,0] representa las posiciones en listaEstructura
        """
        if posicion is None:
            posicion = []                                   # Inicializar la posicion como una lista vacía
        if not lista: 
            lista=self.listaEstructura            
            """ >>> self.listaEstructura es la lista Inicial. 
            """
        for indice, elemento in enumerate(lista):
            # Agregar el índice actual a la posicion
            NewPosicion = posicion + [indice]

            if isinstance(elemento, list):
                # Llamar recursivamente si el elemento es otra lista
                resultado = self.getPosicion_ByObj(objBuscado=objBuscado, 
                                                    lista=elemento, 
                                                    posicion=NewPosicion)
                if resultado is not None:
                    return resultado                 
            elif elemento == objBuscado:
                return NewPosicion  # Devolver la posicion si se encontró el objBuscado

        return None  # Devolver None si no se encontró el objBuscado en esta lista

    # ===============================
    # OBTIENE UN ITEM DE LA LISTA POR LA POSICION
    def getItem_ByPosicion(self, lista, posicion):
        """ 
        >>> Def: Obtiene un item de la listaEstructura o su copia o una lista pasada como argumento.
        [lista]: Es una estructura de lista de listas cualquiera. en este caso self.listaEstructura
        [posicion]: es una lista de posicion en listaEstructura. es de la forma [0,0,1,2]
        Retorno: El Valor del item en esa poscion. None si no encuentra nada.
        """
        elemento = lista
        try:
            for indice in posicion:
                elemento = elemento[indice]  # Navega al siguiente nivel usando el índice
            return elemento
        except (IndexError, TypeError):
            return None

    # ===============================
    # GET LISTAKEYS
    def getListaPlana_ByEstructura(self, lista):
        """ 
        Def: Genera una lista de str con todos los elemntos de la lista pasada.
        Es una funcion recursiva: Se basa en que si elemento es str se añade a una lista de retorno,
        y si es lista, el resultado la tiene que añadir(extend), pero la recorre llamandose a si misma.

        Va recorriendo item por item encontrando elemento por elemento.
        """
        resultado = []  # Lista para almacenar todos los elementos

        for elemento in lista:
            if isinstance(elemento, list):
                # Llamada recursiva para aplanar la sublista y extender el resultado
                resultado.extend(self.getListaPlana_ByEstructura(elemento))
            else:
                # Añadir elementos que no son listas directamente a resultado
                resultado.append(elemento)

        return resultado

    # ===============================
    # RETORNA UN VALOR DE self.listaValues por una keyStrucTK o indice
    def getValue(self, datoBusca):
        """ 
        [datoBusca]: puede ser: (1-)Un keyStrucTK  (2-)Un indice leido de izquierda a derecha en listaKeys
        >>> Retorno: (1-)un VALOR de self.listaValues (2-)None si no Encuentra Nada.
        >>> ejemplo: (1-)getValue("c:3") (2-)getValue(5)
        """
        if isinstance(datoBusca, int):            
            if 0<=datoBusca<=len(self.listaKeys):
                keyStrtk=self.listaKeys[datoBusca]
                """>>> Si me pasa un indice, se busca 1º en self.listaKeys el nombre de la keyStrtk('c:x')
                """
                posicion_busca=self.dictEstructura.get([keyStrtk], None)
            else:
                return None
            pass
        elif isinstance(datoBusca, str):            
            if datoBusca in self.dictEstructura:
                posicion_busca=self.dictEstructura[datoBusca]
            else:
                return None
        # posicion_busca=self.dictEstructura.get([datoBusca], None)
        valor_busca=self.getItem_ByPosicion(lista=self.listaValues, posicion=posicion_busca)
        return valor_busca

    # ===============================
    # Obtiene el INDEX en self.listaKeys por una keyStrucTK
    def getIndex(self, keyStrcTK):
        """ 
        le paso un keyStrcTK y me dice su index en listaKeys
        """

    # ===============================
    # Devuelve el caracter de creacion de listaEstructura.
    def __get_caracter_StrcTK(self, keyStrcTK):
        """ 
        Obtiene la primera letra de una cadena pasada... Para Validaciones.        
        """
        listaKeyStrcTK=str(keyStrcTK).split(':')
        if listaKeyStrcTK:
            if len(listaKeyStrcTK)==2:
                if self.__valida_caracter_StrcTK()==True:
                    return listaKeyStrcTK[0]
                else:
                    return None
            else:
                return None
        else:
            return None


    # ===============================
    # NO LA USO, PERO LA DEJO POR PASION RECURSIVA BASADA EN BASE-RCSV
    def copiaListaRecursiva(self, lista):        
        if isinstance(lista, list):
            return [self.copiaListaRecursiva(sublista) for sublista in lista]
        else:
            return lista

    # ===============================
    # VALIDACION DE QUE LA ESTRUCTURA ES CORRECTA
    def validaEstructura(self):
        conjListaElementos=set(self.listaKeys)

        listaChanges=[]
        if len(self.listaKeys)!=len(conjListaElementos):
            print("Error, Elemento Repetido")
            return False
        else:
            for i,key in enumerate(self.listaKeys):
                filcol=key.split(sep=':')                
                if str(filcol[0]).lower()=='c' or str(filcol[0]).lower()=='f':
                    continue
                else:
                    listaChanges.append([i, key])
        pass
        if listaChanges:
            # print(listaChanges)
            print("\nErrores entrada en listaEstructura")
            for i in range(len(listaChanges)):
                posicion=self.getPosicion_ByObj(objBuscado=listaChanges[i][1])
                nivel=len(posicion)

                print(f'indice en listaKeys: {listaChanges[i][0]} - valor: {listaChanges[i][1]} => [valores válidos: c ó f]')
            return False

        return True

    # ===============================
    # CALCULA EL NIVEL DE PROFUNDIDAD EN LISTAESTRUCTURA.
    def level(self, lista):
        """ 
        Def: Funcion Recursiva, Que cuenta el numero de listas que hay en una lista pasada.
        No cuenta las listas con un solo elemento.
        """        
        resultado = []  # Lista para almacenar todos los elementos
        # self.cuentaListasInternas=0
        for elemento in lista:
            if isinstance(elemento, list):
                # if len(elemento)==1:    #No cuenta con las listas de un sólo elemento
                #     pass
                # else:
                self.cuentaListasInternas+=1

                self.level(elemento)
        
        return self.cuentaListasInternas
    
    # ===================================
    # IMPRIME DE DICCIONARIO DE DATOS CON FORMATO!!!! (RCSV)
    def imprDiccDATA(self):
        """ 
        Imprime por Terminal la lista de diccionarios generada con getData_RCSV, que recoje una serie de 
        datos sobre la estructura:
        >>> listaTitulosPrint=["Item", "Level", "Contador", "Posicion", "FilaR", "ColumR"...]
        ...Para añadir/quitar datos: (1-) Ponerlos/quitarlos del diccionario => self.getData_RCSV() 
        (2-)luego poner/quitar en la lista de titulos by hand => listaTitulosPrint = ["str1","str2",..."strX"].
        """

        listaTitulosPrint=["Item", "Level", "Contador", "Posicion", "coord1", "coord2", "pre-Last", "Last", "Valor"]        
        """ >>> Los titulos de la impresion en terminal
        """
        PrinteX(listaTitulo=listaTitulosPrint, 
                listaDatos=self.getData_RCSV(self.listaEstructura), 
                nombrePrinteX="Dicc Data")
        """ >>> Impresion en Terminal del diccionario retornado por self.getData_RCSV
        """

    # ==============================
    # INICIALIZA EL VALOR DE LISTAVALUES A NONE
    def iniValues(self):
        """ 
        Inicializa self.listValues a None
        """
        for keyStrucTK in self.listaKeys:
            self.updtVal(keyStrucTK, None)

    # ==============================
    # ACTUALIZACION DE UN VALOR DE LISTAVALUES
    def updtVal(self, keyStrucTK, nuevo_valor):
        """ 
        >>> Def: Llamada a la Actualizacion en listaValues, que es copia profunda de listaEstructura.
        -Obtengo la posicion de la key de la estructura de entrada(listaEstructura).
        -Con la posicion llamo a self.__updateItem() y cambia el valor en listaValues
        [keyStrucTK]: Es la clave inicial del dibujo de la lista de entrada.('c:0', 'c:3')
        [nuevo_valor]: el Valor a asignar en la posicion dada....depende del uso ;)....A JUGARRRR
        >>> Retorno: True si ha ido bien la actualización, False si no ha ido tan bien (falta try/except)
        """
        # 1ª Forma
        posicion_valor = self.getPosicion_ByObj(keyStrucTK)
        # 2ª Forma
        if keyStrucTK in self.listaKeys:
            posicion_valor = self.dictEstructura[keyStrucTK]
        else:
            return False

        if not posicion_valor: return False
        self.__updateItem(lista=self.listaValues, posicion=posicion_valor, nuevo_valor=nuevo_valor)
        if not self.listaValues: 
            return False
        return True
        
    # ===============================
    # ACTUALIZACION REAL DE UN VALOR DE LISTAVALUES....Llamada desde self.UpdtVal
    def __updateItem(self, lista, posicion, nuevo_valor):
        """ 
        >>> Def: Actualiza un valor en listaValues        
        [lista]: self.listaValues, que es una copia profunda de listaEstructura
        [posicion]: lista de posicion en la listaEstructura. sacado de self.getPosicion_ByObj()
        [nuevo_valor]: el Valor a asignar en la posicion dada.
        >>> Retorno: la lista de entrada modificada. self.listaValues.
        >>> esta linea "elemento = lista" y "elemento[posicion[-1]] = nuevo_valor"  es I.A. ;)
        """
        elemento = lista
        try:
            # Navegar hasta el penúltimo nivel
            for i in range(len(posicion) - 1):
                elemento = elemento[posicion[i]]
            # Cambiar el valor en la posición especificada
            elemento[posicion[-1]] = nuevo_valor
            return lista
        except (IndexError, TypeError):
            return None    
        
            print(f'item {i}: {item}')

    # ===============================
    # VALIDA QUE EL PRIMER CARACTER ES UNA 'c' o una 'f' 
    def __valida_caracter_StrcTK(self, caracterStrcTK):
        """ 
        Def: valida que el caracter pasado por parametro es uno de los seleccionados.
        Update: Para Otras aplicaciones se puede crear una lista de valores permitidos y consultar.
        """
        min_caracterStrcTK=caracterStrcTK.lower()
        return True if min_caracterStrcTK in self.lst_valid_char else False
    
    def getTitulo(self, keyStrucTK):
        pass
    # =============================================================
    # T H E   F A M I L Y 
    # UPDTE: Clase Hijo o Padre u objeto de la clase CajasDraw() ?
    # Depende de si consigo hacer el caracter general del comportamiento familiar como 
    # una clase en si misma que no dependa de los valores de CajasDraw
    # =============================================================
class Familia():
    """ UPDTE 2: DESPUES DE FAMILIA VIENE   C O M U N I D A D: 
    Un mundo donde se relacionan estructuras de datos entre si. """
    # =============================================================
    def __init__(self):

        self.lst_familias=[]
        """ >>> Listado Donde se añaden las familias inicialmente. 
        """
        self.dcc_familias={}
        """ >>> Una vez en lst_familias, pasan a diccionario_familias. 
        Un diccionario_familias es un dict cuya (key) es un miembro de la familia y 
        (value) es Una lista de (1)Un Objeto Generico de ese miembro y (2)Una descripcion(str)
        Para el caso enfileitor, el Objeto Generico que quiero guardar es el diccioario getData
        """


    def add_family(self, new_family, descripcion=''):        
        """ 
        >>> Def: Registra un str, como una Familia.
        Una familia es un conjunto de keyStrcTK unidos por un mismo nombre. 
        Se pueden devolver los objetos de la familia y actuar sólo sobre los objetos de la familia.        
        """
        if isinstance(new_family, list):
            try:
                for una_familia in new_family:
                    if not una_familia in self.lst_familias:
                        self.lst_familias.append(una_familia)
            except Exception as e:
                return False
        elif isinstance(new_family, str):
            try:
                if not new_family in self.lst_familias:
                    self.lst_familias.append(new_family)
                    return True
            except Exception as e:
                return False
        else:
            return False
        pass

    def del_family(self,strFamily=''):
        """ >>> Def: Elimina una familia de self.lista_familias
        """        
        if strFamily in self.lst_familias:
            self.lst_familias.pop(self.lst_familias.index(strFamily)) 
        else:
           return None
    
    # ________________________
    # OBTIENE EL INDEX  
    def get_index_familia(self, strFamily=''):
        """ >>> Def: Obtiene el indice en self.lst_familias de una familia.
        """
        for i, familia in enumerate(self.lst_familias):
            if str(familia).lower==str(strFamily).lower:
                return i
    
    # ________________________
    # 
    def upt_family(self, strFamily='', newFamily=''):
        """ >>> Def: Tengo que decidir si se actualiza el nombre de la familia o su contendido.
        Quiza cambiar el nombre de la familia no le veo tanta utilidad como a cambiar 
        un miembro o un grupo de miembros de la familia. si la quieres con otro nombre, la borras, la registras de nuevo y listo.
    
        """
        if strFamily in self.lst_familias:
            pass
        else:
            pass
        pass
    
    # ________________________
    # 
    def add_miembro(self, strFamily='', keyStrcTK=''):
        """ >>> Def: Añade un miembro a la familia. En TK add_miembro('familia_azules', 'c:X')
        """
        if strFamily in self.lst_familias:
            pass
        else:
            pass
        pass
    # ________________________
    # 
    def get_family(self, strFamily=''):
        """ >>> Def: 
        """
        pass
    
    # ________________________
    # 
    def view_family(self, strFamiy=''):
        """ >>> Def: 
        """
        if strFamily in self.lst_familias:
            pass
        else:
            pass
        pass
    
    # ________________________
    # 
    def view_families(self, strFamiy=''):
        """ >>> Def: 
        """
        if strFamily in self.lst_familias:
            pass
        else:
            pass
            
    # ________________________
    # 
    def search(self, strFamiy=''):
        """ >>> Def: 
        """
        if strFamily in self.lst_familias:
            pass
        else:
            pass
        pass
    def clone(self, strFamiy=''):
        """ >>> Def: devuelve una copia profunda de la lista/diccionario familia.
        """
        if strFamily in self.lst_familias:
            pass
        else:
            pass
        pass

# ==============================================================================
# C L A S S    P R I N T E X 
# ==============================================================================
# [rowformat] Admite una cadena con formato '{:<num1}{:<num2}{:<num3}{:<numN}' 
#                                           ' {:<30}  {:<15}  {:<25}'
# >>> signnifica: 
#     (':') Inicio de opciones de formato
#     ('<') alineado a la izquierda
#     (30) numero de espacios reservados para esa columna

# >>> print('{:<30}{:<15}{:<25}'.format("Nombre", "Edad", "Ocupación"))
# ==============================================================================
class PrinteX():
    """ 
    Quiero con esta clase dar formato a la impresion en terminal.
    >>> Updte: Seleccion de origen de los titulos:
    (1)en una lista de listas de str en la primera posicion?, ultima?(Xa pop()), (2)en una lista aparte, 
    (3)en una lista de diccionarios: el titulo puede estar en el (3-1)primer o (3-2)último registro?

    ...es mas, puedo elegir los datos que quiero sacar impresos???
    
    >>> Recibir una listaTitulos. Lista de str: 
    lista=['str1','str2', 'str3'...]

    >>> Recibir unA lista de DICCIONARIOS con datos que pasar a str.  key(en str) + values(en str)
    listaValues=list=[ {'key1':[0, 1, [0,1,0],2,1]}. '{ key2':[0, 0, [0,0],0,1] } ...]
    .... updte: que se pueda elegir si quieres la key o no la quieres.
    
    >>> Recibir una lista de lista de str de columnas-titulo: 
    listaValues=list=[  'key1':[0, 1, [0,1,0],2,1] , 'key2':[2, 1, [2,1,0],0,0] ...]


    Imprimir en funcion de la cantidad de titulos y formatear una salida standar.
    """
    def __init__(self, listaTitulo, listaDatos, esAjustado=True, nombrePrinteX=''):        
        """ 
        Espera ("Tit1", "Tit2", "Tit3") ,  ( (2, 3, 4) , (5, 6, 7) ,.... ) )
        """
        if self.validaEntrada(listaTitulo, listaDatos)==False: 
            print("Error de Entrada")
            return None
        
        
        self.listaTitulo=listaTitulo
        self.listaDatos=self.convierteToString(listaDatos)

        # self.strformato=self.getFormato(listaTitulo=self.listaTitulo, listaDatos=self.listaDatos, esAjustado=esAjustado)
        self.Impr(listaTitulo=self.listaTitulo, 
                listaDatos=self.listaDatos, 
                esAjustado=esAjustado, nombrePrinteX=nombrePrinteX)

    # ___________________________________
    # DEVUELVE EL FORMATO DINAMICAMENTE        
    def getFormato(self, listaTitulo=None, listaDatos=None, esAjustado=False):
        """ 
        Establece el formato según la listaTitulo pasada, que es una lista de str tipo:
        >>> listaTitulosPrint=["Item", "Level", "Contador", "Posicion", "FilaR", "ColumR"]        
        -Puede ser un formato ajustado = True al tamaño maximo de CADA COUMNA o ajustado = False, se ajuta al tamaño del maximo str de la lista
        
        -Se Basa en saber cuantas columnas quieres(listaTitulos) y formatear cada linea al formato generado dinamicamente.
        >>> strformato += "{:<" + str(num_espacios_columna) + "}"  pejem: {:<"+str(15)+"}"  
        """
        if listaTitulo==None: 
            listaTitulo=self.listaTitulo if self.listaTitulo else None
        if listaDatos==None: 
            listaDatos=self.listaDatos if self.listaDatos else None
        if not listaTitulo and not listaDatos: return None

        totalLen=0
        strformato=''
        if esAjustado==True:
            listaMaxCol = self.__maximoXColumna(listaTitulo=listaTitulo, listaDatos=listaDatos)
            """ lista con el numero maximo de caracteres por columna. 
            Devuelve tantos numeros como columnasa tiene tanto listaTitulo como listaDatos
            Con estos datos Genera el Formato ajustado a la columna. """
            listaMaxCol = [item+2 for item in listaMaxCol]
            for i in range (len(listaTitulo)):
                strformato += "{:<" + str(listaMaxCol[i]) + "}"
            
            # totalLen = sum(listaMaxCol) + len(listaMaxCol)
            totalLen = sum(listaMaxCol)
            # totalLen+=2
        else:
            maximo = self.__get_maximo(listaTitulo, listaDatos)        
            for i in range (len(listaTitulo)):
                strformato += "{:<" + str(maximo) + "}"

            totalLen = maximo

        # print(strformato)
        return strformato, totalLen
    # ___________________________________
    # VALIDA QUE SE PASA LO QUE SE TIENE QUE PASAR
    def validaEntrada(self, listaTitulo=None, listaDatos=None):
        """ 
        Valida que listaTitulo es una lista de str
        Valida que listaDatos es una lista de lista de str o diccionario de listas de str
        Devuelve True/False                                    
        """
        if listaTitulo==None: 
            listaTitulo=self.listaTitulo if self.listaTitulo else None
        if listaDatos==None: 
            listaDatos=self.listaDatos if self.listaDatos else None
        if not listaTitulo and not listaDatos: return None

        # primera Validacion
        if not isinstance(listaTitulo, list): return None
        if not isinstance(listaDatos, list): return None
        
        # Valida que todos los elementos de listaDatos son diccionario
        for iterador in listaDatos:
            if isinstance(iterador, list) or isinstance(iterador, tuple):
                pass
            elif isinstance(iterador, dict): 
                pass
            else:
                return False

        return True
    # ___________________________________
    # CONVIERTE UNA CADENA DE DATOS A STR
    def convierteToString(self, listaDatos):
        t_fila_str=[]
        
        for iterador in listaDatos:
            if isinstance(iterador, list) or isinstance(iterador, tuple):                
                t_fila_str.append(iterador)
        
            elif isinstance(iterador, dict): 
                t_fila = [(key, *item) for key, item in iterador.items()][0]          
                """ >>> Convierte en una lista con el primer elemento la key del diccionario """
                fila_str = [str(item) for item in t_fila]
                """ >>> Convierte a string cada elemento de la lista """
                t_fila_str.append(fila_str)
        
        return t_fila_str
    # ___________________________________
    # FUNCION DE IMPRIMIR
    def Impr(self, listaTitulo=None, listaDatos=None, esAjustado=True, nombrePrinteX=''):
        """ 
        Es la funcion que hay que llamar para IMPRIMIR en Terminal con Formato
        >>> [listaTitulo]: lista de str. listaTitulo=['Titcol1', 'Titcol2'", 'Titcol3',...]
        [listaDatos]: puede ser: (1) diccionario de str (2)
        [esAjustado]: bool, (True) Ajustado al tamaño maximo de cada columna; (False) Ajustado al tamaño del str mas grande
        [nombrePrinteX]: El nombre que va a salir de Titulo General.

        """

        # SE ESTABLECE LA CADENA STR DE FORMATO()
        self.strformato, sumaTotChar=self.getFormato(listaTitulo=listaTitulo, 
                                                     listaDatos=listaDatos, 
                                                     esAjustado=esAjustado)        
        # _________
        # Encabezado        
        print(f'{str(nombrePrinteX).upper()}')
        numChar=len(nombrePrinteX)+2
        print(f'{'='*numChar}')

        print(self.strformato.format(*listaTitulo))   
        if esAjustado==False:
            maximo = self.__get_maximo(listaTitulo=listaTitulo, listaDatos=listaDatos)        
            print("-"*len(listaTitulo)*(maximo))     #Linea de corte
        else:
            print("-"*(sumaTotChar))     #Linea de corte
            
        # _________
        # Datos
        for iterador in listaDatos:           
            print(self.__imprListaDatos(listaDatos=iterador))
        
        # _________
        # Fin
        if esAjustado==False:
            maximo = self.__get_maximo(listaTitulo=listaTitulo, listaDatos=listaDatos)        
            print("-"*len(listaTitulo)*(maximo))     #Linea de corte
        else:
            print("-"*(sumaTotChar))     #Linea de corte
    
    # ___________________________________
    # Imprime en consola con un formato alineado. 
    def __maximoXColumna(self, listaTitulo, listaDatos):
        """ 
        Retorna una lista con el máximo número de caracteres de cada columna.
        """
        # Inicia la lista `retorno` con las longitudes de cada título en `listaTitulo`
        retorno = [len(titulo) for titulo in listaTitulo]

        # Recorre las filas en `listaDatos` y compara con el máximo de cada columna
        for fila in listaDatos:
            for columna, item in enumerate(fila):
                retorno[columna] = max(retorno[columna], len(item))
        
        return retorno
    # ___________________________________
    # Imprime en consola con un formato alineado. 
    def __imprListaDatos(self, listaDatos=None):
        """ 
        Def: Imprime en la Terminal CON FORMATO
        -Calculando la longitud maxima para alinear correctamente.
        listaDatos tiene que ser un list de str
        """        
        if listaDatos==None: 
            listaDatos=self.listaDatos if self.listaDatos else None
        if not listaDatos: return None
        # TIENE QUE SER RECURSIVA PARA QUE COJA LAS LISTAS DE LISTAS 
        # tupleDatos=tuple(listaDatos)
        try:               
            return self.strformato.format(*listaDatos)
        except Exception as e:
            return f'Error: {e}'
            # print(f'Error: {e}')
            # return False
        else:
            return True
    # _________________________
    def __imprTitulos(self, listaTitulo=None):
        print(self.strformato.format(*listaTitulo))   
        print("-"*len(listaTitulo)*(self.maximo))     #Linea de corte
    # _________________________
    def __get_maximo(self,listaTitulo=None, listaDatos=None):
        if listaTitulo==None: 
            listaTitulo=self.listaTitulo if self.listaTitulo else None
        if listaDatos==None: 
            listaDatos=self.listaDatos if self.listaDatos else None
        if not listaTitulo and not listaDatos: return None
        # _____________________
        # Recojo datos de listaTitulo
        longTitulo=len(listaTitulo)
        max_len_titulo=self.__getMaxLenListaStr(listaTitulo)
        # _____________________
        # Recojo datos de listaDatos
        # Funcion Recursiva para Recorrer listas y devolver el str mas largo
        max_len_datos=self.__maxLenRcsv(listaDatos)
        # _____________________
        # CALCULO EL MAXIMO DE ESPACIO 
        maximo=max_len_titulo if max_len_titulo>=max_len_datos else max_len_datos 
        return maximo+1
    # ________________________
    def __maxLenRcsv(self, iterador):
        listaCadenas=self.___listRcsv(iterador=iterador)
        if listaCadenas:
            listaLen=[len(string) for string in listaCadenas]
            return max(listaLen)
    # ________________________
    # Calcula la maxima longitud de un titulo o un genero en la tupla de peliculas
    def __getMaxLenListaStr(self, iterador):
        listLargos=[len(item) for item in iterador]        
        # Como ya tengo una lista con solo números, puedo aplicar max()         
        max_longitud = max(listLargos)        
        return max_longitud
    # ________________________
    # Busqueda recursiva por un iterador lista
    def ___listRcsv(self, iterador, retorno=None):
        
        if retorno==None: retorno=[]        

        if isinstance(iterador, list) or isinstance(iterador, tuple):
            for subList in iterador:
                self.___listRcsv(subList, retorno)
        else:
            retorno.append(iterador)
        return retorno

        pass
# ==============================================================================
# F I N    C L A S S    P R I N T E X 
# ==============================================================================
