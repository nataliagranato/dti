# Sistema de Escolha de Petshop para Banho de Cães

Este sistema foi desenvolvido para ajudar o Sr. Eduardo, proprietário de um canil em Belo Horizonte, a escolher o melhor petshop para banhar seus cães com base em critérios de distância e custo.

## Premissas

1. **Dados de Entrada Válidos:** O usuário é responsável por fornecer uma data válida no formato YYYY-MM-DD e quantidades inteiras de cães pequenos e grandes.
2. **Distâncias Fixas:** As distâncias entre o canil e os petshops são consideradas fixas e fornecidas no momento da definição dos petshops.
3. **Petshops Considerados:** Os petshops considerados são Meu Canino Feliz, Vai Rex e ChowChawgas, com preços e distâncias específicos.

## Decisões de Projeto

1. **Estrutura de Dados:** Utiliza-se um dicionário para armazenar informações sobre os petshops, incluindo distância, preços para dias úteis e fins de semana.
2. **Cálculo de Custos:** Os custos são calculados com base nas quantidades de cães pequenos e grandes, considerando preços diferentes para dias úteis e fins de semana quando aplicável.
3. **Critério de Escolha:** O petshop escolhido é o que oferece o menor custo total. Em caso de empate, o critério de desempate é a proximidade do petshop.

## Instruções de Execução

1. **Requisitos:** Certifique-se de ter o Python instalado no seu sistema.
2. **Baixar o Código:** Clone ou faça o download do repositório.
3. **Executar o Código:**
    - Abra um terminal ou prompt de comando na pasta do código.
    - Execute o comando: `python3 canil.py`.

4. **Entrada de Dados:**
    - O programa solicitará a data no formato YYYY-MM-DD, quantidade de cães pequenos e quantidade de cães grandes.
    - Insira as informações conforme solicitado.

5. **Resultado:**
    - O programa exibirá o nome do petshop recomendado com base nas entradas fornecidas.

---
**Observação:** Dê as permissões necessárias para a execução do código. Certifique-se de fornecer entradas válidas para garantir o correto funcionamento do programa.

**Teste unitário:** Execute o teste unitário com o seguinte comando:

```
python3 test_canil.py
```

Você pode receber um resultado semelhante a saída abaixo:

```
-------------------------------------------------------------
Ran 0 tests in 0.000s

OK
```
