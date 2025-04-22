import random
import sys
import matplotlib.pyplot as plt
import math


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

def genera_graficos(res,promedios,varianzas,desvios,cant_tiradas,frecuencias,prom_esp,var_esp,desv_esp,frec_rel_esp,num_elegido):
    numero_jugada = list(range(1,len(promedios)+1))
    promedios_esperados = [promedio_esperado for i in range(len(promedios))]
    frec_rel_esperadas = [frec_rel_esp for i in range(len(frecuencias))]
    frec_num_elegido = [frecuencias[i][num_elegido] for i in range(len(frecuencias))]
    varianzas_esperada = [varianza_esperada for i in range(len(varianzas))]
    desvios_esperados = [desvio_esperado for i in range(len(desvios))]

    fig,ax = plt.subplots(2, 2, figsize=(15, 8))
    ax[0, 0].plot(numero_jugada,promedios,linestyle='-',label='Promedios')
    ax[0, 0].plot(numero_jugada,promedios_esperados,linestyle='-.',label='Promedios esperados')
    ax[0, 0].set_title('Promedio por jugada')
    ax[0, 0].set_xlabel('Numero Jugada')
    ax[0, 0].set_ylabel('Promedio')
    ax[0, 0].legend()
    
    ax[0, 1].plot(numero_jugada,frec_num_elegido,linestyle='-',label=f'Frecuencia del numero {num_elegido}')
    ax[0, 1].plot(numero_jugada,frec_rel_esperadas,linestyle='--',label=f'Frecuencia esperada')
    ax[0, 1].set_title('Frecuencia por jugada')
    ax[0, 1].set_xlabel('Numero Jugada')
    ax[0, 1].set_ylabel('Frecuencia')
    ax[0, 1].legend()
    
    ax[1, 0].plot(numero_jugada,varianzas,linestyle='-',label='Varianzas')
    ax[1, 0].plot(numero_jugada,varianzas_esperada,linestyle='--',label='Varianza esperada')
    ax[1, 0].set_title('Varianza por jugada')
    ax[1, 0].set_xlabel('Numero Jugada')
    ax[1, 0].set_ylabel('Varianza')
    ax[1, 0].legend()
    
    ax[1, 1].plot(numero_jugada,desvios,linestyle='-',label='Desvio')
    ax[1, 1].plot(numero_jugada,desvios_esperados,linestyle='--',label='Desvios esperado')
    ax[1, 1].set_title('Desvio por jugada')
    ax[1, 1].set_xlabel('Numero Jugada')
    ax[1, 1].set_ylabel('Desvio')
    ax[1, 1].legend()
    
    plt.tight_layout()
    plt.show()


    


def main(cant_corridas, cant_tiradas, numero):
    promedios = []
    varianzas = []
    desvios = []
    frecuencias = []
    for i in range(cant_corridas):
        res=[0 for k in range(cant_tiradas)] 
        for j in range(cant_tiradas):
            res[j] = random.randint(0,36) ## Resultado de la j-esima tirada
        frec_abs_corrida = [0 for k in range(37)]
        promedio_corrida = 0
        for j in range(cant_tiradas):
            frec_abs_corrida[res[j]] += 1
            promedio_corrida = promedio_corrida + res[j]
        promedio_corrida /= cant_tiradas
        varianza_corrida = 0
        for j in range(cant_tiradas):
            varianza_corrida = varianza_corrida + ((res[j] - promedio_corrida)**2)
        varianza_corrida /= cant_tiradas
        desvio_corrida = math.sqrt(varianza_corrida)
        print(f"Resultados de la corrida {i}: {res}")
        print(f"Promedio de la corrida {i}: {promedio_corrida}")
        print(f"Varianza de la corrida {i}: {varianza_corrida}")
        print(f"Desvio de la corrida {i}: {desvio_corrida}")
        frec_rel_corrida = [0 for x in range(37)]
        for num in range(37):
            frec_rel_corrida[num] = frec_abs_corrida[num]/cant_tiradas
            print(f"Frecuencia del numero {num}: -Absoluta {frec_abs_corrida[num]} -Relativa {frec_rel_corrida[num]}")
        print("\n")
        ## Guardar resultados de la i-esima corrida
        promedios.append(promedio_corrida)
        varianzas.append(varianza_corrida)
        desvios.append(desvio_corrida)
        frecuencias.append(frec_rel_corrida)

    ## Despues de todas las corridas    
    genera_graficos(res,promedios,varianzas,desvios,cant_tiradas,frecuencias,
                    promedio_esperado,varianza_esperada,desvio_esperado,frec_esperada,numero)


##Ingreso de los parametros por consola
##python tp1.py -c XX -n YY -e ZZ
if (len(sys.argv)!=7 or sys.argv[1] != "-c" or sys.argv[3] != "-n" or sys.argv[5] != "-e"):
    print("Uso: python tp1.py -c <cant_tiradas> -n <cant_corridas> -e <num_elegido>")
    sys.exit(1)

cant_tiradas = int(sys.argv[2])
cant_corridas = int(sys.argv[4])
num_elegido = int(sys.argv[6])
promedio_esperado,varianza_esperada,desvio_esperado,frec_esperada = calcular_estadisticos_esperados()

main(cant_corridas,cant_tiradas,num_elegido)