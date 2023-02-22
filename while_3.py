print('Digite um numero:')
numero = int(input(">: "))
fatorial = numero 
contador = 1 
while (numero-contador)>1:
    fatorial= fatorial * (numero-contador)
    contador+=1
    
print(f'{numero}! = {fatorial}')





