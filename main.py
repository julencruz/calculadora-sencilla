import tkinter as tk
def ANS(operaciones, ultimo):
    cadena = list(str(ultimo[-1]))
    for elemento in cadena:
        operaciones.append(elemento)
    pantalla.config(text=operaciones)
    resultado.config(text="")

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
        if (elemento == "-" and len(aux) == 0) or (elemento == "+" and len(aux) == 0) or elemento == "." or elemento == "0" or elemento == "1" or elemento == "2" or elemento == "3" or elemento == "4" or elemento == "5" or elemento == "6" or elemento == "7" or elemento == "8" or elemento == "9":
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
                else:
                    operacion.append(elemento)
                    resultado.config(text="SYNTAX\nERROR")


    if len(aux) > 0:
        if aux.count(".") > 1:
            resultado.config(text="SYNTAX\nERROR")
        else:
            operacion.append(float("".join(map(str, aux))))

def PEMDAS(operacion):
    result = 0
    aux = []
    if operacion.count("×") > 0 or operacion.count("÷"):
        try:
            pemdas = operacion.index("×")
            result = operacion[pemdas-1] * operacion[pemdas+1]
            elemento = 0
            while elemento < len(operacion):
                if elemento == pemdas-1:
                    aux.append(result)
                    elemento += 3
                else:
                    aux.append(operacion[elemento])
                    elemento += 1
            operacion.clear()
            for elemento in aux:
                operacion.append(elemento)
            print(operacion)


        except:
            pemdas = operacion.index("÷")
            if operacion[pemdas+1] == 0:
                resultado.config(text="MATH\nERROR")
            result = operacion[pemdas - 1] / operacion[pemdas + 1]
            elemento = 0
            while elemento < len(operacion):
                if elemento == pemdas - 1:
                    aux.append(result)
                    elemento += 3
                else:
                    aux.append(operacion[elemento])
                    elemento += 1
            operacion.clear()
            for elemento in aux:
                operacion.append(elemento)
            print(operacion)




def operar(operaciones, ultimo):
    operacion=[]
    unir(operaciones, operacion)
    error = False
    print(operacion)
    if (operacion[-1] == "+" or operacion[-1] == "-" or operacion[-1] == "×" or operacion[-1] == "÷"):
        resultado.config(text="SYNTAX\nERROR")
    else:
        while operacion.count("÷") > 0 or operacion.count("×") > 0:
            PEMDAS(operacion)

    resultante = 0

    if operacion[0] == "×" or operacion[0] == "÷" or operacion[-1] == "+" or operacion[-1] == "-" or operacion[-1] == "×" or operacion[-1] == "÷":
        resultado.config(text="SYNTAX\nERROR")
    else:
        primero = True
        for elemento in range(len(operacion)):
            if (isinstance(operacion[elemento], int) or isinstance(operacion[elemento], float)) and primero == True:
                resultante = float(operacion[elemento])
                primero = False
            else:
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
            ultimo.append(resultante)
            print(resultante)
            resultado.config(text=str(round(resultante,4)))

def escribir(tecla):
    operaciones.append(tecla)
    pantalla.config(text=operaciones)

''' Calculator UI '''

operaciones = []
ventana = tk.Tk()
ultimo = []
ventana.config(height=305, width=340, bg="#cfcfcf", cursor="hand2")
ventana.title("Calculadora")
pantalla = tk.Label(font="Arial 15", anchor="w", cursor="arrow", borderwidth="5")
pantalla.place(width=220, height=75, x=5, y=5)
resultado = tk.Label(font="Arial 15", anchor="w", cursor="arrow", borderwidth="5")
resultado.place(height=75, width=105, x=230, y=5)
botonANS = tk.Button(text="ANS", font="Arial 15", command=lambda: ANS(operaciones, ultimo))
botonDecimal = tk.Button(text=",", font="Arial 15", command=lambda: escribir("."))
botonIgual = tk.Button(text="=", font="Arial 15", command=lambda: operar(operaciones, ultimo))
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
botonANS.place(width=70, height=50, x=155, y=250)
botonIgual.place(width=105, height=50, x=230, y=250)
botonSuma.place(width=50, height=50, x=230, y=140)
botonResta.place(width=50, height=50, x=230, y=195)
botonMultiplica.place(width=50, height=50, x=285, y=140)
botonDivide.place(width=50, height=50, x=285, y=195)
botonDEL.place(width=50, height=50, x=230, y=85)
botonAC.place(width=50, height=50, x=285, y=85)
ventana.mainloop()


