# # Sentences we'll respond with if the user greeted us
# GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up",)
# 
# GREETING_RESPONSES = ["'sup bro", "hey", "*nods*", "hey you get my snap?"]
# 
# 
# def check_for_greeting(sentence):
#     """If any of the words in the user's input was a greeting, return a greeting response"""
#     for word in sentence.words:
#         if word.lower() in GREETING_KEYWORDS:
#             return random.choice(GREETING_RESPONSES)

# import speech_recognition as sr
# r = sr.Recognizer()
# mic = sr.Microphone()
# with mic as source:
#     audio = r.listen(source)
#     print(audio)


import speech_recognition as sr

#def recognize_speech_from_mic(recognizer, microphone):
def recognize_speech_from_mic():
    
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    
#     
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        print('wait')
        audio = recognizer.listen(source)

    try:
        response= recognizer.recognize_google(audio)
        response = "Could not request results from Google Speech Recognition service"
    except sr.UnknownValueError:
        response = "Unknown speech"

    return response


if __name__ == "__main__":  
    # create recognizer and microphone instances
    r = sr.Recognizer()
    mic = sr.Microphone()
    test = recognize_speech_from_mic(r, mic)
    
