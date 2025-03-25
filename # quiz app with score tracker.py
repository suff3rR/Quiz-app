# quiz app with score tracker
import random 
if __name__ == "__main__":
    score = 0 
    lives = 3
    questions = {
        1 : "What is the chemical symbol for gold?",
        2 : "Which planet is known as the Red Planet?",
        3 : "What is the capital of Australia?"
    }
    options = {
        1 : ("A. Pb","B. Au","C. Zn","D. None of these"),
        2 : ("A. Mercury","B. Venus","C. Earth","D. None of these"),
        3 : ("A. Canberra","B. Toronto","C. Mexico","D. Beijing")
    }
    
    answers = {
        1 : "B",
        2 : "D",
        3 : "A"
    }
    while lives:
        if score == 10 : break
        question_num = random.randrange(1,4)  
        ques = questions.get(question_num)
        opts = options.get(question_num)
        print(ques)
        for option in options:
            if option == question_num:
                for i in options[option]:
                    print(i)

        guess = input("Enter your answer: ").upper()
        if len(guess) != 1:
            print("Please enter valid answer")
        print(guess)
        if guess == answers.get(question_num):
            print("Correct!")
            score+=1
        else :
            print("Incorrect") 
            lives-=1
    print("You ran out of lives")
    print(f"Your score is {score}")


## Fix repeating questions
## attach  question database
## make program sundar