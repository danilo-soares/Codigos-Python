def fibonacci (valor,ultimo=0,penultimo=1):

    for i in range (valor):
        penultimo = ultimo + penultimo
        ultimo= penultimo - ultimo
    return ultimo


