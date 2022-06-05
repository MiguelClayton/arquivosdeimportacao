from time import sleep


# utilidades


def fatorar(n, p):
    contn = n - 1
    contp = p - 1
    np = n - p
    contnp = np - 1
    while True:
        if contnp == 0:
            break
        np = np * contnp
        contnp -= 1

    while True:
        if contn == 0:
            break
        n = n * contn
        contn -= 1

    while True:
        if contp == 0:
            break
        p = p * contp
        contp -= 1

    try:
        c = n / (np * p)
    except ZeroDivisionError:
        c = n

    return c


def cabecalho(msg, num=50):
    pontilados()
    print(f'{msg}'.center(num))
    pontilados()


def menu(lista):
    cabecalho('Menu Principal')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[0:92m{item}\033[m')
        c += 1
    pontilados()
    opcao = leiaint('Sua opçao: ')
    return opcao


def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0:31mERRO: Digite um numero inteiro valido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0:31mEntrada de dador interrompida pelo ususario\033[m')
            return 0
        else:
            return n


def leianum(msg):
    while True:
        try:
            n = leiaint(msg)
        except (ValueError, TypeError):
            n = leiafloat(msg)

        return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg).replace(',', '.'))
        except (ValueError, TypeError):
            print('\033[0:31mERRO: Digite um numero real valido\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0:31mEntrada de dador interrompida pelo ususario\033[m')
            return 0
        else:
            return n


def arqExiste(nome):
    try:
        a = open(nome, 'r')
        a.close()
    except (FileExistsError, FileNotFoundError):
        return False
    else:
        return True


def criaArq(nome):
    try:
        a = open(nome, 'wt+')
    except:
        vermelho('Erro: falha ao criar o arquivo.')
    else:
        verde('Arquivo criado com sucesso.')


def lerErq(nome):
    try:
        a = open(nome, 'rt')
    except:
        vermelho('Erro: falha ao abrir o arquivo')
    else:
        cabecalho('Pessoas cadastradas')
        cont = 1
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{cont}: {dado[0]:<30}{dado[1]:>3} anos')
            cont += 1
    finally:
        a.close()


def cadastrar(nomearq, nome='desconhecido', idade=0):
    try:
        a = open(nomearq, 'at')
    except:
        vermelho('Erro: falha ao editar arquivo.')
    else:
        try:
            a.writelines(f'{nome};{idade}\n')
            a.close()
        except:
            vermelho('Erro: falha ao escrever os dados')
        else:
            print(f'Novo registro de {nome} adicionado')


def pontilados(num=50):
    print('-' * num)


def carregamentosimples():
    sleep(1.5)
    print('.', end='')
    sleep(1.5)
    print('.', end='')
    sleep(1.5)
    print('.')
    sleep(2)


# def maiorQoutro(valor):


# cores


def vermelho(msg):
    print(f'\033[0:31m{msg}\033[m')


def verde(msg):
    print(f'\033[1;92m{msg}\033[m')


def azul(msg):
    print(f'\033[34m{msg}\033[m')


def ciano(msg):
    print(f'\033[36m{msg}\033[m')


def magenta(msg):
    print(f'\033[35m{msg}\033[m')


def amarelo(msg):
    print(f'\033[33m{msg}\033[m')


def preto(msg):
    print(f'\033[30m{msg}\033m')


def branco(msg):
    print(f'\033[37m{msg}\033[m')


def negrito(msg):
    print(f'\033[1m{msg}\033[m')
