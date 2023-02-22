import time
contador = 0

#contador é uma vatiavel com o numero 0

 

while contador <10:
    print('Ainda não deu')
    contador = contador + 1
    if contador == 5:
        print('Chegamos a metade')
        break
    time.sleep(1)
#nesse programa enquanto a variavel contador nao chegar a 10 o programa vai
#repedir a frase 'Ainda nao deu'
 #quando chegar o programa vai printar a frase 'Agora deu'
# porem quando o script ver a declaraçao break ela para o loop e continua o programa ou
# para ele de vez


print('Agora deu')
