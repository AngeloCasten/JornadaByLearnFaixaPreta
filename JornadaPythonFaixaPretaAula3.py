#CONDICIONAIS
    #Tomada de decisao caso a condicao seja verdadeira
    # != é diferente

temperatura = 'quente'

print(temperatura)

quente = True
gosta_praia = False
gosta_chocolate_quente = True

if quente == True:
    print('Esta quente')
    if gosta_praia == True:
        print('Va para a praia')
    else:
        print('Nao va para a praia')
else:
    print('Esta frio')
    if gosta_chocolate_quente == True:
        print('tome nescau')
    else:
        print('nao tome nescau')


##OPERADORES LOGICOS
    # E (and)=> Ambas precisam ser verdade
    # OU (or)=> Pelo menos UMA precisa ser verdade

# 1, 3, 6 e 10 => Valido
# qualquer outro = Invalido

numero = input('Insira um numero: ')
if numero == 1 or numero == 3 or numero == 6 or numero == 10:
    print('numero valido')
else:
    print('numero invalido')

meu_nome = 'Angelo'
nome = input('Digite seu nome: ')

meu_sobrenome = 'Casten'
sobrenome = input('Digite seu sobrenome: ')

if meu_nome == nome and meu_sobrenome == sobrenome:
    print('Welcome Mr. Casten')
else:
    print('Some daqui')

#LACOS DE REPETICAO
    #NO CASO DE 1 a 10
        #Na Programacao o Minimo(1) é INCLUSIVO .=> ELE EXISTE
        #Já o maxixo (10) é EXCLUSIVO => Ele nao existe

for numero in range(10):
    print(numero)

#for                numero          in          range(10)
#para cada          numero          no          intervalo ate 10

for numero in range (10):
    print('O numero atual é: ')

notas = [6, 7.5, 9, 10]

soma = 0

for nota in notas:
    soma = soma + nota
print(soma)

            #len => Tamanho em ingles

media = soma / len(notas)

print('Á média é', soma)

numero_sorte = 10

escolhido = int(input('Digite um numero: '))

if escolhido == numero_sorte:
    print('ACERTOU')
else:
    print('ERRROOOOUUUUU')

#FUNCAO
    #Eu defino(def) uma rotina e a executo quantas vezes quiser

#definindo a funcao
def nome_funcao():
    #Codigo da funcao
    print('Codigo da funcao')

#chamando a funcao
            #ret retorna valor da funcao calculado
nome_funcao()

                #EXEMPLO COM PARAMETRO
def calcular_media(nota1, nota2):
    soma = nota1 + nota2
    media = soma / 2
    return media

media_calculada = calcular_media(10,8)

print(media_calculada)

#IMC => PESO(KG) / ALTURA (M)²
def numero_quadrado(numero):
    quadrado = numero * numero
    return quadrado
def calcular_imc(peso, altura):
    altura_quadrada = numero_quadrado(altura)
    meu_imc = peso ; altura_quadrada

    return meu_imc

def classificar_imc(meu_imc):
    if imc < 18.5:
        print('Magreza')
    elif imc >= 18.5 and imc <25:
        print('Normal')
    elif imc >= 25 and imc <30:
        print('Sobrepeso')
    else:
        print('Obesidade Morbida')


imc = calcular_imc(49, 1.67)
print(imc)
