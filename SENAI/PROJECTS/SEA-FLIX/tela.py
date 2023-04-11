from tkinter import *
from tkinter import ttk
from create import creat_db

janela = Tk()

class ApplicationX():
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frames()
        self.botoes()
        self.labels()
        self.inputs()
        self.lista_frame2()
        janela.mainloop()

    def tela(self):
        self.janela.title("SEA-FLIX")
        self.janela.geometry('700x500')
        self.janela.configure(background="#2596be")
        self.janela.resizable(True, True)
        self.janela.maxsize(width='700', height='500')
        self.janela.minsize(width='700', height='500')
    
    def frames(self):
        self.frame_0 = Frame(self.janela, bg='green',
        highlightthickness=0.5, highlightbackground="red",)
        self.frame_0.place(relx=0.03, rely=0.03, relwidth=0.94, relheight=0.11)

        self.frame_1 = Frame(self.janela, bg='darkblue',
        highlightthickness=0.5, highlightbackground="red",)
        self.frame_1.place(relx=0.03, rely=0.20, relwidth=0.94, relheight=0.35)
        
        self.frame_2 = Frame(self.janela, bg='darkblue',
        highlightthickness=0.5, highlightbackground="red",)
        self.frame_2.place(relx=0.03, rely=0.60, relwidth=0.94, relheight=0.35)

    def botoes(self):
        self.bt_buscar = Button(self.frame_0, text='Buscar', bg="#70bfb3")
        self.bt_buscar.place(relx=0.10, rely=0.25, relwidth=0.1, relheight=0.5)

        self.bt_limpar = Button(self.frame_0, text='Limpar', bg="#70bfb3")
        self.bt_limpar.place(relx=0.22, rely=0.25, relwidth=0.1, relheight=0.5)
        
        #CRUD 
        self.bt_create = Button(self.frame_0, text='Create', bg="#70bfb3", command=self.insert_user)
        self.bt_create.place(relx=0.40, rely=0.25, relwidth=0.1, relheight=0.5)

        self.bt_read = Button(self.frame_0, text='Read', bg="#70bfb3")
        self.bt_read.place(relx=0.52, rely=0.25, relwidth=0.1, relheight=0.5)

        self.bt_update = Button(self.frame_0, text='Update', bg="#70bfb3")
        self.bt_update.place(relx=0.64, rely=0.25, relwidth=0.1, relheight=0.5)

        self.bt_delete = Button(self.frame_0, text='Delete', bg="#70bfb3")
        self.bt_delete.place(relx=0.76, rely=0.25, relwidth=0.1, relheight=0.5)

    def labels(self):
        self.lb_id_user = Label(self.frame_0, text="ID", background='#70bfb3')
        self.lb_id_user.place(relx=0.005, rely=0.01, relwidth=0.1,relheight=0.3)
        
        self.lb_name_user = Label(self.frame_1, text="Name", background='#70bfb3')
        self.lb_name_user.place(relx=0.005, rely=0.05, relwidth=0.1,relheight=0.15)
        
        self.lb_email_user = Label(self.frame_1, text="Email", background='#70bfb3')
        self.lb_email_user.place(relx=0.005, rely=0.25, relwidth=0.1,relheight=0.15)
        
        self.lb_plan_user = Label(self.frame_1, text="Plan", background='#70bfb3')
        self.lb_plan_user.place(relx=0.005, rely=0.45, relwidth=0.1,relheight=0.15)
        
        self.lb_type_user = Label(self.frame_1, text="Type", background='#70bfb3')
        self.lb_type_user.place(relx=0.3, rely=0.45, relwidth=0.1,relheight=0.15)
        
        self.lb_age_user = Label(self.frame_1, text="Age", background='#70bfb3')
        self.lb_age_user.place(relx=0.6, rely=0.45, relwidth=0.1,relheight=0.15)

    def inputs(self):
        self.input_id_user = Entry(self.frame_0)
        self.input_id_user.place(relx=0.005, rely=0.35, relwidth=0.1, relheight=0.5)
        
        self.input_name_user = Entry(self.frame_1)
        self.input_name_user.place(relx=0.12, rely=0.05, relwidth=0.85, relheight=0.15)

        self.input_email_user = Entry(self.frame_1)
        self.input_email_user.place(relx=0.12, rely=0.25, relwidth=0.85, relheight=0.15)
        
        self.input_plan_user = Entry(self.frame_1)
        self.input_plan_user.place(relx=0.12, rely=0.45, relwidth=0.15, relheight=0.15)
        
        self.input_type_user = Entry(self.frame_1)
        self.input_type_user.place(relx=0.42, rely=0.45, relwidth=0.15, relheight=0.15)
        
        self.input_age_user = Entry(self.frame_1)
        self.input_age_user.place(relx=0.82, rely=0.45, relwidth=0.15, relheight=0.15)

    
    def lista_frame2(self):
        self.lista_cliente = ttk.Treeview(self.frame_2, height=3, columns=('col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7'))
        self.lista_cliente.heading('#0', text='')
        self.lista_cliente.heading('#1', text='ID')
        self.lista_cliente.heading('#2', text='Name')
        self.lista_cliente.heading('#3', text='E-mail')
        self.lista_cliente.heading('#4', text='Plan')
        self.lista_cliente.heading('#5', text='Type')
        self.lista_cliente.heading('#6', text='Age')

        self.lista_cliente.column("#0", width=1)
        self.lista_cliente.column("#1", width=10)
        self.lista_cliente.column("#2", width=210)
        self.lista_cliente.column("#3", width=210)
        self.lista_cliente.column("#4", width=50)
        self.lista_cliente.column("#5", width=50)
        self.lista_cliente.column("#6", width=50)

        self.lista_cliente.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

    def insert_user(self):
        creat_db(self.input_name_user.get(),
                 self.input_age_user.get(),
                 self.input_email_user.get(),
                 self.input_plan_user.get(),
                 self.input_type_user.get(),
                 self.input_id_user.get())
