# pip install pyautogui

import pandas
import pyautogui
import time

# Uma pausa para executar todos os comandos
pyautogui.PAUSE = 0.5

# pyautogui.click -> clicar
# pyautogui.press -> pressionar uma tecla
# pyautogui.write -> escrever
# pyautogui.hotkey -> atalho de teclado (ctrl + c)

# Passo 1: Abrir o sistema da empresa

# abrir o google chrome
# apertar a tecla win
pyautogui.press("win")

# digitar o texto chrome
pyautogui.write("chrome")

# apertar a tecla enter
pyautogui.press("enter")

# entrar no link https://dlp.hashtagtreinamentos.com/python/intensivao/login
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# Pedir para o computador esperar 3 segundos
time.sleep(3)

# Passo 2: Fazer login
pyautogui.click(x=835, y=374)
pyautogui.write("joaocostadf5@gmail.com")

pyautogui.press("tab") # passa para o campo da senha
pyautogui.write("minhasenha_@123")

pyautogui.press("tab") # passa para o botão de login
pyautogui.press("enter")


# Passo 3: Importar a base de dados dos produtos
# pip install pandas openpyxl

tabela = pandas.read_csv("produtos.csv")

print(tabela)


time.sleep(2)

# Passo 4: Cadastrar um produto

for linha in tabela.index:
    pyautogui.click(x=847, y=258) # clica no primeiro campo

    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # marca2    
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria)) # str -> string = texto
    pyautogui.press("tab") 

    # preço unitario 
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")

    # custo 
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # obs 
    obs = str(tabela.loc[linha, "obs"])

    if obs != "nan":
        pyautogui.write(obs)
        
    pyautogui.press("tab")

    pyautogui.press("enter") # apertar o botão de enviar
    pyautogui.press("enter") # apertar o botão de enviar novamente, pois apenas uma vez não esta enviando os dados

    # numero positivo = scroll para cima
    # numero negativo = scroll para baixo
    pyautogui.scroll(10000) # scroll na tela


# Passo 5: Repetir o passo 4 até acabar todos os produtos

# nan = valor vazio em base de dados
# Not a number
