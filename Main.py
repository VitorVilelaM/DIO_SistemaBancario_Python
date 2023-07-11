valor_conta = 0
LIMITE_SAQUE_DIARIO = 3
saques_por_dia = 0
extrato = '### Extrato da Conta ###\n'

def Deposito(valor_conta, valor_para_depositar):
    global extrato

    novoValor = valor_conta + valor_para_depositar
    print(f"Valor depositado com sucesso!")
    
    operacao = f'R$ ' + str(float(valor_para_depositar))
    extrato += 'Depósito: ' + operacao + '\n'
    
    return novoValor

def Saque(valor_conta, valor_para_sacar):
    global extrato, saques_por_dia
    if(valor_para_sacar <= valor_conta and saques_por_dia < 3):
        novoValor = valor_conta - valor_para_sacar
        saques_por_dia += 1

        print(f"Valor sacado com sucesso!")
        
        operacao = f'R$ ' + str(float(valor_para_sacar))
        extrato += 'Saque: ' + operacao + '\n'
        
        return novoValor
   
    elif valor_para_sacar > valor_conta:
        print("Voce nao tem saldo o suficiente para essa operação!\n")
   
    elif saques_por_dia == 3:
        print("Você atingiu o limite máximo de saques por dia!\n")
    return valor_conta

operacao = 0
while(operacao != 4):
    print("""
        ######## MENU ########
        [1] - Saque
        [2] - Depósito
        [3] - Verificar Extrato
        [4] - Sair do Programa
        ######################
    """)
    operacao = int(input("Qual operação você deseja fazer:"))

    if operacao == 1:    
        valor_para_sacar = float(input("Informe a quantia que deseja sacar: "))
        valor_conta = Saque(valor_conta, valor_para_sacar)

    elif operacao == 2:
        valor_para_depositar = float(input("Informe a quantia que deseja depositar: "))
        valor_conta = Deposito(valor_conta, valor_para_depositar)

    elif operacao == 3:
        extrato += '\n\n' + 'Total: ' + str(float(valor_conta))
        print(extrato)

    elif operacao == 4:
        print("Obrigado por usar nosso programa, até mais!\n")
    
    else:
        print("Operação informada nao existe!\n")
    