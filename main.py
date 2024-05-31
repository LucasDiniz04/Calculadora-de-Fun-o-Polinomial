import math  # biblioteca de operações matemáticas
import numpy as np  # biblioteca que lida com logaritmos
import sympy as sp  # biblioteca de funções matemáticas
import os  # biblioteca de comandos do sistema

def bisseccao(f, a, b, erro):  # função de Bissecção
    n = (np.log(b - a) - np.log(erro)) / np.log(2)  # calcula o numero de iterações p/ o método da bissecção alcançar a tolerância de erro especificada
    n = np.ceil(n)  # ceil vai pegar o próximo número que seja inteiro, p/ garantir que tenhamos pelo menos esse número de iterações
    i = 0  # incrementador
    print("Valor das iterações: ")
    while i < n:
        if f(a) * f(b) > 0:  # se o produto de f(a) e f(b) for maior que zero
            print("Não tem zero nesse intervalo")
            voltarMenu()
        else:  # cria uma variavel 'media' para receber a bissecção
            media = (a + b) / 2
            media = round(media, 6)  # arredonda para aparecer 6 digitos após a virgula
            if f(a) * f(media) < 0:
                b = media

            else:
                a = media
            print("Valor de x", i + 1, "= ", media)  # pra cada valor de interação ele mostra o valor do X
            i += 1  # incrementa o i até que o numero de interações corresponda ao pedido do usuário e assim sair do loop
    print()  # pula uma linha
    print("O valor aproximado da raiz com o erro < ", erro, "é: ", media)  # valor final
    print("Número de iterações: ",i)
    voltarMenu()  # chama a função perguntando se o usuário deseja voltar para o menu inicial

def falsaPosicao(f, a, b, erro):  # função da Falsa Posição
    i = 0  # incrementador
    print("\nValor das iterações: ")
    while True:
        if f(a) * f(b) > 0:  # se o produto de f(a) e f(b) for maior que zero
            print("Não tem zero nesse intervalo")
            voltarMenu()
        else:  # cria uma variavel 'c' para receber o ponto de Falsa Posição
            c = (a * f(b) - b * f(a)) / (f(b) - f(a))
            c = round(c, 6)  # arredonda para aparecer 6 digitos após a virgula
            if abs(f(c)) < erro:  # verifica se o valor absoluto de f(c) é menor que o erro
                break
            if f(a) * f(c) < 0:
                b = c
            else:
                a = c
            print("Valor de x", i + 1, "= ", c)  # pra cada valor de interação ele mostra o valor do X
            i += 1  # incrementa o i até que o numero de interações corresponda ao pedido do usuário e assim sair do loop
    print("\nO valor aproximado da raiz com o erro < ", erro, "é: ", c)  # valor final
    print("Número de iterações: ",i)
    voltarMenu()  # chama a função perguntando se o usuário deseja voltar para o menu inicial

def newtonRaphson(f, df, x0, erro):  # função de Newton-Raphson
    i = 0  # incrementador
    print("\nValor das iterações: ")
    while True:
        x1 = x0 - f(x0) / df(x0)  # aplica a fórmula do método de Newton-Raphson
        x1 = round(x1, 6)  # arredonda para aparecer 6 digitos após a virgula
        print("Valor de x", i + 1, "= ", x1)  # pra cada valor de interação ele mostra o valor do X
        if abs(x1 - x0) < erro:  # verifica se a diferença entre x1 e x0 é menor que o erro
            break
        x0 = x1
        i += 1  # incrementa o i até que o numero de interações corresponda ao pedido do usuário e assim sair do loop
    print("\nO valor aproximado da raiz com o erro < ", erro, "é: ", x1)  # valor final
    print("Número de iterações: ",i)
    voltarMenu()  # chama a função perguntando se o usuário deseja voltar para o menu inicial

def voltarMenu():  # função para perguntar se o usuário deseja voltar para o menu inicial
  continuar = input("\nDeseja voltar para o menu inicial?\nDigite sim para continuar.\n").lower() # pergunta ao usuário se ele quer sair da função newton-raphson e talvez fazer outro calculo
  if continuar == 'sim':  # se o usuario digitar 'sim', limpa a tela do console e chama a função 'main()'
    os.system('cls' if os.name == 'nt' else 'clear')
    main()
  elif continuar != 'sim':  # se a resposta for diferente de 'sim', fecha o programa.
    print("Programa finalizado.")
    exit()  # fecha o programa

def main():  # função principal
    print("=" * 40)
    print("Calculadora de Função Polinomial")
    print("=" * 40)
    funcao = input("Escreva a função (ex: 'x**3 - 2*x - 5'): ")  # variável que vai receber a função digitada pelo usuário
    # definição do intervalo [a,b] e o erro
    a = float(input("Valor de a: "))
    b = float(input("Valor de b: "))
    erro = float(input("Informe a tolerância do erro: (ex: '0.01') "))

    print("Selecione o método que deseja usar: ")
    print("1: Bissecção")
    print("2: Falsa posição")
    print("3: Newton-Raphson")
    print("4: Sair do programa")
    escolha = int(input("Escolha uma opção: "))  # menu do programa

    match escolha: #estrutura de condição match case
        case 1:  # caso a escolha seja 1 envia pra função 'bissecção()', passando 'a', 'b' e 'erro' como parâmetros
            bisseccao(eval(f'lambda x: {funcao}'), a, b, erro)
        case 2:  # caso a escolha seja 2 envia pra função 'falsaPosição()'
            falsaPosicao(eval(f'lambda x: {funcao}'), a, b, erro)
        case 3:  # caso a escolha seja 3 calcula a derivada e redireciona pra função 'newtonRapshon()'
            x0 = float(input("Informe o valor inicial x0: "))
            x = sp.symbols('x')  #cria uma variável simbólica para a função
            try: #tenta executar o bloco abaixo
              funcao = sp.sympify(funcao) #Converte a entrada do usuário em uma expressão simbólica
              derivada = sp.diff(funcao, x)  #Calcula a derivada da função
              print("A derivada de ",funcao,"em relação a x é: ",derivada) #Exibe a derivada
              newtonRaphson(eval(f'lambda x: {funcao}'), eval(f'lambda x: {derivada}'), x0, erro) #passa 'funcao' e a 'derivada' como parâmetros pra função 'newthonRapshon()'
            except (sp.SympifyError, sp.SyntaxError) as err: #caso ocorra um erro no calculo da derivada, imprime o erro
              print(f"Erro ao interpretar a função: {err}")
        case 4:  # caso a escolha seja 4, fecha o programa
            print("Saindo do programa...")
            exit()  # Fecha o programa
    if escolha <= 0 or escolha > 5:  # se a escolha for um numero menor ou igual a 0 ou maior que a 5, a opção será inválida
        print("Opção inválida.")
        exit()  # Fecha o programa.

main()  # começo do programa, chamando a função main()
