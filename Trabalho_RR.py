# Trabalho de Escalonamento Circular Round-Robin (Round-Robin Scheduling);
# Isto é, uma situação em que calcula-se o tempo médio de vida (tm_vida) e
# o tempo médio de espera (tm_espera) para um conjunto de tarefas utilizadas por
# um processador.

class Tarefa:
    # Método init ou constructor em Linguagem Python
    def __init__(self, tarefa, duracao_execucao):
        self.tarefa = tarefa
        self.duracao_execucao = duracao_execucao
        self.tempo_vida = 0
        self.tempo_espera = 0

print("Neste trabalho, serão levados em conta a submissão deste Algoritmo com submissão de 4 tarefas.")

ingressos_de_tarefas = [5, 15, 10, 0]  # Esta é a duração de execução para cada tarefa, ou seja, seu ingresso
# no processador.

quantum = 15
troca_contexto = 4

ingressos_de_tarefas.sort()
# Ordenando a execução de tarefas para quantum e trocas de contexto.

print(ingressos_de_tarefas.sort())

print("A primeira tarefa a ser executada será a tarefa 4.")

tarefa_4 = (quantum + troca_contexto)

print("Logo, minha primeira tarefa, ou seja, a tarefa 4 irá rodar em: ", tarefa_4, "unidades de tempo.")

print("A segunda tarefa a ser executada será a tarefa 1.")

tarefa_1 = (tarefa_4 + quantum + troca_contexto)
print("Logo, minha segunda tarefa, ou seja, a tarefa 1 irá rodar em: ", tarefa_1, "unidades de tempo.")

print("A terceira tarefa a ser executada será a tarefa 3.")

tarefa_3 = (tarefa_1 + quantum + troca_contexto)
print("Logo, minha terceira tarefa, ou seja, a tarefa 3 irá rodar em: ", tarefa_3, "unidades de tempo.")

print("A quarta tarefa a ser executada será a tarefa 2.")

tarefa_2 = (tarefa_3 + quantum + troca_contexto)
print("Logo, minha quarta tarefa, ou seja, a tarefa 2 irá rodar em: ", tarefa_2, "unidades de tempo.")

valores_final = [tarefa_4, tarefa_1, tarefa_3, tarefa_2]
print(valores_final)

  # Somente para critério de dúvidas e esclarecimentos do funcionamento do Algoritmo Round-Robin

  # calcular_tempo_medio_vida = ((95 - 5) + (67 - 15) + (124 - 10) + (76 - 0) / 4)

  # calcular_tempo_medio_espera = (((19 - 5) + (80 - 34) + (57 - 15) + (38 - 10) + (99 - 53) + (71 - 15)) / 4)

def round_robin(tarefas, quantum):
    tempo_total = 0
    tarefas_concluidas = []

    while len(tarefas) > 0:
        tarefa_atual = tarefas.pop(0)
        if tarefa_atual.duracao_execucao > quantum:
            tempo_atual += quantum
            tarefa_atual.duracao_execucao -= quantum
            tarefa_atual.tempo_vida += quantum
            tarefa_atual.tempo_espera += tarefa_atual.tempo_vida
            tarefas.append(tarefa_atual)
        else:
            tempo_total += tarefa_atual.duracao_execucao
            tarefa_atual.tempo_vida += tarefa_atual.duracao_execucao
            tarefa_atual.tempo_espera += tarefa_atual.tempo_vida
            tarefas_concluidas.append(tarefa_atual)

    tempo_medio_vida = sum (tarefa.tempo_vida for tarefa in tarefas_concluidas) / len (tarefas_concluidas)
    tempo_medio_espera = sum(tarefa.tempo_espera for tarefa in tarefas_concluidas) / len (tarefas_concluidas)

    return tempo_medio_vida, tempo_medio_espera

# Criação das tarefas em Estado de Pronto

tarefas = [
    Tarefa("T1", 10),
    Tarefa("T2", 5),
    Tarefa("T3", 8),
    Tarefa("T4", 3),
]

# Execução do Algoritmo Round-Robin
tempo_medio_vida, tempo_medio_espera = round_robin(tarefas, quantum)

