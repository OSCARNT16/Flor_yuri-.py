import turtle  
from playsound import playsound  
import threading  

# Función para reproducir música
def reproducir_musica():
    playsound("amlr.mp3", block=False)  # Cambia el nombre por tu canción

# Iniciar la música en un hilo separado
musica = threading.Thread(target=reproducir_musica)
musica.start()

# Configuración de la pantalla
screen = turtle.Screen()
screen.title("Flor Amarilla para Yuri 🌻")
screen.bgcolor("white")

# Flor
flor = turtle.Turtle()
flor.speed(0)
flor.width(2)

# Dibujar pétalos
def petalo(t, color):
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.circle(100, 60)
        t.left(120)
    t.end_fill()

# Pétalos
flor.penup()
flor.goto(0, 0)
flor.setheading(0)

colores = ["yellow", "gold", "orange"]

for i in range(12):
    flor.setheading(i * 30)
    petalo(flor, colores[i % len(colores)])

# Centro de la flor
flor.penup()
flor.goto(0, -30)
flor.setheading(0)
flor.pendown()
flor.color("darkorange")
flor.begin_fill()
flor.circle(30)
flor.end_fill()

# Tallo
flor.penup()
flor.goto(0, -30)
flor.setheading(270)
flor.pendown()
flor.color("green")
flor.width(10)
flor.forward(150)

# Hojas
def hoja(t, size):
    t.color("forest green")
    t.begin_fill()
    for _ in range(2):
        t.circle(size, 90)
        t.circle(size // 2, 90)
    t.end_fill()

# Dos hojas
flor.penup()
flor.goto(0, -100)
flor.setheading(45)
flor.pendown()
hoja(flor, 50)

flor.penup()
flor.goto(0, -130)
flor.setheading(-45)
flor.pendown()
hoja(flor, 50)

# Texto personalizado
texto = turtle.Turtle()
texto.hideturtle()
texto.penup()
texto.goto(0, 60)
texto.color("darkred")
texto.write("Para Yuri 🌻", align="center", font=("Arial", 20, "bold"))

# Finalizar
flor.hideturtle()
screen.mainloop()
