#VARIAVEIS

nome= 'Angelo'
sobrenome = 'Casten'
apelido = 'Shaman'
idade = 19

nome_completo = nome + ' ' + sobrenome

print (nome_completo)

#TIPOS DE DADOS
	## Toda variavel tem yum tipo, que a define se é um texto, numero, boolenao (0,1)

inteiro = 10
decimal = 10.5
texto = 'Angelo Casten'
verdadeiro_falso =  False #True or False

type(23) #numero

type('23') #texto

type (inteiro) #int

type (decimal) #float

type (texto) #string

type (verdadeiro_falso) #bool

#converter
	#!  variavel = type(variavel)
		#ex:  idade  = str(idade)

# Operações Matematicas

soma = 10 + 20

subtracao = 20 - 10

multiplicaçao = 2 * 3

divisao = 8 / 2

primeiro_numero = 20
segundo_numero = 30
terceiro_numero = 10
quarto_numero = 5

valor_final = (primeiro_numero + segundo_numero + terceiro_numero) / quarto_numero


#Metodos de entrada
	#forma como vai ser passado o numero parar o Python
	#usamos a funcao input()

nome = input('Insira seu nome: ')
idade - int(input('Insira sua idade: '))

#Metodos de saida
	#Mostrar um valor para o user
	#print()

print('Seu nome é', nome, 'sua idade é', idade)

print('Seja bem vindo a minha calculadora de multiplicacao')

valor1 = float(input('Insira seu primeiro numero: '))
valor2 = float(input('Insira seu segundo numero: '))

print('O resultado da multiplicacao entre', valor1, 'e', valor2, 'é de')

	#ELEMENTOS EM LISTAS
lista_animais = ['Cachorro','Gato','Coelho','Furão','Pássaro','Peixe']
		#posicao         1         2      3       4       5         6
		#indice          0         1      2       3       4         5	
			#posicao = animais
			#indices = animais - 1
furao = lista_animais[3]
gato = lista_animais[1]


