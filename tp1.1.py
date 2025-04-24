import random
import sys
import matplotlib.pyplot as plt
import math
import numpy as np


def calcular_estadisticos_esperados():
    promedio_esperado=0
    desvio_esperado=0
    varianza_esperada=0
    frec_rel_esperada = 0
    promedio_esperado = 18
    for i in range(37):
        varianza_esperada = varianza_esperada + ((i-promedio_esperado)**2) 
    varianza_esperada = varianza_esperada/(37)
    desvio_esperado = math.sqrt(varianza_esperada)
    frec_rel_esperada = 1/37
    return promedio_esperado,varianza_esperada,desvio_esperado,frec_rel_esperada

def genera_graficos(promedios,varianzas,desvios,cant_tiradas,frecuencias,prom_esp,var_esp,desv_esp,frec_rel_esp,num_elegido):
    numero_jugada = list(range(1,cant_tiradas+1))
    promedios_esperados = [prom_esp for i in range(cant_tiradas)]
    frec_rel_esperadas = [frec_rel_esp for i in range(cant_tiradas)]
    varianzas_esperada = [var_esp for i in range(cant_tiradas)]
    desvios_esperados = [desv_esp for i in range(cant_tiradas)]

    ##fig,ax = plt.subplots(2, 2, figsize=(15, 8))
    plt.figure(figsize=(25,10))
    cant = 1
    for prom in promedios: 
        plt.plot(numero_jugada,prom,linestyle='-',label=f'Promedio corrida {cant}')
        cant += 1
    plt.plot(numero_jugada,promedios_esperados,linestyle='-.',label='Promedios esperados')
    plt.title('Promedio por jugada')
    plt.xlabel('Numero Jugada')
    plt.ylabel('Promedio')
    plt.legend()
    plt.show()
    
    cant = 1
    for frecu in frecuencias:
        plt.plot(numero_jugada,frecu,linestyle='-',label=f'Frecuencia del numero {num_elegido}')
        cant += 1
    plt.plot(numero_jugada,frec_rel_esperadas,linestyle='--',label=f'Frecuencia esperada')
    plt.title('Frecuencia por jugada')
    plt.xlabel('Numero Jugada')
    plt.ylabel('Frecuencia')
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    cant = 1
    for vari in varianzas:
        plt.plot(numero_jugada,vari,linestyle='-',label=f'Varianza corrida {cant}')
        cant += 1
    plt.plot(numero_jugada,varianzas_esperada,linestyle='--',label='Varianza esperada')
    plt.title('Varianza por jugada')
    plt.xlabel('Numero Jugada')
    plt.ylabel('Varianza')
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    cant = 1
    for des in desvios:
        plt.plot(numero_jugada,des,linestyle='-',label=f'Desvio corrida {cant}')
        cant += 1
    plt.plot(numero_jugada,desvios_esperados,linestyle='--',label='Desvios esperado')
    plt.title('Desvio por jugada')
    plt.xlabel('Numero Jugada')
    plt.ylabel('Desvio')
    plt.legend()
    plt.tight_layout()
    plt.show()


    


def main(cant_corridas, cant_tiradas, numero):
    promedios = []
    varianzas = []
    desvios = []
    frecuencias = []
    for i in range(cant_corridas):
        promedios_corrida = []
        varianzas_corrida = []
        desvios_corrida = []
        frecuencias_corrida = []
        res=[0 for k in range(cant_tiradas)] 
        for j in range(cant_tiradas):
            res[j] = random.randint(0,36) ## Resultado de la j-esima tirada
        cant_elegido = 0
        promedio_corrida = 0
        varianza_corrida = 0
        for j in range(cant_tiradas):
            if (res[j] == numero): cant_elegido += 1
            promedio_corrida = promedio_corrida + res[j]
            varianza_corrida = np.var(res[:j+1])
            desvio_corrida = math.sqrt(varianza_corrida)
            promedios_corrida.append(promedio_corrida/(j+1))
            varianzas_corrida.append(varianza_corrida)
            desvios_corrida.append(desvio_corrida)
            frecuencias_corrida.append(cant_elegido/(j+1))
        promedios.append(promedios_corrida)
        varianzas.append(varianzas_corrida)
        desvios.append(desvios_corrida)
        frecuencias.append(frecuencias_corrida)
    ## Despues de todas las corridas    
    genera_graficos(promedios,varianzas,desvios,cant_tiradas,frecuencias,
                    promedio_esperado,varianza_esperada,desvio_esperado,frec_esperada,numero)


##Ingreso de los parametros por consola
##python tp1.py -c XX -n YY -e ZZ
if (len(sys.argv)!=7 or sys.argv[1] != "-c" or sys.argv[3] != "-n" or sys.argv[5] != "-e"):
    print("Uso: python tp1.py -c <cant_corridas> -n <cant_tiradas> -e <num_elegido>")
    sys.exit(1)

cant_corridas = int(sys.argv[2])
cant_tiradas = int(sys.argv[4])
num_elegido = int(sys.argv[6])
promedio_esperado,varianza_esperada,desvio_esperado,frec_esperada = calcular_estadisticos_esperados()

main(cant_corridas,cant_tiradas,num_elegido)