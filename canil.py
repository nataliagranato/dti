import sys
from datetime import datetime


def melhor_petshop(data, pequenos, grandes):
    # Dados dos petshops
    petshops = {
        'Meu Canino Feliz': {'distancia': 2, 'semana_pequeno': 20, 'semana_grande': 40, 'fim_semana_pequeno': 20 * 1.2, 'fim_semana_grande': 40 * 1.2},
        'Vai Rex': {'distancia': 1.7, 'semana_pequeno': 15, 'semana_grande': 50, 'fim_semana_pequeno': 20, 'fim_semana_grande': 55},
        'ChowChawgas': {'distancia': 0.8, 'pequeno': 30, 'grande': 45}
    }

    # Converter a data para dia útil ou fim de semana
    dia_util = data.weekday() < 5  # 0-4 representa dias úteis

    # Calcular custo total para cada petshop
    custos = []
    for petshop, info in petshops.items():
        if 'semana_pequeno' in info:
            custo_pequeno = info['semana_pequeno'] if dia_util else info['fim_semana_pequeno']
            custo_grande = info['semana_grande'] if dia_util else info['fim_semana_grande']
        else:
            custo_pequeno = info['pequeno']
            custo_grande = info['grande']

        custo_total = pequenos * custo_pequeno + grandes * custo_grande
        custos.append({'petshop': petshop, 'custo': custo_total,
                      'distancia': info['distancia']})

    # Selecionar o petshop mais barato e mais próximo
    melhor = min(custos, key=lambda x: (
        x['custo'], x['distancia'], x['petshop']))

    return melhor['petshop']


if __name__ == "__main__":
    # Entrada do usuário
    try:
        data = input("Informe a data no formato YYYY-MM-DD: ")
        quantidade_pequenos = int(input("Quantidade de cães pequenos: "))
        quantidade_grandes = int(input("Quantidade de cães grandes: "))

        # Convertendo a string da data para o tipo de dados datetime
        data = datetime.strptime(data, "%Y-%m-%d")

        # Chamando a função principal
        resultado = melhor_petshop(
            data, quantidade_pequenos, quantidade_grandes)

        # Calculando o valor total dos banhos
        valor_total_banhos = quantidade_pequenos * 15 + quantidade_grandes * 40

        # Exibindo a mensagem com o valor total dos banhos
        print(
            f"O melhor petshop é '{resultado}' para banhar seus cães. O valor total dos banhos é R${valor_total_banhos:.2f}.")
    except ValueError:
        print("Erro: Certifique-se de fornecer uma data válida e quantidades inteiras de cães pequenos e grandes.")
        sys.exit(1)
