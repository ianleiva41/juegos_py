import tkinter as tk

class Trivia:
    def __init__(self, master):
        self.master = master
        self.master.title("Trivia")
        self.questions = [("¿Cuál es la capital de Francia?", "Paris"),
                          ("¿En qué año se fundó Apple?", "1976"),
                          ("¿Quién escribió la novela 'Cien años de soledad'?", "Gabriel García Márquez")]
        self.current_question = 0
        self.score = 0
        self.create_widgets()

    def create_widgets(self):
        self.question_label = tk.Label(self.master, text=self.questions[self.current_question][0])
        self.question_label.pack()

        self.answer_entry = tk.Entry(self.master)
        self.answer_entry.pack()

        self.submit_button = tk.Button(self.master, text="Enviar", command=self.check_answer)
        self.submit_button.pack()

        self.score_label = tk.Label(self.master, text="Puntuación: {}".format(self.score))
        self.score_label.pack()

    def check_answer(self):
        answer = self.answer_entry.get()
        if answer.lower() == self.questions[self.current_question][1].lower():
            self.score += 1
        self.current_question += 1
        if self.current_question == len(self.questions):
            self.show_results()
        else:
            self.question_label.config(text=self.questions[self.current_question][0])
            self.answer_entry.delete(0, tk.END)
            self.score_label.config(text="Puntuación: {}".format(self.score))

    def show_results(self):
        self.question_label.config(text="¡Fin del cuestionario!")
        self.answer_entry.destroy()
        self.submit_button.destroy()
        self.score_label.config(text="Puntuación final: {}".format(self.score))

root = tk.Tk()
app = Trivia(root)
root.mainloop()