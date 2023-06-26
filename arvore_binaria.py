from no import No
from time import sleep
import tkinter as tk

class Arvore:

    def __init__(self, valor=None) -> None:

        self.raiz = No(valor)


    def add(self, valor):

        if self.raiz.valor == None:
            self.raiz.valor = valor
        else:
            no = No(valor)
            comp_raiz = self.raiz
            comp_raiz = self.recursion_add(no.valor, comp_raiz)

            if no.valor < comp_raiz.valor:
                comp_raiz.esquerda = no
            else:
                comp_raiz.direita = no

    def recursion_add(self, valor, comp_raiz=None):

        if comp_raiz == None:
            comp_raiz = self.raiz

        if valor < comp_raiz.valor:

            if comp_raiz.esquerda != None:

                comp_raiz = self.recursion_add(valor, comp_raiz.esquerda)
        else:
            if comp_raiz.direita != None:
                comp_raiz = self.recursion_add(valor, comp_raiz.direita)

        return comp_raiz

    def pre_ordem(self, raiz=None):
        if raiz == None:
            print('Pre-Ordem: ', end="")
            raiz = self.raiz

        print(raiz.valor, end=" ")

        if raiz.esquerda != None:
            self.pre_ordem(raiz.esquerda)

        if raiz.direita != None:
            self.pre_ordem(raiz.direita)

    def ordem(self, raiz=None):

        if raiz == None:

            print('Em Ordem:', end=" ")
            raiz = self.raiz

        if raiz.esquerda == None:

            print(raiz.valor, end=" ")

        if raiz.esquerda != None:

            self.ordem(raiz.esquerda)

        if raiz.esquerda != None:

            print(raiz.valor, end=" ")

        if raiz.direita != None:

            self.ordem(raiz.direita)

    def pos_ordem(self, raiz=None):

        if raiz == None:
            print('Pos-Ordem:', end=' ')
            raiz = self.raiz

        if (raiz.esquerda == None and raiz.direita == None):
            print(raiz.valor, end=' ')

        if raiz.esquerda != None:
            self.pos_ordem(raiz.esquerda)

        if raiz.direita != None:
            self.pos_ordem(raiz.direita)

        if raiz.direita != None and raiz.esquerda != None:
            print(raiz.valor, end=' ')
        elif raiz.esquerda == None and raiz.direita != None:
            print(raiz.valor, end=' ')
        if raiz.esquerda != None and raiz.direita == None:
            print(raiz.valor, end=' ')

    def remover(self,valor,raiz = None):

        if raiz == None:
            raiz = self.raiz 

        if raiz == None:
            return raiz
        
        if valor < raiz.valor:
            raiz.esquerda =  self.remover(valor,raiz.esquerda)
        elif valor > raiz.valor:
            raiz.direita = self.remover(valor,raiz.direita)
        else:
            
            if raiz.esquerda == None and raiz.direita == None:
                return None
            elif raiz.esquerda != None and raiz.direita == None:
                return raiz.esquerda
            elif raiz.esquerda == None and raiz.direita != None:
                return raiz.direita
            else:
                menor = self.menor(raiz.direita)
                raiz.valor = menor.valor
                raiz.direita = self.remover(menor.valor,raiz.direita)
        return raiz
            




    def menor(self, raiz=None):
        if raiz == None:
            raiz = self.raiz

        if raiz.esquerda != None:
            return self.menor(raiz.esquerda)

        if raiz.esquerda == None:
            return raiz

    def maior(self, raiz=None):
        if raiz == None:
            raiz = self.raiz

        if raiz.direita != None:
            return self.maior(raiz.direita)

        if raiz.direita == None:
            return raiz


    def folhas(self, raiz = None,folhas = None):

        if raiz == None:
            raiz = self.raiz
            folhas = list()

        
        if raiz.esquerda is None and raiz.direita is None:
            folhas.append(raiz)

        if raiz.esquerda != None:
            self.folhas(raiz.esquerda,folhas)

        if raiz.direita != None:
            self.folhas(raiz.direita,folhas)
            return folhas

    def tamanho(self,folhas = None):
        
        if folhas is None:
            folhas = self.folhas()


            
        tamanho  = 0
        if folhas != None:
            for folha in folhas:
                cont = 0 
                raiz = self.raiz
                while raiz != folha:
                    
                    if folha.valor >= raiz.valor:
                        raiz = raiz.direita
                    elif folha.valor < raiz.valor:
                        raiz = raiz.esquerda 
                    cont += 1
                if cont > tamanho:
                    tamanho = cont
        
        return tamanho



    def exibir_arvore(self,raiz = None):

        def adicionar_arvore():

            valor = int(caixa_entrada.get())
            self.add(valor)
            canvas.delete("all")
            raiz = self.raiz
            desenhar_no(raiz, 400, 50, 200, 100)
            informações()
        def remover_arvore():

            valor = int(caixa_entrada.get())
            print(valor)
            self.remover(valor)
            canvas.delete("all")
            raiz = self.raiz
            desenhar_no(raiz, 400, 50, 200, 100)
            informações()


        def informações():
            label1 = tk.Label(janela, text='Árvore binária de busca',font=16).pack()
            altura = tk.Label(janela, text=f'A altura da Arvore: {str(self.tamanho())}',font=14).pack()
            maior = tk.Label(janela,text=f'Maior valor da Arvore: {str(self.maior().valor)}',font = 14).pack()
            menor = tk.Label(janela,text=f'Menor valor da Arvore: {str(self.menor().valor)}',font = 14 ).pack()




        # Função auxiliar para desenhar os nós da árvore
        
        def desenhar_no(no, x, y, dx, dy):
            raio = 20
            cor = "white"
            if no is not None:
                canvas.create_oval(x - raio, y - raio, x + raio, y + raio, fill=cor)
                canvas.create_text(x, y, text=str(no.valor))
                if no.esquerda:
                    canvas.create_line(x, y + raio, x - dx, y + dy - raio)
                    desenhar_no(no.esquerda, x - dx, y + dy, dx/2, dy)
                if no.direita:
                    canvas.create_line(x, y + raio, x + dx, y + dy - raio)
                    desenhar_no(no.direita, x + dx, y + dy, dx/2, dy)
            return


        if raiz is None:
            raiz = self.raiz
        janela = tk.Tk()
        caixa_entrada = tk.Entry(janela)
        caixa_entrada.pack()
        adicionar = tk.Button(janela,text='Adcionar',command=adicionar_arvore).pack()
        remover = tk.Button(janela,text='Remover',command=remover_arvore).pack()



        canvas = tk.Canvas(janela, width=800, height=600)
        canvas.pack()
        # Criação da janela e do canvas


        informações()

    # Desenhar a árvore
        desenhar_no(raiz, 400, 50, 200, 100)


    # Executar a janela
        janela.mainloop()