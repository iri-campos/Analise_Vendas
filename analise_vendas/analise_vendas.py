def analise_vendas(vendas):
    #Calcula o total de vendas:
    total_vendas = sum(vendas)

    #Calcula o valor da média mensal de vendas:
    media_vendas = total_vendas / len(vendas)
    
    return f"{total_vendas}, {media_vendas:.2f}"

def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()

    #Converte a entrada em uma lista de inteiros:
    vendas = list(map(int, entrada.split(', ')))
    
    return vendas

#Obtém a lista de vendas mensais
vendas = obter_entrada_vendas()
print(analise_vendas(vendas))