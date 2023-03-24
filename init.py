from classes.run import Run
from tkinter import *
import threading

#cria o programa
app = Tk()

#configuraçoes do programa
app.title('driverPill')
app.geometry('1366x720') #tamanho da janela
app.configure(background="black") #estilos visuais, parece com css

def start():
    run = Run()
    #evita que app fique travado enquanto executa função
    threading.Thread(target=run.start).start()


init = Button(app, command=start, text='start srapping')
init.pack()

#abre o programa
app.mainloop()





#alterar bootload do pyinstaller para problema no antivirus
#https://pyinstaller.org/en/stable/bootloader-building.html




