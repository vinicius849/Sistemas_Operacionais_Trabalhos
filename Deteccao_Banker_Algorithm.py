# Trabalho avaliativo de Sistemas Operacionais, com foco no assunto dado em sala de aula
# sobre DEADLOCK, isto é, uma situação em que um processo aguarda por um recurso que nunca
# estará disponível ou um evento que não ocorrerá. É como se cada processo estivesse esperando
# que o utro liberasse o recurso alocado, estabelecendo uma condição conhecida por espera circular,
# caracterizando uma situação de Deadlock; existindo muitas vezes em Sistemas Multiprogramáveis.

# Exemplo do Algoritmo do Banqueiro simplifica bem a implementação deste algoritmo, e de como detectar
# o deadlock em Sistemas Operacionais.

class BankerAlgorithm:
    # Método init ou constructor em Linguagem Python
    def __init__(self, num_processos, num_recursos):
        self.num_processos = num_processos
        self.num_recursos = num_recursos
        self.max_claim = [[0] * num_recursos for _ in range(num_processos)]
        self.allocated = [[0] * num_recursos for _ in range(num_processos)]
        self.available = [0] * num_recursos

def set_max_claim(self, processos, recursos):
    self.max_claim[processos] = recursos

def set_allocated(self, processos, recursos):
    self.allocated[processos] = recursos

def set_available(self, recursos):
    self.available = recursos

def deteccao_deadlock(self):
    work = self.available[:]
    finish = [False] * self.num_processos
    need = [self.max_claim[i][j] - self.allocated[i][j] for j in range(self.num_recursos) for i in range(self.num_processos)]
    deadlock_ocorrencia = False

    while True:
        found = False
        for i in range(self.num_processos):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(self.num_recursos)):
                work = [work[j] + self.allocated[i][j] for j in range(self.num_recursos)]
                finish[i] = True
                found = True

        if not found:
            break

    if not all(finish):
        deadlock_ocorrencia = True

    return deadlock_ocorrencia

# Exemplo de uso para um exemplo do PDF de Recursos Existentes, onde E = (4 2 3 1), sendo E[i][j]
# o vetor de recursos existentes e sendo A[i][j] o vetor de recursos disponíveis.
# E == A e vice-versa;
# 4 dvdrw, 2 plotters, 3 impressoras e 1 blu-ray;

if __name__ == '__main__':
    banker = BankerAlgorithm(num_processos = 3, num_recursos = 4)

# Considerando na situação-problema uma mariz 3x4 no Algoritmo do Banqueiro.

# Definindo as máximas demandas para os processos, 3 no caso do Banqueiro.
# Ou seja, definindo quais processos irão entrar em deadlock, irão rodar.

banker.set_max_claim = (0,[2, 2, 2, 0])
banker.set_max_claim = (1,[4, 2, 2, 1])
banker.set_max_claim = (2,[4, 2, 3, 1])

# Definindo os recursos alocados atualmente para cada processo, 4 no caso do Banqueiro.
# Ou seja, definimos aqui as requisições para a Matriz Corrente.

print("Com isso, caso não haja nenhum processo nestas situações, o Algoritmo termina.")

banker.set_allocated = (0,[2, 1, 0, 0])
banker.set_allocated = (1,[2, 2, 2, 0])
banker.set_allocated = (2,[4, 2, 2, 1])

print("Com isso, defini-se com o uso do Algoritmo do Banqueiro, que termina caso seja dada a condição de SIM ou NÃO para Deadlock.")

# Disponibilidade de recursos
banker.set_available = (0,[2, 1, 0, 0])

if deteccao_deadlock(0):
    print("Deadlock detectado.")
else:
    print("Nenhum Deadlock detectado.")

print("Em seguida, definimos as máximas demandas, os recursos alocados e a disponibilidade dos recursos. Por fim, chamamos o método.")
print("Fim do Algoritmo.")

a1 = [2, 1, 0, 0]   # Sendo considerado aqui Recursos Disponíveis em A, ou melhor, como se fosse P4.
a2 = [2, 2, 2, 0]
a3 = [4, 2, 2, 1]
a4 = [4, 2, 3, 1]   # Prova ou demonstração do fim de Recursos Disponíveis em A.

print("De acordo com o sisteminha, o Processo 3 irá rodar, P3 roda com: ", a2, "rodar em A.")
print("De acordo com o sisteminha, o Processo 2 irá rodar, P2 roda com: ", a3, "rodar em A.")
print("De acordo com o sisteminha, o Processo 1 irá rodar, P1 roda com: ", a4, "e, caso ele execute, porém em P1 não há deadlock.")







