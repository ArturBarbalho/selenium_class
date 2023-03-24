from classes.run import Run
from tkinter import *

#cria o programa
app = Tk()

#configuraçoes do programa
app.title('driverPill')
app.geometry('1366x720') #tamanho da janela
app.configure(background="black") #estilos visuais, parece com css

run = Run()

init = Button(app, command=run.start, text='start srapping')
init.pack()

#abre o programa
app.mainloop()



#https://pt.stackoverflow.com/questions/293902/tkinter-travando-na-fun%C3%A7%C3%A3o

#alterar bootload do pyinstaller para problema no antivirus
#https://pyinstaller.org/en/stable/bootloader-building.html

#resolver console do crhomedriver


