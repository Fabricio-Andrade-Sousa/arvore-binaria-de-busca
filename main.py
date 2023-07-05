from arvore_binaria import Arvore


arvore = Arvore()
# arvore.add(4)
# arvore.add(5)
# arvore.add(4)
# arvore.add(10)
# arvore.add(8)
# arvore.add(9)
# arvore.add(12)
# arvore.add(7)
# arvore.add(11)
# arvore.add(14)
# arvore.add(13)
# print(arvore.altura(arvore.raiz))
# arvore.add(7)
# arvore.add(6)
# arvore.add(8)
# arvore.add(-2)
# arvore.balancear(arvore.raiz)
# arvore.pre_ordem()
# # arvore.remover(4)
# print(arvore.tamanho())
cont = 0
while cont != 31:
    arvore.add(cont)
    cont += 1
# # print(arvore.tamanho())
# arvore.pre_ordem()
# arvore.remover(4)
# # print(arvore.folhas())
# arvore.pre_ordem()
# arvore.ordem()
# print(arvore.procurar(5))

arvore.exibir_arvore()
# arvore.pos_ordem()
# print(arvore.minimo().valor)
