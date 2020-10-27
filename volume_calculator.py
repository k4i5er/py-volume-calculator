from tkinter.ttk import Frame, Button, Entry, Label, Style
from tkinter import Tk, END, LEFT, X


def litters_to_all(litter):
    declitter = litter * 10
    millilitter = litter * 1000
    gallon = litter * 0.2642
    ounce = litter * 33.81
    entry_declitter.delete(0, END)
    entry_millilitter.delete(0, END)
    entry_gallon.delete(0, END)
    entry_ounce.delete(0, END)
    entry_declitter.insert(0, str(declitter))
    entry_millilitter.insert(0, str(millilitter))
    entry_gallon.insert(0, str(gallon))
    entry_ounce.insert(0, str(ounce))
    entry_declitter.state(['readonly'])
    entry_millilitter.state(['readonly'])
    entry_gallon.state(['readonly'])
    entry_ounce.state(['readonly'])


def declitters_to_all(declitter):
    litter = declitter * 10
    millilitter = declitter * 1000
    gallon = declitter * 0.2642
    ounce = declitter * 33.81
    entry_litter.delete(0, END)
    entry_millilitter.delete(0, END)
    entry_gallon.delete(0, END)
    entry_ounce.delete(0, END)
    entry_litter.insert(0, str(litter))
    entry_millilitter.insert(0, str(millilitter))
    entry_gallon.insert(0, str(gallon))
    entry_ounce.insert(0, str(ounce))
    entry_litter.state(['readonly'])
    entry_millilitter.state(['readonly'])
    entry_gallon.state(['readonly'])
    entry_ounce.state(['readonly'])


def new_conversion():
    entry_litter.state(['!readonly'])
    entry_declitter.state(['!readonly'])
    entry_millilitter.state(['!readonly'])
    entry_gallon.state(['!readonly'])
    entry_ounce.state(['!readonly'])

    entry_litter.delete(0, END)
    entry_declitter.delete(0, END)
    entry_millilitter.delete(0, END)
    entry_gallon.delete(0, END)
    entry_ounce.delete(0, END)

    btn_conversion.configure(text='Convertir', command=do_conversion)


def do_conversion():
    if len((entry_litter.get())) > 0 and len(entry_declitter.get()) == 0 and len(entry_millilitter.get()) == 0 and len(entry_gallon.get()) == 0 and len(entry_ounce.get()) == 0:
        # Aquí va la llamada a la función de conversión
        try:
            litters_to_all(float(entry_litter.get()))
            btn_conversion.configure(
                text='Nueva conversión', command=new_conversion)
            lbl_error.pack_forget()
        except:
            lbl_error.configure(
                text='ERROR: Escribe sólo números', style='error_lbl.TLabel')
            lbl_error.pack(before=frm_litter)

    elif len((entry_declitter.get())) > 0 and len(entry_litter.get()) == 0 and len(entry_millilitter.get()) == 0 and len(entry_gallon.get()) == 0 and len(entry_ounce.get()) == 0:
        # Aquí va la llamada a la función de conversión
        declitters_to_all(float(entry_declitter.get()))
        btn_conversion.configure(
            text='Nueva conversión', command=new_conversion)
        lbl_error.pack_forget()
    else:
        # Aquí tengo que decirle al usuario que no escriba en más de un lugar
        lbl_error.configure(
            text='ERROR: Escribe en un sólo cuado para\nconvertir a las demás unidades', style='error_lbl.TLabel')
        lbl_error.pack(pady=5, before=frm_litter)


root = Tk()

root.geometry('300x350')
root.title('Convertidor de unidades de volumen v1.0')

myStyle = Style()
myStyle.configure('error_lbl.TLabel', foreground='red')

Label(root, text='Convertidor de unidades').pack(pady=10)

lbl_error = Label(root)

frm_litter = Frame(root)
Label(frm_litter, text='Litros').pack(side=LEFT)
entry_litter = Entry(frm_litter)
entry_litter.pack(side=LEFT, padx=10, fill=X, expand=1)
frm_litter.pack(fill=X, padx=10, pady=10)

frm_declitter = Frame(root)
Label(frm_declitter, text='Decilitros').pack(side=LEFT)
entry_declitter = Entry(frm_declitter)
entry_declitter.pack(side=LEFT, padx=10, fill=X, expand=1)
frm_declitter.pack(fill=X, padx=10, pady=10)

frm_millilitter = Frame(root)
Label(frm_millilitter, text='Mililitros').pack(side=LEFT)
entry_millilitter = Entry(frm_millilitter)
entry_millilitter.pack(side=LEFT, padx=10, fill=X, expand=1)
frm_millilitter.pack(fill=X, padx=10, pady=10)

frm_gallon = Frame(root)
Label(frm_gallon, text='Galón').pack(side=LEFT)
entry_gallon = Entry(frm_gallon)
entry_gallon.pack(side=LEFT, padx=10, fill=X, expand=1)
frm_gallon.pack(fill=X, padx=10, pady=10)

frm_ounce = Frame(root)
Label(frm_ounce, text='Onzas').pack(side=LEFT)
entry_ounce = Entry(frm_ounce)
entry_ounce.pack(side=LEFT, padx=10, fill=X, expand=1)
frm_ounce.pack(fill=X, padx=10, pady=10)

frm_buttons = Frame(root)
btn_conversion = Button(frm_buttons, text='Convertir', command=do_conversion)
btn_conversion.pack(side=LEFT, expand=1)
Button(frm_buttons, text='Salir', command=root.destroy).pack(side=LEFT, expand=1)
frm_buttons.pack(fill=X, pady=20)

root.mainloop()
