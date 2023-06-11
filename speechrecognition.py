import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

def listen_and_process(retry_count=0):
    # Use the microphone as source for input.
    with sr.Microphone() as source:
        print("Please say something...")
        
        # Record the audio
        audio = r.listen(source)
        
        try:
            # Using google speech recognition
            print("Processing, please wait...")
            text = r.recognize_google(audio)
            if "I am sad" in text:
                print("User said 'I am sad'.")
            else:
                if retry_count < 10:
                    print("Sorry, I didn't get that. Can you repeat please?")
                    listen_and_process(retry_count+1)  # repeat the process
                else:
                    print("Sorry, I was unable to recognize your speech. Please try again later.")
        except:
            if retry_count < 10:
                print("Sorry, I did not get that. Can you repeat please?")
                listen_and_process(retry_count+1)  # repeat the process
            else:
                print("Sorry, I was unable to recognize your speech. Please try again later.")

# Call the function to start
listen_and_process()
