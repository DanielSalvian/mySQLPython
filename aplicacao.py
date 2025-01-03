from Gui import *
import objetodeTransacao as core

app = None
db = core.objetodeTransacao() 

def view_command():
    rows = db.view()
    app.listclientes.delete(0, END)
    for r in rows:
        app.listclientes.insert(END, r)

def search_command():
    rows = db.search(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    app.listclientes.delete(0, END)
    for r in rows:
        app.listclientes.insert(END, r)

def insert_command():
    db.insert(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    view_command()

def update_command():
    db.update(selected[0], app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
    view_command()

def del_command():
    db.delete(selected[0])
    view_command()

def getSelectedRow(event):
    global selected
    if app.listclientes.curselection():
        index = app.listclientes.curselection()[0]
        selected = app.listclientes.get(index)
        app.entNome.delete(0, END)
        app.entNome.insert(END, selected[1])
        app.entSobrenome.delete(0, END)
        app.entSobrenome.insert(END, selected[2])
        app.entEmail.delete(0, END)
        app.entEmail.insert(END, selected[3])
        app.entCPF.delete(0, END)
        app.entCPF.insert(END, selected[4])

if __name__ == "__main__":
    app = Gui()
    app.listclientes.bind('<<ListboxSelect>>', getSelectedRow)
    app.btnvViewAll.configure(command=view_command)
    app.btnBuscar.configure(command=search_command)
    app.btnInserir.configure(command=insert_command)
    app.btnUpdate.configure(command=update_command)
    app.btnDel.configure(command=del_command)
    app.btnClose.configure(command=app.window.destroy)
    app.run()
