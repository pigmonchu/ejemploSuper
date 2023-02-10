import pygame as pg
pg.init()
WIDTH = 800
HEIGHT = 600

class Dibujo:
    def __init__(self, x = WIDTH//2, y = HEIGHT//2):
        self.x = x
        self.y = y
        self.vx = 5
        self.vy = 0

        self.disfraces = []
        self.posicion_disfraz = 0
        self.disfraz = None

    def actualizar(self):
        #Cambia la posición (movimiento)
        self.x += self.vx
        if self.x < 0 or self.x > WIDTH:
            self.vx *= -1

        self.y += self.vy
        if self.y < 0 or self.y > HEIGHT:
            self.vy *= -1

        #cambia la foto (animación)
        self.posicion_disfraz += 1
        if self.posicion_disfraz >= len(self.disfraces):
            self.posicion_disfraz = 0

        self.disfraz = self.disfraces[0]

class Robot(Dibujo):
    def __init__(self, x = WIDTH//2, y = HEIGHT//2):
        super().__init__(x, y)


        self.disfraces.append(pg.image.load("images/robot_r01.png"))
        self.disfraces.append(pg.image.load("images/robot_r02.png"))
        self.disfraces.append(pg.image.load("images/robot_r03.png"))
        self.disfraces.append(pg.image.load("images/robot_r04.png"))

        self.posicion_disfraz = 0
        self.disfraz = self.disfraces[0]
    

class Gatita(Dibujo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.disfraces = [pg.image.load("images/kitti.png")]

class Juego:

    def __init__(self):
        self.pantalla = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Un ejemplo")
        self.jugador = Robot()
        self.perseguidor = Robot(100, 150)
        self.perseguidor.vy = -3
        self.gatita = Gatita(300, 300)

    def bucle_principal(self):
        salir = False
        while not salir:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    salir = True

            self.jugador.actualizar()
            self.perseguidor.actualizar()
            self.gatita.actualizar()
            

            self.pantalla.fill((125, 229, 100))
            self.pantalla.blit(self.jugador.disfraz, (self.jugador.x, self.jugador.y))
            self.pantalla.blit(self.perseguidor.disfraz, (self.perseguidor.x, self.perseguidor.y))
            self.pantalla.blit(self.gatita.disfraz, (self.gatita.x, self.gatita.y))

            pg.display.flip()

