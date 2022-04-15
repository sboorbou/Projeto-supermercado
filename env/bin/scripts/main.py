
from compras import AdicionaCarrinho
from cria_nota import Inicia_Nova_Nota, Encerra_Nota


if  __name__ == '__main__':
    carrinho = {}
    comprar = True
    Inicia_Nova_Nota()
    print('\033[31m{:=^80}'.format('Bem vindo ao caixa'))
    print('\033[33m{:^80}'.format('Para cada produto digite o Nome e o Valor do mesmo'))
    option = 1
    while comprar == True:
        try:
            option = int(input(''' 
                            1 - Adicionar outo item 
                            2 - Sair
                            :'''))
        except:
            print('escolha apenas 1 ou 2')
        if option == 1:
            retorno = AdicionaCarrinho()
        elif option == 2:
            comprar = False
            Encerra_Nota()
        else:
            print('Por favor, digite apenas 1 ou 2')
        