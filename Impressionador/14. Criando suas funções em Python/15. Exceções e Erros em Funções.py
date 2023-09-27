try:
    print('Não deu erro')
except:
    print('Deu erro, mas não parou')


def descobrir_servidor(email):
    try:
        i = email.index('@')
        servidor = email[i]
    except:
        raise ValueError('Email digitado sem o @. Digite novamente')
    else:
        if 'gmail' in servidor:
            return 'gmail'
        elif 'hotmail' in servidor or 'outlook' in servidor or 'live' in servidor:
            return 'hotmail'
        elif 'yahoo' in servidor:
            return 'yahoo'
        elif 'uol' in servidor or 'bol' in servidor:
            return 'uol'
        else:
            return 'não determinado'

'''
    try:
        Tente fazer isso
    execpt ErroEspecífico:
        Deu esse erro aqui que era esperado
    else:
        Caso não dê o erro esperado, rode isso
    finally:
        independente do que acontecer, faça isso


'''