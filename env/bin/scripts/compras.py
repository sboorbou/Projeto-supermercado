from time import sleep
global produto, valor

def AdicionaCarrinho():
    global produto, valor
    print('Digite o valor desejado e aperte enter')
    print('Digite apenas o nome do produto, sem valores ou outros dados')
    produto = input(str('Digite o nome do produto: '))
    print('Digite apenas numeros, para centavos coloque um ponto, exemplo:')
    print('14.99')
    a = True
    while a == True:
        try:
            valor = float(input('Digite o valor do produto: '))
            a = False   
        except:
            print('Por favor digite um valor no formato:')
            print('14.99')
            sleep(1)
        
    return produto,valor