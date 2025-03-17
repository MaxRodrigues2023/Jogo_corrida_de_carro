# import pygame
# import os
# import random
# import sys
#
#
#
# # Inicialização do Pygame
# pygame.init()
#
#
# # Função para converter caminhos relativos em absolutos
# def resource_path(relative_path):
#     if hasattr(sys, '_MEIPASS'):
#         # Executando no executável compilado
#         return os.path.join(sys._MEIPASS, relative_path)
#     # Executando no script Python
#     return os.path.join(os.path.abspath("."), relative_path)
#
#
# # Configurações da tela
# LARGURA_TELA = 900
# ALTURA_TELA = 600
# tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
# pygame.display.set_caption("Jogo de Corrida")
#
# # Cores
# BRANCO = (255, 255, 255)
# PRETO = (0, 0, 0)
#
# # Carregar assets
# carro_jogador_img = pygame.image.load(resource_path("assets/carro_jogador.png"))
# carro_contrario_1_img = pygame.image.load(resource_path("assets/carro_contrario_1.png"))
# carro_contrario_2_img = pygame.image.load(resource_path("assets/carro_contrario_2.png"))
# carro_contrario_3_img = pygame.image.load(resource_path("assets/carro_contrario_3.png"))
# carro_contrario_4_img = pygame.image.load(resource_path("assets/carro_contrario_4.png"))
# carro_contrario_5_img = pygame.image.load(resource_path("assets/carro_contrario_5.png"))
# carro_contrario_6_img = pygame.image.load(resource_path("assets/carro_contrario_6.png"))
# estrada_img = pygame.image.load(resource_path("assets/estrada.png"))
#
#
# # Classe do Carro do Jogador
# class CarroJogador(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = carro_jogador_img
#         self.rect = self.image.get_rect()
#         self.rect.center = (LARGURA_TELA // 2, ALTURA_TELA - 100)
#         self.velocidade = 5
#
#     def update(self):
#         # Movimentação horizontal
#         teclas = pygame.key.get_pressed()
#         if teclas[pygame.K_LEFT]:
#             self.rect.x -= self.velocidade
#         if teclas[pygame.K_RIGHT]:
#             self.rect.x += self.velocidade
#
#         # Impede que o carro saia da tela
#         if self.rect.left < 0:
#             self.rect.left = 0
#         if self.rect.right > LARGURA_TELA:
#             self.rect.right = LARGURA_TELA
#
#
# # Classe do Carro Inimigo
# class CarroContrario(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.image = random.choice([
#             carro_contrario_1_img,
#             carro_contrario_2_img,
#             carro_contrario_3_img,
#             carro_contrario_4_img,
#             carro_contrario_5_img,
#             carro_contrario_6_img
#         ])
#         self.rect = self.image.get_rect()
#         self.rect.x = random.randint(0, LARGURA_TELA - self.rect.width)
#         self.rect.y = random.randint(-100, -50)  # Começa acima da tela
#         self.velocidade_y = random.randint(3, 6)  # Velocidade de queda
#
#     def update(self):
#         self.rect.y += self.velocidade_y  # Move o carro para baixo
#
#         # Remove o carro se ele sair da tela
#         if self.rect.top > ALTURA_TELA:
#             self.kill()
#
#
# # Inicialização do jogo
# carro_jogador = CarroJogador()
# todas_sprites = pygame.sprite.Group()
# todas_sprites.add(carro_jogador)
#
# carros_contrarios = pygame.sprite.Group()
# tempo_entre_carros = 2  # Segundos entre a aparição de cada carro inimigo
# tempo_ultimo_carro = 0  # Tempo desde o último carro criado
#
# pontuacao = 0
# fonte = pygame.font.Font(None, 36)
# relogio = pygame.time.Clock()
#
#
# # Função para criar carros inimigos
# def criar_carro_contrario():
#     carro = CarroContrario()
#     carros_contrarios.add(carro)
#     todas_sprites.add(carro)
#
#
# # Loop principal do jogo
# rodando = True
# while rodando:
#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             rodando = False
#
#     # Atualiza sprites
#     todas_sprites.update()
#
#     # Verifica colisões entre o carro do jogador e os carros inimigos
#     if pygame.sprite.spritecollideany(carro_jogador, carros_contrarios):
#         rodando = False  # Fim do jogo
#
#     # Cria novos carros inimigos
#     tempo_atual = pygame.time.get_ticks() / 1000  # Tempo em segundos
#     if tempo_atual - tempo_ultimo_carro >= tempo_entre_carros:
#         criar_carro_contrario()
#         tempo_ultimo_carro = tempo_atual
#
#     # Atualiza a pontuação
#     pontuacao += 0.1  # Aumenta a pontuação ao longo do tempo
#
#     # Desenha na tela
#     tela.blit(estrada_img, (0, 0))
#     todas_sprites.draw(tela)
#
#     # Mostra pontuação
#     texto_pontuacao = fonte.render(f"Pontuação: {int(pontuacao)}", True, BRANCO)
#     tela.blit(texto_pontuacao, (10, 10))
#
#     # Atualiza a tela
#     pygame.display.flip()
#     relogio.tick(60)
#
# # Fim do jogo
# pygame.quit()
# sys.exit()

