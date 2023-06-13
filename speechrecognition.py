import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

def listen_and_process():
    # Use the microphone as source for input.
    with sr.Microphone() as source:
        # Record the audio
        audio = r.listen(source)
        
        try:
            # Using google speech recognition
            text = r.recognize_google(audio)
            if "I am sad" in text:
                pass  # User said 'I am sad', do something here
            else:
                listen_and_process()  # repeat the process
        except:
            listen_and_process()  # repeat the process

# Call the function to start
listen_and_process()
