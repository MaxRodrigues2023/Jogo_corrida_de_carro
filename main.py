import os
import random
import sys
import pygame

# Inicialização do Pygame e do mixer
pygame.init()
pygame.mixer.init()


# Função para converter caminhos relativos em absolutos
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


# Configurações da tela
LARGURA_TELA = 900
ALTURA_TELA = 600
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Car on the Road")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
CINZA = (100, 100, 100)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Carregar assets
carro_jogador_img = pygame.image.load(resource_path("asset/carro_jogador.png"))
carro_contrario_1_img = pygame.image.load(resource_path("asset/carro_contrario_1.png"))
carro_contrario_2_img = pygame.image.load(resource_path("asset/carro_contrario_2.png"))
carro_contrario_3_img = pygame.image.load(resource_path("asset/carro_contrario_3.png"))
carro_contrario_4_img = pygame.image.load(resource_path("asset/carro_contrario_4.png"))
carro_contrario_5_img = pygame.image.load(resource_path("asset/carro_contrario_5.png"))
carro_contrario_6_img = pygame.image.load(resource_path("asset/carro_contrario_6.png"))
estrada_img = pygame.image.load(resource_path("asset/estrada.png"))

# Carregar sons
som_motor = pygame.mixer.Sound(resource_path("asset/motor.wav"))
som_colisao = pygame.mixer.Sound(resource_path("asset/colisao.wav"))


class CarroJogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = carro_jogador_img
        self.rect = self.image.get_rect()
        self.rect.center = (LARGURA_TELA // 2, ALTURA_TELA - 100)
        self.velocidade = 5

    def update(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidade
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidade

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > LARGURA_TELA:
            self.rect.right = LARGURA_TELA


class CarroContrario(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = random.choice([
            carro_contrario_1_img,
            carro_contrario_2_img,
            carro_contrario_3_img,
            carro_contrario_4_img,
            carro_contrario_5_img,
            carro_contrario_6_img
        ])
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, LARGURA_TELA - self.rect.width)
        self.rect.y = random.randint(-100, -50)
        self.velocidade_y = random.randint(3, 6)

    def update(self):
        self.rect.y += self.velocidade_y
        if self.rect.top > ALTURA_TELA:
            self.kill()


class Botao:
    def __init__(self, x, y, largura, altura, texto, cor_normal, cor_hover, acao=None):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.texto = texto
        self.cor_normal = cor_normal
        self.cor_hover = cor_hover
        self.acao = acao
        self.fonte = pygame.font.Font(None, 36)

    def desenhar(self, superficie):
        mouse_pos = pygame.mouse.get_pos()
        cor = self.cor_hover if self.rect.collidepoint(mouse_pos) else self.cor_normal
        pygame.draw.rect(superficie, cor, self.rect, border_radius=10)
        pygame.draw.rect(superficie, PRETO, self.rect, 2, border_radius=10)

        texto_surf = self.fonte.render(self.texto, True, PRETO)
        texto_rect = texto_surf.get_rect(center=self.rect.center)
        superficie.blit(texto_surf, texto_rect)

    def verificar_clique(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos) and self.acao:
            return self.acao
        return None


class MenuPrincipal:
    def __init__(self):
        self.fonte_titulo = pygame.font.Font(None, 72)
        self.botoes = [
            Botao(LARGURA_TELA // 2 - 100, ALTURA_TELA // 2 - 50, 200, 50, "Play", VERDE, (100, 255, 100), "Play"),
            Botao(LARGURA_TELA // 2 - 100, ALTURA_TELA // 2 + 20, 200, 50, "Exit", VERMELHO, (255, 100, 100), "Exit")
        ]

    def desenhar(self, superficie):
        superficie.fill(CINZA)

        titulo = self.fonte_titulo.render("Car on the Road", True, BRANCO)
        titulo_rect = titulo.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA // 4))
        superficie.blit(titulo, titulo_rect)

        for botao in self.botoes:
            botao.desenhar(superficie)

    def processar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "sair"
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    for botao in self.botoes:
                        acao = botao.verificar_clique(evento.pos)
                        if acao:
                            return acao
        return None


class MenuPausa:
    def __init__(self):
        self.fonte_titulo = pygame.font.Font(None, 72)
        self.botoes = [
            Botao(LARGURA_TELA // 2 - 100, ALTURA_TELA // 2 - 80, 200, 50, "Continue", VERDE, (100, 255, 100),
                  "continue"),
            Botao(LARGURA_TELA // 2 - 100, ALTURA_TELA // 2 - 10, 200, 50, "Menu", AZUL, (100, 100, 255), "menu"),
            Botao(LARGURA_TELA // 2 - 100, ALTURA_TELA // 2 + 60, 200, 50, "Exit", VERMELHO, (255, 100, 100), "Exit")
        ]

    def desenhar(self, superficie):
        s = pygame.Surface((LARGURA_TELA, ALTURA_TELA), pygame.SRCALPHA)
        s.fill((50, 50, 50, 128))
        superficie.blit(s, (0, 0))

        titulo = self.fonte_titulo.render("Paused", True, BRANCO)
        titulo_rect = titulo.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA // 4))
        superficie.blit(titulo, titulo_rect)

        for botao in self.botoes:
            botao.desenhar(superficie)

    def processar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "Exit"
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return "continue"
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    for botao in self.botoes:
                        acao = botao.verificar_clique(evento.pos)
                        if acao:
                            return acao
        return None


class Jogo:
    def __init__(self):
        self.carro_jogador = CarroJogador()
        self.todas_sprites = pygame.sprite.Group()
        self.todas_sprites.add(self.carro_jogador)
        self.carros_contrarios = pygame.sprite.Group()
        self.tempo_entre_carros = 2
        self.tempo_ultimo_carro = 0
        self.pontuacao = 0
        self.fonte = pygame.font.Font(None, 36)
        self.relogio = pygame.time.Clock()
        self.rodando = False

    def criar_carro_contrario(self):
        carro = CarroContrario()
        self.carros_contrarios.add(carro)
        self.todas_sprites.add(carro)

    def reiniciar(self):
        self.__init__()
        self.iniciar()

    def iniciar(self):
        self.rodando = True
        som_motor.play(-1)

    def pausar(self):
        self.rodando = False
        som_motor.stop()

    def atualizar(self):
        self.todas_sprites.update()

        if pygame.sprite.spritecollideany(self.carro_jogador, self.carros_contrarios):
            som_colisao.play()
            return "game_over"

        tempo_atual = pygame.time.get_ticks() / 1000
        if tempo_atual - self.tempo_ultimo_carro >= self.tempo_entre_carros:
            self.criar_carro_contrario()
            self.tempo_ultimo_carro = tempo_atual

        self.pontuacao += 0.1

        return None

    def desenhar(self, superficie):
        superficie.blit(estrada_img, (0, 0))
        self.todas_sprites.draw(superficie)
        texto_pontuacao = self.fonte.render(f"Score: {int(self.pontuacao)}", True, BRANCO)
        superficie.blit(texto_pontuacao, (10, 10))

    def processar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "Exit"
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return "Pause"
        return None


class TelaGameOver:
    def __init__(self, pontuacao):
        self.pontuacao = pontuacao
        self.fonte_titulo = pygame.font.Font(None, 72)
        self.fonte_pontuacao = pygame.font.Font(None, 48)
        self.botoes = [
            Botao(LARGURA_TELA // 2 - 100, ALTURA_TELA // 2, 200, 50, "Play Again", VERDE, (100, 255, 100),
                  "Play"),
            Botao(LARGURA_TELA // 2 - 100, ALTURA_TELA // 2 + 70, 200, 50, "Menu", AZUL, (100, 100, 255), "menu"),
            Botao(LARGURA_TELA // 2 - 100, ALTURA_TELA // 2 + 140, 200, 50, "Exit", VERMELHO, (255, 100, 100), "Exit")
        ]

    def desenhar(self, superficie):
        superficie.fill(CINZA)

        titulo = self.fonte_titulo.render("Game Over", True, VERMELHO)
        titulo_rect = titulo.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA // 4))
        superficie.blit(titulo, titulo_rect)

        texto_pont = self.fonte_pontuacao.render(f"Score: {int(self.pontuacao)}", True, BRANCO)
        pont_rect = texto_pont.get_rect(center=(LARGURA_TELA // 2, ALTURA_TELA // 3))
        superficie.blit(texto_pont, pont_rect)

        for botao in self.botoes:
            botao.desenhar(superficie)

    def processar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "Exit"
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    for botao in self.botoes:
                        acao = botao.verificar_clique(evento.pos)
                        if acao:
                            return acao
        return None


def main():
    estado = "menu"
    jogo = Jogo()
    menu_principal = MenuPrincipal()

    rodando = True
    while rodando:
        if estado == "menu":
            acao = menu_principal.processar_eventos()
            if acao == "Play":
                jogo.reiniciar()
                estado = "Playing"
            elif acao == "Exit":
                rodando = False
            menu_principal.desenhar(tela)

        elif estado == "Playing":
            acao = jogo.processar_eventos()
            if acao == "Exit":
                rodando = False
            elif acao == "Pause":
                jogo.pausar()
                estado = "paused"

            resultado = jogo.atualizar()
            if resultado == "game_over":
                estado = "game_over"
                jogo.pausar()

            jogo.desenhar(tela)

        elif estado == "paused":
            menu_pausa = MenuPausa()
            acao = menu_pausa.processar_eventos()
            if acao == "continue":
                jogo.iniciar()
                estado = "Playing"
            elif acao == "menu":
                estado = "menu"
            elif acao == "Exit":
                rodando = False
            jogo.desenhar(tela)
            menu_pausa.desenhar(tela)

        elif estado == "game_over":
            tela_game_over = TelaGameOver(jogo.pontuacao)
            acao = tela_game_over.processar_eventos()
            if acao == "Play":
                jogo.reiniciar()
                estado = "Playing"
            elif acao == "menu":
                estado = "menu"
            elif acao == "Exit":
                rodando = False
            tela_game_over.desenhar(tela)

        pygame.display.flip()
        jogo.relogio.tick(60)

    som_motor.stop()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
