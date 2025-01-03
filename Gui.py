from tkinter import *

class Gui():

    x_pad = 5
    y_pad = 3
    width_entry = 30

    def __init__(self):
        self.window = Tk()
        self.window.wm_title("PySQL versão 1.0")

       
        self.txtNome = StringVar()
        self.txtSobrenome = StringVar()
        self.txtEmail = StringVar()
        self.txtCPF = StringVar()

      
        self.lblnome = Label(self.window, text="Nome")
        self.lblsobrenome = Label(self.window, text="Sobrenome")
        self.lblemail = Label(self.window, text="Email")
        self.lblcpf = Label(self.window, text="CPF")

       
        self.entNome = Entry(self.window, textvariable=self.txtNome, width=self.width_entry)
        self.entSobrenome = Entry(self.window, textvariable=self.txtSobrenome, width=self.width_entry)
        self.entEmail = Entry(self.window, textvariable=self.txtEmail, width=self.width_entry)
        self.entCPF = Entry(self.window, textvariable=self.txtCPF, width=self.width_entry)

        self.listclientes = Listbox(self.window, width=100)
        self.scrollClientes = Scrollbar(self.window)
        self.listclientes.config(yscrollcommand=self.scrollClientes.set)
        self.scrollClientes.config(command=self.listclientes.yview)

       
        self.btnvViewAll = Button(self.window, text="Ver todos")
        self.btnBuscar = Button(self.window, text="Buscar")
        self.btnInserir = Button(self.window, text="Inserir")
        self.btnUpdate = Button(self.window, text="Atualizar Selecionados")
        self.btnDel = Button(self.window, text="Deletar Selecionados")
        self.btnClose = Button(self.window, text="Fechar")

       
        self.lblnome.grid(row=0, column=0, padx=self.x_pad, pady=self.y_pad)
        self.lblsobrenome.grid(row=1, column=0, padx=self.x_pad, pady=self.y_pad)
        self.lblemail.grid(row=2, column=0, padx=self.x_pad, pady=self.y_pad)
        self.lblcpf.grid(row=3, column=0, padx=self.x_pad, pady=self.y_pad)

        self.entNome.grid(row=0, column=1, padx=self.x_pad, pady=self.y_pad)
        self.entSobrenome.grid(row=1, column=1, padx=self.x_pad, pady=self.y_pad)
        self.entEmail.grid(row=2, column=1, padx=self.x_pad, pady=self.y_pad)
        self.entCPF.grid(row=3, column=1, padx=self.x_pad, pady=self.y_pad)

        self.listclientes.grid(row=0, column=2, rowspan=10, padx=self.x_pad, pady=self.y_pad, sticky='NS')
        self.scrollClientes.grid(row=0, column=3, rowspan=10, padx=self.x_pad, pady=self.y_pad, sticky='NS')

        self.btnvViewAll.grid(row=4, column=0, columnspan=2, padx=self.x_pad, pady=self.y_pad, sticky='WE')
        self.btnBuscar.grid(row=5, column=0, columnspan=2, padx=self.x_pad, pady=self.y_pad, sticky='WE')
        self.btnInserir.grid(row=6, column=0, columnspan=2, padx=self.x_pad, pady=self.y_pad, sticky='WE')
        self.btnUpdate.grid(row=7, column=0, columnspan=2, padx=self.x_pad, pady=self.y_pad, sticky='WE')
        self.btnDel.grid(row=8, column=0, columnspan=2, padx=self.x_pad, pady=self.y_pad, sticky='WE')
        self.btnClose.grid(row=9, column=0, columnspan=2, padx=self.x_pad, pady=self.y_pad, sticky='WE')

    def run(self):
        self.window.mainloop()


