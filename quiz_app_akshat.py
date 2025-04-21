import tkinter as tk
from tkinter import messagebox
import random

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("PythonQuiz App")
        self.master.geometry("500x400")
        self.score = 0
        self.lives = 3
        self.current_q_index = 0

        self.questions = {
            1: "What is the chemical symbol for gold?",
            2: "Which planet is known as the Red Planet?",
            3: "What is the capital of Australia?",
            4: "Which language is used for web apps?",
            5: "What is the square root of 64?",
            6: "Who wrote 'Romeo and Juliet'?",
            7: "What is the largest ocean on Earth?",
            8: "Which country hosted the 2021 Olympics?",
            9: "What is the boiling point of water in Celsius?",
            10: "What does CPU stand for?"
        }

        self.options = {
            1: ["A. Pb", "B. Au", "C. Zn", "D. Fe"],
            2: ["A. Mercury", "B. Venus", "C. Earth", "D. Mars"],
            3: ["A. Canberra", "B. Toronto", "C. Mexico", "D. Beijing"],
            4: ["A. Python", "B. HTML", "C. Java", "D. C++"],
            5: ["A. 6", "B. 7", "C. 8", "D. 9"],
            6: ["A. J.K. Rowling", "B. Shakespeare", "C. Dickens", "D. Tolkien"],
            7: ["A. Indian", "B. Arctic", "C. Atlantic", "D. Pacific"],
            8: ["A. China", "B. Japan", "C. Brazil", "D. USA"],
            9: ["A. 50", "B. 90", "C. 100", "D. 110"],
            10: ["A. Central Processing Unit", "B. Computer Processor Unit", "C. Core Processor Unit", "D. Central Power Unit"]
        }

        self.answers = {
            1: "B",
            2: "D",
            3: "A",
            4: "B",
            5: "C",
            6: "B",
            7: "D",
            8: "B",
            9: "C",
            10: "A"
        }

        self.question_ids = random.sample(list(self.questions.keys()), len(self.questions))

        self.question_label = tk.Label(master, text="", wraplength=400, font=('Helvetica', 14))
        self.question_label.pack(pady=20)

        self.option_vars = []
        self.selected_option = tk.StringVar()
        for i in range(4):
            rb = tk.Radiobutton(master, variable=self.selected_option, value='', text='', font=('Helvetica', 12), anchor='w')
            rb.pack(fill='x', padx=50, pady=2)
            self.option_vars.append(rb)

        self.submit_btn = tk.Button(master, text="Submit", command=self.submit_answer)
        self.submit_btn.pack(pady=10)

        self.status_label = tk.Label(master, text=f"Score: {self.score} | Lives: {self.lives}", font=('Helvetica', 12))
        self.status_label.pack(pady=10)

        self.next_question()

    def next_question(self):
        if self.lives == 0 or self.current_q_index == len(self.question_ids):
            self.end_quiz()
            return

        q_id = self.question_ids[self.current_q_index]
        self.current_question_id = q_id
        self.question_label.config(text=self.questions[q_id])
        options = self.options[q_id]
        self.selected_option.set("")
        for i, opt in enumerate(options):
            self.option_vars[i].config(text=opt, value=opt[0])

        self.status_label.config(text=f"Score: {self.score} | Lives: {self.lives}")

    def submit_answer(self):
        selected = self.selected_option.get()
        if not selected:
            messagebox.showwarning("Select Option", "Please select an answer!")
            return

        correct_ans = self.answers[self.current_question_id]
        if selected == correct_ans:
            self.score += 1
            messagebox.showinfo("Correct!", "Good job! That's the right answer.")
        else:
            self.lives -= 1
            messagebox.showerror("Incorrect", f"Wrong answer! Correct was: {correct_ans}")

        self.current_q_index += 1
        self.next_question()
    def end_quiz(self):
        percentage = (self.score / len(self.questions)) * 100
        msg = f"Quiz Over!\nFinal Score: {self.score}/{len(self.questions)}\nPercentage: {percentage:.2f}%"
        messagebox.showinfo("Result", msg)
        self.master.quit()

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = QuizApp(root) # Create an instance of QuizApp
        root.mainloop()
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
