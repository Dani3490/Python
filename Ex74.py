import pygame
import sys
import random

# Inicialitzar Pygame
pygame.init()

# Constants
AMPLADA = 800
ALTURA = 600
FPS = 60

# Colors
BLANC = (255, 255, 255)
NEGRE = (0, 0, 0)
VERMELL = (255, 0, 0)
VERD = (0, 255, 0)
BLAU = (0, 0, 255)
GROC = (255, 255, 0)
TARONJA = (255, 165, 0)

# Crear finestra
pantalla = pygame.display.set_mode((AMPLADA, ALTURA))
pygame.display.set_caption("Arkanoid")
rellotge = pygame.time.Clock()

# Carregar imatges (canviar les rutes segons necessitat)
try:
    img_fons = pygame.image.load("/home/cicles/AO/Tasca11/fons.png")
    img_fons = pygame.transform.scale(img_fons, (AMPLADA, ALTURA))
except:
    img_fons = None

try:
    img_pilota = pygame.image.load("/home/cicles/AO/Tasca11/pilota.png")
    img_pilota = pygame.transform.scale(img_pilota, (20, 20))
except:
    img_pilota = None

try:
    img_pala = pygame.image.load("/home/cicles/AO/Tasca11/pala.png")
    img_pala = pygame.transform.scale(img_pala, (100, 20))
except:
    img_pala = None

try:
    img_totxo = pygame.image.load("/home/cicles/AO/Tasca11/totxo.png")
    img_totxo = pygame.transform.scale(img_totxo, (75, 30))
except:
    img_totxo = None


class Pala:
    def __init__(self):
        self.amplada = 100
        self.altura = 20
        self.x = AMPLADA // 2 - self.amplada // 2
        self.y = ALTURA - 50
        self.velocitat = 8
        self.rect = pygame.Rect(self.x, self.y, self.amplada, self.altura)

    def moure(self, direccio):
        if direccio == "esquerra" and self.x > 0:
            self.x -= self.velocitat
        elif direccio == "dreta" and self.x < AMPLADA - self.amplada:
            self.x += self.velocitat
        self.rect.x = self.x

    def dibuixar(self):
        if img_pala:
            pantalla.blit(img_pala, (self.x, self.y))
        else:
            pygame.draw.rect(pantalla, BLAU, self.rect)


class Pilota:
    def __init__(self):
        self.radi = 10
        self.x = AMPLADA // 2
        self.y = ALTURA - 70
        self.velocitat_x = 5 * random.choice([-1, 1])
        self.velocitat_y = -5
        self.activa = False
        self.rect = pygame.Rect(self.x - self.radi, self.y - self.radi, 
                               self.radi * 2, self.radi * 2)

    def moure(self, pala):
        if not self.activa:
            self.x = pala.x + pala.amplada // 2
            self.y = pala.y - self.radi - 5
        else:
            self.x += self.velocitat_x
            self.y += self.velocitat_y

            # Rebot amb parets
            if self.x - self.radi <= 0 or self.x + self.radi >= AMPLADA:
                self.velocitat_x *= -1

            if self.y - self.radi <= 0:
                self.velocitat_y *= -1

            # Rebot amb la pala
            if self.rect.colliderect(pala.rect) and self.velocitat_y > 0:
                self.velocitat_y *= -1
                # Afegir angle segons on colpeja la pala
                diferencia = (self.x - (pala.x + pala.amplada / 2)) / (pala.amplada / 2)
                self.velocitat_x = 5 * diferencia

        self.rect.x = self.x - self.radi
        self.rect.y = self.y - self.radi

    def dibuixar(self):
        if img_pilota:
            pantalla.blit(img_pilota, (self.x - self.radi, self.y - self.radi))
        else:
            pygame.draw.circle(pantalla, BLANC, (int(self.x), int(self.y)), self.radi)

    def ha_caigut(self):
        return self.y > ALTURA


