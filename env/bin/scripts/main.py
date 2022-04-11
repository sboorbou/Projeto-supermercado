
from compras import AdicionaCarrinho


if  __name__ == '__main__':
    carrinho = {}
    comprar = True
    print('\033[31m{:^80}'.format('Bem vindo ao caixa'))
    print('\033[33m{:^80}'.format('Para cada produto digite o Nome e o Valor do mesmo'))
    option = 1
    while comprar == True:
        option = int(input(''' 
                            1 - Adicionar outo item 
                            2 - Sair
                            :'''))
        if option == 1:
            retorno = AdicionaCarrinho()
            carrinho[retorno[0]] = retorno[1]
        elif option == 2:
            print(carrinho)
            comprar = False
        