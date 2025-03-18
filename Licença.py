import sys
from tkinter import *

from fontTools.varLib.featureVars import buildGSUB

from Principal import principal


class Licença:
    def __init__(self):
        self.janela= Tk()
        self.janela.title('TERMOS E CONDIÇÕES')
        self.janela.resizable(False,False)
        self.janela.geometry('600x360+340+150')
        self.janela.iconbitmap(r'C:\Calculadora_ferias\icon0.ico')

        self.fundo=PhotoImage(file=r'C:\Calculadora_ferias\coca-cola-l.png')
        Label(self.janela, image=self.fundo).place(x=300,y=220)

        #Labels
        self.label1=Label(self.janela, text='TERMOS E CONDIÇÕES')
        self.label1.config(font=('arial',13,'bold'))
        self.label1.place(x=180, y=10)

        self.texto_condicoes= Text(self.janela, width=96, height=12)
        self.texto_condicoes.configure(font=('arial',8), bg='white', state=NORMAL)
        self.texto_condicoes.insert(INSERT, '''
    TERMOS E CONDIÇÕES

    A. PROIBIDA A VENDA OU DISTRIBUIÇÃO SEM AUTORIZAÇÃO DA EMPRESA.
    B. PROIBIDA A ALTERAÇÃO DO CÓDIGO-FONTE OU DESIGN DAS INTERFACES GRÁFICAS.
    C. A EMPRESA NÃO SE RESPONSABILIZA PELO USO INDEVIDO DESTE SOFTWARE.

    OS ACORDOS LEGAIS EXPOSTOS A SEGUIR REGEM O USO QUE VOCÊ FAÇA DESTE SOFTWARE
    (EMPRESA),NÃO SE RESPONSABILIZANDO PELO USO QUE VOCÊ FAÇA COM ESTE SOFTWARE E SEU SERVIÇO.
    PARA ACEITAR ESTES TERMOS, CLIQUE EM (ACEITO).
    SE VOCÊ NÃO ACEITAR ESTES TERMOS, CLIQUE EM (NÃO ACEITO) E NÃO UTILIZE ESTE SOFTWARE.
    ''')
        self.texto_condicoes.place(x=10,y=40)
        self.texto_condicoes.config(state=DISABLED)

        self.aceito=IntVar()
        self.check_aceito=Checkbutton(self.janela,text='Eu aceito', font=('arial',12,'bold'),\
                                      command=self.aceitar)
        self.check_aceito.place(x=10,y=260)

        #Botão
        self.continuar=Button(self.janela,text='Aceito',font=('arial',11,'bold'),\
                              width=7,height=2,bd=3, state=DISABLED, command=self.acesso)
        self.continuar.place(x=10,y=290)
        self.cancelar = Button(self.janela, text='Cancelar', font=('arial', 11, 'bold'), \
                                width=7, height=2, bd=3, command=self.cancelar)
        self.cancelar.place(x=100, y=290)


        self.janela.mainloop()

    def aceitar(self):
        if (self.continuar['state']==DISABLED):
            self.continuar['state']=NORMAL
        else:
            self.continuar['state']=DISABLED

    def acesso(self):
        self.janela.destroy()
        principal()

    def cancelar(self):
        sys.exit()