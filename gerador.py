from tkinter import *
import random, string
import pyperclip



## janela do programa ######################

root =Tk()
root.geometry("400x300")
root.title("Gerador de Senhas")

heading = Label(root, text = 'Gerador de Senhas' , font ='arial 16 bold').pack()
Label(root, text ='by vicdron', font ='arial 16 bold').pack(side = BOTTOM)

# Seleciona o tamanho da senha
# entre 8 e 32 caracteres ######################

passwd_label = Label(root, text = 'Tamanho da Senha', font = 'arial 12 bold').pack()
passwd_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 32 , textvariable = passwd_len , width = 15).pack()


##### Função que gera a senha ####################

pass_str = StringVar() # variavel q armazenada a senha

def Gerador():
    password = ''
    for x in range (0,4):
        password = random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.digits)+random.choice(string.punctuation)
    for y in range(passwd_len.get()- 4):
        password = password+random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)
   


###button

Button(root, text = "Gerador de Senhas" , command = Gerador ).pack(pady= 5)

Entry(root , textvariable = pass_str).pack()

######## Função para copiar senha

def copiarSenha():
    pyperclip.copy(pass_str.get())
Button(root, text = 'COPIAR', command = copiarSenha).pack(pady=5)



mainloop()
