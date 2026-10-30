#Pojeto de algoritmo: Estacionamento

o = ['Reg. Moto', 'Reg. Carro', 'Reg. Caminhonete', 'Quantidade de Veículos', 'Valor Arrecadado', 'Encerrar']
p = [5.00, 10.00, 15.00]
vt = 0
qtd = 0
re = 0
qtdm = 0
qtdc = 0
qtdcm = 0
while re!=6:
    print('Bem vindo ao Estacionamento!\n')
    print('OPÇÃO   PREÇO')
    print(f'1 - {o[0]}   {p[0]}')
    print(f'2 - {o[1]}   {p[1]}')
    print(f'3 - {o[2]}   {p[2]}')
    print(f'4 - {o[3]}')
    print(f'5 - {o[4]}')
    print(f'6 - {o[5]}\n')

    re = int(input('Escolha uma opção: \n'))

    if re==1:
        print(f'Você registrou: Moto.')
        qtd+=1
        vt+=5
        qtdm+=1

    elif re==2:
        print(f'Você registrou: Carro.')
        qtd += 1
        vt += 10
        qtdc+=1

    elif re==3:
        print(f'Você registrou: Caminhonete .')
        qtd += 1
        vt += 15
        qtdcm+=1

    elif re==4:
        print(f'A quantidade de veículos registrados até o momento é de {qtd}.')

    elif re==5:
        print(f'O valor arrecadado até o momento é de {vt}')

    elif re==6:
        print(f'Obrigado por registrar conosco! Você registrou {qtd} veículos, sendo: {qtdm} Motos, {qtdc} Carros e {qtdcm} Caminhonetes. O valor arrecadado foi de {vt}. Encerrando programa...')

    else:
        print('Esse número não está listado! Escolha um listado!')






