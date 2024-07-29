import pyautogui
import time

pyautogui.click(x=820, y=1053) # Excel
time.sleep(3)
pyautogui.hotkey('ctrl', 'c') # Copia o 'IMEI'
pyautogui.click(x=762, y=1053) # Google
time.sleep(3)
pyautogui.click(x=1310, y=590) # Botão 'OK'
time.sleep(3)
pyautogui.click(x=1600, y=250) # Botão 'ADD USERS'
time.sleep(2)
pyautogui.click(x=850, y=392) # Click 'IMEI'
time.sleep(2)
pyautogui.hotkey('ctrl', 'v') # Cola o "IMEI"
time.sleep(2)
pyautogui.click(x=895, y=452) # Click 'IMEI 2'

# APAGA 'matheus'
pyautogui.hotkey('backspace') 
pyautogui.hotkey('backspace') 
pyautogui.hotkey('backspace') 
pyautogui.hotkey('backspace') 
pyautogui.hotkey('backspace') 
pyautogui.hotkey('backspace') 
pyautogui.hotkey('backspace') 

pyautogui.hotkey('ctrl', 'v') # Cola o "IMEI"
time.sleep(2)
pyautogui.click(x=895, y=590) # Click 'DOMINIO'
time.sleep(2)

#Escreve 'Lactalis'
pyautogui.hotkey('L') 
pyautogui.hotkey('a') 
pyautogui.hotkey('c') 
pyautogui.hotkey('t') 
pyautogui.hotkey('a') 
pyautogui.hotkey('l') 
pyautogui.hotkey('i') 
pyautogui.hotkey('s') 

pyautogui.click(x=895, y=650) # Click 'E-mail'
time.sleep(2)
pyautogui.hotkey('ctrl', 'v') # Cola o "IMEI"

# Digita '@lactalis.com.br'
pyautogui.hotkey('@') 
pyautogui.hotkey('l') 
pyautogui.hotkey('a') 
pyautogui.hotkey('c') 
pyautogui.hotkey('t') 
pyautogui.hotkey('a') 
pyautogui.hotkey('l') 
pyautogui.hotkey('i') 
pyautogui.hotkey('s') 
pyautogui.hotkey('.') 
pyautogui.hotkey('c') 
pyautogui.hotkey('o') 
pyautogui.hotkey('m') 
pyautogui.hotkey('.') 
pyautogui.hotkey('b') 
pyautogui.hotkey('r') 

pyautogui.click(x=895, y=820) # Click 'Dominio'
time.sleep(2)

#Escreve 'Lac'
pyautogui.hotkey('L') 
pyautogui.hotkey('a') 
pyautogui.hotkey('c') 
time.sleep(2)

pyautogui.click(x=895, y=880) # Click 'Kiosk Lactalis'
time.sleep(2)
pyautogui.click(x=865, y=880) # Click 'NUMBER'
time.sleep(2)

#Escreve 'BR'
pyautogui.hotkey('B') 
pyautogui.hotkey('R') 
pyautogui.hotkey('Enter') 

pyautogui.hotkey('TAB') 
pyautogui.hotkey('TAB') 
pyautogui.hotkey('TAB') 

pyautogui.click(x=820, y=800) # Click 'Box'
time.sleep(2)


pyautogui.click(x=1350, y=266) # Click 'Subir'
pyautogui.click(x=1350, y=266) # Click 'Subir'
pyautogui.click(x=1350, y=266) # Click 'Subir'
pyautogui.click(x=1350, y=266) # Click 'Subir'
time.sleep(2)

pyautogui.click(x=706, y=334) # Click 'Advance'
time.sleep(2)

pyautogui.click(x=1033, y=404) # Click 'Polytic'
time.sleep(2)

pyautogui.click(x=840, y=470) # Click 'Android'
time.sleep(2)

pyautogui.click(x=1025, y=460) # Click 'Polytic 2'
time.sleep(2)

pyautogui.click(x=1004, y=656) # Lactalis V3'
time.sleep(2)

pyautogui.hotkey('TAB') 
pyautogui.hotkey('TAB') 
pyautogui.hotkey('TAB') 
pyautogui.hotkey('TAB') 

pyautogui.click(x=1270, y=856) # Click 'Save'
time.sleep(2)

pyautogui.click(x=930, y=350) # Click 'Passwaord'
time.sleep(2)

pyautogui.click(x=1040, y=410) # 
time.sleep(2)

pyautogui.click(x=1230, y=410) # Click 'Confirm'

time.sleep(40)





