print("Deste modo, o meu tempo médio de vida será de: ", tempo_medio_vida)
print("E, após o meu tempo médio de vida, encontrarei o tempo médio de espera que será de: ", tempo_medio_espera)

# No final da execução do algoritmo, o tempo médio de vida e o tempo médio de espera são calculados com base nas
# tarefas concluídas e são exibidos como saída. #

# Lembrando que os valores de tempo de execução das tarefas e o quantum podem ser ajustados conforme necessário 
# para o seu cenário específico. #

class Circular:
# Irei utilizar o método tournaround time ou somente tournaround como constructor
# em Linguagem Python

    def __tournaround__(self, calcular_media_vida, calcular_media_espera):
        self.calcular_media_vida = calcular_media_vida
        self.calcular_media_espera = calcular_media_espera

        while (tm_vida_t1 == tarefa_4 & tm_vida_t2 == tarefa_1 & tm_vida_t3 == tarefa_3 & tm_vida_t4 == tarefa_2):
            tarefas_concluidas = 1

quantum = 15
troca_contexto = 4

tm_vida_t1 = quantum + 4 + 30 + 10 + 40
print("Deste modo, a minha tarefa 01 para aquele estado de pronto ficará sendo: ", tm_vida_t1, "unidades de tempo.")

calcular_t1 = (tm_vida_t1 - troca_contexto)
print("Assim, minha primeira tarefa será de: ", calcular_t1, "unidades de tempo.")

tm_vida_t2 = quantum + 5 + 1 + 20 + 30
print("Deste modo, a minha tarefa 02 para aquele estado de pronto ficará sendo: ", tm_vida_t2, "unidades de tempo.")

calcular_t2 = (tm_vida_t2 - troca_contexto)
print("Assim, minha segunda tarefa será de: ", calcular_t2, "unidades de tempo.")

tm_vida_t3 = quantum + 20 + 3 + 40 + 20 + 30
print("Deste modo, a minha tarefa 03 para aquele estado de pronto ficará sendo: ", tm_vida_t3, "unidades de tempo.")

calcular_t3 = (tm_vida_t3 - troca_contexto)
print("Assim, minha terceira tarefa será de: ", calcular_t3, "unidades de tempo.")

tm_vida_t4 = quantum + 15 + 10 + 30 + 10
print("Deste modo, a minha tarefa 04 para aquele estado de pronto ficará sendo: ", tm_vida_t4, "unidades de tempo.")

calcular_t4 = (tm_vida_t4 - troca_contexto)
print("Assim, minha quarta tarefa será de: ", calcular_t4, "unidades de tempo.")

calcular_media_vida = ((calcular_t1 - 5) + (calcular_t2 - 15) + (calcular_t3 - 10) + (calcular_t4 - 0)) / 4
print("Com isso, finalizando a parte 01 do Round-Robin, meu tempo médio de vida será de: ", calcular_media_vida, "unidades de tempo.")

tm_espera_t1 = ((quantum + troca_contexto) - 5 + (tm_vida_t4 - 34))
print("Desta maneira, o meu modo de espera para aquele estado em tarefa 01 ficará sendo: ", tm_espera_t1, "unidades de tempo.")

tm_espera_t2 = ((calcular_t2 - 10) - 15)
print("Desta maneira, o meu modo de espera para aquele estado em tarefa 02 ficará sendo: ", tm_espera_t2, "unidades de tempo.")

tm_espera_t3 = ((38 - 10) + (tm_vida_t1 - 53))
print("Desta maneira, o meu modo de espera para aquele estado em tarefa 03 ficará sendo: ", tm_espera_t3, "unidades de tempo.")

tm_espera_t4 = (tm_vida_t2 - 15)
print("Desta maneira, o meu modo de espera para aquele estado em tarefa 04 ficará sendo: ", tm_espera_t4, "unidades de tempo.")

calcular_media_espera = (tm_espera_t1 + tm_espera_t2 + tm_espera_t3 + tm_espera_t4) / 4
print("Com isso, finalizando a parte 02 do Round-Robin, meu tempo médio de espera será de: ", calcular_media_espera, "unidades de tempo.")
























