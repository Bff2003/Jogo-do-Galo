import os
from random import randint

def ValorAleatorio(min = 1, max = 10): 
    return randint(min, max)

def LimparTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

class JogoDoGalo:

    # 1 = X; 2 = O
    jogo = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

    vitorias = [0, 0]

    ultimo_jogador = None

    def __init__(self) -> None:
        pass

    def menu(self): # mostra o menu
        LimparTerminal()
        print("-- MENU --")
        print("1- Um Jogador")
        print("2- Dois Jogadores")
        print("---------------")
        while True:
            opcao = input("Opção: ")
            if(opcao.isdigit() and (opcao == "1" or opcao == "2")):
                break
        LimparTerminal()
        return opcao

    def desenha(self): # desenha jogo na tela
        LimparTerminal()
        escrever = ""
        for linha in self.jogo:
            i = 1
            for casa in linha:
                if(casa == 1):
                    escrever = escrever + "X"
                elif(casa == 2):
                    escrever = escrever + "O"
                else :
                    escrever = escrever + " "
                if(i == 1 or i == 2):
                    escrever = escrever + "|"
                i = i + 1
            print(escrever)
            print("-----")
            escrever = ""
    
    def reiniciarJogo(self):
        for l in range(len(self.jogo)):
            for c in range(len(self.jogo[0])):
                self.jogo[l][c] = 0

    def contaPreenchidos(self): # conta todas as casa ja preenchidas
        i = 0
        for linha in self.jogo:
            for casa in linha:
                if(casa != 0):
                    i = i + 1
        return i

    def valida(self): # valida casos todos
        try:
            # posicao 00
            self.verificaJogador(self.jogo[0][0], self.jogo[0][1], self.jogo[0][2])
            self.verificaJogador(self.jogo[0][0], self.jogo[1][0], self.jogo[2][0])
            self.verificaJogador(self.jogo[0][0], self.jogo[1][1], self.jogo[2][2])
            # posicao 02
            self.verificaJogador(self.jogo[0][2], self.jogo[1][2], self.jogo[2][2])
            self.verificaJogador(self.jogo[0][2], self.jogo[1][1], self.jogo[2][0])
            # posicao 20
            self.verificaJogador(self.jogo[2][0], self.jogo[2][1], self.jogo[2][2])

            #Meio 
            self.verificaJogador(self.jogo[1][0], self.jogo[1][1], self.jogo[1][2])
            self.verificaJogador(self.jogo[0][1], self.jogo[1][1], self.jogo[2][1])

            #verifica se ninguem ganhou
            if(self.contaPreenchidos() == 9):
                raise Exception(0)
        except Exception as e:
            if(str(e).isdigit()):
                return str(e)
        pass

    def verificaJogador(self, posicao1, posicao2, posicao3): # retorna jogador que ganhou
        # if(posicao1 == posicao2 and posicao2 == posicao3 or posicao4 == posicao5 and posicao5 == posicao6):
        if(posicao1 == posicao2 and posicao2 == posicao3 and posicao1 != 0):
            raise Exception(str(posicao1))
        else:
            return 0
    
    def jogadorJoga(self, jogador):
        while True:
            try: 
                l = int(input("Linha: ")) - 1
                c = int(input("Coluna: ")) - 1
            except ValueError:
                LimparTerminal()
                self.desenha()
                continue
            if(l > 2 or l < 0 or c > 2 or c < 0):
                LimparTerminal()
                self.desenha()
                continue
            if(self.jogo[l][c] == 0):
                self.jogo[l][c] = jogador
                break
            else:
                LimparTerminal()
                self.desenha()
    
    def computadorJoga(self):
        linha = ValorAleatorio(0, 2)
        coluna = ValorAleatorio(0, 2)
        while(self.jogo[linha][coluna] != 0):
            linha = ValorAleatorio(0, 2)
            coluna = ValorAleatorio(0, 2)
        self.jogo[linha][coluna] = 2

    def Jogo(self):
        opcao = self.menu()
        i = 0
        while True:
            i = i + 1

            if( self.ultimo_jogador == None or self.ultimo_jogador == 2):
                i = 1
            elif(self.ultimo_jogador == 1):
                i = 2

            self.desenha() # desenha 
            valida = self.valida()
            if(valida == "1"):
                return 1
            elif(valida == "2"):
                return 2
            elif(valida == "0"):
                return 0

            # faz jogador ou computador jogar
            if(i % 2 == 1):
                print("Jogador 1")
                self.jogadorJoga(1)
                self.ultimo_jogador = 1
            elif(i % 2 == 0):
                if(opcao == "1"):
                    print("Computador Joga")
                    self.computadorJoga()
                    self.ultimo_jogador = 2
                elif(opcao == "2"):
                    print("Jogador 2")
                    self.jogadorJoga(2)
                    self.ultimo_jogador = 2
    def iniciarJogo(self):
        while True:
            self.reiniciarJogo()
            jogo = self.Jogo()
            if(jogo == 1):
                print("O jogador 1 Ganhou!!")
                self.vitorias[0] = self.vitorias[0] + 1
            elif(jogo == 2):
                print("O jogador 2 Ganhou!!")
                self.vitorias[1] = self.vitorias[1] + 1
            elif(jogo == 0):
                print("Nenhum jogador ganhou!")

            while True:
                resposta = input("Pretende Jogar denovo [1- Sim; 2-Não]? ")
                if(resposta.isdigit() and resposta == "1"):
                    self.ultimo_jogador = 2
                    # self.Jogo()
                    break
                elif(resposta.isdigit() and resposta == "2"):
                    print("Vitorias do Jogador 1: " + str(self.vitorias[0]))
                    print("Vitorias do Jogador 2: " + str( self.vitorias[1]))
                    return None
            

jogo = JogoDoGalo()
jogo.iniciarJogo()