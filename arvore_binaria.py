from no import No
import tkinter as tk
from tkinter import font, IntVar


class Arvore:

    def __init__(self, valor=None) -> None:

        self.raiz = None

    # Função pra adicionar um elemto na arvore

    def add(self, valor):

        # adicionar elemento em uma arvore vazia
        if self.raiz == None:
            self.raiz = No(valor)

        # adicionar elemento em uma arvore que não está vazia
        else:
            no = No(valor)
            raiz = self.raiz
            raiz = self.procurar_add(no.valor, raiz)

            if no.valor < raiz.valor:
                raiz.esquerda = no
            else:
                raiz.direita = no

        self.pecorrer_balancear()

    # procura o nó que será adicionado o novo elemento
    def procurar_add(self, valor, raiz=None):
        if raiz == None:
            raiz = self.raiz

        if valor < raiz.valor:

            if raiz.esquerda != None:

                raiz = self.procurar_add(valor, raiz.esquerda)
        else:
            if raiz.direita != None:
                raiz = self.procurar_add(valor, raiz.direita)

        return raiz

    def procurar(self, valor, raiz=None):

        if raiz == None:
            raiz = self.raiz

        if valor > raiz.valor:
            if raiz.direita != None:
                raiz = self.procurar(valor, raiz.direita)
        elif valor < raiz.valor:
            if raiz.esquerda != None:
                raiz = self.procurar(valor, raiz.esquerda)

        if valor == raiz.valor:
            return raiz

    # procura a sub-arvore para apagar ate encontrar o valor que quer apagar

    def remover(self, valor, raiz=None):

        if raiz == None:
            raiz = self.raiz

        if valor < raiz.valor:
            raiz.esquerda = self.remover(valor, raiz.esquerda)

        elif valor > raiz.valor:
            raiz.direita = self.remover(valor, raiz.direita)

        else:

            # Se o elemento for uma folha
            if raiz.esquerda == None and raiz.direita == None:
                if raiz == self.raiz:
                    self.raiz = None
                return None

            # Se o elemento tiver somente filho no lado esquerdo
            elif raiz.esquerda != None and raiz.direita == None:
                if raiz == self.raiz:
                    self.raiz = raiz.esquerda
                return raiz.esquerda

            # Se o elemento tiver somente filho no lado direito
            elif raiz.esquerda == None and raiz.direita != None:
                if raiz == self.raiz:
                    self.raiz = raiz.direita
                return raiz.direita

            # Se o elemento tiver dois filhos
            else:
                menor = self.menor(raiz.direita)
                raiz.valor = menor.valor
                raiz.direita = self.remover(menor.valor, raiz.direita)

        self.pecorrer_balancear()
        return raiz

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
            print('Em Ordem:', end=' ')
            raiz = self.raiz

        if raiz.esquerda != None:
            self.ordem(raiz.esquerda)

        print(raiz.valor, end=' ')

        if raiz.direita != None:
            self.ordem(raiz.direita)

    def pecorrer_balancear(self, raiz=None):

        if raiz == None:

            raiz = self.raiz

        if raiz.esquerda != None:
            self.pecorrer_balancear(raiz.esquerda)

        if raiz.direita != None:
            self.pecorrer_balancear(raiz.direita)

        self.balancear(raiz)

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

    def quantidade_no(self, raiz=None, cont=1):

        if raiz == None:
            raiz = self.raiz

        if raiz.esquerda != None:
            cont += 1
            cont = self.quantidade_no(raiz.esquerda, cont)

        if raiz.direita != None:
            cont += 1
            cont = self.quantidade_no(raiz.direita, cont)

        return cont

    def altura(self, raiz=None, cont_esquerda=0):

        if raiz == None:
            raiz = self.raiz

        if raiz.esquerda is None and raiz.direita is None:
            cont = 1
            return cont

        if raiz.esquerda is not None:

            cont = self.altura(raiz.esquerda) + 1
            cont_esquerda = cont

        if raiz.direita is not None:

            cont = self.altura(raiz.direita, cont_esquerda) + 1

        if cont_esquerda > cont:
            return cont_esquerda

        return cont

    def balancear(self, raiz):

        tamanho_esquerda = 0
        tamanho_direita = 0

        if raiz.esquerda != None:

            tamanho_esquerda = self.altura(raiz.esquerda)

        if raiz.direita != None:

            tamanho_direita = self.altura(raiz.direita)

        raiz.fator = tamanho_esquerda - tamanho_direita

        if raiz.fator > 1 and raiz.esquerda.fator == 1:

            self.rotacao_direita(raiz)

        elif raiz.fator < -1 and raiz.direita.fator == -1:

            self.rotacao_esquerda(raiz)

        elif raiz.fator == 2 and (raiz.esquerda.fator == -1 or raiz.esquerda.fator == 0):

            self.rotacao_esquerda(raiz.esquerda)
            self.rotacao_direita(raiz)

        elif raiz.fator == -2 and (raiz.direita.fator == 1 or raiz.direita.fator == 0):

            self.rotacao_direita(raiz.direita)
            self.rotacao_esquerda(raiz)

    def rotacao_direita(self, raiz):

        raiz.valor, raiz.esquerda.valor = raiz.esquerda.valor, raiz.valor
        esquerda_raiz = raiz.esquerda
        raiz.esquerda = raiz.esquerda.esquerda
        direita = raiz.direita
        raiz.direita = esquerda_raiz
        raiz.direita.esquerda = raiz.direita.direita
        raiz.direita.direita = direita

    def rotacao_esquerda(self, raiz):

        raiz.valor, raiz.direita.valor = raiz.direita.valor, raiz.valor
        direita_raiz = raiz.direita
        raiz.direita = raiz.direita.direita
        esquerda = raiz.esquerda
        raiz.esquerda = direita_raiz
        raiz.esquerda.direita = raiz.esquerda.esquerda
        raiz.esquerda.esquerda = esquerda

    def exibir_arvore(self, raiz=None):

        def adicionar_arvore():

            valor = int(caixa_entrada.get())
            self.add(valor)
            canvas.delete("all")
            raiz = self.raiz
            desenhar_no(raiz, 680, 50, 200, 100)
            informacoes()

        def remover_arvore():

            valor = int(caixa_entrada.get())
            self.remover(valor)
            canvas.delete("all")
            raiz = self.raiz
            desenhar_no(raiz, 680, 50, 200, 100)
            informacoes()

        def informacoes():

            altura_var.set(self.altura())
            maior_var.set(self.maior().valor)
            menor_var.set(self.menor().valor)
            quantidade_var.set(self.quantidade_no())

        def mostrar_no():

            valor = int(caixa_entrada.get())
            no_buscado = self.procurar(valor)
            canvas.delete("all")
            raiz = self.raiz
            desenhar_no(raiz, 680, 50, 200, 100, no_buscado)
            informacoes()

        # Função auxiliar para desenhar os nós da árvore

        def desenhar_no(no, x, y, dx, dy, no_buscado=None):

            raio = 18
            cor = "#f2f2f2"
            cor_texto = "black"

            if no is not None:
                espessura_borda = 2
                if no_buscado == no:
                    cor = "#ff4A4a"
                    cor_texto = "#f2f2f2"
                canvas.create_oval(x - raio, y - raio, x + raio,
                                   y + raio, fill=cor, width=espessura_borda)
                canvas.create_text(x, y, text=(str(no.valor)),
                                   font='bold', fill=cor_texto)

                if no.esquerda:
                    canvas.create_line(x, y + raio, x - dx,
                                       y + dy - raio, width=2)
                    desenhar_no(no.esquerda, x - dx, y +
                                dy, dx/2, dy, no_buscado)
                if no.direita:
                    canvas.create_line(x, y + raio, x + dx,
                                       y + dy - raio, width=2)
                    desenhar_no(no.direita, x + dx, y +
                                dy, dx/2, dy, no_buscado)

        raiz = self.raiz

        janela = tk.Tk()
        janela.configure(bg='#0a0c0d')
        font_grande = font.Font(size=16)
        font_padrao = font.Font(size=15)

        altura_var = IntVar()
        maior_var = IntVar()
        menor_var = IntVar()
        quantidade_var = IntVar()
        altura_var.set(0)
        maior_var.set(0)
        menor_var.set(0)
        quantidade_var.set(0)

        titulo = tk.Label(janela, text='Árvore binária de busca balanceada',
                          font=font_grande, fg='#f2f2f2', bg='#3d3334').pack(side='top')

        # Criação da janela e do canvas
        canvas = tk.Canvas(janela, width=1350, height=800, bg="#348e91")
        canvas.pack(side='top')

        # Desenhar a árvore
        desenhar_no(raiz, 680, 50, 200, 100)

        tex1 = tk.Label(janela, text='Altura da árvore: ', bg="#348e91",
                        font=font_padrao, fg="#f2f2f2").place(x=10, y=50)
        altura = tk.Label(janela, textvariable=altura_var, bg="#348e91",
                          font=font_padrao, fg="#f2f2f2").place(x=160, y=50)
        tex2 = tk.Label(janela, text='Maior valor: ', bg="#348e91",
                        font=font_padrao, fg="#f2f2f2").place(x=10, y=80)
        maior = tk.Label(janela, textvariable=maior_var, bg="#348e91",
                         font=font_padrao, fg="#f2f2f2").place(x=130, y=80)
        tex3 = tk.Label(janela, text='Menor valor: ', bg="#348e91",
                        font=font_padrao, fg="#f2f2f2").place(x=10, y=110)
        menor = tk.Label(janela, textvariable=menor_var, bg="#348e91",
                         font=font_padrao, fg="#f2f2f2").place(x=130, y=110)
        tex4 = tk.Label(janela, text='Quantidade de nó(s): ', bg="#348e91",
                        font=font_padrao, fg="#f2f2f2").place(x=10, y=140)
        quantidade = tk.Label(janela, textvariable=quantidade_var, bg="#348e91",
                              font=font_padrao, fg="#f2f2f2").place(x=205, y=140)

        procurar = tk.Button(janela, text='Procurar', command=mostrar_no,
                             bg='blue', fg='#f2f2f2', font=('Arial', 13), width=8).place(x=550, y=625)
        remover = tk.Button(janela, text='Remover', command=remover_arvore,
                            bg='red', fg='#f2f2f2', font=('Arial', 13), width=8).place(x=638, y=625)
        adicionar = tk.Button(janela, text='Adicionar', command=adicionar_arvore,
                              bg='#1c5052', fg='#f2f2f2', font=('Arial', 13)).place(x=724, y=625)
        caixa_entrada = tk.Entry(janela, bg='#f2f2f2', font=(
            'Arial', 16), justify='center', width=21)
        caixa_entrada.place(x=550, y=590)

    # Executar a janela
        janela.mainloop()