import pygame
import os
import random
import sys

# Inicialização do Pygame e do mixer
pygame.init()
pygame.mixer.init()

# Função para converter caminhos relativos em absolutos
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        # Executando no executável compilado
        return os.path.join(sys._MEIPASS, relative_path)
    # Executando no script Python
    return os.path.join(os.path.abspath("."), relative_path)

# Configurações da tela
LARGURA_TELA = 900
ALTURA_TELA = 600
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption("Jogo de Corrida")

# Cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)

# Carregar assets
carro_jogador_img = pygame.image.load(resource_path("assets/carro_jogador.png"))
carro_contrario_1_img = pygame.image.load(resource_path("assets/carro_contrario_1.png"))
carro_contrario_2_img = pygame.image.load(resource_path("assets/carro_contrario_2.png"))
carro_contrario_3_img = pygame.image.load(resource_path("assets/carro_contrario_3.png"))
carro_contrario_4_img = pygame.image.load(resource_path("assets/carro_contrario_4.png"))
carro_contrario_5_img = pygame.image.load(resource_path("assets/carro_contrario_5.png"))
carro_contrario_6_img = pygame.image.load(resource_path("assets/carro_contrario_6.png"))
estrada_img = pygame.image.load(resource_path("assets/estrada.png"))

# Carregar sons
som_motor = pygame.mixer.Sound(resource_path("assets/motor.wav"))
som_colisao = pygame.mixer.Sound(resource_path("assets/colisao.wav"))

# Reproduzir som do motor em loop
som_motor.play(-1)  # -1 faz o som repetir infinitamente

# Classe do Carro do Jogador
class CarroJogador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = carro_jogador_img
        self.rect = self.image.get_rect()
        self.rect.center = (LARGURA_TELA // 2, ALTURA_TELA - 100)
        self.velocidade = 5

    def update(self):
        # Movimentação horizontal
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidade
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidade

        # Impede que o carro saia da tela
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > LARGURA_TELA:
            self.rect.right = LARGURA_TELA

# Classe do Carro Contrário
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
        self.rect.y = random.randint(-100, -50)  # Começa acima da tela
        self.velocidade_y = random.randint(3, 6)  # Velocidade de queda

    def update(self):
        self.rect.y += self.velocidade_y  # Move o carro para baixo

        # Remove o carro se ele sair da tela
        if self.rect.top > ALTURA_TELA:
            self.kill()

# Inicialização do jogo
carro_jogador = CarroJogador()
todas_sprites = pygame.sprite.Group()
todas_sprites.add(carro_jogador)

carros_contrarios = pygame.sprite.Group()
tempo_entre_carros = 2  # Segundos entre a aparição de cada carro contrário
tempo_ultimo_carro = 0  # Tempo desde o último carro criado

pontuacao = 0
fonte = pygame.font.Font(None, 36)
relogio = pygame.time.Clock()

# Função para criar carros contrários
def criar_carro_contrario():
    carro = CarroContrario()
    carros_contrarios.add(carro)
    todas_sprites.add(carro)

# Loop principal do jogo
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Atualiza sprites
    todas_sprites.update()

    # Verifica colisões entre o carro do jogador e os carros contrários
    if pygame.sprite.spritecollideany(carro_jogador, carros_contrarios):
        som_colisao.play()  # Reproduz o som de colisão
        rodando = False  # Fim do jogo

    # Cria novos carros contrários
    tempo_atual = pygame.time.get_ticks() / 1000  # Tempo em segundos
    if tempo_atual - tempo_ultimo_carro >= tempo_entre_carros:
        criar_carro_contrario()
        tempo_ultimo_carro = tempo_atual

    # Atualiza a pontuação
    pontuacao += 0.1  # Aumenta a pontuação ao longo do tempo

    # Desenha na tela
    tela.blit(estrada_img, (0, 0))
    todas_sprites.draw(tela)

    # Mostra pontuação
    texto_pontuacao = fonte.render(f"Pontuação: {int(pontuacao)}", True, BRANCO)
    tela.blit(texto_pontuacao, (10, 10))

    # Atualiza a tela
    pygame.display.flip()
    relogio.tick(60)

# Fim do jogo
som_motor.stop()  # Para o som do motor
pygame.quit()
sys.exit()