import turtle

    #Funcioines de primer nivel capaces de invocarse a sí misma y generar copias de sí misma
#OBjetos que con el mismo código puedo hacer que sus propiedades y comportamientos sean distintos
tortuguita = turtle.Turtle()
otraTortuguita = turtle.Turtle()

tortuguita.shape('turtle')
tortuguita.fd(50)

otraTortuguita.color('green')
otraTortuguita.left(90)
otraTortuguita.fd(50)