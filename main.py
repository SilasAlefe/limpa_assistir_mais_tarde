#TAMANHO DE TEXTO DO WINDOWS TEM QUE ESTAR EM 170%

import pyautogui as py
import keyboard
import time

from PIL.ImageOps import grayscale

telas = py.getAllWindows()

for tela in telas:
    tela.minimize()

py.PAUSE = 0.2

py.hotkey('win', 'r')
keyboard.write('C:\\Users\\silas\\OneDrive\\Área de Trabalho\\Eu\\Programação\\estagio_neoenergiacoelba\\Projetos\\limpa_assistir_mais_tarde\\endereco.url')
py.press('enter')
time.sleep(8)
py.moveTo(1105, 490, 0.5)
py.vscroll(-200)

py.hotkey('ctrl', '0')

def localizar_imagem(nome, conf=0.8, tentativas=10):
    for i in range(tentativas):
        pos = py.locateOnScreen(nome, grayscale=True, confidence=conf)
        if pos:
            return pos
        time.sleep(0.5)
    return None

btn1 = localizar_imagem("botao_ordenar.png", conf=0.8)
py.moveTo(btn1, duration=0.2)
py.click()

time.sleep(0.5)

btn2 = localizar_imagem("botao_ordenar_maisantigo.png" or "botao_ordenar_maisantigo2.png", conf=0.8)
py.moveTo(btn2, duration=0.2)
py.click()

py.press('f5')
time.sleep(5)

py.moveTo(1105, 490, 0.5)
py.vscroll(-200)

time.sleep(1)

for a in range(1, 1001):
    btn3 = py.locateOnScreen("botao_3ponto.png", grayscale=True, confidence=.8) #Para funcionar direito tem que instalar o 'Pillow' e 'opencv-pyton'
    py.moveTo(btn3, duration=0.2)
    py.click()

    btn4 = py.locateOnScreen("botao_excluir.png", grayscale=True, confidence=.8)
    py.moveTo(btn4, duration=0.2)
    py.click()