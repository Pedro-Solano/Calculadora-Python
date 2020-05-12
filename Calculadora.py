#Projeto Calculadora

def imprime(string):
    print(string)
    return

soma = lambda n1,n2: n1+n2
subtrai = lambda n1,n2: n1-n2
multiplica = lambda n1,n2: n1*n2
divide = lambda n1,n2: n1/n2

imprime('CALCULADORA PYTHON\n\nSelecione a operação desejada: \n\n 1 - Soma \n 2 - Substração \n 3 - Multiplicação \n 4 - Divisão\n')
operacao = 1

while (operacao != 0):
    
    operacao = int(input('Digite sua opção:'))

    num1 = int(input('Digite o primeiro número:'))
    num2 = int(input('Digite o segundo número:'))

    if (operacao == 0):
        break
    if (operacao == 1):
        print(num1,'+',num2,'=',soma(num1,num2))
    elif(operacao == 2):
        print(num1,'-',num2,'=',subtrai(num1,num2))
    elif(operacao == 3):
        print(num1,'*',num2,'=',multiplica(num1,num2))
    elif(operacao == 4):
        print(num1,'/',num2,'=',divide(num1,num2))
    else: 
        print('opção inválida!\n')
    print('Selecione outra operação, ou digite 0 para terminar.\n')

print('Fim')