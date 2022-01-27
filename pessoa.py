# encoding: utf-8
class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome= nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self, alimento):
        if self.comendo:
            print('{} já está comendo.'.format(self.nome))
            return

        if self.falando:
            print('{} não pode comer falando.'.format(self.nome))
            return

        print('{} está comendo {}.'.format(self.nome, alimento))
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print('{} não está comendo.'.format(self.nome))
            return

        print('{} parou de comer.'.format(self.nome))
        self.comendo = False

    def falar(self, assunto):
        if self.comendo:
            print('{} não pode falar comendo.'.format(self.nome))
            return

        if self.falando:
            print('{} já está falando.'.format(self.nome))
            return

        print('{} está falando.'.format(self.nome))
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print('{} não está falando.'.format(self.nome))
            return

        print('{} parou de falar.'.format(self.nome))
        self.falando = False