import os
from sobreForms.classCajasDraw import CajasDraw

# mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
# El Menu de todo Esto mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
from classXindeX import XindeX 


""" 
        
listaEstructura=[
            ["c:0", "c:1","c:2","c:3"], 
            ["c:4", ["c:5",'c:6',"c:7"]], 
            ["c:A", ["f:B",'c:C'],"c:D"], 
            ["c:8", "c:9",[['c:10', ['c:52']] ,'c:11']],
            ["c:V", "c:X",'c:Y','c:Z']
        ]
listaEstructura=[
            ["c:0", ["f:1","f:2"],"c:3"], 
            ["c:4", ["c:5",'f:6'],"c:7"], 
            ["c:8", "c:9",'c:10','c:11']
        ]
"""
listaEstructura=[
            [["c:0","c:x"], [["f:3", "f:A"],"c:4"],["f:5", 'f:9']], 
            ["c:1", "c:6", 'c:M'], 
            ["c:2", "c:7", 'c:8']
        ]

def prueba():
    print(".gitignore")


# iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii  objeto  iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii
# iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii  ppal    iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii
CAJAS = CajasDraw(listaEstructura=listaEstructura)    
# iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii          iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii
# iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii          iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii


# _____________________________
# Practica de la funcion de Actualizar de MirrowStrucTK
def update_valor():
    global CAJAS
    keyStrucTK = input(f'Intro keyStrucTK a buscar... ')
    new_valor  = input(f'Intro Nuevo Valor a Introducir... ')

    if CAJAS:
        bActualizado=CAJAS.updtVal(keyStrucTK, new_valor)
        if bActualizado==True:
            print(CAJAS)
        else:
            print(f'Eleemnto {keyStrucTK} No Encontrado. :(')
    pass
# _____________________________
# Practica de funcion recursiva....OK
def base_recursiva():
    global CAJAS
    if CAJAS:
        CAJAS.BaseRCSV(CAJAS.listaEstructura)
# _____________________________
def imprimir_PrinteX():
    global CAJAS
    if CAJAS:
        """ 
        Funcion de StrucTK que imprime el diccionario generado en getData_RCSV()        """        
        CAJAS.imprDiccDATA()      
    pass
# _____________________________
def get_data_recursiva():
    global CAJAS
    if CAJAS:
        diccDataStrucTK=CAJAS.getData_RCSV(item=CAJAS.listaEstructura)
        print(diccDataStrucTK)
    pass

# _____________________________
def obtener_valor():
    global CAJAS
    if CAJAS:
        keyStrcTK = input(f'Intro (keyStrcTK) o (indice) para Obtener su valor... ')
        valor_obtenido=CAJAS.getValue(keyStrcTK)
        print(f'\nValor obtenido: {valor_obtenido}')
    pass
# _____________________________
def iniciar_valores_caja():
    global CAJAS
    if CAJAS:
        CAJAS.iniValues()        
        print('\nlistaValues Inicializada :) ')
        input('Pulsa tecla para mostrar menu.... ')
    pass

# ==============================================================================================
# ==============================================================================================
# ==============================================================================================
#  M E N U   I N I C I O 
def main():
    print('\n B I E N V E N I N D O   A   C A J A S  ')
    # CAJAS = load_CAJA()

    # 1- INSTANCIO EL OBJETO XINDEX_____________________________________________________________
    The_X_Men = XindeX()
    # 2- CREO LOS MENUS Y SUS FUNCIONES ASOCIADAS ______________________________________________
    The_X_Men.addX(titulo='MenuPpal',  padre=None, ipadre=None,  
                    fraseHead="| - M A I N    O V E R   C A J A S  - "  , 
                    lst_items=[ ("Base Recursiva" , None),("Sobre Valores" , None),("Impresion" , None)] )
    The_X_Men.addX(     titulo='Sub_Cajas', padre='MenuPpal', ipadre="Base Recursiva" , lst_items=[("Ver Base Recursiva",base_recursiva)])  
    The_X_Men.addX(     titulo='Sub_Valores'  , padre='MenuPpal', ipadre="Sobre Valores" , lst_items=[("Inicia Values",iniciar_valores_caja) , ("obtener Value", obtener_valor) , ("Obtener Datos Recursivos", get_data_recursiva) , ('Actualiza Valor', update_valor)])
    The_X_Men.addX(     titulo='Sub_Impresion'  , padre='MenuPpal', ipadre="Impresion" , lst_items=[("PrinteX",imprimir_PrinteX)])
    # 3- LLAMO A MYSTYCA PARA VISUALIZAR EL MENU _______________________________________________
    retorno = The_X_Men.Mystyca(titulo='MenuPpal', configurado=True, execFunc=True, tipo_marcador='a', execAll=False, Loop=True , padX=50)
    # 4- SALE DEL MENU__________________________________________________________________________
    print(f"::: T H E   E N D  en MAIN() ::: {retorno if retorno else 'Configurado sin retorno'} ")

# ==============================================================================================
# ==============================================================================================
# ==============================================================================================
if __name__ == "__main__":
    # ---- Limpio la terminal 
    os.system('cls') 
    print('\nI N I C I O')   
    # ---- Empezamos!!
    main() 
