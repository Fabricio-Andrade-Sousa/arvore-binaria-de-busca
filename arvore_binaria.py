from no import No
import tkinter as tk
from tkinter import font, IntVar

class Arvore:

    def __init__(self, valor=None) -> None:

        self.raiz = None #No(valor)


    def add(self, valor):

        if self.raiz == None:
            self.raiz = No(valor)
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
            print('Em Ordem:', end=' ')
            raiz = self.raiz

        if raiz.esquerda != None:
            self.ordem(raiz.esquerda)
        
        print(raiz.valor,end=' ')

        if raiz.direita != None:
            self.ordem(raiz.direita)

    def pos_ordem(self, raiz=None):

        if raiz == None:
            # print('Pos-Ordem:', end=' ')
            raiz = self.raiz

        if raiz.esquerda != None:
            self.pos_ordem(raiz.esquerda)
        
        if raiz.direita != None:
            self.pos_ordem(raiz.direita)

        self.balancear(raiz)
        # print(raiz.valor,end=' ')
       

    def remover(self,valor,raiz = None):

        if raiz == None:
            raiz = self.raiz 
        
        if valor < raiz.valor:
            raiz.esquerda =  self.remover(valor,raiz.esquerda)
        elif valor > raiz.valor:
            raiz.direita = self.remover(valor,raiz.direita)
        else:
            
            if raiz.esquerda == None and raiz.direita == None:
                if raiz == self.raiz:
                    self.raiz = None
                return None
            
            elif raiz.esquerda != None and raiz.direita == None:
                if raiz == self.raiz:
                    self.raiz = raiz.esquerda
                return raiz.esquerda
            
            elif raiz.esquerda == None and raiz.direita != None:
                if raiz == self.raiz:
                    self.raiz = raiz.direita
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

        if folhas is None:
            folhas = list()

        if raiz != None:
            if raiz.esquerda is None and raiz.direita is None:
                folhas.append(raiz)

            if raiz.esquerda != None:
                self.folhas(raiz.esquerda,folhas)

            if raiz.direita != None:
                self.folhas(raiz.direita,folhas)

        
        return folhas

    def tamanho(self,folhas = None,raiz_balancear = None):
        
        if raiz_balancear != None:
            raiz = raiz_balancear
        if folhas is None:
            
            folhas = self.folhas(raiz_balancear)

            
        tamanho  = 0
        # print(folhas[0].valor)
        # print(folhas[1].valor)
        # print('raiz: ',raiz.valor)
        # print('folhas: ', folhas)
        if len(folhas) != 0:
            for folha in folhas:
                cont = 1
                # print('folha: ',folha.valor)
                if raiz_balancear == None:
                    raiz = self.raiz
                # print('raiz: ',raiz.valor,'folha: ',folha.valor)
                procurar = raiz
                while procurar != folha:

                    cont += 1
                    
                    if folha.valor >= procurar.valor:
                        procurar = procurar.direita
                    elif folha.valor < procurar.valor:
                        procurar = procurar.esquerda 
                if cont > tamanho:
                    tamanho = cont
        
        return tamanho

    def balancear(self,raiz):
        print('raiz: ',raiz.valor,end=' ')
        tamanho_esquerda = 0 
        tamanho_direita = 0 
        if raiz.esquerda != None:
            tamanho_esquerda = self.tamanho(raiz_balancear=raiz.esquerda)
        if raiz.direita != None:
            tamanho_direita = self.tamanho(raiz_balancear=raiz.direita)

        raiz.fator = tamanho_esquerda - tamanho_direita
        




        print('fator: ',raiz.fator)


    def exibir_arvore(self,raiz = None):

        def adicionar_arvore():

            valor = int(caixa_entrada.get())
            self.add(valor)
            canvas.delete("all")
            raiz = self.raiz
            informacoes()
            desenhar_no(raiz, 400, 50, 200, 100)

        def remover_arvore():

            valor = int(caixa_entrada.get())
            self.remover(valor)
            canvas.delete("all")
            raiz = self.raiz
            informacoes()
            desenhar_no(raiz, 400, 50, 200, 100)

        def informacoes():
            altura_var.set(self.tamanho())
            maior_var.set(self.maior().valor)
            menor_var.set(self.menor().valor)




        # Função auxiliar para desenhar os nós da árvore
        
        def desenhar_no(no, x, y, dx, dy):
            raio = 18
            cor = "white"
            if no is not None:
                espessura_borda = 2
                canvas.create_oval(x - raio, y - raio, x + raio, y + raio, fill=cor,width=espessura_borda)
                canvas.create_text(x, y, text=str(no.valor),font='bold')
                if no.esquerda:
                    canvas.create_line(x, y + raio, x - dx, y + dy - raio,width=2)
                    desenhar_no(no.esquerda, x - dx, y + dy, dx/2, dy)
                if no.direita:
                    canvas.create_line(x, y + raio, x + dx, y + dy - raio,width=2)
                    desenhar_no(no.direita, x + dx, y + dy, dx/2, dy)


        if raiz is None:
            raiz = self.raiz
        janela = tk.Tk()
        janela.configure(bg='#3d3334')
        font_grande = font.Font(size = 16)
        font_padrao = font.Font(size = 15)
        altura_var = IntVar()
        maior_var = IntVar()
        menor_var = IntVar()
        altura_var.set(0)
        maior_var.set(0)
        menor_var.set(0)

        titulo = tk.Label(janela, text='Árvore binária de busca',font=font_grande,fg='white',bg='#3d3334').pack(side='top')
    # Criação da janela e do canvas
        canvas = tk.Canvas(janela, width=800, height=600,bg="#386dbd")
        canvas.pack(side='top')

        tex1 = tk.Label(janela,text='Altura da árvore: ',bg="#386dbd",font=font_padrao,fg="white").place(x=10,y=50)
        altura = tk.Label(janela, textvariable=altura_var,bg="#386dbd",font=font_padrao,fg="white").place(x=160,y=50)
        tex2 = tk.Label(janela,text='Maior valor: ',bg="#386dbd",font=font_padrao,fg="white").place(x=10, y = 80)
        maior = tk.Label(janela,textvariable= maior_var,bg="#386dbd",font=font_padrao,fg="white").place(x=130, y = 80)
        tex3 = tk.Label(janela,text='Menor valor: ',bg="#386dbd",font=font_padrao,fg="white").place(x=10,y=110)
        menor = tk.Label(janela,textvariable=menor_var,bg="#386dbd",font=font_padrao,fg="white").place(x=130,y=110)

        # informacoes()
        remover = tk.Button(janela,text='Remover',command=remover_arvore,bg='red',fg='white').place(x=10,y=600)
        adicionar = tk.Button(janela,text='Adcionar',command=adicionar_arvore,bg='green',fg='white').place(x=75,y=600)
        caixa_entrada = tk.Entry(janela,bg='white')
        caixa_entrada.place(x=10,y=570)
        # caixa_entrada.place(x=50,y=50)




    # Desenhar a árvore
        desenhar_no(raiz, 400, 50, 200, 100)


    # Executar a janela
        janela.mainloop()