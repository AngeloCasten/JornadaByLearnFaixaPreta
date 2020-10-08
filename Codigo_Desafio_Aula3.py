#          SISTEMA BASICO DE LOGIN              #

print('Bem-Vindo ao Login Test ByLearn')
usuario_existente = str(input('Você já possui conta em nosso sistema? (Y / N)'))

if usuario_existente == 'Y':
    print('Por favor se conecte')
    login = str(input('Digite seu login: '))
    senha = str(input('Digite sua senha: '))
elif usuario_existente == 'N':
    print('Para se cadastrar insira um login e senha: ')
    loginCad = str(input('Digite seu login: '))
    senhaCad = str(input('Digite sua senha: '))
  #REDIRECIONAMENTO PARA LOGIN EM SISTEMA#  
    print('Por favor se conecte')
    login = str(input('Digite seu login: '))
    senha = str(input('Digite sua senha: '))
    

if login == loginCad and senha == senhaCad:
    print('Olá', login, 'Como está?')
else:
    print('Acesso Negado! Finalizando sistema')