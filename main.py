# IMPORTANTE: ler o arquivo README.md é de suma importância para a compriensão do projeto.
# A main é uma demostração de como baixar o nosso banco de dados, mas neste projeto ja disponilizarei o arquivo.

import pyautogui
from time import sleep # biblioteca para a espero de um determinado código
import pyperclip 

# pyautogui.click -> clicar  rightClick(Botão direito)
# pyautogui.press -> apertar 1 tecla
# pyautogui.hotkey -> conjunto de teclas
# pyautogui.write -> escreve um texto

pyautogui.PAUSE = 1

# Entrar no sistema da empresa (no nosso caso é o link do drive)
pyautogui.press("Win")
pyautogui.write("Chrome")
pyautogui.press("Enter")
pyautogui.click(x=907, y=622) # No nosso caso, o Chrome irá abrir uma tela para escolhermos o perfil do usuário desejado.
                            # Abra o arquivo position.ipynb para mais info.
sleep(5)
pyautogui.hotkey("ctrl", "t")
pyperclip.copy("https://drive.google.com/drive/folders/1EbYxfjkfLz2qANcm5EvUuP5LyEXEt2aP?usp=sharing")
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")
sleep(10)

# Fazer o download da base de vendas
pyautogui.rightClick(x=531, y=543)
pyautogui.click(x=686, y=922)
sleep(5)

# Após o download seguiremos no arquivo send_email.py