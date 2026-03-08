
# EXIGÊNCIA 2: Criado Classe para representar o Nodo da Lista Encadeada- Contendo Sigla, Nome Estado e Próximo
class Nodo:
    def __init__(self, sigla, nomeEstado):
        self.sigla = sigla
        self.nomeEstado = nomeEstado
        self.proximo = None

# EXIGÊNCIA 1 e 3: Criado Classe para a Tabela Hash
class TabelaHash:
    def __init__(self):
        # EXIGÊNCIA 1: Aqui irá criar a tabela com 10 posições iniciando vazias (None)
        self.tabela = [None] * 10

    # Criar Função para limpar o Hash (Reseta a tabela) -- Não foi solicitado, porém acredito que ficou legal com essa função
    def limparTabela(self):
        self.tabela = [None] * 10
        print("\n>>> Tabela Hash limpa com sucesso! Todos os dados foram removidos. <<<")

    # EXIGÊNCIA 5: Função Hash com regra ASCII e exceção para DF
    def funcaoHash(self, sigla):
        if sigla.upper() == "DF":
            return 7 # Regra de superstição para o DF
        
        # Aqui irá obter os valores ASCII conforme a tabela fornecida no documento da atividade
        char1_ascii = ord(sigla[0].upper())
        char2_ascii = ord(sigla[1].upper())
        
        # Aqui irá aplicar a Fórmula: (CHAR1 + CHAR2) MOD 10
        return (char1_ascii + char2_ascii) % 10

    # EXIGÊNCIA 3: Inserção sempre no INÍCIO da lista encadeada
    def inserir(self, sigla, nomeEstado):
        posicao = self.funcaoHash(sigla)
        novo_nodo = Nodo(sigla.upper(), nomeEstado)
        
        # Aqui o novo nodo irá apontar para o que já estava em "HEAD" daquela posição
        novo_nodo.proximo = self.tabela[posicao]
        # A tabela passa a apontar para o novo nodo (novo Head)
        self.tabela[posicao] = novo_nodo

    # EXIGÊNCIA 4: Aqui irá ser realizado a impressão formatada da tabela hash separada por posição
    def imprimirTabela(self):
        print("\n" + "="*40)
        print("      ESTADO ATUAL DA TABELA HASH")
        print("="*40)
        for i in range(10):
            print(f"Posição {i}: ", end="")
            atual = self.tabela[i]
            if atual is None:
                print("None")
            else:
                while atual:
                    print(f"[{atual.sigla}]", end=" -> ")
                    atual = atual.proximo
                print("None")
        print("="*40)

# --- MENU E INTERAÇÃO VIA TECLADO---

def menu():
    hashSistema = TabelaHash()
    
    while True:
        print("\n--- MENU PARA GERENCIANDO DO HASH ---")
        print("1 - Exibir Tabela Atual") #Aqui não exibido antes da inserção
        print("2 - Exibir os 26 Estados + DF") # Aqui irá iniciar a inserção automaticamente
        print("3 - Exibir o Estado Fictício") # Aqui vamos inserir um estado fictício via teclado
        print("4 - Limpar Tabela") # Resetar a tabela
        print("5 - Sair")
        
        # Aqui será escolhido via teclado uma das opções acima
        opcao = input("Escolha uma das opções: ")

        if opcao == '1':
            # EXIGÊNCIA DE SAÍDA 1: Aqui vamos exibir a Tabela vazia
            hashSistema.imprimirTabela()

        elif opcao == '2':
            # EXIGÊNCIA 6: Aqui vamos exisbir os 26 estados + DF adicionados
            estadosBrasil = [
                ("AC", "Acre"), ("AL", "Alagoas"), ("AP", "Amapá"), ("AM", "Amazonas"),
                ("BA", "Bahia"), ("CE", "Ceará"), ("DF", "Distrito Federal"), ("ES", "Espírito Santo"),
                ("GO", "Goiás"), ("MA", "Maranhão"), ("MT", "Mato Grosso"), ("MS", "Mato Grosso do Sul"),
                ("MG", "Minas Gerais"), ("PA", "Pará"), ("PB", "Paraíba"), ("PR", "Paraná"),
                ("PE", "Pernambuco"), ("PI", "Piauí"), ("RJ", "Rio de Janeiro"), ("RN", "Rio Grande do Norte"),
                ("RS", "Rio Grande do Sul"), ("RO", "Rondônia"), ("RR", "Roraima"), ("SC", "Santa Catarina"),
                ("SP", "São Paulo"), ("SE", "Sergipe"), ("TO", "Tocantins")
            ]
            for s, n in estadosBrasil:
                hashSistema.inserir(s, n)
            #Aqui será exibido a mensagem sobre os estados terem sido adicionados com sucesso    
            print("\nParabéns! Estados brasileiros inseridos com sucesso!")
            hashSistema.imprimirTabela()

        elif opcao == '3':
            # EXIGÊNCIA 7: Aqui será solicitado o estado fictício via teclado
            nome = input("Por favor, informe o nome do estado completo: ")
            # Lógica utilizada: Primeira letra do nome e primeira do último sobrenome, para que fique parecido com o estado real
            partes = nome.split()
            sigla = partes[0][0] + partes[-1][0] if len(partes) >= 2 else partes[0][0] + "X"
            hashSistema.inserir(sigla, nome)
            print(f"\nEstado '{nome}' ({sigla.upper()}) inserido!")
            # EXIGÊNCIA DE SAÍDA 3: Tabela completa com todos os estados reais + o estado fictício
            hashSistema.imprimirTabela()

        elif opcao == '4':
            hashSistema.limparTabela()

        elif opcao == '5':
            print("Encerrando programa...")
            break
        else:
            print("Ops! Opção inválida! Vamos tentar novamente?")

if __name__ == "__main__":
    menu()    