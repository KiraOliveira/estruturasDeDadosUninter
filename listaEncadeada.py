
# Criado Classe para representar o Nodo (Cartão) - Contendo Número, Cor e Próximo
class Nodo:
    def __init__(self, numero, cor):
        self.numero = numero
        self.cor = cor
        self.proximo = None

# Criado Classe para gerenciar a Lista Encadeada
class ListaEncadeada:
    def __init__(self):
        self.head = None
        self.count_v = 1    # Inserido contador para cartões do tipo Verdes
        self.count_a = 201  # Inserido contador para cartões do tipo Amarelos

    # EXIGÊNCIA 2: Inserir o paciente cadastrado no final (para cartões Verdes)
    def inserirSemPrioridade(self, novo_nodo):
        if not self.head:
            self.head = novo_nodo
            return
        
        atual = self.head
        while atual.proximo:
            atual = atual.proximo
        atual.proximo = novo_nodo

    # EXIGÊNCIA 3: Inserir após todos os cartões do tipo 'A', mas antes dos cartões do tipo 'V'
    def inserirComPrioridade(self, novo_nodo):
        # Se a lista inicialmente estiver vazia ou o primeiro cartão for do tipo Verde, o Amarelo vira a "Head" ou seja mais urgente ou primeiro
        if not self.head or self.head.cor == 'V':
            novo_nodo.proximo = self.head
            self.head = novo_nodo
            return

        # Caso contrário então, percorrer até encontrar o último cartão do tipo 'A'
        atual = self.head
        while atual.proximo and atual.proximo.cor == 'A':
            atual = atual.proximo
        
        # Aqui ele vai inserir o novo cartão do tipo 'A' entre o último cartão do tipo 'A' e o primeiro cartão do tipo 'V' (ou final da lista)
        novo_nodo.proximo = atual.proximo
        atual.proximo = novo_nodo

    # EXIGÊNCIA 4: Coletar dados via teclado e decidir a inserção
    def inserir(self):
        cor = input("Informe por favor, a cor do cartão (A/V): ").strip().upper()
        
        if cor == 'V':
            novo = Nodo(self.count_v, 'V')
            self.count_v += 1
            if not self.head:
                self.head = novo
            else:
                self.inserirSemPrioridade(novo)
            print(f"Paciente V-{novo.numero} adicionado.")
            
        elif cor == 'A':
            novo = Nodo(self.count_a, 'A')
            self.count_a += 1
            if not self.head:
                self.head = novo
            else:
                self.inserirComPrioridade(novo)
            print(f"Paciente A-{novo.numero} adicionado.")
        else:
            print("Ops! Cor informada é inválida! Use 'A' para Amarelo ou 'V' para Verde. Tente novamente")

    # EXIGÊNCIA 5: Aqui vamos imprimir a fila
    def imprimirListaEspera(self):
        if not self.head:
            print("\n--- Fila vazia ---")
            return
        
        print("\n--- Lista de pacientes em espera ---")
        atual = self.head
        while atual:
            print(f"[{atual.cor} - {atual.numero}]", end=" -> ")
            atual = atual.proximo
        print("Fim")

    # EXIGÊNCIA 6: Aqui vamos iniciar o Atendimento (Remover o primeiro), neste caso será removido a cada vez que for solicitado
    def atenderPaciente(self):
        if not self.head:
            print("\nFila vazia! Não há pacientes aguardando para atender.")
            return
        
        atendido = self.head
        self.head = self.head.proximo
        print(f"\nChamando paciente para atendimento: Cartão {atendido.cor} número {atendido.numero}")

# EXIGÊNCIA 7: Aqui é criado o "Menu Principal"
def menu():
    hospital = ListaEncadeada()
    
    while True:
        print("\n--- MENU HOSPITAL ---")
        print("1 – Adicionar paciente a fila")
        print("2 – Mostrar lista de pacientes aguardando")
        print("3 – Chamar paciente para atendimento")
        print("4 – Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            hospital.inserir()
        elif opcao == '2':
            hospital.imprimirListaEspera()
        elif opcao == '3':
            hospital.atenderPaciente()
        elif opcao == '4':
            print("Encerrando o sistema...")
            break
        else:
            print("Ops! Opção inválida! Vamos tentar novamente?")

if __name__ == "__main__":
    menu()