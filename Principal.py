import sys
from tkinter import *
from tkinter import ttk, messagebox


class principal:
    def __init__(self):
        self.janela= Tk()
        self.janela.title('Pantalla principal')
        self.janela.resizable(False,False)
        self.janela.geometry('640x535+300+60')
        self.janela.config(bg='red')
        self.janela.iconbitmap(r'C:\Calculadora_ferias\icon0.ico')

        #Menú de opções
        self.menubar1=Menu(self.janela)
        self.janela.config(menu=self.menubar1)
        self.opciones1=Menu(self.menubar1, tearoff=0)
        self.opciones2=Menu(self.menubar1, tearoff=0)
        self.menubar1.add_cascade(label='Opções', menu=self.opciones1)
        self.opciones1.add_command(label='Sair', command=self.sair, font=('arial',10,'bold'))

        self.menubar1.add_cascade(label='Sobre..', menu=self.opciones2)
        self.opciones2.add_command(label='Informação', command=self.acerca, font=('arial', 10, 'bold'))

        #Imagem do logo
        self.fundo = PhotoImage(file=r'C:\Calculadora_ferias\coca-cola-p.png')
        Label(self.janela, image=self.fundo, bg='red').place(x=0, y=0)

        #Label boas vindas
        self.l_boas=Label(self.janela, text='Bem-vindos!')
        self.l_boas.config(fg='white',bg='red',font=('andale mono regular',20,'bold'))
        self.l_boas.place(x=340,y=30)

        #Label detalhe
        self.l_detalhe = Label(self.janela, text='Dados do trabalhador para o cálculo de férias')
        self.l_detalhe.config(fg='white', bg='red', font=('andale mono regular', 18, 'bold'))
        self.l_detalhe.place(x=30, y=110)

        # Label nome completo
        self.l_nome = Label(self.janela, text='Nome completo')
        self.l_nome.config(fg='white', bg='red', font=('andale mono regular', 11, 'bold'))
        self.l_nome.place(x=30, y=160)

        self.datonome=StringVar()
        self.e_nome=Entry(self.janela,bd=2,bg='#eee8e8',fg='red',textvariable=self.datonome)
        self.e_nome.config(font=('andale mono regular',12,'bold'), width=22)
        self.e_nome.place(x=30,y=185)

        # Label sobrenome materno
        self.l_smaterno = Label(self.janela, text='Sobrenome materno')
        self.l_smaterno.config(fg='white', bg='red', font=('andale mono regular', 11, 'bold'))
        self.l_smaterno.place(x=30, y=225)

        self.datosobre = StringVar()
        self.e_smaterno = Entry(self.janela, bd=2, bg='#eee8e8', fg='red', textvariable=self.datosobre)
        self.e_smaterno.config(font=('andale mono regular', 12, 'bold'), width=22)
        self.e_smaterno.place(x=30, y=250)

        # Label sobrenome paterno
        self.l_spaterno = Label(self.janela, text='Sobrenome paterno')
        self.l_spaterno.config(fg='white', bg='red', font=('andale mono regular', 11, 'bold'))
        self.l_spaterno.place(x=30, y=295)

        self.datopat = StringVar()
        self.e_spaterno = Entry(self.janela, bd=2, bg='#eee8e8', fg='red', textvariable=self.datopat)
        self.e_spaterno.config(font=('andale mono regular', 12, 'bold'), width=22)
        self.e_spaterno.place(x=30, y=320)

        #Label departamento
        self.l_departamento = Label(self.janela, text='Selecione seu departamento')
        self.l_departamento.config(fg='white', bg='red', font=('andale mono regular', 11, 'bold'))
        self.l_departamento.place(x=310, y=160)

        self.var_combo1=StringVar()
        self.op_combo=(' ', 'Atendimento ao cliente', 'Departamento de logística', 'Departamento de gerência')
        self.combobox1=ttk.Combobox(self.janela, state='readonly',
                                      width=20,font=('andale mono regular',11,'bold'),
                                     textvariable=self.var_combo1,values=self.op_combo)
        self.combobox1.current(0)
        self.combobox1.place(x=310,y=185)

        #select Antiguidade
        self.l_antiguidade = Label(self.janela, text='Selecione a antiguidade')
        self.l_antiguidade.config(fg='white', bg='red', font=('andale mono regular', 11, 'bold'))
        self.l_antiguidade.place(x=310, y=225)

        self.var_combo2 = StringVar()
        self.op_combo2 = (' ', '1 ano de serviço', '2 a 6 anos de serviço', '7 ou mais anos de serviço')
        self.combobox2 = ttk.Combobox(self.janela, state='readonly',
                                      width=20, font=('andale mono regular', 11, 'bold'),
                                      textvariable=self.var_combo2, values=self.op_combo2)
        self.combobox2.current(0)
        self.combobox2.place(x=310, y=250)

        estilo=ttk.Style()
        estilo.theme_use('clam')
        estilo.configure("TCombobox", background='red')

        #Label resultado
        self.l_resultado=Label(self.janela, text='Resultado do cálculo')
        self.l_resultado.config(fg='white',bg='red',font=('andale mono regular',11,'bold'))
        self.l_resultado.place(x=310,y=295)

        self.area_resultado=Text(self.janela,width=35,height=7)
        self.area_resultado.config(font=('andale mono regular',11,'bold'),bg='#eee8e8',\
                                   fg='red', state=DISABLED)
        self.area_resultado.place(x=310,y=320)

        #Rodapé da interface
        self.l_footer = Label(self.janela, text='©2025 The Coca-Cola Company.')
        self.l_footer.config(fg='white', bg='red', font=('andale mono regular', 10, 'bold'))
        self.l_footer.place(x=205, y=480)

        #botoes
        self.b_calcular=Button(self.janela,text='Calcular',width=8,height=2, command=self.control_dados)
        self.b_calcular.config(font=('Andale mono regular',12,'bold'),fg='white',bg='red',bd=5)
        self.b_calcular.place(x=130,y=365)

        self.b_limpar = Button(self.janela, text='Limpar', width=8, height=2, command=self.limpiadados)
        self.b_limpar.config(font=('Andale mono regular', 12, 'bold'), fg='white', bg='red', bd=5)
        self.b_limpar.place(x=30, y=365)

        self.janela.mainloop()

    def control_dados(self):
        if not self.datonome.get() or not self.datosobre.get() or not self.datopat.get()\
            or self.var_combo1.get==' ' or self.var_combo2.get==' ':
            messagebox.showerror('AVISO','NÃO DEVEM FICAR CAMPOS VAZIOS.')
        if len(self.datonome.get())>12 or len(self.datosobre.get())>15 or len(self.datopat.get())>15:
            messagebox.showerror('AVISO','NOME/SOBRENOME(S) MUITO LONGOS.')
        else:
            self.area_resultado.config(state=NORMAL)
            self.area_resultado.delete("1.0","end")
            if self.var_combo1.get()=='Atendimento ao cliente':
                if self.var_combo2.get()=='1 ano de serviço':
                    self.area_resultado.insert(INSERT, self.datonome.get()+' '+self.datosobre.get()+\
                                               ' '+self.datopat.get()+\
                                               '\n Departamento: '+self.var_combo1.get()+\
                                               '\n Antiguidade: '+self.var_combo2.get()+\
                                               '\n\n RECEBE 14 DIAS DE FERIAS')

                if self.var_combo2.get() == '2 a 6 anos de serviço':
                    self.area_resultado.insert(INSERT,
                                               self.datonome.get() + ' ' + self.datosobre.get() + ' ' + self.datopat.get() + \
                                               '\n Departamento: ' + self.var_combo1.get() + \
                                               '\n Antiguidade:' + self.var_combo2.get() + \
                                               '\n\n RECEBE 18 DIAS DE FERIAS')
                if self.var_combo2.get() == '7 ou mais anos de serviço':
                    self.area_resultado.insert(INSERT,
                                               self.datonome.get() + ' ' + self.datosobre.get() + ' ' + self.datopat.get() + \
                                               '\n Departamento: ' + self.var_combo1.get() + \
                                               '\n Antiguidade:' + self.var_combo2.get() + \
                                               '\n\n RECEBE 22 DIAS DE FERIAS')

            if self.var_combo1.get() == 'Departamento de logística':
                    if self.var_combo2.get() == '1 ano de serviço':
                        self.area_resultado.insert(INSERT, self.datonome.get() + ' ' + self.datosobre.get() + \
                                                   ' ' + self.datopat.get() + \
                                                   '\n Departamento: ' + self.var_combo1.get() + \
                                                   '\n Antiguidade: ' + self.var_combo2.get() + \
                                                   '\n\n RECEBE 10 DIAS DE FERIAS')

                    if self.var_combo2.get() == '2 a 6 anos de serviço':
                        self.area_resultado.insert(INSERT,
                                                   self.datonome.get() + ' ' + self.datosobre.get() + ' ' + self.datopat.get() + \
                                                   '\n Departamento: ' + self.var_combo1.get() + \
                                                   '\n Antiguidade:' + self.var_combo2.get() + \
                                                   '\n\n RECEBE 15 DIAS DE FERIAS')
                    if self.var_combo2.get() == '7 ou mais anos de serviço':
                        self.area_resultado.insert(INSERT,
                                                   self.datonome.get() + ' ' + self.datosobre.get() + ' ' + self.datopat.get() + \
                                                   '\n Departamento: ' + self.var_combo1.get() + \
                                                   '\n Antiguidade:' + self.var_combo2.get() + \
                                                   '\n\n RECEBE 20 DIAS DE FERIAS')

            if self.var_combo1.get() == 'Departamento de gerência':
                        if self.var_combo2.get() == '1 ano de serviço':
                            self.area_resultado.insert(INSERT, self.datonome.get() + ' ' + self.datosobre.get() + \
                                                       ' ' + self.datopat.get() + \
                                                       '\n Departamento: ' + self.var_combo1.get() + \
                                                       '\n Antiguidade: ' + self.var_combo2.get() + \
                                                       '\n\n RECEBE 18 DIAS DE FERIAS')

                        if self.var_combo2.get() == '2 a 6 anos de serviço':
                            self.area_resultado.insert(INSERT,
                                                       self.datonome.get() + ' ' + self.datosobre.get() + ' ' + self.datopat.get() + \
                                                       '\n Departamento: ' + self.var_combo1.get() + \
                                                       '\n Antiguidade:' + self.var_combo2.get() + \
                                                       '\n\n RECEBE 25 DIAS DE FERIAS')
                        if self.var_combo2.get() == '7 ou mais anos de serviço':
                            self.area_resultado.insert(INSERT,
                                                       self.datonome.get() + ' ' + self.datosobre.get() + ' ' + self.datopat.get() + \
                                                       '\n Departamento: ' + self.var_combo1.get() + \
                                                       '\n Antiguidade:' + self.var_combo2.get() + \
                                                       '\n\n RECEBE 30 DIAS DE FERIAS')

            self.area_resultado.config(state=DISABLED)


    def acerca(self):
        messagebox.showinfo('Info','''        SISTEMA DE CONTROLE DE FÉRIAS
        Desenvolvido por Kevin Andres Prado Sanchez©
        Direitos reservados 2025''')

    def sair(self):
        sys.exit()



    def limpiadados(self):
        self.area_resultado.config(state=NORMAL)
        self.area_resultado.delete("1.0","end")
        self.area_resultado.config(state=DISABLED)
        self.e_nome.delete("0","end")
        self.e_smaterno.delete("0","end")
        self.e_spaterno.delete("0","end")
        self.combobox1.current(0)
        self.combobox2.current(0)

