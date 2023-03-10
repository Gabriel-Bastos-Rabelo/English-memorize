import random
while True:
    with open("banco_palavras.txt", "r", encoding="utf-8") as arquivo:
        lista_de_palavras = []
        for linha in arquivo.readlines():
            palavra, significado = linha.split()
            lista_de_palavras.append([palavra, significado.upper()])
    print("""
    Digite 1 para cadastrar uma nova palavra
    Digite 2 para sortear uma nova palavra
    Digite 3 para sair do programa
    """)
    op = int(input())
    if op == 1:
        palavra = input("Digite a palavra em ingles")
        significado = input("Digite o significado")
        lista_de_palavras.append([palavra, significado.upper()])
        print(lista_de_palavras)
        with open("banco_palavras.txt", "w", encoding="utf-8") as arquivo:
            for e in lista_de_palavras:
                arquivo.write(f"{e[0]} {e[1]}\n")

    elif op == 2:
        numero = random.randint(0, (len(lista_de_palavras)-1))
        resposta = input(
            f"Qual o siginificado de {lista_de_palavras[numero][0]}? ")
        if resposta.upper() == lista_de_palavras[numero][1]:
            print("Voce acertou")
        else:
            print(f"Voce errou, a resposta é {lista_de_palavras[numero][1]}")
    else:
        break
