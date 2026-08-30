# import random

# subjects = ["Python", "C", "Robotics", "AI", "Mathematics"]

# topic = random.choice(subjects)

# print(topic)

subjects = ["Python", "C", "AI"]

for numbers, subjects in enumerate(subjects, start=1):
    print(numbers, subjects)

# qwiz_questions = {
#     "python" : {
#         "Which keyword is used to define a function?\nA. func\nB. define\nC. def\nD. function" : "C",
#         "Which symbol is used to create a list in Python?\nA. ()\nB. []\nC. {}\nD. <>": "B",
#         "How do you output data to the screen in Python?\nA. print()\nB. echo()\nC. output()\nD. write()": "A"
#     },

#     "C" : {
#         "What is the file extension for a C source code file?\nA. .cpp\nB. .c\nC. .cs\nD. .txt": "B",
#         "Which function is used to read input from the user in C?\nA. printf()\nB. cin\nC. scanf()\nD. get()": "C",
#         "Which operator is used for logical AND in C?\nA. &\nB. ||\nC. &&\nD. !": "C"
#     },

#     "Robotics" : {
#         "What does the acronym 'DOF' stand for in robotics?\nA. Direction of Force\nB. Degree of Freedom\nC. Data on Frame\nD. Dynamic Output Frequency": "B",
#         "Which sensor is commonly used by robots to measure the distance to an obstacle?\nA. Gyroscope\nB. Barometer\nC. Ultrasonic sensor\nD. Thermistor": "C",
#         "Which process calculates the position of a robot's end-effector given its joint angles?\nA. Inverse kinematics\nB. Forward kinematics\nC. Reverse kinematics\nD. Dynamic kinematics": "B"
#     }
# }

# print(qwiz_questions["python"].keys())