class Totxo:
    def __init__(self, x, y, color):
        self.amplada = 75
        self.altura = 30
        self.x = x
        self.y = y
        self.color = color
        self.rect = pygame.Rect(x, y, self.amplada, self.altura)
        self.actiu = True

    def dibuixar(self):
        if self.actiu:
            if img_totxo:
                # Canviar el color de la imatge
                img_coloreada = img_totxo.copy()
                img_coloreada.fill(self.color, special_flags=pygame.BLEND_MULT)
                pantalla.blit(img_coloreada, (self.x, self.y))
            else:
                pygame.draw.rect(pantalla, self.color, self.rect)
                pygame.draw.rect(pantalla, NEGRE, self.rect, 2)


def crear_totxos():
    totxos = []
    colors = [VERMELL, TARONJA, GROC, VERD, BLAU]
    files = 5
    columnes = 10
    espai_x = 5
    espai_y = 5
    margin_superior = 60

    for fila in range(files):
        for columna in range(columnes):
            x = columna * (75 + espai_x) + 10
            y = fila * (30 + espai_y) + margin_superior
            color = colors[fila % len(colors)]
            totxos.append(Totxo(x, y, color))

    return totxos


def mostrar_text(text, mida, x, y, color=BLANC):
    font = pygame.font.Font(None, mida)
    superficie = font.render(text, True, color)
    rect = superficie.get_rect(center=(x, y))
    pantalla.blit(superficie, rect)


def joc():
    # Inicialitzar objectes
    pala = Pala()
    pilota = Pilota()
    totxos = crear_totxos()
    
    puntuacio = 0
    vides = 3
    joc_començat = False
    joc_acabat = False
    victori = False

    executant = True
    while executant:
        rellotge.tick(FPS)

        # Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                executant = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not joc_començat:
                    joc_començat = True
                    pilota.activa = True
                elif event.key == pygame.K_SPACE and joc_acabat:
                    # Reiniciar joc
                    pala = Pala()
                    pilota = Pilota()
                    totxos = crear_totxos()
                    puntuacio = 0
                    vides = 3
                    joc_començat = False
                    joc_acabat = False
                    victori = False

        if not joc_acabat:
            # Tecles premudes
            tecles = pygame.key.get_pressed()
            if tecles[pygame.K_LEFT]:
                pala.moure("esquerra")
            if tecles[pygame.K_RIGHT]:
                pala.moure("dreta")

            # Moure pilota
            pilota.moure(pala)

            # Comprovar col·lisions amb totxos
            if pilota.activa:
                for totxo in totxos:
                    if totxo.actiu and pilota.rect.colliderect(totxo.rect):
                        totxo.actiu = False
                        pilota.velocitat_y *= -1
                        puntuacio += 10
                        break

            # Comprovar si la pilota ha caigut
            if pilota.ha_caigut():
                vides -= 1
                if vides <= 0:
                    joc_acabat = True
                else:
                    pilota = Pilota()
                    joc_començat = False

            # Comprovar victòria
            if all(not totxo.actiu for totxo in totxos):
                joc_acabat = True
                victori = True

        # Dibuixar
        if img_fons:
            pantalla.blit(img_fons, (0, 0))
        else:
            pantalla.fill(NEGRE)

        # Dibuixar totxos
        for totxo in totxos:
            totxo.dibuixar()

        # Dibuixar objectes
        pala.dibuixar()
        pilota.dibuixar()

        # Mostrar informació
        mostrar_text(f"Puntuació: {puntuacio}", 30, 80, 20)
        mostrar_text(f"Vides: {vides}", 30, AMPLADA - 80, 20)

        # Missatges
        if not joc_començat and not joc_acabat:
            mostrar_text("Prem ESPAI per començar", 40, AMPLADA // 2, ALTURA // 2)
            mostrar_text("Utilitza ← → per moure la pala", 30, AMPLADA // 2, ALTURA // 2 + 40)

        if joc_acabat:
            if victori:
                mostrar_text("VICTÒRIA!", 60, AMPLADA // 2, ALTURA // 2, GROC)
            else:
                mostrar_text("GAME OVER", 60, AMPLADA // 2, ALTURA // 2, VERMELL)
            mostrar_text(f"Puntuació final: {puntuacio}", 40, AMPLADA // 2, ALTURA // 2 + 60)
            mostrar_text("Prem ESPAI per tornar a jugar", 30, AMPLADA // 2, ALTURA // 2 + 100)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    joc()