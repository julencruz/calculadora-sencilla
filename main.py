import tkinter as tk
def AC():
    operaciones.clear()
    pantalla.config(text=operaciones)
    resultado.config(text="")

def DEL():
    if len(operaciones) > 0:
        operaciones.pop()
    pantalla.config(text=operaciones)
    resultado.config(text="")

def unir(operaciones, operacion):
    aux = []
    for elemento in operaciones:
        if elemento == "." or elemento == "0" or elemento == "1" or elemento == "2" or elemento == "3" or elemento == "4" or elemento == "5" or elemento == "6" or elemento == "7" or elemento == "8" or elemento == "9":
            aux.append(elemento)
        else:
            if elemento == "+" or elemento == "-" or elemento == "÷" or elemento == "×":
                if len(aux) > 0:
                    if aux.count(".") > 1:
                        resultado.config(text="SYNTAX\nERROR")
                    else:
                        operacion.append(float("".join(map(str, aux))))
                        aux.clear()
                        operacion.append(elemento)


    if len(aux) > 0:
        if aux.count(".") > 1:
            resultado.config(text="SYNTAX\nERROR")
        else:
            operacion.append(float("".join(map(str, aux))))

def operar(operaciones):
    operacion=[]
    unir(operaciones, operacion)
    resultante = 0
    error = False
    print(operacion)
    if operacion[0] == "×" or operacion[0] == "÷" or operacion[-1] == "+" or operacion[-1] == "-" or operacion[-1] == "×" or operacion[-1] == "÷":
        resultado.config(text="SYNTAX\nERROR")
    else:
        primero = True
        for elemento in range(len(operacion)):
            if (isinstance(operacion[elemento], int) or isinstance(operacion[elemento], float)) and primero == True:
                resultante = float(operacion[elemento])
                primero = False
            else:
                '''
                PEMDAS TO-DO
                IZQUIERDA A DERECHA
                1 - Multiplicar/Dividir
                2 - Sumar/Restar
                Puede que con un lista.count() o un lista.index()
                '''
                if operacion[elemento] == "+":
                    resultante += operacion[elemento+1]
                else:
                    if operacion[elemento] == "-":
                        resultante -= operacion[elemento+1]
                    else:
                        if operacion[elemento] == "×":
                            resultante *= operacion[elemento+1]
                        else:
                            if operacion[elemento] == "÷":
                                if operacion[elemento+1] == 0:
                                    error = True
                                    resultado.config(text="MATH\nERROR")
                                else:
                                    resultante /= operacion[elemento+1]
        if not(error):
            resultado.config(text=str(round(float(resultante),4)))

def escribir(tecla):
    operaciones.append(tecla)
    pantalla.config(text=operaciones)

operaciones = []

ventana = tk.Tk()
ventana.config(height=305, width=340, bg="#cfcfcf")
ventana.title("Calculadora")

pantalla = tk.Label(font="Arial 15", anchor="w")
pantalla.place(width=220, height=75, x=5, y=5)
resultado = tk.Label(font="Arial 15", anchor="w")
resultado.place(height=75, width=105, x=230, y=5)

botonArchivo = tk.Button(text="ARC", font="Arial 15")
botonDecimal = tk.Button(text=",", font="Arial 15", command=lambda: escribir("."))
botonIgual = tk.Button(text="=", font="Arial 15", command=lambda: operar(operaciones))
boton0 = tk.Button(text="0", font = "Arial 15", command=lambda: escribir("0"))
boton1 = tk.Button(text="1", font = "Arial 15", command=lambda: escribir("1"))
boton2 = tk.Button(text="2", font = "Arial 15", command=lambda: escribir("2"))
boton3 = tk.Button(text="3", font = "Arial 15", command=lambda: escribir("3"))
boton4 = tk.Button(text="4", font = "Arial 15", command=lambda: escribir("4"))
boton5 = tk.Button(text="5", font = "Arial 15", command=lambda: escribir("5"))
boton6 = tk.Button(text="6", font = "Arial 15", command=lambda: escribir("6"))
boton7 = tk.Button(text="7", font = "Arial 15", command=lambda: escribir("7"))
boton8 = tk.Button(text="8", font = "Arial 15", command=lambda: escribir("8"))
boton9 = tk.Button(text="9", font = "Arial 15", command=lambda: escribir("9"))
botonSuma = tk.Button(text="+", font="Arial 15", command=lambda: escribir("+"))
botonResta = tk.Button(text="-", font="Arial 15", command=lambda: escribir("-"))
botonMultiplica = tk.Button(text="×", font="Arial 15", command=lambda: escribir("×"))
botonDivide = tk.Button(text="÷", font="Arial 15", command=lambda: escribir("÷"))
botonDEL = tk.Button(text="DEL", font="Arial 15", command=DEL)
botonAC = tk.Button(text="AC", font="Arial 15", command=AC)

boton7.place(width=70, height=50, x=5, y=85)
boton8.place(width=70, height=50, x=80, y=85)
boton9.place(width=70, height=50, x=155, y=85)
boton4.place(width=70, height=50, x=5, y=140)
boton5.place(width=70, height=50, x=80, y=140)
boton6.place(width=70, height=50, x=155, y=140)
boton1.place(width=70, height=50, x=5, y=195)
boton2.place(width=70, height=50, x=80, y=195)
boton3.place(width=70, height=50, x=155, y=195)
boton0.place(width=70, height=50, x=5, y=250)
botonDecimal.place(width=70, height=50, x=80, y=250)
botonArchivo.place(width=70, height=50, x=155, y=250)
botonIgual.place(width=105, height=50, x=230, y=250)
botonSuma.place(width=50, height=50, x=230, y=140)
botonResta.place(width=50, height=50, x=230, y=195)
botonMultiplica.place(width=50, height=50, x=285, y=140)
botonDivide.place(width=50, height=50, x=285, y=195)
botonDEL.place(width=50, height=50, x=230, y=85)
botonAC.place(width=50, height=50, x=285, y=85)


ventana.mainloop()


