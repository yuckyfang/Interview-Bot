import random

QuestionList = ["What was the first programming language that you learned?",                                        #0
                "What’s the hardest thing about working as a computer programmer?",                                 #1
                "What’s your favorite programming language?",                                                       #2
                "Can you tell me about your favorite programming project?",                                         #3
                "What’s the most recent language that you learned?",                                                #4
                "What would your skills and personality contribute to our team?",                                   #5
                "What made you apply for this position?",                                                           #6
                "where do you see yourself in 10 years?",                                                           #7
                "What qualities do you think a successful programmer should have? Do you have them?",               #8
                "Why do you think this job is a perfect fit for you?",                                              #9
                "Do you have previous job experience? If so, Why did you leave your last job. \nIf not, what would" #A
                "put you above other candidates?",
                "What is your ideal job environment?",                                                               #B
                "What do you like least about programming?"                                                          #C
                ]

goodResponseList = ["Interesting... A lot of people have started with those. Good Choice.",
                    "I agree with you. It can be hard, but the rest makes it worth it.",
                    "You can really learn a lot about a programmer by the language they prefer.",
                    "That project sounded pretty interesting and challenging. Good Job!",
                    "Good Job mastering your the most prominent languages, you should try learning some new ones too.",
                    "Those are some good qualities. Greatly valued here.",
                    "That's great to know that your interests align with ours.",
                    "It's good to aim high and have a plan. You'll definitely make it.",
                    "I think so too! Programmers need to be creative and think outside the box.",
                    "I'm starting to think so, too.",
                    "That's pretty good. Well, you'll have a great time here.",
                    "Then you'll be a great fit here",
                    "I agree, it's tough but it's necessary."
                    ]
badResponseList = ["I rarely hear of that one. Interesting.",
                   "I agree with you. It can be hard, but the rest makes it worth it.",
                   "You can really learn a lot about a programmer by the language they prefer.",
                   "Hopefully you can find something here.",
                   "Good Job keeping up with modern languages. It's good to stay familiar with older ones though.",
                   "Hopefully there are some better qualities in you.",
                   "Your interests should be aligning with the company's, not just earning a paycheck.",
                   "You should be aiming high. It'll improve your work and give yourself something to work towards.",
                   "You should develop some good traits like being creative and thinking outside the box.",
                   "Hmm... Interesting...",
                   "Even if you don't have job experience, you can be better in other ways, such as having experience"
                   "in another field, which may give different ways of thinking.",
                   "Our work environment greatly affects our performance you know... I pride myself on having the best"
                   " work environment.",
                   "Hmmm...Interesting..."
                   ]
# def getResponse(responseList):
#     userResponse = input("Your Answer: ")
#     sentence = userResponse.split()
#     if any(x in responseList for x in sentence):
#         return 1;
#     else:
#         return 0;

# print("Hi, do you need a glass of water or anything? If so, let me know.\n"
#       "My name is John Smith. What do you think of the weather today?\n")

# positiveResponse = ["great", "good", "sunny", "perfect", "amazing"]

# if getResponse(positiveResponse) == 1:
#     print("That's great to hear.")
# else:
#     print("Yeah, it could be better.")

# print("Anyway, I\'m the hiring manager here and we\'re looking for a candidate for the position of Tech Developer.\n"
#       "I heard you were interested in the position. Could you tell me what got you interested in programming?\n")
# positiveResponse = ["fun", "joy", "creative", "exciting", "love", "changing lives", "puzzle", "build", "create", "learn"]

# if getResponse(positiveResponse) == 1:
#     print("Hmmm... That's pretty interesting to hear. Sounds like you're really into programming.")
# else:
#     print("Hmmm... It doesn't seem like you're too passionate about programming.")
# usedQuestions = [-1, -1, -1]

# def ask(index):
#     print(QuestionList[index])
#     if index == 0 | index == 2 | index == 4:
#         PositiveResponse = ["c", "c plus plus", "java", "ruby", "c sharp", "java script", "swift"]
#     if index == 1:
#         PositiveResponse = ["documentation", "fun", "boring", "figuring", "hard"]
#     if index == 3:
#         PositiveResponse = ["difficult", "learn", "learned", "fun", "challenging", "interesting"]
#     if index == 5:
#         PositiveResponse = ["teamwork", "work", "leadership", "cooperative", "team player", "hard", "worker",
#                             "motivated", "quick", "fast", "learner", "team"]
#     if index == 6:
#         PositiveResponse = ["love", "interesting", "interested", "help", "learn", "build", "create", "opportunity"]
#     if index == 7:
#         PositiveResponse = ["manager", "head", "create", "start", "new", "lead", "leader", "leadership", "owner"]
#     if index == 8:
#         PositiveResponse = ["yes", "creative", "thinking", "box", "learner", "learn", "team", "flexible"]
#     if index == 9:
#         PositiveResponse = ["fit", "perfect", "team", "hard", "computer", "create", "program", "programming", "flexible"]
#     if index == 10:
#         PositiveResponse = ["yes", "not", "fit", "interested", "unfair", "work", "good", "pay", "unethical", "hard"]
#     if index == 11:
#         PositiveResponse = ["friendly", "cooperative", "clean", "fairly", "paid", "understanding", "understand"]
#     if index == 12:
#         PositiveResponse = ["documentation"]
#     goodResponse = goodResponseList[index]
#     badResponse = badResponseList[index]
#     if getResponse(PositiveResponse) == 1:
#         print(goodResponse)
#     else:
#         print(badResponse)

# for x in range(3):
#     newQuestion = random.randint(0, 12)
#     while newQuestion in usedQuestions:
#         newQuestion = random.randint(0, 12)
#     usedQuestions[x] = newQuestion
#     ask(newQuestion)
