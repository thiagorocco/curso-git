import random

n = random.randint(1,10)
tentativas = 0
myNumber = 0
acertar = False
while acertar==False:
    tentativas+=1
    myNumber = int(input('Tente adivinhar um número entre 01 e 10: '))
    if myNumber == n:
        if tentativas == 1:
            print('Parabéns você acertou na primeira tentativa!!!')
        else:
            print('Você acertou em ',tentativas,' tentativas')
        acertar = True
    elif myNumber > n:
        print('O número sorteado é menor que ',myNumber)
    else:
        print('O número sorteado é maior que ',myNumber)
