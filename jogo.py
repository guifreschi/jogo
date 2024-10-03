from colorama import Fore, Back, Style
import random

# Personagem: classe mãe
# Herói: controlado pelo usuário
# Inimigo: adversário do usuário

class Personagem:
    def __init__(self, nome, vida, nivel):
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel
        
    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}"
    
    def receber_ataque(self, dano):
        self.__vida -= dano    
        if self.__vida < 0:
            self.__vida = 0
    
    def atacar(self, alvo):
        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4)
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")
        
class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade
    
    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return Fore.BLUE + f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}\n"
    
    def ataque_especial(self, alvo):
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 8) 
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} usou a habilidade especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano!")
        
        
class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo
        
    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return Fore.RED + f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}\n"
