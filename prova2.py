def exercicio_1():
    list = []
    soma = 0
    while len ( list ) < 3:
        list.append ( int(input ("nota do aluno: ") ) )
    for number in list:
        soma += number
    media = soma/3
    return media

def exercicio_2(n):
    list = []
    while len ( list ) != n:
        opcao = input ( "Insira um número aqui: " )
        list.append ( opcao )
        return list

def exercicio_3():
    opcao = input ( "Digite a, b, z ou Z: " )
    if ( opcao == 'z' or opcao == 'Z' ):
        return
    elif ( opcao == 'a' ):
        print ( "globo" )
    elif ( opcao == 'b' ):
        print ( 'sbt' )
    else:
        print ( 'inválido' )

def exercicio_4( list ):
    mediaMenor7 = 0
    for media in list:
        if ( media < 7 ):
            mediaMenor7 += 1
    if ( mediaMenor7 < ( len(list) * 0.25 )):
        return "Professor Coxa"
    else:
        return "Professor Padrão"
