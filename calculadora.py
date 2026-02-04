import tkinter

valores_botoes = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

simbolos_direita = ["÷", "×", "-", "+", "="]
simbolos_topo = ["AC", "+/-", "%"]

quantidade_linhas = len(valores_botoes)   # 5
quantidade_colunas = len(valores_botoes[0])  # 4

cor_cinza_claro = "#D4D4D2"
cor_preto = "#1C1C1C"
cor_cinza_escuro = "#505050"
cor_laranja = "#0044FF"
cor_branco = "white"

janela = tkinter.Tk()
janela.title("Calculadora")
janela.resizable(False, False)

quadro = tkinter.Frame(janela)

visor = tkinter.Label(
    quadro,
    text="0",
    font=("Arial", 45),
    background=cor_preto,
    foreground=cor_branco,
    anchor="e",
    width=quantidade_colunas
)

visor.grid(row=0, column=0, columnspan=quantidade_colunas, sticky="we")


for linha in range(quantidade_linhas):
    for coluna in range(quantidade_colunas):
        valor = valores_botoes[linha][coluna]

        botao = tkinter.Button(
            quadro,
            text=valor,
            font=("Arial", 30),
            width=quantidade_colunas - 1,
            height=1,
            command=lambda valor=valor: botao_clicado(valor)
        )

        if valor in simbolos_topo:
            botao.config(foreground=cor_preto, background=cor_cinza_claro)
        elif valor in simbolos_direita:
            botao.config(foreground=cor_branco, background=cor_laranja)
        else:
            botao.config(foreground=cor_branco, background=cor_cinza_escuro)

        botao.grid(row=linha + 1, column=coluna)

quadro.pack()


valor_A = "0"
operador = None
valor_B = None

def limpar_tudo():
    global valor_A, valor_B, operador
    valor_A = "0"
    operador = None
    valor_B = None

def remover_decimal_zero(numero):
    if numero % 1 == 0:
        numero = int(numero)
    return str(numero)

def botao_clicado(valor):
    global simbolos_direita, simbolos_topo, visor, valor_A, valor_B, operador

    if valor in simbolos_direita:
        if valor == "=":
            if valor_A is not None and operador is not None:
                valor_B = visor["text"]
                numero_A = float(valor_A)
                numero_B = float(valor_B)

                if operador == "+":
                    visor["text"] = remover_decimal_zero(numero_A + numero_B)
                elif operador == "-":
                    visor["text"] = remover_decimal_zero(numero_A - numero_B)
                elif operador == "×":
                    visor["text"] = remover_decimal_zero(numero_A * numero_B)
                elif operador == "÷":
                    visor["text"] = remover_decimal_zero(numero_A / numero_B)

                limpar_tudo()

        elif valor in "+-×÷":
            if operador is None:
                valor_A = visor["text"]
                visor["text"] = "0"
                valor_B = "0"

            operador = valor

    elif valor in simbolos_topo:
        if valor == "AC":
            limpar_tudo()
            visor["text"] = "0"

        elif valor == "+/-":
            resultado = float(visor["text"]) * -1
            visor["text"] = remover_decimal_zero(resultado)

        elif valor == "%":
            resultado = float(visor["text"]) / 100
            visor["text"] = remover_decimal_zero(resultado)

    else:
        if valor == ".":
            if valor not in visor["text"]:
                visor["text"] += valor
        elif valor in "0123456789":
            if visor["text"] == "0":
                visor["text"] = valor
            else:
                visor["text"] += valor

janela.update()
largura_janela = janela.winfo_width()
altura_janela = janela.winfo_height()
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()

posicao_x = int((largura_tela / 2) - (largura_janela / 2))
posicao_y = int((altura_tela / 2) - (altura_janela / 2))

janela.geometry(f"{largura_janela}x{altura_janela}+{posicao_x}+{posicao_y}")

janela.mainloop()
