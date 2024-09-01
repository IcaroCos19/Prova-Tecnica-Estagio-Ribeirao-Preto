def letras_a(string):
    qtd=0

    for cara in string:
        if cara == 'a' or cara == 'A':
            qtd += 1

    if qtd >0:
        return f"A letra 'a' apareceu {qtd} vez(es) na string."
    else:
        return f"A letra 'a' não apareceu na string."
    
n = input("Digite uma frase: ")
resp = letras_a (n)
print(resp)
