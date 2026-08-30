
import random

def learn_topic():
    topic = input("What topic you want to learn?\n").lower().strip()

    knowledge = {
        "python" : "Python is a popular, beginner-friendly programming language known for its simple, English-like syntax. It's incredibly versatile and widely used for artificial intelligence, data science, web development, and automating tasks.",

        "c" : "C is a powerful, high-performance programming language that operates very close to the computer's hardware. Created in the 1970s, it is incredibly fast and remains the foundation for building operating systems, game engines, and embedded devices, though it is much more complex to learn than modern languages.",

        "robotics" : "Robotics is an interdisciplinary field that blends mechanical engineering, electronics, and computer science to design, build, and operate programmable machines. These robots use sensors, software, and artificial intelligence to interact with the physical world, performing tasks autonomously or assisting humans across various industries."
    }

    if topic in knowledge:
        print(f"Explanation:\n{knowledge[topic]}")
    else:
        print("Sorry, I dont have information about that topic yet.")

# learn_topic()

def take_quiz():
    qwiz_questions = {
        "python" : {
            "Which keyword is used to define a function?\nA. func\nB. define\nC. def\nD. function" : "C",
            "Which symbol is used to create a list in Python?\nA. ()\nB. []\nC. {}\nD. <>": "B",
            "How do you output data to the screen in Python?\nA. print()\nB. echo()\nC. output()\nD. write()": "A"
        },

        "c" : {
            "What is the file extension for a C source code file?\nA. .cpp\nB. .c\nC. .cs\nD. .txt": "B",
            "Which function is used to read input from the user in C?\nA. printf()\nB. cin\nC. scanf()\nD. get()": "C",
            "Which operator is used for logical AND in C?\nA. &\nB. ||\nC. &&\nD. !": "C"
        },

        "robotics" : {
            "What does the acronym 'DOF' stand for in robotics?\nA. Direction of Force\nB. Degree of Freedom\nC. Data on Frame\nD. Dynamic Output Frequency": "B",
            "Which sensor is commonly used by robots to measure the distance to an obstacle?\nA. Gyroscope\nB. Barometer\nC. Ultrasonic sensor\nD. Thermistor": "C",
            "Which process calculates the position of a robot's end-effector given its joint angles?\nA. Inverse kinematics\nB. Forward kinematics\nC. Reverse kinematics\nD. Dynamic kinematics": "B"
        }
    }

    print("\n==========  qwiz  ================\n")

    print("Choose your Subject:\n1. Python\n2. C\n3. Robotics\n4. Mix\n5. Back")

    choice = input("Enter your choice: \n").strip()

    if choice == "1":
        subject = "python"
        questions = qwiz_questions[subject]
    elif choice == "2":
        subject = "c"
        questions = qwiz_questions[subject]
    elif choice == "3":
        subject = "robotics" 
        questions = qwiz_questions[subject]
    elif choice == "5":
        return 0
    elif choice == "4":
        print("Starting Mixed Qwiz.......")
        all_questions = {}
        all_questions.update(qwiz_questions["python"])
        all_questions.update(qwiz_questions["c"])
        all_questions.update(qwiz_questions["robotics"])
        questions=all_questions
    else:
        print("Invalid Choice.")
        return 0

    selected_questions = random.sample(list(questions), min(3, len(questions)))

    score = 0

    for number, question in enumerate(selected_questions, start=1):
        print(f"Question {number}/{len(selected_questions)}")
        print(f"{question}")       
        answer = input("Enter Your Answer: ").upper().strip()
        if answer == questions[question]:  
            print("Correct\n")
            score = score + 1
        else:
            print(f"Wrong! The correct answer is {questions[question]}.\n")

    print("======================================")
    print(f"Final Score: {score}/{len(selected_questions)}")
    print("======================================\n")

    return score

# take_quiz()

print("===========================================\n")
print("            AI Study Assistant             \n")
print("===========================================\n")
print(" 1. Learn a topic\n2. Take a quiz\n3. View progress\n4. Exit\n")

while True:
    user = input("Enter your Choice: ")
    if user == '1':
        print("You choose to Learn a topic.\n")
        learn_topic()

    elif user == '2':
        print("You choose to Take a quiz.")
        take_quiz()

    elif user == '3':
        print("You choose to View Your Progress.")
        
    elif user == '4':
        print("Good Bye!!")
        break

    else:
        print("Invalid Choice.")
