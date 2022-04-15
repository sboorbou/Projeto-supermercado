from time import sleep
from cria_nota import Inicia_Nova_Nota, Adiciona_Item_Nota, Encerra_Nota
global produto, valor

def AdicionaCarrinho():
    global produto, valor
    produto = input(str('{} \033[31m{}\033[33m {}: '.format('Digite o','nome','do produto')))
    a = True
    while a == True:
        try:
            print('exemplo: 14.99')
            valor = float(input('{} \033[31m{}\033[33m {}'.format('Digite o ','valor ','do produto: ')))
            a = False   
        except:
            print('Por favor digite um valor no formato:')
            print('exemplo: 14.99')
            sleep(1)
        #Adiciona_Item_Nota(item = [produto,valor])
        Adiciona_Item_Nota([produto,valor])