import pyautogui
from time import sleep 
import pyperclip 
import pandas as pd # biblioteca para tratamentos de dados

pyautogui.PAUSE = 1.3

# Aqui faremos o tratamentos dos dados, para verificar a analize completa, verifique o arquivo jupiter analysis.ipynb
tabela = pd.read_excel("Vendas - Dez.xlsx")
faturamento = tabela["Valor Final"].sum()
quantidade = tabela["Quantidade"].sum()

# abrir gmail
pyautogui.press("Win")
sleep(2)
pyautogui.write("Chrome")
pyautogui.press("Enter")
pyautogui.click(x=907, y=622) # No nosso caso, o Chrome irá abrir uma tela para escolhermos o perfil do usuário desejado.
                            # Abra o arquivo position.ipynb para mais info.
sleep(5)

# Entrar no link do email - https://mail.google.com/mail/u/0/#inbox
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://mail.google.com/mail/u/0/#inbox")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
sleep(5)

# clicar no botão escrever
pyautogui.click(x=108, y=244)
sleep(7)

# preencher as informações do e-mail
pyautogui.write("teoalves.dev@gmail.com") #use seu email
pyautogui.press("Enter")
pyautogui.press("tab") # selecionar o email

pyperclip.copy("Relatório de Vendas")
pyautogui.hotkey("ctrl", "v")

pyautogui.press("tab") # pular para o campo de corpo do email

texto = f"""
Prezados,

Segue relatório de vendas.
Faturamento: R${faturamento:,.2f}
Quantidade de produtos vendidos: {quantidade:,}

Qualquer dúvida estou à disposição.
Att.,
Matheus Alves
"""
# formatação dos números (moeda, dinheiro)

pyperclip.copy(texto)
pyautogui.hotkey("ctrl", "v")

# enviar o e-mail
pyautogui.hotkey("ctrl", "enter")