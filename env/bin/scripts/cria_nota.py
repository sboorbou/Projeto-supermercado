import csv
import os
from pagamento import  meio_pagamento

dic = {}

def Inicia_Nova_Nota():
    global escre_nota, nota 
    nota = open('Projeto-supermercado/env/bin/files/nota.csv','w+',encoding='utf-8',newline='')  
    nota.truncate(0)
    nome_campos = ['Produto','Valor']
    escre_nota = csv.DictWriter(nota, fieldnames = nome_campos)
    escre_nota.writeheader()
    nota.flush()

def Adiciona_Item_Nota(item = []):
    global escre_nota, nota
    dic[item[0]] = item[1]
    escre_nota.writerow({'Produto':item[0],'Valor':item[1]})
    nota.flush()
    
def Encerra_Nota():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('\033[31m{:^80}'.format('   Compra Encerrada'))
    print('\033[33m{:^80}'.format(' '))
    global escre_nota, nota
    nota.flush()
    dic = {}
    nota.seek(0,0)
    lines = nota.read().splitlines()
    total = float(0)
    for line in lines:
        key = line.split(',')[0]
        value = line.split(',')[1]
        value = value.strip()
        print('{:^40} - {:^40}'.format(key,value))
        if value == 'Produto' or value == None or value == '\n' or value == ' ' or value == 'valor' or value == 'Valor':
            pass
        else:
            total = float(total) + float(value)
    print('{:^40} \033[31m{:.2f}\033[33m'.format('O Total da Compra foi ',total))
    print('\n')
    meio_pagamento(total)
    print('\n')
    print('\n')
    #return dic
    


