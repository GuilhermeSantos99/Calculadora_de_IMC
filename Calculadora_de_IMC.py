from tkinter import *

root = Tk()
cor = '#B0E0E6'
fonte = 'Courier 12'
root.title('Calculadora de IMC')
root.configure(bg = cor)
root.geometry('500x300')
root.resizable(False, False)
largura = 400
altura = 200

largura_tela = root.winfo_screenwidth()
altura_tela = root.winfo_screenheight()

posx = largura_tela / 2 - largura / 2
posy = altura_tela / 2 - altura / 2

root.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

def calcular():   
    altura = float(text_box_altura.get())
    massa = float(text_box_massa.get())
    imc = massa / (altura ** 2)

    label_IMC = Label(
    root,
    text = f'IMC = {imc:.2f}',
    font = f'{fonte}',
    bg = f'{cor}'
).pack()
       
    if imc < 16.9:
        Faixa = ('Muito abaixo do peso')
    elif 17 <= imc <= 18.4:
        Faixa = ('Abaixo do peso')   
    elif 18.5 <= imc <= 24.9:
        Faixa = ('Peso normal')
    elif 25 <= imc <= 29.9:
        Faixa = ('Acima do peso')
    elif 30 <= imc <= 34.9:
        Faixa = ('Obesidade Grau I')
    elif 35 <= imc <= 40:
        Faixa = ('Obesidade Grau II')
    elif imc > 40:
        Faixa = ('Obesidade Grau III')

    label_Faixa = Label(
    root,
    text = f'Classificação: {Faixa}',
    font = f'{fonte}',
    bg = f'{cor}'   
).pack()
    
label_Altura = Label(
    root, 
    text = 'Digite a altura em metros:',
    font = f'{fonte}',
    bg = f'{cor}'
).pack()

text_box_altura = StringVar()
text_box_altura = Entry(root, textvariable = text_box_altura)
text_box_altura.focus()
text_box_altura.pack()

label_Peso = Label(
    root,
    text = 'Digite a massa em kg:',
    font = f'{fonte}',
    bg = f'{cor}'
).pack()

text_box_massa = StringVar()
text_box_massa = Entry(root, textvariable = text_box_massa)
text_box_massa.pack()

Botão = Button(
    root, text = 'Calcular IMC', 
    bg = f'{cor}', 
    borderwidth = 4,
    relief = 'groove',
    font = f'{fonte}',
    command = lambda: calcular()
    )
Botão.pack()

root.mainloop()
        