import banco_questoes
from random import choice

class Question():
    def __init__(self, question):
        self.pergunta = question['pergunta']
        self.resposta_correta = question['resposta']
        self.options = {
            'a': question['a'],
            'b': question['b'],
            'c': question['c'],
            'd': question['d']
        }

    def show_question(self):
        print(f"{self.pergunta}")
        for key, value in self.options.items():
            print(f"{key}) {value}")

    def check_answer(self, user_answer):
        return user_answer == self.resposta_correta
            
class Gamequiz():
    def __init__(self):
        self.lista = []
        self.score = 0
        self.is_running = True

    def receive_input(self, user_input):
        user_input = input("Digite aqui: ")
        
    def set_difficulty(self):
        print("--- CHEMQUIZ ---")
        print("Para encerrar a qualquer momento, digite 'e'.\n")
        
        while True:
            self.difficulty = input("Selecione a dificuldade: (f)ácil (m)édio"
                                    " (d)ifícil (a)leatório\n")
            if self.difficulty == 'f':
                self.lista = banco_questoes.perguntas_faceis
                break
            elif self.difficulty == 'm':
                self.lista = banco_questoes.perguntas_intermediarias
                break
            elif self.difficulty == 'd':
                self.lista = banco_questoes.perguntas_avancadas
                break
            elif self.difficulty == 'a':
                self.lista.extend(banco_questoes.perguntas_faceis)
                self.lista.extend(banco_questoes.perguntas_intermediarias)
                self.lista.extend(banco_questoes.perguntas_avancadas)
                break
            elif self.difficulty == 'e':
                print("Até logo!")
                self.is_running = False
                break
            else:
                print("\nResposta inválida.")
                continue
                
    def play_round(self):
        if not self.lista:
            return
            
        question_data = choice(self.lista)
        current_question = Question(question_data)

        current_question.show_question()
        
        while True:
            answer = input("Resposta: ").lower().strip()
            
            if answer == 'e':
                print(f"Fim de jogo! Sua pontuação final: {self.score}")
                print("Até logo!")
                self.is_running = False
                return
                
            if answer in ['a', 'b', 'c', 'd']:
                if current_question.check_answer(answer):
                    print("Correto!")
                    self.score += 1
                else: 
                    print("Resposta incorreta. A resposta é: "
                    f"{current_question.resposta_correta}")
                break
            else:
                print("Resposta inválida. Digite a, b, c, d ou 'e' para sair.")
    
    def ask_continue(self):
        if not self.is_running:
            return
        while True:
            continuar = input("Continuar? (s/n) ").lower().strip()
            if continuar == 'n' or continuar == 'e':
                print(f"Fim de jogo! Sua pontuação final: {self.score}")
                self.is_running = False
                break
            elif continuar == 's':
                break
            else:
                print("Por favor, digite 's' para sim ou 'n' para não.")
    def run(self):
        self.set_difficulty()

        while self.is_running:
            self.play_round()
            self.ask_continue()

        
if __name__ == "__main__":
    game = Gamequiz()
    game.run()