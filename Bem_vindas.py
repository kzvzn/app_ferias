from tkinter import *
from tkinter import messagebox

from Licença import Licença


class Bemvinda:
    def __init__(self):
        self.janela=Tk()
        self.janela.title('Acesso')
        self.janela.resizable(False,False)
        self.janela.geometry('350x450+450+130')
        self.janela.config(bg='red')
        self.janela.iconbitmap(r'C:\Calculadora_ferias\icon0.ico')

        self.fundo= PhotoImage(file=r'C:\Calculadora_ferias\logo-coca.png')
        Label(self.janela, image=self.fundo, bg='red').pack()

        #Labels
        self.label1=Label(self.janela, text='Sistema de controle de férias.')
        self.label1.config(fg='White',bg='red',font=('Andale Mono Regular',18,'italic'))
        self.label1.place(x=10,y=140)
        self.label2=Label(self.janela, text='Digite seu nome')
        self.label2.config(fg='white', bg='red',font=('Andale Mono Regular',12,'bold'))
        self.label2.place(x=50,y=230)
        self.label3=Label(self.janela, text='©2025 The Coca-Cola Company')
        self.label3.config(fg='white',bg='red', font=('Andale Mono Regular',10,'bold'))
        self.label3.place(x=70,y=410)


        #Entry nome user
        self.dado1=StringVar()
        self.entry1=Entry(self.janela, bd=2, bg='#eee8e8',fg='red',textvariable=self.dado1)
        self.entry1.config(font=('Andale Mono Regular',12,'bold'), width=27)
        self.entry1.place(x=50, y=255)

        #Botão
        self.botao1= Button(self.janela, text='Entrar',bd=2,bg='white',fg='red')
        self.botao1.config(font=('Andale Mono Regular',14), width=12, command=self.acesso)
        self.botao1.place(x=100,y=285)

        self.janela.mainloop()

    def acesso(self):
        self.largo=self.dado1.get()
        if not self.dado1.get():
            messagebox.showerror('Atenção', 'Deve colocar o nome de usuário!')
        elif len(self.largo)>0 and len(self.largo)<8:
            messagebox.showerror('Atenção', 'O nome de usuário deve ter mais de 8 caracteres')
        else:
            self.janela.destroy()
            Licença()


if __name__=='__main__':
    ejecutar=Bemvinda()





