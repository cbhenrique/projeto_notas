class GerenciadorNotas:
    def __init__(self):
        self.notas = []

    def cadastrar_nota(self, nota):
        if nota < 0 or nota > 10:
            raise ValueError("Nota inválida! Deve ser entre 0 e 10.")
        self.notas.append(nota)

    def calcular_media(self):
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)

    def verificar_situacao(self):
        media = self.calcular_media()
        if media >= 7:
            return "Aprovado"
        elif media >= 5:
            return "Recuperação"
        else:
            return "Reprovado"