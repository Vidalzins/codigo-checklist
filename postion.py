
import pyautogui
import time

try:
    while True:
        # Limpa a tela antes de imprimir a nova posição
        print('\033c', end='')
        
        # Obtém e imprime a posição atual do mouse
        current_mouse_position = pyautogui.position()
        print(f"A posição atual do mouse é: x = {current_mouse_position.x}, y = {current_mouse_position.y}")
        
        # Aguarda um pequeno intervalo antes de atualizar novamente
        time.sleep(1)  # Intervalo de 1 segundo
        
except KeyboardInterrupt:
    print("\nPrograma encerrado pelo usuário.")
