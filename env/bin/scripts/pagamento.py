
def meio_pagamento(total : float) -> None :
    print('Escolha o Meio de pagamento: ')
    print('1 - Cartão de crédito ')
    print('2 - Debito')
    print('3 - Dinheiro')
    tratamento = True
    opcao = int(0)
    erro = False
    tipo = 'Erro'
    while tratamento == True:
        if erro == True:
            print('\033[31m{}\033[33m'.format('Por favor escolha uma opção valida'))
        
        if opcao == int(1) or opcao == int(2) or opcao == int(3):
            tratamento = False
            pass
        else:
            try:
                opcao = int(input('Qual meio de pagamento: '))
                erro = True
                tratamento = False
                if opcao == 1:
                    tipo = 'Cartão de Credito'
                elif opcao == 2:
                    tipo = 'Cartão de Debito'
                    total = float(total * 0.95)
                elif opcao == 3:
                    tipo = 'Dinheiro'
                    total = float(total * 0.95)
            except:
                print('\033[31m{}\033[33m'.format('Por favor escolha uma opção valida'))
    
    print('\033[33m{}\033[31m{:.2f}\033[33m {} {}'.format('O total fica ',float(total),' com pagamento a ',tipo))        
    
    

#meio_pagamento(100.99)