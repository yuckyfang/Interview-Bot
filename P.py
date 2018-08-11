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
                    ]

def getResponse():
    userResponse = input("Your Answer: ")
    sentence = userResponse.split()
    if any(x in positiveResponse for x in sentence):
        return 1;
    else:
        return 0;

flags = [0]

print("Hi, do you need a glass of water or anything? If so, let me know.\n"
      "My name is John Smith. What do you think of the weather today?\n")

positiveResponse = ["great", "good", "sunny", "perfect", "amazing"]

if getResponse() == 1:
    print("That's great to hear.")
else:
    print("Yeah, it could be better.")

print("Anyway, I\'m the hiring manager here and we\'re looking for a candidate for the position of Java Developer.\n"
      "I heard you were interested in the position. Could you tell me what got you interested in programming?\n")
positiveResponse = ["fun", "joy", "creative", "exciting", "love", "changing lives", "puzzle"]

if getResponse() == 1:
    print("Hmmm... That's pretty interesting to hear. Sounds like you're really into programming.")
else:
    print("Hmmm...")
    flags[0] = 1                    #flags that the user doesn't show interest
usedQuestions = [-1, -1, -1]

def ask(index):
    print(QuestionList[index])
    if index == 0:
        positiveResponse = ["C", "C++", "Java", "Ruby", "C#", "JavaScript", "Swift"]
        goodResponse = goodResponseList
    if getResponse() == 1:
        print(goodResponse)
    else:
        print(badReponse)

for x in range(3):
    newQuestion = random.randint(0, 12)
    while newQuestion in usedQuestions:
        newQuestion = random.randint(0, 12)
    usedQuestions[x] = newQuestion
    ask(newQuestion)
